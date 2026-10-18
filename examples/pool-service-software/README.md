# Example: Route-and-invoice app for small pool service companies

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: PIVOT, 56/100.** The pain is real: six different Skimmer reviewers describe repeated price hikes, and another app's owner-operator with 20 stops saw his bill go from $65 to $115. But "cheaper" is already for sale (Paythepoolman at $50 + $15 per tech, QuoteIQ from $29.99) and Skimmer's own $1-per-pool tier is cheap for a small route, so a price wedge alone is thin. Pivot the angle to an offline-first, fast route log with a written price lock for owner-operators, and test it through your cousin's network before building. Customer voice comes from App Store reviews only (Reddit and the review sites blocked this network), so treat it as directional.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/pool-service-software/). |
| [`evidence.jsonl`](evidence.jsonl) | All 40 quotes (27 customer and third-party, 13 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 320 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
