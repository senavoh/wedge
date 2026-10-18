# Example: Taking customers from Bookly and Amelia

A real Wedge run in **beat my competitors** mode, at **quick** depth, done on 2026-10-17.

**Verdict: PIVOT, 63/100.** The pain is real and recent, mostly with Amelia: updates break live bookings and support takes days to weeks. But well-rated LatePoint and SSA already catch switchers, and nobody has shown they'll pay a newcomer. Don't launch as booking plugin #785. Sell a done-for-you migration and rescue off Amelia/Bookly first, at $149, with your plugin as the destination. If 3 people pay within 7 days, re-score.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/wordpress-booking-plugin/). |
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

Dates on WordPress.org quotes are approximate (year and month), worked out from the forum's "N years ago" labels at fetch time.
