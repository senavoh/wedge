#!/usr/bin/env python3
"""Wedge fetcher: pull raw customer voice from free, keyless sources.

Every record is printed as one JSON line with the same shape, so later steps
(signals.py, verify.py) never care where it came from:

    {"source", "url", "title", "text", "author", "date", "score", "rating", "meta"}

Usage:
    python3 fetch.py hn "invoice software" --limit 50
    python3 fetch.py reddit "alternative to quickbooks" --sub smallbusiness
    python3 fetch.py appstore-search "invoice maker"
    python3 fetch.py appstore-reviews 1234567890 --max-rating 2 --pages 3
    python3 fetch.py github-issues "repo:owner/name is:issue sort:reactions-+1-desc"
    python3 fetch.py page https://competitor.com/pricing
    python3 fetch.py pages URL1 URL2 URL3          # many pages in parallel
    python3 fetch.py links LIST_URL --match /support/topic/ | python3 fetch.py --out raw/r.jsonl pages --from -

Add --out FILE to append to a JSONL file instead of printing.
Python 3.8+ standard library only. No API keys required. Optional: GITHUB_TOKEN raises
GitHub's rate limit; REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET (a free Reddit
"script" app) use Reddit's official API where the public JSON is blocked.
"""
import argparse
import base64
import concurrent.futures
import html
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "wedge/1.0 (+https://github.com/senavoh/wedge)"
TIMEOUT = 20


def get(url, headers=None, retries=1):
    hdrs = {"User-Agent": UA, "Accept": "*/*"}
    hdrs.update(headers or {})
    last = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                charset = r.headers.get_content_charset() or "utf-8"
                return r.read().decode(charset, errors="replace")
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503) and attempt < retries:
                time.sleep(2 * (attempt + 1))
                continue
            raise
        except urllib.error.URLError as e:
            last = e
            if attempt < retries:
                time.sleep(1)
                continue
            raise
    raise last


def get_json(url, headers=None, retries=1):
    return json.loads(get(url, headers, retries))


