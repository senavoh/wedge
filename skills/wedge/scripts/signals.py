#!/usr/bin/env python3
"""Wedge signals: turn a pile of raw records into a short, cited digest.

Reads JSONL from fetch.py and scans every sentence for demand and pain
patterns (wishes, switching, price, support, bugs, missing features,
complexity, lock-in). Prints a compact markdown digest the agent can read
instead of the raw dump, which keeps runs cheap. Every snippet is an exact
sentence from the source plus its URL, so it can be quoted and verified.

Usage:
    python3 signals.py raw.jsonl [more.jsonl ...] [--names "Acme,Globex"] [--top 5] [--json out.json]
    python3 signals.py raw/*.jsonl --find "renewal,price increase" [--limit 15]

--find prints only the exact sentences that contain any of the terms, each
with its URL and date, ready to paste into evidence.jsonl. Use it instead of
opening raw files: it is much cheaper than reading whole pages.
"""
import argparse
import collections
import json
import re
import sys

PATTERNS = collections.OrderedDict([
    ("wish", [r"\bi wish\b", r"wish there (was|were)", r"is there (a|an|any) (tool|app|service|software|way)",
              r"looking for (a|an) (tool|app|service|software|alternative)", r"does anyone know (a|an|of)",
              r"would (pay|love) (for|to have)", r"someone should (build|make)", r"why (is there no|isn't there)"]),
    ("switching", [r"alternative(s)? to\b", r"switch(ed|ing)? (from|to|away)", r"mov(ed|ing) (away )?from",
                   r"migrat(e|ed|ing) (from|to|off)", r"replac(e|ed|ing) (it|them|our)", r"looking to leave",
                   r"\bditch(ed|ing)?\b", r"(leaving|left|dropped|dropping) (them|it) for"]),
    ("price", [r"too expensive", r"price (increase|hike)", r"raised (their|the) prices?", r"overpriced",
               r"can'?t afford", r"per (seat|user|tech|agent)", r"\bpricing\b", r"cost(s)? (too|way) much",
               r"not worth (the|it)", r"hidden (fees|costs)"]),
    ("support", [r"(customer )?support (is|was|has been) (terrible|awful|bad|slow|useless|non-?existent)",
                 r"no (response|reply|answer) from", r"never (replied|responded|got back)",
                 r"(bad|terrible|awful|horrible|poor) (customer )?(service|support)",
                 r"waiting (days|weeks)", r"account manager"]),
    ("bugs", [r"\bbuggy\b", r"\bcrash(es|ed|ing)?\b", r"\bbroken\b", r"doesn'?t work", r"\bslow\b",
              r"\bglitch", r"\blag(gy|s)?\b", r"keeps (failing|breaking|crashing)", r"\bdowntime\b"]),
    ("missing", [r"doesn'?t (have|support|offer|let)", r"\black(s|ing)\b", r"no way to", r"can'?t even",
                 r"feature request", r"wish it (had|could)", r"still (no|doesn'?t|can'?t)",
                 r"(is|are) missing (a|an|the|basic)"]),
    ("complexity", [r"too (complicated|complex)", r"learning curve", r"\bconfusing\b", r"\bclunky\b",
                    r"\bbloated\b", r"hard to (use|set up|setup|configure)", r"\bunintuitive\b", r"steep"]),
    ("lockin", [r"(\d+[- ](year|yr|month)|long|annual|multi-?year) contract", r"contract (renewal|term|lock)",
                r"locked (in|into)", r"can'?t (export|cancel|get out)", r"\bauto-?renew", r"cancell?ation (fee|policy)",
                r"\bminimum (term|seats|commitment)", r"held hostage", r"\bhostage\b"]),
])
COMPILED = {k: [re.compile(p, re.I) for p in v] for k, v in PATTERNS.items()}
SENT_RE = re.compile(r"(?<=[.!?])\s+|\n+")


def sentences(text):
    for s in SENT_RE.split(text or ""):
        s = s.strip().lstrip("#*->\\ ").strip()
        if 25 <= len(s) <= 300:
            yield s


def load(paths):
    seen = set()
    for p in paths:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                key = (r.get("url"), r.get("text", "")[:80])
                if key in seen:
                    continue
                seen.add(key)
                yield r


