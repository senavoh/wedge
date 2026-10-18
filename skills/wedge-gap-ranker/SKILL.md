---
name: wedge-gap-ranker
description: Rank business opportunities and find the single best gap, then attack it with a separate critic pass before giving a GO, PIVOT or KILL verdict. Scores pain, willingness to pay, competition gap, founder fit, reachability and build cost with reasoning shown. Use for "which idea is best", "is this idea good", "validate my idea", "score these ideas", "should I build this", "rip apart my idea".
---

# Wedge: gap ranker and critic

Picks the opening worth betting on, then tries hard to kill it. Part of the Wedge pipeline; it also works on its own.

## Part 1: Rank

Inputs: `founder.md`, `niches.md` (or the user's idea), `competitors.md` and `pains.md`.

1. **Write each candidate gap as one sentence:** "<Buyer> who <situation> can't get <outcome> because every option <failure>." If you can't fill in every blank from evidence, it isn't a gap yet.
2. **Score each opportunity 0 to 10 on six axes** (rubric in the `wedge` skill's `references/scoring.md`):
   - **pain:** severity × frequency from `pains.md`.
   - **willingness_to_pay:** do they already pay competitors? Are there price complaints but not "I'd never pay"?
   - **competition_gap:** how empty is the space in the feature matrix and the complaint themes?
   - **founder_fit:** skills, budget, hours.
   - **reachability:** can you name 3 specific places these buyers gather?
   - **build_cost:** 10 means a weekend with free tools; 0 means hardware or regulation.
   - **total** = round(pain×2.5 + willingness_to_pay×2 + competition_gap×2 + founder_fit×1.5 + reachability×1.2 + build_cost×0.8). The maximum is 100.
3. Every score gets one line of reasoning that cites evidence IDs. A score backed by no `yes` or `captured` evidence is capped at 5.

Write `ideas/<slug>/gaps.md` with a ranked table, the reasoning and the winning gap sentence.

## Part 2: Critic pass

Switch roles. At quick depth, run at least the first two checks below (two searches). At deep depth, run all of them. If your agent can start a subagent, give this to a fresh one with only `gaps.md`, `competitors.md` and `pains.md`, so it isn't anchored by the excitement of ranking. Otherwise, explicitly reset and argue against your own ranking.

The critic's brief: "You are a skeptical investor who has seen 1,000 of these. Find the strongest reasons the top opportunity fails." Check each of these with a search:

- **Someone tried and died:** search `"<idea>" shut down`, `"<idea>" postmortem`, `"why we stopped"`, and look for dead Product Hunt launches.
- **A free incumbent:** a big player that bundles this for free (Google, Microsoft, Shopify, the platform itself).
- **The pain is real but nobody pays:** people complain loudly but won't pay.
- **The channel is closed:** buyers only purchase through a channel you can't access, such as enterprise procurement or an app store gatekeeper.
- **Copyable in a week:** an incumbent can ship your wedge as a feature.
- **Regulation, liability or trust barriers.**

For each risk, record its severity and either a rebuttal backed by evidence or "Unresolved". Write `ideas/<slug>/critic.md`.

**How to set severity.** Only `high` can block a GO, so it has to be earned:
- **high:** specific to this idea and backed by a source you found and cited. Put the quote in `evidence.jsonl` with the claim `risk-<n>`, and list its id in the risk's `evidence`. Examples: a named product that already does this exact wedge, a company that tried it and shut down, a platform policy or law that blocks it.
- **medium:** a risk that could apply to almost any small software business, with no source showing it is happening here: "an incumbent could copy it", "the platform might add this someday", "forums don't allow self-promotion". Keep it in the report; it just can't block a GO alone.
- **low:** worth knowing, unlikely to matter.

A rebuttal also needs a source. Don't resolve a risk by arguing.

## Part 3: Verdict

Apply the thresholds in the `wedge` skill's `references/scoring.md`. Don't restate or loosen them here. For PIVOT, name the specific pivot: a different buyer, price or channel. For KILL, name the next best opportunity. Never KILL only because sources were unreachable for verification; cap the verdict at PIVOT and say why.

Run `state.py done <slug> gaps` and `state.py done <slug> critic`.
