---
name: wedge
description: Find a business worth building and the gap that lets you win it. Runs the full pipeline, from founder fit and niche discovery through competitor mapping, review mining, gap ranking, a critic pass and a win plan, to a launch kit, with every claim cited and verified. Use when someone asks for a business idea, wants to find a niche, validate or stress-test an idea, research competitors, find what customers hate about competitors, figure out how to beat or take customers from competitors, or says "what should I build", "is this a good idea", "who are my competitors", or "how do I win this market".
---

# Wedge

Wedge turns "I want to start something" into a ranked, evidence-backed opportunity and a plan to take customers from incumbents. It runs as a pipeline of stages. Each stage is also its own skill, so a user can run one piece alone.

**The rule that makes Wedge different: evidence or it didn't happen.** Every pain point, gap and claim about a competitor must link to a real source. A claim needs at least two verified sources from different URLs, or it is shown as "unverified". Never invent quotes, market sizes, revenue figures, review counts or customer numbers. If you don't know, say so and say how to find out.

## Scripts

All scripts are in `scripts/` next to this file. They use only the Python 3.8+ standard library and need no API keys. Run them from the user's project folder, so runs land in `./ideas/`, by giving the full path to this skill's `scripts/` folder. In the examples below, `$W` stands for that path, for example `~/.claude/skills/wedge/scripts`. Write it out in full in each command; don't rely on a shell variable.

```bash
python3 $W/state.py init dog-groomer-app --mode idea --depth quick
python3 $W/fetch.py --out ideas/dog-groomer-app/raw/reviews.jsonl hn "moego" --limit 40
python3 $W/fetch.py --out ideas/dog-groomer-app/raw/reviews.jsonl appstore-reviews 1561621817 --max-rating 3
python3 $W/signals.py ideas/dog-groomer-app/raw/reviews.jsonl --names "MoeGo,Gingr" --topic "groom,grooming,groomer" > ideas/dog-groomer-app/signals.md
python3 $W/verify.py ideas/dog-groomer-app/evidence.jsonl
python3 $W/report.py ideas/dog-groomer-app
```

`--out` appends, and can go before or after the subcommand. Always save raw records with `--out`: `verify.py` uses them as a fallback when a live source blocks re-checking.

**Fetch in batches, not one page at a time.** Each separate command costs you a full round trip, so batching is the biggest speed-up in a run. `pages` fetches many URLs in parallel (politely: at most 2 at a time per site), and `links` lists the links on a page so you can feed them straight in:

```bash
python3 $W/fetch.py links "https://wordpress.org/support/plugin/<slug>/reviews/?filter=1" --match /support/topic/ > ideas/<slug>/raw/urls.txt
python3 $W/fetch.py --out ideas/<slug>/raw/reviews.jsonl pages --from ideas/<slug>/raw/urls.txt
python3 $W/fetch.py --out ideas/<slug>/raw/pricing.jsonl pages https://a.com/pricing https://b.com/pricing https://c.com/pricing
```

| Script | Does |
|---|---|
| `state.py` | Creates `ideas/<slug>/`, tracks finished stages, tells you what's next. Use it to resume. |
| `fetch.py` | Pulls raw customer voice: `hn`, `reddit`, `reddit-thread`, `appstore-search`, `appstore-reviews`, `github-issues`, `page`, and `pages` (many URLs in parallel). `links` lists a page's links to feed into `pages`. Outputs JSONL. |
| `signals.py` | Turns raw JSONL into a short, cited digest of pain and demand signals. Read this instead of raw dumps. `--find "terms"` prints only the matching sentences with URLs, ready to quote. |
| `verify.py` | Fetches every cited source and checks the quote is really there, then applies the two-source rule. |
| `domain.py` | Checks domain and GitHub handle availability through public RDAP. |
| `report.py` | Renders `report.json` + `evidence.jsonl` into `report.html` and a `card.svg` share card. |

If a fetcher fails (network, rate limit, blocked source), fall back to your own web search and fetch tools for that source and keep going. Don't stop the run.

