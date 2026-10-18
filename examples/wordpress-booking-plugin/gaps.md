# Gaps: candidate wedges against Bookly and Amelia

Mode is `compete`, so these are positionings for the plugin the founder is already building, not new niches. They're scored with `references/scoring.md`. All cited evidence passed `verify.py` as `yes`.

## Candidate gap sentences
1. **Switch-in plugin.** Small appointment businesses (salons, barbers, tutors, therapists) on Bookly or Amelia can't get updates that don't break today's bookings, or support that answers in a day, because both leaders ship breaking updates behind slow ticket queues. Leaving means re-entering customers, services and future appointments by hand. (e10, e13, e4, e2, e46, e47)
2. **Developer-first engine.** WordPress freelancers and agencies who install booking for clients can't extend or debug it the WordPress way, because Amelia keeps its own users and tables with few hooks, and Bookly's hooks are undocumented. Their clients phone *them* when it breaks. (e39, e40, e41, e42, e62, e63, e65)
3. **Rescue and migration service, then productize.** Owners and freelancers stuck on a broken Bookly or Amelia install can't get it fixed fast or moved out cleanly, because vendor support takes days to weeks and nobody I found offers a done-for-you move between plugins. Self-serve importers exist: e84, e85. (e5, e6, e18, e46, e47, e48)

## Ranked table

| # | Opportunity | pain | WTP | gap | fit | reach | build | **Total** |
|---|---|---|---|---|---|---|---|---|
| 3 | Rescue & migration service → importers inside your plugin | 7 | 5 | 4 | 9 | 6 | 9 | **63** |
| 2 | Developer-first, WP-native booking engine for freelancers/agencies | 6 | 6 | 5 | 9 | 6 | 4 | **61** |
| 1 | Switch-in booking plugin (import + update-safe + fast support) | 7 | 6 | 5 | 7 | 6 | 4 | **60** |

Totals use `round(pain×2.5 + wtp×2 + gap×2 + fit×1.5 + reach×1.2 + build×0.8)`:
- #3: 17.5 + 10 + 8 + 13.5 + 7.2 + 7.2 = 63.4, which rounds to **63**.
- #2: 15 + 12 + 10 + 13.5 + 7.2 + 3.2 = 60.9, which rounds to **61**.
- #1: 17.5 + 12 + 10 + 10.5 + 7.2 + 3.2 = 60.4, which rounds to **60**.

## Reasoning per score

### #1 Switch-in booking plugin (the founder's current plan, sharpened)
- **pain 7:** two high-severity themes with many different authors. Updates breaking bookings: e10, e13, e14, e18. Slow support: e2, e4, e5, e6. Reviewers say they are leaving (e54, e55, e57, e58). Not 8+, because it's one source site (WP.org), these are 7 to 9% of ratings, and Bookly's stream is stale: 0 low-star reviews in the last 12 months, against Amelia's 11.
- **willingness_to_pay 6:** they already pay ($39 to $149+ per year) and complain about add-ons and renewals, not about paying at all (e25, e26, e19, e24). Held at 6 because entry prices are being pushed down: Bookly Pro is $39 for the first year (e67) and LatePoint is $79 with every feature (e72).
- **competition_gap 5:** the complaint is shared by Bookly, Amelia and BookingPress. But LatePoint (98/100 from 104 ratings, all features on every plan, e71) and SSA (100/100, 1-business-day replies, e75) already look like a reliable, well-supported destination. Whether they import from Bookly or Amelia is unknown.
- **founder_fit 7:** squarely WP/PHP and under $1k. But 15 h/week makes "support that answers in a day" hard to keep, and that promise is the wedge itself.
- **reachability 6:** unhappy customers are public on the review pages linked in `win-plan.md`. Amelia also has public Discord and Reddit communities (linked from its help center). But WP.org forbids promoting plugins in its forums (e80), so reach is indirect: content, comparison pages and contacting reviewers through their own sites.
- **build_cost 4:** a full booking plugin (payments, calendar sync, notifications, timezones, staff) plus importers is months of work at 15 h/week, even with work already started.

### #2 Developer-first engine
- **pain 6:** medium-severity, real friction for devs (e39, e40, e41, e42, e45). Client-facing fallout for agencies (e62, e63, e64, e65). Few reviewers say they left over this alone.
- **willingness_to_pay 6:** agency tiers exist and are bought: LatePoint, Bookly, Amelia and BookingPress all sell 5 to 100 site licenses (pricing pages). No direct quote of an agency complaining about price.
- **competition_gap 5:** a reviewer switched to Fluent Booking, calling it "better integrated" (e56), so WP-native rivals exist. BookingPress advertises developer hooks.
- **founder_fit 9:** he is the buyer.
- **reachability 6:** devs who reviewed are identifiable (e62 to e65). Other dev communities weren't verified in this run (Reddit blocked).
- **build_cost 4:** same engine as #1, plus docs and APIs.

### #3 Rescue and migration service → importers
- **pain 7:** business-stopping incidents (e18, e65). Lock-in (e46, e47, e48). Weeks without help (e4, e5).
- **willingness_to_pay 5:** owners clearly spend money on these plugins ("paid more than 500 dollar", in `bookly-data-handling-is-insufficient`). But this run found **no evidence anyone pays a third party** to rescue or migrate a booking plugin, and reviewers are refund-sensitive (e60, e61). Capped at 5 until tested.
- **competition_gap 4:** self-serve importers already exist. BookingPress imports from Amelia, Bookly, Booknetic and LatePoint (e84). Sugar Calendar imports from Amelia (e85). PW Amelia Migration moves Amelia between sites (e86). I found no done-for-you rescue-and-migrate offer, but that's an absence, not proof.
- **founder_fit 9:** PHP plus SQL work, no budget needed, fits 15 h/week, and pays per job, which suits side income.
- **reachability 6:** same channels as #1.
- **build_cost 9:** export/import scripts for two known schemas, plus a checklist. Weekend to weeks.

## Winning gap sentence
> **Small appointment businesses on Bookly or Amelia, and the WordPress freelancers who set them up, can't get updates that don't break today's bookings or support that answers within a day, because both market leaders ship breaking updates behind slow ticket queues, and leaving means rebuilding customers, services and future appointments by hand.**

Evidence (claim `gap`): g1, g2, g3, g4, g5, g6, g7. These are 7 quotes across 6 URLs, all `yes`.

The wedge isn't "a better booking plugin", and it isn't "an importer" either, since importers exist (e84, e85). It's **the safe way off Bookly or Amelia**: a migration done for you with a no-lost-bookings promise, an update-safety layer, and the developer answering. Opportunity #3 is how to start selling it this month. #1 is where it ends up.

## Verdict (applying `references/scoring.md`)
- **GO fails.**
  - No opportunity reaches 65 (the best is 63).
  - #3 also has willingness_to_pay 5 (it must be 6 or more).
  - There are unresolved high-severity critic risks (see `critic.md`).
- **Pain is 7, which is 6 or more, so the verdict is PIVOT.**
- **The pivot (angle and channel):** don't launch as one more booking plugin among 784. Lead with **migration plus rescue** for people already stuck on Bookly or Amelia. Sell it first as a fixed-price service, and to the freelancers who installed them. Build the importers and the update-safety layer into your plugin, and use each migration as the onboarding to it. If the 7-day test shows people will pay for a migration, willingness_to_pay moves to 6+ and the verdict can be re-run.
