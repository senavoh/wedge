# Changelog

## Unreleased

- 12 new real example runs, 16 in total: 11 PIVOT, 5 KILL, 0 GO. They include Wedge stress-testing a paid version of itself (KILL) and Wedge testing its own pivot (the score went down). README and site list them all; raw data is trimmed to the records behind each quote.
- Site: a labelled illustration of what a GO takes, kept separate from the real runs.
- Critic risks are `high` (and can block a GO) only when they are specific to the idea and backed by a cited source. Generic risks like "an incumbent could copy it" are `medium`. Reports show the source behind each risk.
- A recommended pivot must beat the current score: Wedge pre-checks 2 or 3 candidate pivots (does it already exist? is there a free incumbent?), scores them, and recommends one only if its projected total is higher. If none is, it says so and suggests a cheap test instead. Reports show the projected score.
- After a PIVOT, Wedge offers once to stress-test the pivot as a new run. The follow-up report links back to the original and shows projected vs actual score.
- Docs and the `fetch.py` Reddit message no longer call Reddit API keys free and self-serve: new Reddit apps need Reddit's approval. The fallback is web search, keyless marketplace reviews, or reviews the user pastes.

## 1.1.0 (2026-10-18)

Uses fewer tokens by default.

- Quick mode is the default; deep runs only when asked or clearly high-stakes.
- `fetch.py` prints a short preview instead of raw records when `--out` is missing (preview shows app IDs and ratings).
- `signals.py --find "terms"` prints only matching sentences with URLs, complaints and low-star reviews first. Digest defaults to 5 quotes per category.
- "Keep it lean" rules in the skill: never read raw files, write each fact once, extras (landing page, drafts) on request in quick mode.
- Gap and pain claims must rest on customer quotes; vendor pages only back price and feature claims.
- Clearer verdict rule when evidence exists but can't be re-checked.
- New INCONCLUSIVE verdict when no customer voice could be reached, and a fallback: ask the user to paste reviews or add Reddit access.
- Evidence floor for quick runs: at least 150 raw records, 3 customer quotes per main pain theme, 15 in total. `verify.py` reports customer vs vendor quotes and warns when there are none, fewer than 15, or no gap evidence.
- `state.py done/status` works from any folder inside the project, including the run folder.
- Installer: a piped install (`curl … | sh`) always downloads from GitHub, even when run inside a copy of the repo.
- getwedge.dev now deploys on Vercel; the GitHub Pages workflow is removed.
- Measured: a quick run dropped from about 123k to about 100k tokens (runs: 99k, 102k, 93k, 102k). The 102k WordPress-backup run met the new evidence floor: 307 records, 19 customer quotes, every pain theme backed by 6–7 sources.

## 1.0.0 (2026-10-17)

First release.

- Eight skills: `wedge`, `wedge-niche-scout`, `wedge-competitor-map`, `wedge-review-miner`, `wedge-gap-ranker`, `wedge-win-plan`, `wedge-launch-kit`, `wedge-watch`.
- Four modes (from scratch, from what you know, stress-test an idea, beat my competitors) and two depths (quick, deep).
- Zero-dependency Python scripts: `fetch.py`, `signals.py`, `verify.py`, `domain.py`, `state.py`, `report.py`.
- Quote verification with a two-source rule. Official vendor pages count alone for a vendor's own claims. When a live source blocks re-checking, quotes are matched against the raw text saved at fetch time (`captured`).
- Reddit through its public JSON, or its official API with free app credentials (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`).
- Self-contained HTML report and a 1200x630 share card.
- Four example runs, one per mode, including a timed deep run (29 minutes). Earlier three: a simpler invoicing app for solo tradespeople (idea), tools for Shopify merchants (expertise), and taking customers from Bookly and Amelia (compete).
- `fetch.py pages` fetches many URLs in parallel (at most 2 at a time per site), and `fetch.py links` lists a page's links to feed into it. Batching is the biggest speed-up in a run.
- `fetch.py` follows 308 redirects, decodes compressed pages, labels page records by site, and creates `--out` folders; `state.py init` creates `raw/`; `report.py` handles list-valued claims.
- Animated terminal demo for the README (`docs/demo.svg`, rebuilt with `docs/make_demo.py`).
- `fetch.py page` reads Shopify App Store and WordPress.org review pages. A quote can back several claims (`"claim": [...]`).
