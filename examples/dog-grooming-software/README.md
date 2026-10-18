# Example: Booking and client app for independent and mobile dog groomers

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: PIVOT, 55/100.** The pain is real but narrow. About 15 different groomers in App Store reviews complain about slow, buggy apps on the road, wrong addresses, metered texts and payment fees, and charges after cancelling. But a general 'cheaper MoeGo' is already taken: MoeGo is well rated, and ZendPaw ($39) and BooknBuddy (from $29.99) already pitch solo groomers and MoeGo switchers. Only build if the speed-on-the-road angle passes a 10-groomer interview test first. Evidence comes from App Store reviews only; Reddit, Capterra, G2 and Trustpilot were blocked.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/dog-grooming-software/). |
| [`evidence.jsonl`](evidence.jsonl) | All 34 quotes (24 customer and third-party, 10 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 545 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
