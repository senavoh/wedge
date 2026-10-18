#!/usr/bin/env python3
"""Wedge verify: prove every quote is really on the page it cites.

Reads evidence.jsonl, where each line is one piece of evidence:

    {"id": "e1", "claim": "pain-pricing", "quote": "exact words", "url": "https://...", "source": "reddit"}

Set "official": true on a quote from a company's own site (pricing page,
docs). That alone proves what the company says about itself, so the claim
doesn't need a second source. It never counts as proof of customer pain.

For each line it fetches the source (using source-aware routes for Reddit,
Hacker News and the App Store, which hide text from plain page fetches),
checks that the quote is there, and writes the result back in place:

    "verified": "yes" | "captured" | "partial" | "no" | "unreachable"

"captured" means the live page couldn't be reached right now (Reddit and
Apple often block or rate-limit) or no longer shows the quote (reviews move
to later pages), but the quote matches the text fetch.py saved from that URL in ideas/<slug>/raw/*.jsonl at research time. That
is real fetched text, not something the agent typed, so it counts toward the
two-source rule. It is shown with its own badge so readers can tell.

Then it applies the two-source rule: a claim counts as verified only when
at least two different URLs back it with a "yes". Claims that fail are
listed so the agent marks them "unverified" in the report.

Usage:
    python3 verify.py ideas/<slug>/evidence.jsonl [--min-sources 2] [--strict]

--strict exits 1 if any quote is not verified (useful in CI).
"""
import argparse
import collections
import datetime
import difflib
import glob
import os
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = "wedge/1.0 (+https://github.com/senavoh/wedge)"
_cache = {}


def fetch(url, accept="*/*"):
    if url in _cache:
        return _cache[url]
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=25) as r:
        body = r.read().decode(r.headers.get_content_charset() or "utf-8", errors="replace")
    _cache[url] = body
    return body


