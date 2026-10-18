# Critic pass (deep: all six checks)

Run by a separate subagent that saw only `gaps.md`, `competitors.md` and `pains.md`. Briefed as "a skeptical investor who has seen 1,000 of these". Every source it cites was saved with `fetch.py` to `raw/critic.jsonl` (15 records; ThunderTix returned HTTP 403, and one Stripe support page saved only 78 characters so it isn't used).

## Headline finding
**The exact product already exists.** Ticket Spot has a free WordPress.org plugin that puts a hosted checkout on the organizer's own page, pays out to the organizer's own Stripe, Square or PayPal account at 0% platform fee, and pitches exactly our "updates can't break checkout" angle (k1, k4). It targets churches, theatres and community centres. It has **40+ active installs** (k2), and paid plans start at $29.99/month (k3). So the gap isn't empty, and the positioning alone hasn't pulled demand through WordPress.org.

## Risks

| # | Check | Risk | Severity | Rebuttal |
|---|---|---|---|---|
| 1 | Tried and died | Ticketing platforms that held organizers' money failed and left them unpaid: Brown Paper Tickets (k9), Lyte in 2024 (k12), Tickets.ie in June 2026 (k10). Small organizers have learned to distrust unknown vendors. | medium | Partial. Every failure was a platform holding the funds. Direct charges into the organizer's own Stripe account (Ticket Spot's model, k4) avoid that. A solo vendor still pays a trust tax. |
| 2 | Free incumbent | Zeffy is free for nonprofits (k7, c17). Ticket Tailor lets organizers pass fees to buyers and "sell tickets for free" (k6), and already markets an embedded WordPress checkout (k5). Ticket Spot is free up to 20 attendees a month (k3). | high | **Unresolved** for nonprofits. For for-profit workshop hosts and promoters, Zeffy doesn't apply, but fee pass-through makes per-ticket cost nearly invisible to the organizer. Our "embed looks foreign" evidence (r23) is one 2021 review against Ticket Tailor's own current claim (k5). |
| 3 | Real pain, nobody pays | The one product selling the exact fix has 40+ installs (k2). Delivery failures are rare in our corpus (pains.md). | high | **Unresolved.** 40+ installs only measures the WordPress.org channel; Ticket Spot's other channels weren't checked. Buyers do pay $99 to $399/yr today (c2, c4, c10) and complain about increases (r10, r9). |
| 4 | Channel closed | WordPress.org forums, where this buyer complains in public, forbid promoting your own or others' plugins (k8). What's left is your own listing plus SEO, and Ticket Spot shows that's slow. | high | **Unresolved** for direct-to-organizer. Partial for a different buyer: agencies and freelancers who build these sites appear repeatedly as reviewers (a1 to a5). They are reachable as a B2B channel, but that's a hypothesis to test. |
| 5 | Copyable in a week | It's already copied (Ticket Spot) and adjacent (Ticket Tailor's embed, k5). No first-mover window. | high | **Unresolved** as a moat. The only room left is price and execution: Ticket Spot is $29.99/mo against $99 to $149/yr plugin renewals. That isn't defensible. |
| 6 | Liability and trust | With destination charges, the platform is liable for chargebacks (k11). Cancelled events cause refund waves. Event-night on-call doesn't fit 10 hours a week. | medium | Partial. Direct charges on the organizer's own Stripe account shift most dispute exposure to the organizer. That part comes from search snippets, not saved evidence. Event-night support is still unresolved. |

## Effect on scores (applied in gaps.md and report.json)
- **competition_gap 5 → 3.** A live product covers the exact proposition (k1, k4), and Ticket Tailor claims the embedded WordPress checkout (k5).
- **reachability 6 → 5.** The forum channel is closed to promotion (k8), and the WordPress.org listing channel is unproven (k2).
- Opportunity A: 7×2.5 + 6×2 + 3×2 + 6×1.5 + 5×1.2 + 6×0.8 = 55.3, which is **55**.

## Verdict after critic
**PIVOT.** Pain is 7 (≥ 6), but the total of 55 is under 65, and there are unresolved high-severity risks (2, 3, 4, 5). GO fails on several counts.

**Named pivot (buyer + channel): sell to WordPress agencies and freelancers who maintain event sites for small clients, not to the organizers directly.** The evidence that this buyer exists and is hurting: agencies report updates "crashing our customer sites" (a1) and breaking "several of our customers sites" (a2), are "slowly removing this from all of the sites I built" (a3), hold multiple licences (a4), and choose plugins on clients' behalf (a5). The offer: hosted, update-proof ticketing with a multi-client dashboard, white-label, and one flat per-agency price. Agencies are a channel Ticket Spot (aimed at organizers) doesn't obviously serve. **Not yet validated:** where agencies gather and whether they'd pay need a 7-day test (see the win plan).
