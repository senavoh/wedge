# report.json schema

`report.py` renders whatever is present and skips empty sections, so a quick run can leave out `first_10`, `cost`, `launch` and `features` if they weren't done. Evidence is referenced by `id` from `evidence.jsonl`, never pasted inline.

Conventions:
- The gap must rest on customer quotes. Quotes marked `"official": true` don't count toward the gap or any `pain-` claim.
- Give the evidence behind `gap.evidence` the claim `"gap"` in `evidence.jsonl`. It needs two sources from different URLs to show as verified. One quote can back several claims, so use a list rather than copying it: `"claim": ["pain-caps", "gap"]`.
- `features.rows[].values` takes `yes`, `no`, `partial` or `unknown`. Use `unknown` rather than guessing.
- `pains[].by_competitor` can name products that aren't in `competitors`.
- Leave out `critic[].rebuttal` when a risk is unresolved. The report shows "Unresolved."

```json
{
  "title": "Bookkeeping inbox for independent bookkeepers",
  "subtitle": "One line on what this report covers.",
  "mode": "scratch | expertise | idea | compete",
  "depth": "quick | deep",
  "date": "2026-10-17",

  "founder": {"budget": "under $1k", "skills": "web dev", "hours": "10/week", "risk": "side income", "channel": "online"},

  "verdict": {"call": "GO | PIVOT | KILL", "score": 74, "summary": "Two or three sentences a busy person can act on."},

  "opportunities": [
    {"name": "Receipt chaser for bookkeepers", "one_liner": "Auto-chases clients for missing receipts.",
     "score": 74,
     "scores": {"pain": 8, "willingness_to_pay": 7, "competition_gap": 7, "founder_fit": 8, "reachability": 7, "build_cost": 8},
     "why": "One paragraph of reasoning.", "evidence": ["e1", "e4"]}
  ],

  "gap": {"statement": "<Buyer> who <situation> can't get <outcome> because every option <failure>.", "evidence": ["e1", "e2", "e7"]},

  "pains": [
    {"theme": "Price jumps at renewal", "severity": "high | medium | low", "summary": "One line.",
     "by_competitor": {"Acme": 9, "Globex": 3}, "evidence": ["e3", "e5"]}
  ],

  "competitors": [
    {"name": "Acme", "url": "https://acme.com", "pricing": "$49/user/mo, annual only",
     "positioning": "Their headline, quoted.", "strengths": ["..."], "weaknesses": ["..."], "evidence": ["e9"]}
  ],

  "features": {"columns": ["Bulk import", "Client portal", "Month-to-month"],
               "rows": [{"name": "Acme", "values": ["yes", "partial", "no"]}]},

  "critic": [{"risk": "Intuit could bundle this.", "severity": "high | medium | low", "rebuttal": "Evidence-backed answer, or omit for Unresolved."}],

  "win_plan": {
    "positioning": "The only X for Y that Z.",
    "switching_triggers": [{"trigger": "Annual renewal with a price hike", "move": "Price-lock offer posted where they complain", "evidence": ["e3"]}],
    "offers": ["Free migration from Acme"],
    "build_first": [{"feature": "CSV import from Acme", "why": "Top switching blocker (pain: lock-in)."}],
    "where_to_find": [{"place": "r/Bookkeeping", "url": "https://www.reddit.com/r/Bookkeeping/", "why": "Weekly Acme complaint threads"}],
    "trust": ["Public pricing that never changes on renewal"],
    "stop_doing": ["Annual-only contracts"],
    "assets": [{"name": "Us vs Acme page", "path": "assets/vs-acme.md"}]
  },

  "pricing": {"recommendation": "$29/mo flat", "competitor_range": "$15 to $79 per user", "rationale": "Two lines."},
  "cost": {"monthly": "$0 to $25", "stack": [{"item": "Cloudflare Pages hosting", "cost": "$0"}]},

  "first_10": [{"step": "Answer 10 open complaint threads", "where": "r/Bookkeeping", "script": "Short, helpful message text."}],

  "validation": {"experiment": "What you will do this week.", "pass_bar": "40 waitlist signups or 5 asks to pay", "days": 7, "steps": ["Day 1: ..."]},
  "kill_criteria": ["Under 15 signups after 7 days"],

  "launch": {"name": "Chaser", "domain": "chaser.dev", "domain_status": "available",
             "alternatives": [{"domain": "getchaser.com", "status": "available"}], "landing_page": "landing/index.html"}
}
```
