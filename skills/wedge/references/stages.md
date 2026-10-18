# Stage instructions (fallback)

Each stage has its own skill with full instructions. If only the `wedge` skill is installed, install the rest with:

```bash
npx skills add senavoh/wedge
```

If installing isn't possible, follow these short versions. Scripts are in `scripts/`.

**scout** (`wedge-niche-scout`): Combine demand phrases ("I wish there was", "alternative to", "too expensive", "is there a tool") with fields the founder fits. Run `fetch.py reddit` and `fetch.py hn` per seed into `raw/scout.jsonl`, then `signals.py`. Cluster the results into specific buyer-plus-job niches. Shortlist 3 (quick) or 6 to 8 (deep). Write `niches.md`.

**competitors** (`wedge-competitor-map`): Use web search, then `fetch.py pages` to fetch all pricing pages and homepages in one parallel call. Record real prices, the model, free tier, contract and the exact headline. Build a feature matrix from features buyers mention in complaints. Note where the market is crowded and where it's empty. Write `competitors.md`.

**reviews** (`wedge-review-miner`): Collect 1 to 3 star App Store reviews, Reddit searches and threads, HN and GitHub issues for each competitor. Get G2, Capterra and Yelp through web search only. Run `signals.py --names`. Write 4 to 8 themes with severity, counts per competitor and 2+ exact quotes from different URLs. Write `pains.md`.

**gaps and critic** (`wedge-gap-ranker`): Write each gap as "<Buyer> who <situation> can't get <outcome> because every option <failure>." Score using `scoring.md`. Then argue against the winner: who tried and died, a free incumbent, pain without payment, a closed channel, copyable in a week, regulation. Write `gaps.md` and `critic.md`.

**win** (`wedge-win-plan`): Cover switching triggers and moves, positioning in customers' words, offers for switchers, what to build first, where unhappy customers are (with URLs), trust signals, what to stop doing, and a first-10-customers plan. Draft assets: a comparison page, outreach, ads and an FAQ. Write `win-plan.md`.

**launch** (`wedge-launch-kit`): Pick names and check them with `domain.py --tlds com,dev,io,ai`. Set pricing anchored to competitors, the cheapest stack with monthly cost, `landing/index.html` with a waitlist, and a 7-day test with a numeric pass bar and kill criteria. Write `launch-kit.md`.
