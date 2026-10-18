# Example: What WooCommerce plugin to build next

A real Wedge run in **from what you know** mode, at **quick** depth, done on 2026-10-18.

**Verdict: PIVOT, 61/100.** The loudest verified pain is product catalog sync to Meta and Google on large WooCommerce stores. The official plugins are rated 2.1 and 2.7 on WordPress.org, and reviews from different authors describe sync jobs that crash servers or stall. But a catalog-sync plugin isn't an open gap: CTX Feed markets itself for large catalogs, WebToffee already ships batched, scheduled Meta sync, and Google can crawl the store for free, so it scores 61 and fails GO. The pivot is a sync-health monitor that works alongside existing sync plugins, not another feed generator. Test that before writing much code.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/woocommerce-plugin-opportunity/). |
| [`evidence.jsonl`](evidence.jsonl) | All 46 quotes (34 customer and third-party, 12 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 764 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
