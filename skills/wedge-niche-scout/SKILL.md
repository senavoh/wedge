---
name: wedge-niche-scout
description: Find business niches with real, unmet demand when someone has no idea yet, or wants ideas from their own expertise. Mines "I wish there was", "is there a tool for", "alternative to" and price-complaint posts across Reddit, Hacker News, app stores and GitHub, then shortlists niches that fit the founder. Use for "give me business ideas", "what should I build", "find me a niche", "what can I build with my skills in X".
---

# Wedge: niche scout

Finds niches where people are already asking for something and not getting it. Part of the Wedge pipeline (`wedge` skill), and it also works on its own.

Scripts are in the `wedge` skill's `scripts/` folder, usually `../wedge/scripts/` next to this skill. If you run it standalone, keep the same `ideas/<slug>/` layout.

## Inputs

- `founder.md` if it exists (budget, skills, hours, risk, online/local). If it doesn't, ask the five founder questions from the `wedge` skill first.
- Mode `expertise`: the field the user knows. Search inside that field.
- Mode `scratch`: no field. Start broad, then let the founder answers narrow it down.

## Steps

1. **Generate search seeds (15 to 25).** Combine demand phrases with fields the founder could serve:
   - Demand phrases: `"I wish there was"`, `"is there an app"`, `"is there a tool"`, `"alternative to"`, `"too expensive"`, `"switched from"`, `"how do you all handle"`, `"spreadsheet for"`, `"still using excel for"`.
   - In `expertise` mode, pair them with that field's tools and jobs, for example `"alternative to ConnectWise"` or `"how do you all handle client offboarding"`.
   - In `scratch` mode, rotate across small-business ops, trades, creators, e-commerce sellers, local services, healthcare admin, education and hobby communities.
2. **Fetch.** For each seed, append to `ideas/<slug>/raw/scout.jsonl` with `fetch.py --out ideas/<slug>/raw/scout.jsonl <source> ...`:
   - `fetch.py reddit "<seed>" --limit 40`
   - `fetch.py hn "<seed>" --limit 30`
   - Add `appstore-search` for consumer or mobile angles, and `github-issues` for developer or tool angles.
   - Quick depth: 8 seeds. Deep depth: all of them.
3. **Digest:** `signals.py ideas/<slug>/raw/scout.jsonl > ideas/<slug>/signals-scout.md`. Read the digest, not the raw file. Use `--find "terms"` for specific quotes.
4. **Cluster** the wish, switching and price signals into candidate niches. A niche is a specific buyer with a specific job, such as "independent bookkeepers reconciling client receipts". "Accounting software" is too broad to count.
5. **Use web search to fill gaps** the fetchers can't reach: Google Play, G2 and Capterra snippets, Product Hunt and niche forums. Take quotes only from pages you actually opened.
6. **Shortlist** 3 niches (quick) or 6 to 8 (deep). Drop any that fail the founder's constraints. Say why each one was dropped.

## Output: `ideas/<slug>/niches.md`

For each niche:
- **Buyer and job:** one line.
- **Signal:** how many hits and from which sources, with 2 or more evidence IDs.
- **Who serves them now:** names only. The competitor map comes next.
- **Founder fit:** one line on why it suits this founder.

Add every quote you rely on to `evidence.jsonl` (see the `wedge` skill). Then run `state.py done <slug> scout`.

## Don't

- Don't pitch trend niches with no complaints behind them ("AI for X") as demand.
- Don't count one viral post as a market. You need repeated signals from different people.
