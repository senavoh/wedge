# Example: Shopify app opportunity for a Remix + Polaris developer

A real Wedge run in **from what you know** mode, at **quick** depth, done on 2026-10-18.

**Verdict: PIVOT, 58/100.** The pain is real and recent. Shopify shut Stocky on Aug 31 2026, and retailers can't print labels for what they just received on native purchase orders. But at least 8 apps already chase that exact gap, some for free, so a new public app has no opening. Pivot to a fixed-fee migration and receiving/label setup for small POS retailers, built on the new PO Read API, and only productize if 3 or more pay.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/shopify-app-opportunity/). |
| [`evidence.jsonl`](evidence.jsonl) | All 47 quotes (29 customer and third-party, 18 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 513 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
