---
name: wedge-competitor-map
description: Map every competitor in a niche with real pricing, positioning, feature coverage, strengths and weaknesses, all cited. Builds a feature matrix and finds where the market is crowded and where it is empty. Use for "who are my competitors", "competitor analysis", "compare X vs Y", "what does the market look like", or before trying to beat incumbents.
---

# Wedge: competitor map

Builds an evidence-backed map of who already serves the niche and how. Part of the Wedge pipeline; it also works on its own.

Scripts are in the `wedge` skill's `scripts/` folder, usually `../wedge/scripts/`.

## Steps

1. **Find competitors** with web search: `"<niche> software"`, `"best <job> tool"`, `"alternative to <known leader>"`, `"<leader> vs"`, plus app store search (`fetch.py appstore-search "<term>"`) and GitHub for open-source options. Include:
   - Direct competitors (same job, same buyer).
   - Substitutes, which are the real competition for small buyers: spreadsheets, an agency, a VA, doing nothing.
   - Quick depth: 3 to 5. Deep depth: 6 to 12.
2. **Pricing and positioning:** fetch every competitor's pricing page and homepage in one call: `fetch.py --out ideas/<slug>/raw/competitors.jsonl pages <url1> <url2> ...`. Record:
   - The real price tiers and what's gated where.
   - Free tier or trial.
   - Contract terms.
   - The headline promise, quoted exactly.
   - If pricing is hidden ("contact sales"), say so. That's a signal.
3. **Feature coverage.** Choose 8 to 15 features the buyer actually cares about. Take them from the review and complaint language, not the vendors' feature lists. Mark each competitor `yes`, `no` or `partial`, based on its docs or pricing page.
4. **Strengths and weaknesses.** Strengths come from what happy reviewers praise; weaknesses come from complaints. Cite both. `wedge-review-miner` goes deeper; here you only need enough to sketch each competitor.

## Output: `ideas/<slug>/competitors.md` (short notes in quick mode, full detail in deep)

- A table of name, URL, starting price, model (per seat, flat or usage), free option, contract, and headline.
- One short section per competitor covering who it's really for, strong at, weak at, and evidence IDs.
- The feature matrix as a table.
- **Where it's crowded and where it's empty:** 3 to 5 bullets. For example: "Everyone does X. Nobody under $50/mo does Y."

Quote pricing and claims exactly in `evidence.jsonl` with `claim: comp-<name>`. Run `state.py done <slug> competitors`.

## Don't

- Don't guess prices. Mark them "not public".
- Don't treat a vendor's marketing claims as facts about the product. Treat them as positioning.
