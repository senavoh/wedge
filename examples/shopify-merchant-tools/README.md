# Example: Tools for Shopify merchants, from a small Shopify merchant

A real Wedge run in **from what you know** mode, at **quick** depth, done on 2026-10-17.

**Verdict: PIVOT, 57/100.** The pain is real: small POS retailers lost Stocky on Aug 31, 2026, and they say Shopify's native POs take triple the time. But don't build another Stocky replacement app. A free, 4.9-rated one (Stockroom) and more than ten cheap apps already cover it, and these shops resist new monthly fees. The pivot is to change the channel and price: sell a one-time $199 setup service on top of the free tools, and run the 7-day test before building anything. Read-only Stocky access ends Nov 29, so test now.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/shopify-merchant-tools/). |
| [`card.png`](card.png) | Share card (1200×630). |
| [`evidence.jsonl`](evidence.jsonl) | All 93 quotes with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| [`win-plan.md`](win-plan.md) | How to win customers, with drafts in [`assets/`](assets/). |
| [`landing/index.html`](landing/index.html) | Landing page from the launch kit, for the 7-day test. |
| `raw/` | Raw records saved by the fetchers. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
