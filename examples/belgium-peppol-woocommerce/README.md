# Example: WooCommerce Peppol plugin for small Belgian web shops

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: KILL, 46/100.** The mandate is real and in force (since 1 Jan 2026, tolerance ended 31 Mar 2026, Hermes shut 31 Dec 2025), but the job is already done for free or almost free: GoRoute's Woo plugin gives 50 invoices a month free with VAT/Peppol-ID lookup, WP Overnight's 300k-install plugin sends from about EUR 5/month, and accounting tools like Accountable receive for free. The pain left is setup friction (missing VAT numbers or Peppol IDs, UBL rejected by receivers), not something shops will pay EUR 9-19 a month for. Next best: sell fixed-price Peppol setup and fixes for Belgian Woo shops on top of the existing free connectors (untested).

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/belgium-peppol-woocommerce/). |
| [`evidence.jsonl`](evidence.jsonl) | All 53 quotes (27 customer and third-party, 26 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 299 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
