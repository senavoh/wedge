# Notes for agents working on this repo

- Skills live in `skills/<name>/SKILL.md`. The `wedge` skill owns the shared scripts in `skills/wedge/scripts/`. Other skills refer to them as `../wedge/scripts/`.
- Scripts must stay Python 3.8+ standard library only. No pip installs, no API keys required.
- Keep each SKILL.md under about 200 lines. Put long material in `skills/wedge/references/`.
- Never add fabricated data to `examples/`. Example runs must be real and pass `verify.py`.
- Smoke test after changing scripts: `python3 skills/wedge/scripts/report.py examples/tradesperson-invoicing` and `python3 skills/wedge/scripts/verify.py examples/tradesperson-invoicing/evidence.jsonl`.
