# Example: Sync-health monitor for large WooCommerce catalogs

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

This is a follow-up run: it tests the pivot named by [Throttled catalog sync for large WooCommerce stores](../woocommerce-plugin-opportunity/) (PIVOT 61).

**Verdict: PIVOT, 54/100.** The pain holds up. Different store owners, across four sync plugins and three sites, describe jobs that stall for days while dashboards say there are no errors (e1, e7, e10). But the monitor as pitched doesn't clear GO. Nobody visibly pays for monitoring on its own: the closest WP.org twin, CatalogCanary, has fewer than 10 installs, and a Shopify monitor has 0 reviews. Feed vendors already email on failed runs. Google pushes approval changes for free. Reading Meta-side status needs App Review. The pivot left to test is an agency multi-site watchdog that reads local jobs only, pre-sold before any build.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/woo-sync-health-monitor/). |
| [`evidence.jsonl`](evidence.jsonl) | All 62 quotes (27 customer and third-party, 35 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 467 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
