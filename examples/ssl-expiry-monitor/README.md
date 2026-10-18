# Example: a $9/month SSL certificate expiry monitor

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: KILL, 47/100.** Expired certificates do take sites down, and Let's Encrypt ending its expiry emails in 2025 left some people without a warning. But the exact product, an email before the certificate expires, is already free from Red Sift, HetrixTools, StatusCake and self-hosted Uptime Kuma. The people who hit this pain are developers who fix it with a script, and an earlier SSL monitor, SSLPing, shut down without ever charging. Don't build this as a standalone paid product.

This is what a KILL looks like: the pain is real, but nobody will pay for this fix.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/ssl-expiry-monitor/). |
| [`card.png`](card.png) | Share card (1200×630). |
| [`evidence.jsonl`](evidence.jsonl) | All 47 quotes (31 customer, 16 vendor) with source URLs and verification status. |
| [`signals.md`](signals.md) | Digest of 569 raw records, read instead of the raw dump. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/` | Raw records from the fetchers: Hacker News, GitHub issues, WordPress.org reviews and pricing pages. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
