# Example: Paid Pomodoro focus timer for students

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: PIVOT, 54/100.** The pain is real: students are angry right now at focus apps that added subscriptions, ads and clutter, Forest above all. But the pitch sells features (streaks, stats, design) that Forest, Flora, FocusPomo and FLIP already give away, and a $4.99/month subscription is the exact thing reviewers are rejecting. Pivot the price and the angle: a one-tap, ad-free timer sold once, aimed at people leaving Forest.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/pomodoro-timer-app/). |
| [`evidence.jsonl`](evidence.jsonl) | All 30 quotes (21 customer and third-party, 9 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 397 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
