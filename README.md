<p align="center">
  <img src="examples/tradesperson-invoicing/card.png" alt="A Wedge report share card" width="720">
</p>

<h1 align="center">◢ Wedge</h1>

<p align="center"><b>Find the gap. Take the customers.</b><br>
Open-source agent skills that find a business worth building, show exactly what customers hate about the competition, and tell you how to win. Every claim is cited and checked.</p>

<p align="center">
  <a href="https://getwedge.dev">getwedge.dev</a> ·
  <a href="https://getwedge.dev/examples/tradesperson-invoicing/">Example report</a> ·
  <a href="#install">Install</a> ·
  <a href="#how-it-works">How it works</a>
</p>

```bash
npx skills add senavoh/wedge
```

Then ask your agent:

> Use wedge to find me a business I can start with $500 and 10 hours a week.

Works with **Claude Code, Codex, Cursor, Gemini CLI, OpenCode**, and any agent that reads `SKILL.md` files.

<p align="center">
  <img src="docs/demo.svg" alt="A Wedge run in the terminal: fetching reviews, mining complaints, verifying every quote, and a PIVOT verdict" width="760">
  <br><sub>What your agent runs under the hood, from a real run (output trimmed). Rebuild with <code>python3 docs/make_demo.py</code>.</sub>
</p>

---

## Why Wedge

Ask an AI for business ideas and you get confident, generic, unsourced lists. Wedge works differently:

