# Example: a simpler invoicing app for solo tradespeople

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-17.

**Verdict: PIVOT, 66/100.** The pain is real and verified: monthly invoice caps, price increases right after subscribing, and paying $20 to $25 a month just to send a PDF. But the generic "simple invoicing app for trades" is crowded with indie builders. The wedge is narrower: uncapped, price-locked, offline estimate-to-invoice.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser. |
| [`card.svg`](card.svg) | Share card (1200×630). |
| [`evidence.jsonl`](evidence.jsonl) | All 28 quotes with source URLs and verification status. |
| [`signals.md`](signals.md) | Digest of 627 raw records, read instead of the raw dump. |
| [`report.json`](report.json) | Structured data behind the report. |
| [`landing/index.html`](landing/index.html) | Landing page from the launch kit, for the 7-day test. |
| `raw/` | Raw records from the fetchers. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```

All 28 quotes were verified against their live sources on the first pass. Apple's review feed is sometimes empty for hours. When it is, App Store quotes are checked against the text `fetch.py` saved in `raw/` and show as `captured` (7 of them in the current report). Quotes verified live on an earlier run keep that result and its date.
