# Example: Update-proof event ticketing for WordPress agencies

A real Wedge run in **from scratch** mode, at **deep** depth, done on 2026-10-17. Timed: **29 minutes** from start to finished report, about 88 tool calls including the critic's separate pass.

**Verdict: PIVOT, 55/100.** The pain is real and well documented: on WordPress.org, small organizers and their agencies say events plugin updates break ticket sales, paid support goes silent and renewals jump 50%. But the obvious fix, a hosted checkout that looks native on WordPress, already exists (Ticket Spot, with only 40+ installs; Ticket Tailor's embed). Nonprofits get ticketing free from Zeffy, and the WordPress.org forums forbid promotion, so organizer-direct scores 55. Pivot to WordPress agencies managing many small-org sites (57 on paper, untested) and run the 7-day agency test before building anything.

| Stage | Minutes |
|---|---|
| Founder fit | 0 |
| Scout (23 seeds, 31 Shopify apps, 18 WordPress plugins) | 6.6 |
| Competitor map | 2.3 |
| Review mining (625 review threads in one parallel fetch) | 9.2 |
| Gap ranking | 0.9 |
| Critic (separate agent) | 4.2 |
| Win plan | 1.0 |
| Launch kit | 1.5 |
| Verify | 2.2 |
| Report | 0.6 |

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report, also on [getwedge.dev](https://getwedge.dev/examples/wordpress-event-ticketing/). |
| [`card.png`](card.png) | Share card (1200×630). |
| [`evidence.jsonl`](evidence.jsonl) | All 78 quotes with source URLs and verification status. |
| [`niches.md`](niches.md), [`critic.md`](critic.md), [`win-plan.md`](win-plan.md) | The scout shortlist, the case against, and the plan. |
| [`landing/index.html`](landing/index.html) | Landing page for the 7-day test. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 1,401 records; the rest were trimmed to keep the repo small. |

Five scout-stage niches rest on a single review page each, so they show as unverified in the report.

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
