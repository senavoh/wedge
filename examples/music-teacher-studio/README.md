# Example: Studio tools for independent music teachers

A real Wedge run in **from what you know** mode, at **quick** depth, done on 2026-10-18.

**Verdict: KILL, 56/100.** The admin pain is real, but it's covered. Teachers complain about makeups, reschedules and late tuition, yet My Music Staff already does makeup credits, self-rescheduling and auto-invoicing for $16.95/mo, Nova is free up to 10 students, and many teachers say Venmo and Excel are enough. The best open gap, practice logs that teachers can correct, comes from three reviews of a single app, in a niche whose best-known app (Tonara) shut down in 2023. Caveat: Capterra, G2, Trustpilot and Reddit were blocked from this network, so complaints about incumbents on those sites weren't read.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/music-teacher-studio/). |
| [`evidence.jsonl`](evidence.jsonl) | All 43 quotes (35 customer and third-party, 8 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 413 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
