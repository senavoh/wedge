---
name: wedge-watch
description: Re-check a market you already ran Wedge on and report what changed. New competitor complaints, price changes, new entrants and fresh switching triggers since the last run. Use monthly for an existing business or a live idea, or for "what changed with my competitors", "any new complaints about X", "competitor update", "monitor competitors".
---

# Wedge: watch

Keeps a finished run current. This is what turns Wedge from a one-off report into a monthly habit.

Scripts are in the `wedge` skill's `scripts/` folder, usually `../wedge/scripts/`.

## Steps

1. Open `ideas/<slug>/` and read `state.json`, `competitors.md`, `pains.md` and `win-plan.md`. Find the date of the last run (`state.json` → `updated`, or the newest `watch-*.md`).
2. **Pricing and positioning drift:** run `fetch.py page` on each competitor's pricing page and homepage. Compare against the quotes saved in `evidence.jsonl` (`claim: comp-<name>`) and record any changes.
3. **New complaints:** run the same review fetches as `wedge-review-miner` into `raw/watch-<date>.jsonl`, using `--sort new` for Reddit where possible. Then run `signals.py` with `--names`. Keep only records dated after the last run.
4. **New entrants:** search `"alternative to <leader>"`, Product Hunt, and `"<category>" launch` limited to the period since the last run.
5. **Fresh triggers:** look for price hikes, acquisitions, outages and shutdowns. Each one is a switching moment. Pair it with a move from `win-plan.md`, or propose a new one.
6. Add new quotes to `evidence.jsonl` and run `verify.py`.

## Output: `ideas/<slug>/watch-<YYYY-MM-DD>.md`

- **Act this week:** 1 to 3 specific moves, such as "<Competitor> raised prices 20% on Oct 2. Post your price-lock offer in r/<sub> and DM the 6 people complaining."
- What changed, per competitor: pricing, positioning, new complaints, each with evidence IDs.
- New entrants.
- Whether the gap is still open: yes, narrowing or closed, with the reason.

Suggest that the user runs this monthly. If their agent supports scheduled tasks, offer to set one up.
