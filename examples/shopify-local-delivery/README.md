# Example: Local delivery and pickup scheduling app for small Shopify food and flower shops

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: PIVOT, 56/100.** The pain is real: merchants say date-picker apps get skipped at checkout, break themes, answer support slowly, and in Zapiet's case cost too much. But the gap is not open. Pickeasy (4.9, 1,327 reviews), Buunto, Bird and Scrollengine already sell slots and daily capacity for $0 to $20 a month, and the critic found the route-sheet add-on pivot already served too. Don't build a general scheduling app. Spend one week testing the add-on by hand with the two florists, and drop it if they won't pay.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/shopify-local-delivery/). |
| [`evidence.jsonl`](evidence.jsonl) | All 47 quotes (34 customer and third-party, 13 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 403 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
