# Changelog

## 1.0.0 (2026-10-17)

First release.

- Eight skills: `wedge`, `wedge-niche-scout`, `wedge-competitor-map`, `wedge-review-miner`, `wedge-gap-ranker`, `wedge-win-plan`, `wedge-launch-kit`, `wedge-watch`.
- Four modes (from scratch, from what you know, stress-test an idea, beat my competitors) and two depths (quick, deep).
- Zero-dependency Python scripts: `fetch.py`, `signals.py`, `verify.py`, `domain.py`, `state.py`, `report.py`.
- Quote verification with a two-source rule. Official vendor pages count alone for a vendor's own claims. When a live source blocks re-checking, quotes are matched against the raw text saved at fetch time (`captured`).
- Reddit through its public JSON, or its official API with free app credentials (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`).
- Self-contained HTML report and a 1200x630 share card.
- Three example runs: a simpler invoicing app for solo tradespeople (idea), tools for Shopify merchants (expertise), and taking customers from Bookly and Amelia (compete).
- `fetch.py pages` fetches many URLs in parallel (at most 2 at a time per site), and `fetch.py links` lists a page's links to feed into it. Batching is the biggest speed-up in a run.
- Animated terminal demo for the README (`docs/demo.svg`, rebuilt with `docs/make_demo.py`).
- `fetch.py page` reads Shopify App Store and WordPress.org review pages. A quote can back several claims (`"claim": [...]`).
