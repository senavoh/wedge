# Competitors: WordPress appointment booking for local service businesses

Run date: 2026-10-17/18 (UTC). Prices are what each vendor's own pricing page showed when fetched with `fetch.py page` (saved in `raw/pricing.jsonl`, `raw/substitutes.jsonl`). Most showed an autumn sale, so the first number is the list price and the second the sale price. Install counts and ratings come from the WordPress.org plugin API (`raw/wporg-plugin-info.jsonl`). They are data, not quotes.

## Overview

| Name | URL | Starting paid price (list → sale) | Model | Free option | Contract / renewal | WP.org installs · rating (n) |
|---|---|---|---|---|---|---|
| **Bookly** | booking-wp-plugin.com | Pro $99 → $39/yr, or $129 → $99 lifetime, 1 site (e67). Business $149 → $129 lifetime (e68) | Per site, tiered bundles | Yes (WP.org) | Annual renews yearly, or lifetime | 60,000+ · 88/100 (585) |
| **Amelia** | wpamelia.com | Annual prices didn't render in fetched text (JS). Pricing is "geo-based" (e70). Up to 40% off the first year only (e82) | Per domain, 4 tiers (Starter, Standard, Pro, Elite) | Yes (WP.org) | Annual renews at the full crossed-out price (e24). 15-day refund (e69) | 90,000+ · 92/100 (790) |
| **LatePoint** | latepoint.com | Starter $99 → $79/yr, 1 site (e72) | Per site; every plan has every feature (e71) | Yes (WP.org) | Renewals at full price (e73) | 100,000+ · 98/100 (104) |
| **Simply Schedule Appointments (SSA)** | simplyscheduleappointments.com | Plus $129 → $99/yr. Team scheduling only in Business, $499 → $399/yr (e74) | Per site, tiered features | Yes (Basic, WP.org) | Annual, full price on renewal | 50,000+ · 100/100 (155) |
| **BookingPress** | bookingpressplugin.com | Standard $89/yr (e76) | Per site, tiered | Its WP.org listing is **closed** (e78, e83) | Annual or lifetime | Closed on WP.org since 2025-02-01, "Guideline Violation" |
| *Substitute:* **Fresha** (SaaS) | fresha.com | Independent $19.95/month (e79), plus a 20% one-time marketplace commission on new clients | Per bookable team member | 7-day trial | Monthly | n/a |
| *Substitute:* **Square Appointments** (SaaS) | squareup.com | Plan prices are JS-rendered and weren't captured. The page shows a solo tier billed only through "Processing fees" | Processing fees + per-location tiers | Solo tier (price not captured) | Monthly | n/a |
| *Adjacent:* **Sugar Calendar Bookings** | sugarcalendar.com | not checked | — | — | — | has a one-click Amelia importer (e85) |
| *Substitute:* phone + paper / Google Calendar | — | $0 | — | — | — | — |

WordPress.org lists **784** results for "appointment booking" (`raw/wporg-plugin-info.jsonl`, query_plugins). Many recently updated entrants sit at 70 to 2,000 installs. Examples: radius-booking (400), truebooker (600), gembooking (200), rox-appointment-booking (1,000). Getting found is hard.

## Bookly
- **Who it's really for:** WordPress site owners and the freelancers who build sites for them, across many verticals (its nav lists salons, nail salons, tutoring, massage, dental clinics).
- **Strong at:** it's mature (on WP.org since 2014) and widely used. Its positioning now leads with "No hidden costs or add-ons" (e66) and "no per-staff seat fees, no per-booking commissions" (e81). Even unhappy reviewers praise the design and booking form ("one of the most visually appealing booking plugins", in `so-much-potential-1`).
- **Weak at:** support speed and quality (e1, e2, e3, e9). Updates that break live bookings (e10, e11, e12). Support and updates tied to license expiry, which reviewers call "ransom" (e19 to e23). A long history of add-on nickel-and-diming (e25 to e28). That last complaint is mostly 2018 to 2023, and the current pricing page bundles add-ons into tiers, so **don't lead with it.**
- Evidence: e1–e3, e9–e12, e19–e23, e25–e28, e32–e34, e38, e46, e49, e51, e53, e66–e68, e81.

## Amelia
- **Who it's really for:** small and mid service businesses that want a polished front end. It also sells events. Its pricing nav targets "Beauty and Spa Salons, Barbershops".
- **Strong at:** a slick UI and a big feature list (reviewers concede "great UI" and "the plugin looks solid"). Top install count of the WP.org booking plugins mapped here except LatePoint.
- **Weak at:** support taking days to weeks (e4 to e7). Updates breaking or wiping data, with several reviews from 2026 (e13 to e15, e17). Not WordPress-native: it has its own user system and tables and few hooks (e39 to e41, e43, e45). The salon front desk can't book a multi-service appointment from the backend (e35). Long-ignored requests (e36). Annual renewal jumps to the full price (e24).
- Evidence: e4–e7, e13–e17, e24, e29–e30, e35–e36, e39–e41, e43, e45, e47–e48, e50, e52, e54–e56, e58, e69–e70, e82.

