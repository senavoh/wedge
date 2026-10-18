# Launch kit: Shelf Sorted (pivot test)

The verdict is PIVOT, not GO. This kit exists to run the 7-day test cheaply. It is not a launch plan for an app.

## 1. Name and domain

Checked with `domain.py ... --tlds com,app,co` on 2026-10-17. Every `.co` lookup came back "unknown" (the registry didn't answer), so no `.co` is claimed.

| Name | Domain | Status from domain.py |
|---|---|---|
| **Shelf Sorted** (pick) | shelfsorted.com | available |
| Backroom Fix | backroomfix.com | available |
| Shelf Setup | shelfsetup.com | available |
| Receive Well | receivewell.com | available |
| Backroom Done | backroomdone.com | available |

Taken: shelfready.com, stocksmith.com/.app/.co, tallyroom.com/.app/.co, shelfwise.com/.app/.co, stockrescue.com, countright.com, stockfixer.com, backroomhq.com, tidystock.com, stocksorted.com, shopbackroom.com. Also checked and available on .app only: stockrescue.app, stockfixer.app, stocksorted.app, shopbackroom.app.

Confirm at a registrar before buying, and run a quick trademark search (USPTO). Avoid any name with "Stocky" or "Stockroom" in it: one is Shopify's product name, the other is a competitor's.

## 2. Pricing

- **Launch price: $199 one-time per location**, covering up to ~50 vendors. Founding offer: $99 for the first 3 shops, in exchange for a testimonial.
- **Competitor range:** apps run from free (Stockroom [c3]) to $19 to $59.99/mo for PO tiers (EZstock [c7], Supremo [c5], Stockie [c11]), $49+/mo (Prediko [c9]), and quote-only (Inventory Planner [c8]). Paid onboarding in the evidence: $5000 (Inventory Planner [e36]).
- **Why:** these shops refuse new monthly bills [e22, k6], so this is one payment with no subscription. $199 is well under the "$1000 to our yearly operating costs" ceiling one owner named [k6].

## 3. Cost to run

Not checked live this run. Confirm each before relying on it.

| Item | Monthly cost |
|---|---|
| Landing page on Cloudflare Pages or GitHub Pages | $0 (free tier) |
| Domain (shelfsorted.com) | registrar price, roughly $1/mo amortized; confirm at checkout |
| Booking: Cal.com or Calendly free plan | $0 |
| Payments: Stripe Payment Link | $0 monthly; Stripe's per-transaction fee only |
| Email: your existing inbox | $0 |
| **Total** | **about $1/mo plus payment fees** |

## 4. Landing page

`landing/index.html`: a single self-contained page. The waitlist/booking form is a `mailto:` placeholder. Replace `you@example.com` with your own address, or with a Tally/Formspree endpoint you control.

## 5. Seven-day validation test

**Experiment:** post one pure-help export checklist thread, and answer 8 to 10 open questions in the six Stocky threads (disclosing the offer at the end). Send message A to up to 10 named Stocky 1-star reviewers through their store contact pages. Point everyone at the landing page with a $99 founding offer.

**Pass bar:** **3 shops pay** (or put down a $50 deposit), or 10 booked calls from different shops.
**Fail:** fewer than 1 payment and fewer than 4 calls by day 7.

| Day | Do |
|---|---|
| 1 | Buy the domain, publish the landing page, create the Stripe link and the booking page. |
| 2 | Post the "read-only ends Nov 29" export checklist thread (no pitch). |
| 3 | Answer 4 open questions in the threads listed in `win-plan.md`. |
| 4 | Send message A to 10 named Stocky reviewers through their store contact forms. |
| 5 | Answer 4 more threads. Follow up on any replies. |
| 6 | Run any booked calls. Ask "would you pay $99 to have this done this week?" |
| 7 | Count payments, deposits, calls and objections. Decide. |

## Kill criteria

- 0 payments and fewer than 4 booked calls after 7 days.
- More than half the calls end with "I'll just use Stockroom myself."
- Thread moderators remove your posts as promotion (the channel is closed).
- After Nov 29, inbound questions in the Stocky threads stop.
- The first 3 setups each take more than 8 hours (no margin at $199).