def analyze(records, names=None, top=8):
    names = [n.strip() for n in (names or []) if n.strip()]
    name_res = {n: re.compile(r"\b%s\b" % re.escape(n), re.I) for n in names}
    hits = collections.defaultdict(list)
    mentions = collections.Counter()
    mention_pain = collections.defaultdict(collections.Counter)
    sources = collections.Counter()
    total = 0
    for r in records:
        total += 1
        sources[r.get("source", "?")] += 1
        body = " ".join(x for x in (r.get("title"), r.get("text")) if x)
        found_names = [n for n, rx in name_res.items() if rx.search(body)]
        for n in found_names:
            mentions[n] += 1
        for s in sentences(body):
            for cat, rxs in COMPILED.items():
                if any(rx.search(s) for rx in rxs):
                    weight = 1 + min(int(r.get("score") or 0), 200) / 50.0
                    if r.get("rating") is not None and r.get("source") == "appstore" and r["rating"] <= 2:
                        weight += 1
                    hits[cat].append({"quote": s, "url": r.get("url"), "source": r.get("source"),
                                      "date": r.get("date"), "weight": round(weight, 2)})
                    for n in found_names:
                        mention_pain[n][cat] += 1
    digest = {"records": total, "sources": dict(sources), "categories": {}, "competitors": {}}
    for cat in PATTERNS:
        items = sorted(hits.get(cat, []), key=lambda h: -h["weight"])
        uniq, seen_q = [], set()
        for h in items:
            k = h["quote"].lower()[:60]
            if k in seen_q:
                continue
            seen_q.add(k)
            uniq.append(h)
        digest["categories"][cat] = {"count": len(items), "distinct_sources": len({h["url"] for h in items}),
                                     "top": uniq[:top]}
    for n in names:
        digest["competitors"][n] = {"mentions": mentions[n], "pain_by_category": dict(mention_pain[n])}
    return digest


def to_markdown(d):
    out = ["# Signal digest", "",
           "%d records from %s" % (d["records"], ", ".join("%s (%d)" % kv for kv in d["sources"].items())), ""]
    ranked = sorted(d["categories"].items(), key=lambda kv: -kv[1]["count"])
    out.append("| Category | Hits | Distinct sources |")
    out.append("|---|---|---|")
    for cat, c in ranked:
        out.append("| %s | %d | %d |" % (cat, c["count"], c["distinct_sources"]))
    if d["competitors"]:
        out += ["", "## Competitor mentions", "", "| Name | Mentions | Top pains |", "|---|---|---|"]
        for n, c in sorted(d["competitors"].items(), key=lambda kv: -kv[1]["mentions"]):
            pains = ", ".join("%s %d" % kv for kv in sorted(c["pain_by_category"].items(), key=lambda kv: -kv[1])[:3])
            out.append("| %s | %d | %s |" % (n, c["mentions"], pains or "-"))
    for cat, c in ranked:
        if not c["top"]:
            continue
        out += ["", "## %s" % cat, ""]
        for h in c["top"]:
            out.append('- "%s" ([%s](%s)%s)' % (h["quote"], h["source"], h["url"], ", " + h["date"] if h["date"] else ""))
    return "\n".join(out) + "\n"


def find(records, terms, limit=15):
    """Print exact sentences containing any term, complaints first, then newest."""
    rxs = [re.compile(re.escape(t), re.I) for t in terms]
    pain = [rx for v in COMPILED.values() for rx in v]
    seen, hits = set(), []
    for r in records:
        body = " ".join(x for x in (r.get("title"), r.get("text")) if x)
        for snt in sentences(body):
            if any(rx.search(snt) for rx in rxs):
                k = snt.lower()[:80]
                if k in seen:
                    continue
                seen.add(k)
                is_pain = 1 if any(rx.search(snt) for rx in pain) else 0
                low_star = 1 if (r.get("rating") or 5) <= 2 else 0
                hits.append((is_pain + low_star, r.get("date") or "", snt, r.get("url"), r.get("source")))
    hits.sort(key=lambda h: (h[0], h[1]), reverse=True)
    for _, d, snt, url, src in hits[:limit]:
        print('"%s"\n    %s %s %s' % (snt, src, d, url))
    sys.stderr.write("signals: %d matching sentences, showing %d\n" % (len(hits), min(limit, len(hits))))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Wedge: digest raw records into cited pain signals.")
    p.add_argument("files", nargs="+")
    p.add_argument("--names", default="", help="comma-separated competitor names to count")
    p.add_argument("--top", type=int, default=5, help="quotes kept per category (default 5)")
    p.add_argument("--find", help="comma-separated terms: print matching sentences with URLs instead of a digest")
    p.add_argument("--limit", type=int, default=15, help="max sentences for --find (default 15)")
    p.add_argument("--json", help="also write the full digest as JSON here")
    p.add_argument("--topic", default="", help="comma-separated topic words; drop records that mention none of these or of --names")
    a = p.parse_args(argv)
    records = load(a.files)
    if a.find:
        return find(records, [t.strip() for t in a.find.split(",") if t.strip()], a.limit)
    # --topic filters; competitor --names count as on-topic too, but never filter on their own.
    terms = [t.strip().lower() for t in (a.topic + "," + a.names).split(",") if t.strip()] if a.topic.strip() else []
    if terms:
        records = (r for r in records
                   if any(t in ("%s %s" % (r.get("title", ""), r.get("text", ""))).lower() for t in terms))
    d = analyze(records, a.names.split(","), a.top)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
    sys.stdout.write(to_markdown(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