## LatePoint
- **Who it's really for:** salons, consultants and tutors (its nav lists Beauty Salons and Private Tutors).
- **Strong at:** every feature on every plan (e71) and multiple agents on the $79 Starter. It's the best rated of the larger plugins: 98/100 from 104 ratings, with only 2 one-star reviews.
- **Weak at:** almost no public complaints. The only two 1-star reviews are about Google Calendar being missing from the free version (e31) and tables left behind on uninstall (e44).
- **Threat level: high.** This is the plugin unhappy Bookly and Amelia users can already switch to.

## Simply Schedule Appointments
- **Who it's really for:** solo service providers and small teams who want simple scheduling.
- **Strong at:** support. It promises a reply to every email within one business day (e75) and is rated 100/100 from 155 ratings. No 1 to 3 star review topics came back from WP.org.
- **Weak at:** team scheduling (any salon with staff) is gated to Business at $399 to $499/yr (e74).

## BookingPress
- **Who it's really for:** the same buyer.
- **Strong at:** a long add-on list. It already sells a **Migration Addon** (e77).
- **Weak at:** bugs and slow support (e8, e18, e37, e61). Its WP.org listing is closed (e78, e83). That cuts it off from free directory discovery.

## Feature matrix (features chosen from complaint language)

Values come from vendors' own pricing and feature pages and from review evidence. `unknown` means it wasn't checked from a fetched source.

| Feature buyers ask for | Bookly | Amelia | LatePoint | SSA | BookingPress | Fresha |
|---|---|---|---|---|---|---|
| All features in the entry paid tier | partial | no | yes | no | no | yes |
| Unlimited staff on entry paid tier | unknown | unknown | yes | no | yes | no |
| Same price at renewal as at purchase | unknown | no | no | no | unknown | unknown |
| Bookings keep working if license lapses | partial | unknown | yes | unknown | unknown | no |
| Stated support reply time of 1 business day or less | unknown | partial | unknown | yes | unknown | unknown |
| Multi-service booking from the admin (front desk) | unknown | no | unknown | unknown | partial | unknown |
| Gap-free slot logic for mixed durations | no | unknown | unknown | unknown | unknown | unknown |
| Uses WordPress users (one login) | unknown | no | unknown | partial | unknown | no |
| Developer hooks + docs | partial | partial | unknown | partial | yes | no |
| Clean uninstall (removes its tables) | no | no | no | unknown | unknown | unknown |
| Import from Bookly / Amelia | unknown | unknown | unknown | unknown | yes | unknown |

Basis for the less obvious cells:
- **All features in entry tier:** Bookly's Business tier is pitched "For growing service businesses that need every core paid feature", so Pro doesn't have them all. Amelia and SSA gate features by tier. LatePoint: e71.
- **Unlimited staff:** the fetched Bookly pricing text lists the same feature names under every plan, with no checkmarks, so per-tier gating couldn't be read. That's why it's `unknown`.
- **Amelia support:** a reviewer says "They are supposed to get to us within 24 hours" (e4).
- **Amelia developer hooks:** the Pro tier lists a REST API, and reviewers complain about hooks (e40).
- **Bookings work on lapse:** LatePoint says sites "will continue to function", per its pricing FAQ. Bookly is `partial` because reviewers say it does, but the dashboard nags or locks (`it-used-to-be-so-great`, e22).
- **SSA uses WordPress users:** its pricing feature list includes "Connect appointments to WordPress users".
- **BookingPress developer hooks:** its nav links "Developer Hooks" and "REST API".
- **Clean uninstall:** e43, e44, e49.
- **BookingPress import:** its Migration Addon imports "from Amelia, Bookly, Booknetic, and LatePoint" (e77, e84).
- **Other importers found during the critic pass:** Sugar Calendar Bookings imports from Amelia in "a few clicks" (e85). PW Amelia Migration moves Amelia data between sites (e86).
- **Update safety:** I didn't find any vendor that promises an update will never break live bookings, so the matrix has no row for it.

## Where it's crowded and where it's empty
- **Crowded:** feature lists. Everyone sells staff, services, payments, calendar sync, SMS and coupons, and 784 directory results fight over "appointment booking". A new plugin can't win on features.
- **Crowded:** low prices. Bookly Pro is $39 for the first year and LatePoint Starter is $79 with everything. There's no room above that for a newcomer.
- **Empty (among the two leaders):** a credible promise that **an update won't break today's bookings**, and **support that answers in a day**. SSA claims the second. Nobody claims the first in fetched copy.
- **Not empty (corrected in the critic pass):** a **self-serve switch-in path** already exists:
  - BookingPress imports from Amelia, Bookly, Booknetic and LatePoint (e84).
  - Sugar Calendar imports from Amelia (e85).

  An importer is table stakes for a challenger, not a moat. What I didn't find is a **done-for-you** move with a "no booking lost" guarantee, from someone who answers.
- **Thin:** salon-specific scheduling logic, such as multi-service front-desk booking and gap-free slots. SaaS (Fresha, Square) covers this well for salons that are willing to leave WordPress.