def rec(source, url, title="", text="", author="", date="", score=None, rating=None, **meta):
    return {
        "source": source,
        "url": url,
        "title": clean(title),
        "text": clean(text),
        "author": author or "",
        "date": date or "",
        "score": score,
        "rating": rating,
        "meta": meta,
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def clean(s):
    if not s:
        return ""
    s = TAG_RE.sub(" ", s)
    s = html.unescape(s)
    return WS_RE.sub(" ", s).strip()


# --- sources ---------------------------------------------------------------

def hn(query, limit=50, kind="all"):
    tags = {"all": "(story,comment)", "story": "story", "comment": "comment"}[kind]
    q = urllib.parse.urlencode({"query": query, "tags": tags, "hitsPerPage": min(limit, 100)})
    data = get_json("https://hn.algolia.com/api/v1/search?" + q)
    for h in data.get("hits", []):
        oid = h.get("objectID")
        yield rec(
            "hn",
            "https://news.ycombinator.com/item?id=%s" % oid,
            title=h.get("title") or h.get("story_title") or "",
            text=h.get("comment_text") or h.get("story_text") or "",
            author=h.get("author", ""),
            date=(h.get("created_at") or "")[:10],
            score=h.get("points"),
        )


_reddit_token = None


def reddit_get(path, params):
    """GET a Reddit JSON endpoint, through the official API when possible.

    With REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET set (a free "script" app
    from https://www.reddit.com/prefs/apps), requests go to oauth.reddit.com,
    which works from networks where the public JSON is blocked. Without them,
    the public www.reddit.com JSON is tried.
    """
    global _reddit_token
    cid, secret = os.environ.get("REDDIT_CLIENT_ID"), os.environ.get("REDDIT_CLIENT_SECRET")
    params = dict(params, raw_json=1)
    if cid and secret:
        if _reddit_token is None:
            req = urllib.request.Request(
                "https://www.reddit.com/api/v1/access_token",
                data=b"grant_type=client_credentials",
                headers={"User-Agent": UA, "Authorization": "Basic " + base64.b64encode(
                    ("%s:%s" % (cid, secret)).encode()).decode()})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                _reddit_token = json.load(r)["access_token"]
        return get_json("https://oauth.reddit.com%s?%s" % (path, urllib.parse.urlencode(params)),
                        {"Authorization": "Bearer " + _reddit_token})
    try:
        return get_json("https://www.reddit.com%s.json?%s" % (path, urllib.parse.urlencode(params)), retries=0)
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            sys.stderr.write(
                "wedge fetch: reddit.com refused the request (HTTP %s). Set REDDIT_CLIENT_ID and "
                "REDDIT_CLIENT_SECRET (free app at https://www.reddit.com/prefs/apps) to use Reddit's "
                "official API, or use your own web search with site:reddit.com for this step.\n" % e.code)
        raise


def reddit(query, limit=50, sub=None, sort="relevance", t="all"):
    params = {"q": query, "limit": min(limit, 100), "sort": sort, "t": t}
    if sub:
        params["restrict_sr"] = 1
        path = "/r/%s/search" % urllib.parse.quote(sub)
    else:
        path = "/search"
    data = reddit_get(path, params)
    for c in data.get("data", {}).get("children", []):
        d = c.get("data", {})
        if d.get("over_18"):
            continue
        yield rec(
            "reddit",
            "https://www.reddit.com" + d.get("permalink", ""),
            title=d.get("title", ""),
            text=d.get("selftext", ""),
            author=d.get("author", ""),
            date=time.strftime("%Y-%m-%d", time.gmtime(d.get("created_utc", 0))),
            score=d.get("score"),
            subreddit=d.get("subreddit"),
            comments=d.get("num_comments"),
        )


def reddit_thread(url, limit=100):
    """Comments of one thread: the place complaints actually live."""
    path = urllib.parse.urlparse(url).path.rstrip("/")
    data = reddit_get(path, {"limit": limit})
    if not isinstance(data, list) or len(data) < 2:
        return
    post = (data[0].get("data", {}).get("children") or [{}])[0].get("data", {})
    if post.get("over_18"):
        return

    def walk(children):
        for c in children:
            if c.get("kind") != "t1":
                continue
            d = c["data"]
            yield rec(
                "reddit",
                "https://www.reddit.com" + d.get("permalink", ""),
                text=d.get("body", ""),
                author=d.get("author", ""),
                date=time.strftime("%Y-%m-%d", time.gmtime(d.get("created_utc", 0))),
                score=d.get("score"),
                subreddit=d.get("subreddit"),
            )
            replies = d.get("replies")
            if isinstance(replies, dict):
                yield from walk(replies.get("data", {}).get("children", []))

    yield from walk(data[1].get("data", {}).get("children", []))


def appstore_search(term, limit=25, country="us"):
    q = urllib.parse.urlencode({"term": term, "entity": "software", "limit": min(limit, 200), "country": country})
    data = get_json("https://itunes.apple.com/search?" + q)
    for a in data.get("results", []):
        yield rec(
            "appstore",
            a.get("trackViewUrl", ""),
            title=a.get("trackName", ""),
            text=a.get("description", "")[:600],
            author=a.get("sellerName", ""),
            date=(a.get("currentVersionReleaseDate") or "")[:10],
            rating=a.get("averageUserRating"),
            app_id=a.get("trackId"),
            ratings_count=a.get("userRatingCount"),
            price=a.get("formattedPrice"),
            genre=a.get("primaryGenreName"),
        )


def appstore_reviews(app_id, pages=3, country="us", max_rating=5):
    # Apple's feed returns nothing for some apps when a sort order is given,
    # so try "most recent" first and fall back to the default order.
    for sort in ("/sortby=mostrecent", ""):
        got = 0
        for page in range(1, pages + 1):
            url = "https://itunes.apple.com/%s/rss/customerreviews/page=%d/id=%s%s/json" % (
                country, page, app_id, sort)
            try:
                data = get_json(url)
            except urllib.error.HTTPError:
                break
            entries = data.get("feed", {}).get("entry", [])
            if isinstance(entries, dict):
                entries = [entries]
            if not entries:
                break
            got += len(entries)
            yield from _reviews(entries, app_id, country, max_rating)
        if got:
            return


def _reviews(entries, app_id, country, max_rating):
    for e in entries:
        if "im:rating" not in e:
            continue  # first entry can be the app itself
        rating = int(e["im:rating"]["label"])
        if rating > max_rating:
            continue
        rid = e.get("id", {}).get("label", "")
        yield rec(
            "appstore",
            "https://apps.apple.com/%s/app/id%s?see-all=reviews#review-%s" % (country, app_id, rid),
            title=e.get("title", {}).get("label", ""),
            text=e.get("content", {}).get("label", ""),
            author=e.get("author", {}).get("name", {}).get("label", ""),
            date=(e.get("updated", {}).get("label") or "")[:10],
            rating=rating,
            app_id=app_id,
        )


def github_issues(query, limit=50):
    hdrs = {"Accept": "application/vnd.github+json"}
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        hdrs["Authorization"] = "Bearer " + tok
    q = urllib.parse.urlencode({"q": query, "per_page": min(limit, 100)})
    data = get_json("https://api.github.com/search/issues?" + q, hdrs)
    for i in data.get("items", []):
        yield rec(
            "github",
            i.get("html_url", ""),
            title=i.get("title", ""),
            text=(i.get("body") or "")[:2000],
            author=(i.get("user") or {}).get("login", ""),
            date=(i.get("created_at") or "")[:10],
            score=(i.get("reactions") or {}).get("total_count"),
            state=i.get("state"),
            comments=i.get("comments"),
        )


SCRIPT_RE = re.compile(r"<(script|style|noscript|svg)[^>]*>.*?</\1>", re.S | re.I)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)