- **Reddit** blocks anonymous requests from many networks. If `fetch.py reddit` says so, search with `site:reddit.com <words>` and read threads with your own fetch tool, and lean on sources that work without keys (App Store, Shopify App Store and WordPress.org reviews, community forums). Reddit API credentials (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`) help only if the user already has them: new Reddit apps need Reddit's approval, so don't send the user to create one. Quotes you get that way may end up `unreachable` in `verify.py`. That's acceptable, but say so in the report.
- **If no customer-voice source works** (Reddit blocked, App Store feeds empty, no marketplace with public reviews), stop collecting and ask the user once. They can paste 10 to 20 reviews or complaints they've seen, add Reddit API credentials if they already have approved access, or tell you to finish without them. Save pasted text with its source to `raw/user-provided.jsonl`, mark those quotes `"source": "user-provided"`, and say so in the report. If they choose to finish without, the verdict is INCONCLUSIVE (see `references/scoring.md`).
- **A page that returns only a cookie or consent banner,** or under about 300 characters of real text, counts as not fetched. Don't quote search snippets of it as fact.

## Start a run

1. **Pick the mode** from what the user said. Ask only if it's genuinely unclear.
   - `scratch`: no idea yet. "Find me a business."
   - `expertise`: start from what they know. "I'm a dental hygienist. What could I build?"
   - `idea`: stress-test their idea. "Is a dog-walking app for apartment buildings good?"
   - `compete`: they already have a business. "How do I take customers from X?"
2. **Pick the depth. Default to `quick`.** Use `deep` only when the user asks for it ("deep", "thorough", "full run") or the decision is clearly high-stakes, such as quitting a job or spending real money. `quick` takes about 5 to 10 minutes. It covers 3 niches in `scratch` and `expertise` modes, 3 to 5 competitors in total, about 100 to 300 raw records, and a short critic pass. `deep` is the full run. Tell the user which depth you picked and that they can ask for deep.
3. **Create the run folder:** `state.py init <slug> --mode <mode> --depth <depth>`. If it already exists, read `state.json` and continue from the next unfinished stage. Never redo finished stages unless the user asks.

## Keep it lean (save the user's tokens)

These rules apply at every depth. Follow them strictly in `quick`.

- **Never print or open raw records.** Always fetch with `--out`. To find quotable sentences, use `signals.py raw/*.jsonl --find "term1,term2" --limit 40`, which prints only the matching sentences with their URLs, complaints first. One search with a higher `--limit` beats several small ones. Don't write your own scripts to search raw files, and don't `cat` or read `raw/*.jsonl`.
- **Batch fetches** with `pages` (see Scripts). Each separate command costs a round trip. For more than about 100 URLs, split the list into batches of about 100 or run the command in the background, so it doesn't hit your tool's time limit.
- **Write each fact once.** In `quick`, keep each stage file (`competitors.md`, `pains.md`, `gaps.md` and so on) to short bullet notes of about 15 lines, and put the full content only in `report.json`. In `deep`, stage files can be complete.
- **Extras on request.** In `quick`, skip the landing page and the drafts in `assets/`. At the end, offer them in one line.
- **Search with specific phrases.** Use `--find` with phrases customers would actually write ("price went up", "cancel my subscription", "no-shows"), not single generic words like "price" or "support", which match noise.
- **Lean means read less, not know less.** Fetching is cheap because records go to disk, not into your context, so gather plenty before you choose quotes. Evidence floor for `quick`:
  - at least **150 raw records** across sources (more in `deep`);
  - at least **3 customer quotes from 2 or more different URLs** for each main pain theme you report, and for the gap;
  - at least **15 customer quotes** in total.

  Vendor pages (`"official": true`) back prices and features only, never pain or the gap. If you're short, fetch more review pages and run another `--find` pass before writing anything. If sources truly run dry (Reddit blocked, empty App Store feeds), say so in the report rather than padding it.

## The pipeline

Run the stages in order and mark each one done with `state.py done <slug> <stage>`. Write each stage's output to its file before moving on, so a different session or agent can resume.

| Stage | Skill with full instructions | Writes |
|---|---|---|
| founder | (below) | `founder.md` |
| scout | `wedge-niche-scout` (skipped in `idea` and `compete`) | `niches.md` |
| competitors | `wedge-competitor-map` | `competitors.md` |
| reviews | `wedge-review-miner` | `raw/*.jsonl`, `signals.md`, `pains.md` |
| gaps | `wedge-gap-ranker` | `gaps.md` |
| critic | `wedge-gap-ranker` (critic pass) | `critic.md` |
| win | `wedge-win-plan` | `win-plan.md`, `assets/` |
| launch | `wedge-launch-kit` | `launch-kit.md`, `landing/index.html` |
| verify | `verify.py` | updates `evidence.jsonl` |
| report | `report.py` | `report.json`, `report.html`, `card.svg` |

If a stage skill is installed, follow its SKILL.md. If not, its instructions are in `references/stages.md`.

### Founder fit (always first, keep it short)

If the user already gave these answers, just save them. Otherwise ask five questions in one message, and accept "skip" for any of them:

1. Budget to start: $0, under $1k, under $10k, more?
2. Skills: what can you build or sell yourself?
3. Hours per week?
4. Risk tolerance: side income, replace a salary, or swing big?
5. Online, local, or either?

Save the answers to `founder.md`. Use them to filter and score everything that follows: a $0, 5-hour-a-week founder should never get a hardware startup at the top of the list.

## Evidence file

Every quote you use goes in `ideas/<slug>/evidence.jsonl`, one JSON object per line:

```json
{"id": "e12", "claim": "pain-pricing", "quote": "exact words copied from the source", "url": "https://...", "source": "reddit", "date": "2026-09-14"}
```

- `quote` must be copied exactly from the fetched text, never paraphrased. Short is fine.
- Add `"official": true` for a quote from a company's own site (pricing page, docs). It proves what the company says about itself on its own, but never proves customer pain.
- `claim` groups evidence: `gap`, `pain-<theme>`, `comp-<name>`, `trigger-<n>`, `opp-<n>`. It can be a list when one quote backs several claims.
- Prefer quotes `signals.py` surfaced, because they are already exact sentences with URLs.

## Verify, then report

1. Run `verify.py ideas/<slug>/evidence.jsonl`. Each quote gets one of these statuses:
   - `yes`: the quote is on the live page.
   - `captured`: the live page is blocked, but the quote matches the text `fetch.py` saved from that URL in `raw/`.
   - `no`: the page loaded but the quote isn't there. Fix or remove it.
   - `unreachable`: the page couldn't be reached and no saved copy exists.

   `yes` and `captured` both count toward the two-source rule. A claim with fewer than two stays in the report marked unverified. Don't hide it.
2. Fill in `ideas/<slug>/report.json` following `references/report-schema.md`. Reference evidence by `id`.
3. Run `report.py ideas/<slug>`. Open `report.html` for the user if you can, and point them to `card.svg` for sharing.

## Verdict and scoring

`references/scoring.md` is the single source of truth for the six scores, the total, and the GO / PIVOT / KILL / INCONCLUSIVE thresholds. In short: GO means a verified gap that people will pay to fix and that you can reach. PIVOT means the pain is real but this angle doesn't work, so name the one that would. KILL means the pain is weak, or nobody will pay to fix it. Saying KILL plainly is a feature, not a failure.

Never KILL only because sources were unreachable for verification. If the pain evidence exists but couldn't be re-checked, say that in the summary and cap the verdict at PIVOT.

## Tone

Write the way a sharp operator talks: direct, specific, no hype. Use customers' own words wherever possible. Never use "revolutionary", "game-changing" or "disrupt". Never claim a market size you didn't source.

## When done

Before you reply, check `verify.py`'s output: no WARNING lines, and the evidence floor above is met (or the shortfall is explained in the report).

Your final message has exactly these parts:
1. The verdict and the single best gap, in two or three sentences.
2. The paths to `report.html` and `card.svg`.
3. The next action: usually the 7-day test, or `wedge-watch` for an existing business.
   - For a PIVOT that names a pivot, also offer once: "Want me to stress-test the pivot as a new run?" If yes, start a new `idea`-mode run with its own slug, read the old run only for leads (collect and verify fresh evidence), answer the old critic's risks with evidence, and set `follows` in `report.json` (with `projected` from the old run's `verdict.pivot`). If the follow-up scores below its projection, say which assumption was wrong. Run at most one follow-up per original run, so the verdict isn't fished for.
4. In `quick`, one line offering the extras: "Want a deep run, the landing page, or the comparison and outreach drafts?"
