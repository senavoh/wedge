# Example: Case-management software for small independent funeral homes

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: KILL, 42/100.** The market is crowded and cheap. About 30 products are listed, with tiers from $49 to $79 a month, a free version and month-to-month terms. Most of the director reviews this run could read praise their current tool. The one sharp complaint, a freezing mobile app, came from a single reviewer, and Gather already sells phone case access. Capterra, G2 and Reddit returned 403, so price and switching complaints there went unread. A cheap check is 10 calls with directors before writing any code.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/funeral-home-software/). |
| [`evidence.jsonl`](evidence.jsonl) | All 31 quotes (19 customer and third-party, 12 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 230 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