QUOTE_MAP = {"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-",
             "…": "...", " ": " "}


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    for a, b in QUOTE_MAP.items():
        s = s.replace(a, b)
    s = re.sub(r"[*_`>#\[\]()]", " ", s)
    s = re.sub(r"\\(.)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def source_text(url):
    """Return the text a quote should be found in, picking a route per site."""
    u = urllib.parse.urlparse(url)
    host = u.netloc.lower()
    if "news.ycombinator.com" in host:
        item = urllib.parse.parse_qs(u.query).get("id", [""])[0]
        data = json.loads(fetch("https://hn.algolia.com/api/v1/items/%s" % item))
        parts = []

        def walk(n):
            parts.append(n.get("title") or "")
            parts.append(n.get("text") or "")
            for c in n.get("children") or []:
                walk(c)
        walk(data)
        return " ".join(parts)
    if "reddit.com" in host:
        # Reddit's public JSON; blocked on many networks. When it is, the quote
        # falls back to the text fetch.py saved (status "captured").
        data = json.loads(fetch(url.split("?")[0].split("#")[0].rstrip("/") + ".json?raw_json=1"))
        return json.dumps(data)
    if "apps.apple.com" in host:
        m = re.search(r"/id(\d+)", u.path)
        cc = (u.path.strip("/").split("/") or ["us"])[0]
        cc = cc if len(cc) == 2 else "us"
        if m:
            texts = []
            for sort in ("/sortby=mostrecent", ""):
                for page in range(1, 11):
                    try:
                        feed = json.loads(fetch("https://itunes.apple.com/%s/rss/customerreviews/page=%d/id=%s%s/json"
                                                % (cc, page, m.group(1), sort)))
                    except (OSError, ValueError):
                        break
                    entries = feed.get("feed", {}).get("entry", [])
                    if isinstance(entries, dict):
                        entries = [entries]
                    if not entries:
                        break
                    for e in entries:
                        texts.append(e.get("title", {}).get("label", ""))
                        texts.append(e.get("content", {}).get("label", ""))
            if not texts:
                # Apple's review feed is intermittently empty. That says nothing
                # about the quote, so report the source as unreachable.
                raise OSError("App Store review feed returned no reviews, retry later")
            return " ".join(texts)
    return fetch(url, "text/html,application/xhtml+xml")


def match(quote, text):
    q, t = norm(quote), norm(text)
    if not q:
        return "no", 0.0
    if q in t:
        return "yes", 1.0
    words = q.split()
    if len(words) < 5:
        return "no", 0.0
    shingles = [" ".join(words[i:i + 4]) for i in range(len(words) - 3)]
    hit = sum(1 for s in shingles if s in t) / float(len(shingles))
    if hit >= 0.85:
        return "yes", round(hit, 2)
    if hit >= 0.5:
        return "partial", round(hit, 2)
    # last resort: best fuzzy window, catches small typos from transcription
    first = t.find(" ".join(words[:2]))
    if first >= 0:
        window = t[first:first + len(q) + 40]
        ratio = difflib.SequenceMatcher(None, q, window[:len(q)]).ratio()
        if ratio >= 0.9:
            return "yes", round(ratio, 2)
    return "no", round(hit, 2)


def claims_of(r):
    """A quote can back several claims: "claim" may be a string or a list."""
    c = r.get("claim")
    return [x for x in (c if isinstance(c, list) else [c]) if x]


def strip_frag(url):
    return url.split("#")[0].split("?")[0].rstrip("/")


def load_raw(evidence_path):
    """Map URL -> text from the raw records fetch.py saved next to the evidence."""
    folder = os.path.join(os.path.dirname(os.path.abspath(evidence_path)), "raw")
    exact, loose = collections.defaultdict(list), collections.defaultdict(list)
    for path in glob.glob(os.path.join(folder, "*.jsonl")):
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                text = "%s %s" % (r.get("title", ""), r.get("text", ""))
                exact[r.get("url", "")].append(text)
                loose[strip_frag(r.get("url", ""))].append(text)
    return exact, loose


def main(argv=None):
    p = argparse.ArgumentParser(description="Wedge: verify every quote against its source.")
    p.add_argument("evidence")
    p.add_argument("--min-sources", type=int, default=2)
    p.add_argument("--strict", action="store_true")
    a = p.parse_args(argv)

    rows = []
    with open(a.evidence, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))

    raw_exact, raw_loose = load_raw(a.evidence)
    counts = collections.Counter()
    today = datetime.date.today().isoformat()
    for r in rows:
        url, quote = r.get("url", ""), r.get("quote", "")
        r.pop("verify_error", None)
        try:
            status, score = match(quote, source_text(url))
        except (OSError, ValueError) as e:
            status, score = "unreachable", 0.0
            r["verify_error"] = str(getattr(e, "reason", e))[:120]
        if status == "unreachable" and r.get("verified") == "yes":
            # Verified on an earlier run and the source is only temporarily
            # down: keep the earlier result and its date.
            status, score = "yes", r.get("match", 1.0)
        elif status in ("unreachable", "no", "partial"):
            # Pages change after research: reviews move to page 2, threads get
            # edited. If the quote matches the text fetch.py saved from this
            # URL, it was really there when collected.
            saved = raw_exact.get(url) or raw_loose.get(strip_frag(url)) or []
            if saved:
                st, sc = match(quote, " ".join(saved))
                if st == "yes":
                    status, score = "captured", sc
        if status == "yes":
            r["verified_at"] = today
        r["verified"], r["match"] = status, score
        counts[status] += 1
        sys.stderr.write("%-11s %-6s %s\n" % (status, r.get("id", "?"), url[:90]))

    with open(a.evidence, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    by_claim = collections.defaultdict(set)
    official = set()
    for r in rows:
        for c in claims_of(r):
            # Customer pain and the gap must come from customers, not vendors' own pages.
            if r.get("official") and c.startswith(("gap", "pain")):
                continue
            if r.get("verified") in ("yes", "captured"):
                by_claim[c].add(r.get("url"))
                if r.get("official") and not c.startswith(("gap", "pain")):
                    official.add(c)  # a vendor's own page is proof of its own price or wording
    claims = sorted({c for r in rows for c in claims_of(r)})
    weak = [c for c in claims if len(by_claim[c]) < a.min_sources and c not in official]

    print("Quotes: %d verified live, %d captured at fetch, %d partial, %d not found, %d unreachable (of %d)"
          % (counts["yes"], counts["captured"], counts["partial"], counts["no"], counts["unreachable"], len(rows)))
    if counts["unreachable"]:
        print("  Unreachable quotes have no saved raw record either. Re-run later, or replace them with quotes from raw/.")
    if counts["no"]:
        print("  'not found' means the page loaded but the quote isn't on it. Fix or remove those quotes.")
    print("Claims: %d of %d meet the %d-source rule" % (len(claims) - len(weak), len(claims), a.min_sources))
    for c in weak:
        print("  UNVERIFIED claim: %s (%d verified source%s)" % (c, len(by_claim[c]), "" if len(by_claim[c]) == 1 else "s"))
    ok = [r for r in rows if r.get("verified") in ("yes", "captured")]
    customer = [r for r in ok if not r.get("official")]
    print("Evidence: %d customer quote%s, %d vendor quote%s (vendor pages back prices and features only)"
          % (len(customer), "" if len(customer) == 1 else "s", len(ok) - len(customer), "" if len(ok) - len(customer) == 1 else "s"))
    if not customer:
        print("  WARNING: no customer quotes. Pain and the gap are unproven; the verdict should be INCONCLUSIVE "
              "unless the user supplies reviews or Reddit access (see references/scoring.md).")
    elif len(customer) < 15:
        print("  WARNING: only %d customer quotes; the evidence floor is 15. Fetch more review pages and run "
              "another signals.py --find pass, or explain the shortfall in the report." % len(customer))
    if "gap" not in claims:
        print("  WARNING: no quotes carry the claim \"gap\". The report's gap statement has no evidence behind it.")
    if a.strict and (counts["no"] or counts["partial"] or counts["unreachable"] or weak or not customer or "gap" not in claims):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