- **Evidence or it didn't happen.** Every pain point and claim about a competitor links to a real review, thread or pricing page. `verify.py` re-fetches each source and checks that the quote is actually there. A claim needs two verified sources from different URLs, or it's labeled **unverified** and can't drive the verdict.
- **It argues with itself.** A separate critic pass tries to kill the top idea (who already tried, a free incumbent, people who complain but won't pay) before anything is ranked.
- **It's honest.** The verdict is **GO**, **PIVOT** or **KILL**, with the reasoning shown.
- **It tells you how to win, not only what to build.** It finds switching triggers, positioning in customers' own words, offers that pull switchers, where unhappy customers hang out, and drafts comparison pages and outreach.
- **It's free to run.** No API keys, no paid data. The scripts use only the Python standard library.
- **It picks up where it left off.** Everything is saved in `ideas/<slug>/`, so a run can continue tomorrow or in a different agent.

## Four ways to start

| Mode | Say something like |
|---|---|
| **From scratch** | "Find me a business I can start." |
| **From what you know** | "I run an IT company. What could I build?" |
| **Stress-test an idea** | "Is a dog-walking app for apartment buildings any good?" |
| **Beat my competitors** | "How do I take customers from Jobber?" |

Choose **quick** (about 10 minutes) or **deep** (the full run).

## How it works

```
founder fit → niche scout → competitor map → review mining → gap ranking → critic → win plan → launch kit → verify → report
```

1. **Founder fit.** Five quick questions (budget, skills, hours, risk, online or local) so ideas are ranked for you.
2. **Niche scout.** Mines "I wish there was…", "alternative to…" and "too expensive" posts to find unmet demand.
3. **Competitor map.** Real pricing, positioning and a feature matrix, all cited.
4. **Review mining.** Turns hundreds of 1 to 3 star reviews and complaint threads into ranked pain themes with exact quotes.
5. **Gap ranking.** Scores six axes (pain, willingness to pay, competition gap, founder fit, reachability, build cost) and shows the reasoning.
6. **Critic.** A skeptical second pass tries to kill the winner.
7. **Win plan.** Switching triggers, positioning, offers, what to build first, where to find unhappy customers, and draft assets.
8. **Launch kit.** A name with a verified-available domain, pricing, the cheapest stack, a landing page, and a 7-day test with a pass bar and kill criteria.
9. **Verify and report.** Every quote is checked, then rendered into one self-contained HTML report and a share card.

## See real runs

Three real runs, one per mode, unedited. Every quote is checked against its source.

| Run | Mode | Verdict | What it found |
|---|---|---|---|
| [A simpler invoicing app for solo tradespeople](https://getwedge.dev/examples/tradesperson-invoicing/) ([files](examples/tradesperson-invoicing/)) | Stress-test an idea | **PIVOT 66** | Invoice caps and price hikes are real pain, but indie builders already make the generic app. Build the uncapped, price-locked, offline version. 28 quotes. |
| [Tools for Shopify merchants, from a small Shopify merchant](https://getwedge.dev/examples/shopify-merchant-tools/) ([files](examples/shopify-merchant-tools/)) | From what you know | **PIVOT 57** | Shopify shut down Stocky and shops are scrambling, but free replacement apps already exist. Sell a done-for-you setup service instead of another app. 93 quotes. |
| [Taking customers from Bookly and Amelia](https://getwedge.dev/examples/wordpress-booking-plugin/) ([files](examples/wordpress-booking-plugin/)) | Beat my competitors | **PIVOT 63** | Updates that break bookings and slow support drive people away, but good alternatives and importers exist. Lead with a done-for-you rescue and migration. 93 quotes. |

## The skills

| Skill | What it does |
|---|---|
| `wedge` | Runs the whole pipeline, keeps state, verifies and renders the report. |
| `wedge-niche-scout` | Finds niches with unmet demand that fit you. |
| `wedge-competitor-map` | Pricing, positioning and a feature matrix for every competitor. |
| `wedge-review-miner` | Pain themes from real reviews and threads, with exact quotes. |
| `wedge-gap-ranker` | Scoring, the critic pass, and GO / PIVOT / KILL. |
| `wedge-win-plan` | How to pull customers from competitors. |
| `wedge-launch-kit` | Name and domain, pricing, stack, landing page, 7-day test. |
| `wedge-watch` | Monthly re-check of competitors: new complaints, price changes, new entrants. |

Each skill works on its own too: "Use wedge-review-miner on Jobber and Housecall Pro."

## Install

**Any agent (recommended)**

```bash
npx skills add senavoh/wedge
```

The `skills` installer needs Node.js 22 or newer. On older Node versions, use the install script below.

**Claude Code plugin**

```text
/plugin marketplace add senavoh/wedge
/plugin install wedge@wedge
```

**Install script.** Copies the skills into every agent skills folder it finds (`~/.claude`, `~/.codex`, `~/.gemini`, `~/.cursor`, `~/.config/opencode`, `~/.agents`):

```bash
curl -fsSL https://getwedge.dev/install.sh | sh
```

**Manual.** Copy the folders in `skills/` into your agent's skills folder.

Requirements: Python 3.8 or newer, which is preinstalled on macOS and most Linux systems.

**Optional, for Reddit.** Reddit blocks anonymous requests from many networks. To use its official API instead, create a free "script" app at [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) and set `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET`. Without them, Wedge uses your agent's own web search for Reddit (`site:reddit.com`). `GITHUB_TOKEN`, if set, raises GitHub's rate limit.

## The scripts

The agent runs these for you. They live in `skills/wedge/scripts/` and you can run them yourself too:

| Script | Does |
|---|---|
| `fetch.py` | Pulls customer voice from Hacker News, Reddit, App Store reviews, GitHub issues and any web page, as JSONL. `pages` fetches many URLs in parallel, and `links` collects review links to feed into it. |
| `signals.py` | Turns raw records into a short, cited digest of pain and demand signals, so the agent reads 100 lines instead of 100,000. |
| `verify.py` | Re-fetches every cited source, checks the quote is there, and applies the two-source rule. |
| `domain.py` | Checks domain availability through public RDAP, and reports "unknown" instead of guessing. |
| `state.py` | Saves progress so any agent can resume a run. |
| `report.py` | Renders the HTML report and the share card. |

## Data and ethics

- Wedge reads public posts and reviews through official or public endpoints: the Hacker News Algolia API, Reddit's JSON and official API, Apple's public review feeds and the GitHub API. It doesn't scrape sites whose terms forbid it. G2, Capterra and Trustpilot content comes in only through ordinary web search results.
- Quotes are short, attributed and linked, used to support analysis.
- The win plan never suggests fake reviews, astroturfing or misleading comparisons.

## Contributing

Issues and pull requests are welcome. Good first contributions: new data sources that need no keys, better signal patterns for non-English markets, and example runs in new industries (add them under `examples/`).

## License

MIT