def page_text(raw):
    t = TITLE_RE.search(raw)
    body = SCRIPT_RE.sub(" ", raw)
    body = re.sub(r"<(br|p|div|li|h[1-6]|tr|section)[^>]*>", "\n", body, flags=re.I)
    return (clean(t.group(1)) if t else ""), clean(body)


def page(url, max_chars=60000):
    raw = get(url, {"Accept": "text/html,application/xhtml+xml"})
    title, text = page_text(raw)
    yield rec("web", url, title=title, text=text[:max_chars], chars=len(text))


# --- cli -------------------------------------------------------------------

HREF_RE = re.compile(r'href=["\']([^"\'#]+)', re.I)


def links(url, match=None, limit=200):
    """URLs linked from a page, optionally filtered by a regex. Feed them to `pages`."""
    raw = get(url, {"Accept": "text/html,application/xhtml+xml"})
    rx = re.compile(match) if match else None
    seen = []
    for h in HREF_RE.findall(raw):
        u = urllib.parse.urljoin(url, html.unescape(h))
        if u.startswith("http") and (not rx or rx.search(u)) and u not in seen:
            seen.append(u)
    return seen[:limit]


class HostGate:
    """At most `per_host` requests in flight per site, spaced `gap` seconds apart."""

    def __init__(self, per_host=2, gap=0.5):
        self.per_host, self.gap = per_host, gap
        self.lock = threading.Lock()
        self.sems, self.last = {}, {}

    def __call__(self, url):
        host = urllib.parse.urlparse(url).netloc
        with self.lock:
            sem = self.sems.setdefault(host, threading.Semaphore(self.per_host))
        return _Slot(self, host, sem)


class _Slot:
    def __init__(self, gate, host, sem):
        self.gate, self.host, self.sem = gate, host, sem

    def __enter__(self):
        self.sem.acquire()
        with self.gate.lock:
            wait = self.gate.last.get(self.host, 0) + self.gate.gap - time.time()
            self.gate.last[self.host] = max(time.time(), self.gate.last.get(self.host, 0) + self.gate.gap)
        if wait > 0:
            time.sleep(wait)

    def __exit__(self, *exc):
        self.sem.release()


def pages(urls, max_chars=60000, workers=6, per_host=2):
    """Fetch many pages at once, politely: several sites in parallel, few hits per site."""
    gate = HostGate(per_host)

    def one(u):
        with gate(u):
            return list(page(u, max_chars))

    failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(one, u): u for u in urls}
        for fut in concurrent.futures.as_completed(futures):
            try:
                yield from fut.result()
            except (OSError, ValueError) as e:
                failed += 1
                code = getattr(e, "code", None)
                sys.stderr.write("wedge fetch: skipped %s (%s)\n" % (futures[fut], ("HTTP %s" % code) if code else getattr(e, "reason", e)))
    if failed:
        sys.stderr.write("wedge fetch: %d of %d pages failed; the rest were saved\n" % (failed, len(urls)))


