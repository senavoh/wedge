---
name: wedge-review-miner
description: Mine what customers actually hate about competitors from app store reviews, Reddit threads, Hacker News, GitHub issues and review-site snippets. Clusters complaints into themes with severity and per-competitor counts, every theme backed by exact verified quotes. Use for "what do customers complain about", "find pain points", "mine reviews", "why do people leave X", "what is X missing".
---

# Wedge: review miner

Turns thousands of scattered complaints into a handful of cited pain themes. Part of the Wedge pipeline; it also works on its own.

Scripts are in the `wedge` skill's `scripts/` folder, usually `../wedge/scripts/`.

## Steps

1. **Collect** for each competitor in `competitors.md`, appending to `ideas/<slug>/raw/reviews.jsonl`:
   - **App Store:** `fetch.py appstore-search "<name>"` to get the `app_id`, then `fetch.py appstore-reviews <app_id> --max-rating 3 --pages 5`. The 1 to 3 star reviews are where the gaps are. Apple's feed is sometimes empty for an hour or more. If it is, move on and retry at the end of the run.
   - **Reddit:** `fetch.py reddit "<name>" --limit 60` plus `"<name> alternative"`, `"<name> expensive"`, `"leaving <name>"`. Fetch the comments of the best threads with `fetch.py reddit-thread <url>`. Restrict to the buyer's own communities with `--sub <subreddit>` (for example `--sub doggrooming`), which cuts the noise sharply. If Reddit refuses the request, follow the fallback in the `wedge` skill.
   - **Hacker News:** `fetch.py hn "<name>"`.
   - **GitHub** (open-source or dev tools): `fetch.py github-issues "repo:<owner>/<repo> is:issue sort:reactions-+1-desc"`.
   - **App marketplaces with public review pages:** if the competitors are apps or plugins, their marketplace reviews are the richest free source, and `fetch.py page` can read them:
     - Shopify App Store: `fetch.py --out raw/reviews.jsonl page "https://apps.shopify.com/<handle>/reviews?ratings%5B%5D=1"` (change the rating to 2 or 3 for more).
     - WordPress.org plugins: `https://wordpress.org/support/plugin/<slug>/reviews/?filter=1` lists 1-star review titles. Get the review links with `fetch.py links <that url> --match /support/topic/`, then fetch them all at once with `fetch.py --out raw/reviews.jsonl pages --from <file>`.
     - Use `pages` for any batch of URLs (several apps' review pages, all competitors' pricing pages). One parallel call is much faster than many single `page` calls.
   - **G2, Capterra, Trustpilot, Google Play and Yelp:** use web search, for example `"<name> reviews cons"` or `site:g2.com <name>`, and quote only from pages you opened. Don't scrape those sites directly; their terms forbid it.
   - **Local businesses** (gyms, plumbers, salons): search for `"<name> reviews"` and Google Maps or Yelp review snippets, and include the city.
   - Quick depth: about 100 records total. Deep depth: as many as the sources give, usually 300 to 1,500.
2. **Digest:** `signals.py ideas/<slug>/raw/reviews.jsonl --names "<Comp A>,<Comp B>,..." --top 12 --json ideas/<slug>/signals.json > ideas/<slug>/signals.md`. Read `signals.md`. Open raw records only to pull a specific quote.
3. **Theme.** Merge signal categories into 4 to 8 pain themes in the customer's language, such as "Price jumps at renewal" or "Can't export my own data". For each theme:
   - **Severity:** high (people leave or threaten to), medium (daily friction), or low (mild annoyance).
   - **Count per competitor:** this feeds the heat map.
   - **At least 2 exact quotes from different URLs,** added to `evidence.jsonl` as `claim: pain-<theme-slug>`.
4. **Look for silence too.** Are there features nobody complains about because nobody offers them? Note them as hypotheses, not facts.

## Output: `ideas/<slug>/pains.md`

Themes ranked by severity × frequency. For each: a one-line summary, counts per competitor and evidence IDs. End with the three themes most likely to make someone switch.

Run `state.py done <slug> reviews`.

## Don't

- Don't paraphrase inside quotation marks. Copy exactly or don't quote.
- Don't let one angry person become a theme. Themes need different authors.
- Treat comparison listicles, "I compared 10 tools" posts and founder launch posts as positioning, not customer pain. They're often written by a vendor.
- Pass `--topic` to `signals.py` with the category's words (for example `"invoice,estimate,contractor"`) so off-topic posts are dropped.
