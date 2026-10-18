# Example: Hosted Wedge for ex-GummySearch users

A real Wedge run in **stress-test an idea** mode, at **quick** depth, done on 2026-10-18.

**Verdict: KILL, 54/100.** The premise holds: GummySearch stopped taking payments on Nov 30, 2025 after failing to get a commercial Reddit Data API license, and it shuts down Dec 1, 2026. Reddit now requires approval for new API apps. But the exact wedge, no-Reddit pain research pitched at GummySearch refugees for $29/mo, is already on sale (GripeFind). Free substitutes (ChatGPT Deep Research, an MIT-licensed MCP with the same sources, Wedge itself) cover most of the rest. Buyer pain after the shutdown is thin: launches in this category get 0 to 2 HN comments.

| File | What it is |
|---|---|
| [`report.html`](report.html) | The full report. Open it in a browser, or see it on [getwedge.dev](https://getwedge.dev/examples/hosted-wedge/). |
| [`evidence.jsonl`](evidence.jsonl) | All 65 quotes (37 customer and third-party, 28 vendor) with source URLs and verification status. |
| [`report.json`](report.json) | Structured data behind the report. |
| `raw/cited.jsonl` | The raw records behind the quotes. The run fetched 1,964 records; the rest were trimmed to keep the repo small. |

Re-check every quote yourself:

```bash
python3 ../../skills/wedge/scripts/verify.py evidence.jsonl
```