def read_urls(items, from_file):
    urls = list(items or [])
    if from_file:
        fh = sys.stdin if from_file == "-" else open(from_file, encoding="utf-8")
        urls += [l.strip() for l in fh if l.strip() and not l.lstrip().startswith("#")]
    out = []
    for u in urls:
        if u not in out:
            out.append(u)
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description="Wedge: fetch customer voice from free sources.")
    p.add_argument("--out", help="append JSONL to this file instead of stdout")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--out", default=argparse.SUPPRESS, help="append JSONL to this file instead of stdout")
    sp = p.add_subparsers(dest="cmd", required=True)
    _add = sp.add_parser
    sp.add_parser = lambda *a, **k: _add(*a, parents=[common], **k)  # accept --out after the subcommand too

    a = sp.add_parser("hn"); a.add_argument("query"); a.add_argument("--limit", type=int, default=50)
    a.add_argument("--kind", choices=["all", "story", "comment"], default="all")

    a = sp.add_parser("reddit"); a.add_argument("query"); a.add_argument("--limit", type=int, default=50)
    a.add_argument("--sub"); a.add_argument("--sort", default="relevance")
    a.add_argument("--time", default="all", dest="t")

    a = sp.add_parser("reddit-thread"); a.add_argument("url"); a.add_argument("--limit", type=int, default=100)

    a = sp.add_parser("appstore-search"); a.add_argument("term"); a.add_argument("--limit", type=int, default=25)
    a.add_argument("--country", default="us")

    a = sp.add_parser("appstore-reviews"); a.add_argument("app_id"); a.add_argument("--pages", type=int, default=3)
    a.add_argument("--country", default="us"); a.add_argument("--max-rating", type=int, default=5)

    a = sp.add_parser("github-issues"); a.add_argument("query"); a.add_argument("--limit", type=int, default=50)

    a = sp.add_parser("page"); a.add_argument("url"); a.add_argument("--max-chars", type=int, default=60000)

    a = sp.add_parser("pages", help="fetch many pages in parallel")
    a.add_argument("urls", nargs="*"); a.add_argument("--from", dest="from_file", help="file of URLs, one per line ('-' for stdin)")
    a.add_argument("--max-chars", type=int, default=60000); a.add_argument("--workers", type=int, default=6)
    a.add_argument("--per-host", type=int, default=2, help="max parallel requests to one site (default 2)")

    a = sp.add_parser("links", help="list links on a page (prints URLs, not JSON)")
    a.add_argument("url"); a.add_argument("--match", help="regex the URL must match"); a.add_argument("--limit", type=int, default=200)

    args = p.parse_args(argv)
    if args.cmd == "links":
        try:
            for u in links(args.url, args.match, args.limit):
                print(u)
        except (OSError, ValueError) as e:
            sys.stderr.write("wedge fetch: links failed (%s)\n" % getattr(e, "reason", e))
            return 2
        return 0
    gen = {
        "hn": lambda: hn(args.query, args.limit, args.kind),
        "reddit": lambda: reddit(args.query, args.limit, args.sub, args.sort, args.t),
        "reddit-thread": lambda: reddit_thread(args.url, args.limit),
        "appstore-search": lambda: appstore_search(args.term, args.limit, args.country),
        "appstore-reviews": lambda: appstore_reviews(args.app_id, args.pages, args.country, args.max_rating),
        "github-issues": lambda: github_issues(args.query, args.limit),
        "page": lambda: page(args.url, args.max_chars),
        "pages": lambda: pages(read_urls(args.urls, args.from_file), args.max_chars, args.workers, args.per_host),
    }[args.cmd]

    out = open(args.out, "a", encoding="utf-8") if args.out else sys.stdout
    n = 0
    try:
        for r in gen():
            out.write(json.dumps(r, ensure_ascii=False) + "\n")
            n += 1
    except urllib.error.HTTPError as e:
        sys.stderr.write("wedge fetch: %s returned HTTP %s. Fall back to web search for this source.\n" % (args.cmd, e.code))
        return 2
    except (urllib.error.URLError, OSError) as e:
        sys.stderr.write("wedge fetch: network error (%s). Fall back to web search.\n" % getattr(e, "reason", e))
        return 2
    finally:
        if args.out:
            out.close()
    sys.stderr.write("wedge fetch: %d records from %s\n" % (n, args.cmd))
    if n == 0:
        sys.stderr.write("wedge fetch: no results. If no error was printed above, the source answered but had nothing; try broader words.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
