# Win plan (for the PIVOT: update-proof ticketing sold to WordPress agencies)

The verdict is PIVOT, so this plan is a **test plan**, not a launch plan. It's built for A′: hosted, update-proof ticketing that WordPress agencies and freelancers install on their small-organizer clients' sites. Every move cites evidence. The moves with no evidence were cut.

## Switching triggers

| Trigger | Evidence | Move |
|---|---|---|
| Licence renewal email with a price rise (TEC Pro is now $399/yr, c2; "gone up BY 50%", r10; "Over $140.00 more", r9) | r9, r10, r12, c2 | A "renewal-season" page: what each competitor charges now (from their pricing pages), and a flat per-agency price that's published and locked. |
| A plugin update breaks a client's site or ticket sales | r1, r2, r3, a1, a2 | A post-mortem-style guide: "Your events plugin update broke a client's checkout: a 30-minute recovery checklist". Rank it for the error searches. The product is the last step of the checklist. |
| Paid support goes silent | r6, r7, r8 | A named human, a published response time, and a status page from day one. |
| Liquid Web / Nexcess-era licensing chaos at The Events Calendar | s14, r20, r9 | Free migration of a client's upcoming events and ticket types from Event Tickets (CSV import), done by you for the first 10 agencies. |
| Tickets go missing before a sold-out event | s15, r13 | A delivery log per order (sent / opened / bounced), plus one-click resend. Make it the demo. |

## Positioning
- **Primary:** "Ticketing for your clients' WordPress sites that a plugin update can't break. One flat price per agency, renewals locked."
- Alt 1: "Stop babysitting event plugins. Checkout runs off-site, the tickets look like the client's site, and you see every ticket that was sent."
- Alt 2: "The events plugin you won't have to remove from all of the sites you built." (Echoes a3.)

Be honest about the overlap: Ticket Spot (k1) and Ticket Tailor (k5) already claim the organizer-facing version. Our claimed spot is **the agency's view across many clients**, which we did not find either of them marketing. That's an absence in our sources, not a verified fact.

## Offers that win switchers
1. **Free migration from Event Tickets / The Events Calendar for the first 10 agencies.** Answers licensing chaos and updates (s14, r1).
2. **A published flat price that never changes on renewal.** Answers price rises (r9, r10, r12).
3. **Payouts straight into each client's own Stripe account, no platform hold.** Answers the trust risk from failed platforms (k9, k10, k12) and keeps chargeback liability off you (k11).
4. **"Fixed: tickets that never arrive."** A delivery log and resend, stated on the pricing page (s15, r13).
5. **Named-human support with a stated response time.** Answers r6, r7, r8.

## Build first (pain answered per unit of effort)
1. **Hosted checkout via Stripe Connect direct charges, plus a WordPress block/shortcode that inherits the theme's fonts and colours.** Answers updates (r1, r2) and the off-brand embed (r23).
2. **Ticket email with QR code, a per-order delivery log and resend.** Answers missing tickets (s15, r13).
3. **A mobile-web (PWA) check-in scanner.** Table stakes; every competitor has one (matrix).
4. **CSV import of events and attendees from Event Tickets.** Answers licensing and switching (s14).
5. **An agency dashboard: all clients, upcoming events, sales, failed deliveries.** The pivot's whole reason to exist (a1 to a4).

Explicitly not first: seating charts, recurring-event series, calendar views. The Events Calendar's bloat is a complaint (r19, r21).

## Where unhappy customers are
| Place | URL | Why | Rule |
|---|---|---|---|
| Event Tickets 1-star reviews | https://wordpress.org/support/plugin/event-tickets/reviews/?filter=1 | 70 1-star reviews; recent price and licensing complaints (s13) | **No promotion allowed** (k8). Read it, learn from it, never pitch there. |
| The Events Calendar 1-star reviews | https://wordpress.org/support/plugin/the-events-calendar/reviews/?filter=1 | 328 1-star reviews; agencies among the reviewers (a1, a3) | Same: no promotion (k8). Many reviewers link their own sites or profiles; contacting them through **their own** public channels is the respectful route. |
| Your own WordPress.org plugin listing | https://wordpress.org/plugins/ | The only WordPress.org surface where you may describe your product | Follow the plugin guidelines. Ticket Spot's 40+ installs (k2) show it is slow. |
| Search: "the events calendar alternative", "event tickets plus alternative" | n/a | Switch-intent searches | Comparison pages (assets/vs-event-tickets.md) |
| WordPress agency and freelancer communities (e.g. Post Status, r/ProWordPress, Codeable) | https://poststatus.com/ , https://www.reddit.com/r/ProWordPress/ , https://www.codeable.io/ | Where agencies discuss plugin choices | **Not verified this run:** Reddit is blocked on this network and the rules weren't fetched. Read each community's rules first. |

## Trust signals (credible from day one)
- A public, fixed price page with a "renewal = same price" promise (against r9, r10).
- Money never touches us: direct charges to the client's own Stripe account (against k9, k10, k12).
- A public status page and delivery stats (against s15).
- A data export promise: attendees and orders as CSV any time.
- The founder's name and support hours on the site (against r6, r8).

## Stop doing (what customers hate that a newcomer is tempted to copy)
- Injecting ads or upsell menus into wp-admin (r19, r20).
- A hidden platform fee on the free tier (r17, c1).
- Feature-gating basics in a "free" version (r21; "The free version is useless" thread).
- Renewal price jumps (r10).

## First 10 customers
1. **Day 1: write the recovery checklist** ("events plugin update broke checkout") and the comparison page (assets/vs-event-tickets.md). Publish both on your own site.
2. **Day 1: build a list of agencies from public reviews.** Take reviewers who say they manage client sites (a1, a2, a3, a4, a5). Find their own agency website from their public WordPress.org profile. Email them there, never in the forum. Script: assets/outreach.md, message 1.
3. **Day 2: answer, don't pitch,** in agency communities whose rules allow it. Give a genuinely useful answer about recovering from a broken events update, with no link unless the rules allow one.
4. **Day 2: run a free migration offer** for the first 10 agencies, delivered by you by hand.
5. **Day 3: run small ads** on switch-intent searches ("the events calendar alternative") with assets/ads.md, $50 cap.
6. **Day 3: ask Codeable/freelance WordPress developers** (on their public profiles' contact forms) whether they'd resell it to clients.
7. **Days 4 to 7: run 5 calls with agencies.** Ask what they pay per client per year for events plugins today, and whether they'd pay a flat agency price.
