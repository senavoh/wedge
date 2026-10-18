# Scoring rubric

This file is the single source of truth for scoring and verdicts. Other skills point here.

Score each axis from 0 to 10. Write one line of reasoning per score that cites evidence IDs. **A score backed by no `yes` or `captured` evidence (see `verify.py`) is capped at 5.**

| Axis | 0 to 3 | 4 to 6 | 7 to 10 |
|---|---|---|---|
| **pain** | Mild annoyance, few mentions | Daily friction, repeated by different people | People leave or threaten to; many authors across 2+ sources |
| **willingness_to_pay** | "Should be free", nobody pays today | People pay for a weak substitute | They already pay competitors and complain about price, not about paying at all |
| **competition_gap** | A strong, loved incumbent covers it | Covered, but badly or too expensively | Nobody covers the gap for this buyer, or every option has the same top complaint |
| **founder_fit** | Needs skills, money or time the founder doesn't have | Doable with a stretch | Plays to the founder's skills and fits their budget and hours |
| **reachability** | Buyers are hidden and only reachable through gatekeepers | Reachable through paid ads | You can name 3+ free places where they gather and complain |
| **build_cost** | Hardware, regulation or a big team | A few months of work | A weekend to a few weeks with free or cheap tools |

**Total out of 100** = round(pain×2.5 + willingness_to_pay×2 + competition_gap×2 + founder_fit×1.5 + reachability×1.2 + build_cost×0.8)

Pain and willingness to pay carry the most weight on purpose: most ideas die because the pain isn't sharp enough or nobody will pay to fix it.

## Verdict thresholds

Check them in this order:

- **GO:** total ≥ 65, the gap claim meets the two-source rule, willingness_to_pay ≥ 6, reachability ≥ 6, and no unresolved high-severity critic risk.
- **PIVOT:** pain ≥ 6, but GO fails. Name the pivot: buyer, angle, price or channel.
- **PIVOT (unverified):** pain evidence exists, but its sources were unreachable for re-checking, so pain is capped at 5. Don't KILL on that alone. Say verification is incomplete and what would complete it, for example adding Reddit API credentials.
- **KILL:** anything else. Most often the pain is weak, nobody will pay to fix it, or a free incumbent covers it.
