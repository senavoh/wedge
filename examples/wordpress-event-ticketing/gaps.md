# Gaps, ranked

Scoring follows `references/scoring.md`: total = round(pain×2.5 + wtp×2 + gap×2 + fit×1.5 + reach×1.2 + build×0.8). The two event-ticketing gaps (A and B) were mined in depth (842 records). The Shopify and cookie niches (C to G) were scored only from scout evidence: one review page each, so their pain scores lean on fewer authors. Each rests on a single review page, which is short of the rubric's 2+ sources for pain ≥ 7, so pain is capped at 6. Reach is held at 6 because free places to pitch weren't checked.

| # | Opportunity | Pain | WTP | Gap | Fit | Reach | Build | Total |
|---|---|---|---|---|---|---|---|---|
| A | **Hosted, update-proof ticket checkout that embeds natively in a small organizer's WordPress site** | 7 | 6 | 3 (was 5 before critic) | 6 | 5 (was 6) | 6 | **55** after critic (60.5 before) |
| A′ | Pivot: A sold to WordPress agencies managing small-org client sites (hypothesis) | 7 | 6 | 4 | 6 | 5 | 6 | 57 |
| B | Simple flat-price WordPress ticketing plugin for micro organizers (under 20 events a year) | 7 | 6 | 3 | 7 | 6 | 6 | 58 |
| C | Shopify site search for small catalogs after the 2026 Search & Discovery regressions | 6 | 6 | 3 | 7 | 6 | 5 | 55 |
| D | Shopify packing-slip and invoice printing (Order Printer refugees) | 6 | 5 | 3 | 8 | 6 | 8 | 57 |
| E | Shopify digital-file and licence-key delivery | 5 | 6 | 3 | 8 | 6 | 8 | 56 |
| F | Shopify bundles with variants | 6 | 6 | 3 | 6 | 6 | 5 | 53 |
| G | Cookie consent for WordPress users whose free plugin went paid | 5 | 3 | 3 | 7 | 6 | 7 | 48 |
| H | Shopify subscriptions for small merchants | 6 | 6 | 2 | 4 | 6 | 3 | 47 |

## Winning gap (A)

> **Small organizers (community theaters, clubs, workshop hosts running roughly 10 to 50 events a year) who sell tickets from their own WordPress site can't get a checkout that keeps working through updates and reliably delivers tickets, at a small predictable price, because every WordPress plugin runs checkout inside their site (where updates break it) and every hosted option charges per ticket and drops an off-brand embed on their page.**

Evidence for the gap claim: r1, r2, r13, s15 (plugins break and tickets go missing), r23 (hosted embed looks foreign), r24 (a buyer wants hosted next time). Three or more different URLs, so it passes the two-source rule as long as they verify.

## Score reasoning for A
- **Pain 7.** People leave and say so: r10 (left over the renewal), r6 (installed another plugin), s15 (moved ticket sales elsewhere), r4 (removing it from sites). Many different authors across 8 plugins, plus HN on fees (r22, r25). Held below 8 because most threads are over 2 years old (101 of 709 are recent), and ticket-delivery failures are rare even though they're severe.
- **WTP 6.** They already pay $99 to $399/yr (c2, c4, c10, c11) and complain about increases rather than about paying (r9, r10, r12). Held at 6 because free options are strong for part of the market: Zeffy is free for nonprofits (c17), the free plugin tiers just take 2 to 3% (c1, c9), and Ticket Tailor's WordPress reviews include several "not free" complaints.
- **Competition gap 5.** "Commission-free plugin" is crowded (c6, c8, c12), and hosted low-fee ticketing exists (c13, c14). The specific gap, a hosted, monitored checkout that looks native in WordPress, is thin, not empty: Ticket Tailor's embed does it badly (r23).
- **Founder fit 6.** It's a web app plus a thin WordPress plugin and Stripe Connect, all within the founder's skills and budget. The stretch: being on call when a customer's event goes live doesn't fit 10 hours a week well.
- **Reachability 6.** Buyers gather in public on the WordPress.org review and support forums of these plugins (709 threads collected), on HN, and in WordPress/nonprofit/theatre communities. But WordPress.org forum rules don't allow soliciting in other plugins' threads, so the main free channel is your own WordPress.org listing plus content. That's paid or slow, not "3+ free places where you can pitch".
- **Build cost 6.** Hosted checkout via Stripe Connect, QR ticket email, a check-in PWA, and a WordPress shortcode/block that renders natively: a few weeks to a couple of months at 10 hours a week.

## Why the others rank lower
- **B:** the same pain, but it competes head-on with Tickera, Eventin and Event Espresso, which all already say "commission-free" (c6, c12), and it inherits the "updates break checkout" problem.
- **C to F:** every Shopify niche already has a loved paid app at 4.7 to 4.9 stars (scout table). The pain is real (s1 to s12), but competition_gap is 3 at best.
- **G:** the complaint is that it should be free (s16, s17), so WTP is low, and there's compliance liability.
- **H:** a crowded, payments-heavy build.

## Verdict
Before the critic, A totalled 60.5. The critic found Ticket Spot already selling the exact proposition (k1, k2, k4) and confirmed the WordPress.org forums forbid promotion (k8). That cuts the gap to 3 and reach to 5, and **A is 55**. Nothing reaches 65. **PIVOT**, toward A′ (the agency buyer/channel); see `critic.md`. D (Order Printer) ties A′ on paper at 57, but they rest on scout-depth evidence only, and each faces a loved 4.7+ paid incumbent.
