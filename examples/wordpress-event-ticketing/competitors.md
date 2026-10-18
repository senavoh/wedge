# Competitor map: selling event tickets from a small organizer's own WordPress site

Sources: the vendors' own pricing and home pages and their WordPress.org plugin pages, fetched 2026-10-17 into `raw/competitors.jsonl`. Ratings and install counts come from the WordPress.org pages. Prices are quoted exactly in evidence (all `official`). Events Manager Pro's pricing page returned HTTP 502, and its homepage came back as undecoded binary, so its price is **not fetched**.

| Name | URL | Starting price | Model | Free option | Contract | Headline (quoted) |
|---|---|---|---|---|---|---|
| Event Tickets / Event Tickets Plus (Liquid Web / StellarWP) | theeventscalendar.com | Free with a 2% commission on Stripe/Square (c1, c18); Pro $399/yr (c2); Elite $599/yr (c3) | Annual licence | Yes, but it takes 2% | Annual, renews | "Zero-commission ticketing" (paid tiers) |
| Tickera | tickera.com | $149 in year one, renewing at $99/yr (c4, c5); Bundle $199/yr; Lifetime $399 | Annual or lifetime licence | Yes (WordPress.org, 2,000+ installs) | Annual | "The commission-free event ticketing plugin for WordPress." (c6) |
| FooEvents | fooevents.com | Bundles $199 / $249 / $399 (c7) | Annual licence; requires WooCommerce | No | Annual | "No commission or ticket fees." (c8) |
| Event Espresso | eventespresso.com | Decaf $0 with 3% pay-as-you-go (c9); $129/yr (c10); $399/yr | Annual licence | Yes, but it takes 3% | Annual | "$0 per-ticket commission fees" |
| Modern Events Calendar | webnus.net | Pro from $99/yr (c11) | Annual licence | Lite (calendar only) | Annual | not captured |
| Eventin (Themewinter) | themewinter.com | From $89/yr | Annual or lifetime licence | Yes (10,000+ installs) | Annual | "No SaaS fees. No per-ticket cuts. Yours to own." (c12) |
| Events Manager (+ Pro) | wp-events-plugin.com | not fetched | Annual licence | Yes (60,000+ installs, 4.2 stars) | n/a | n/a |
| Ticket Tailor (hosted, with a WordPress embed plugin) | tickettailor.com | £0.60 per ticket pay-as-you-go, from £0.22 prepaid (c13, c14); free tickets free | Per ticket | Free events free | None | "Unbeatable prices, no contracts, simple." |
| Eventbrite (hosted) | eventbrite.com | 3.7% + $1.79 per ticket plus 2.9% processing (c15) | Per ticket | Free events free | None | "Create an Event for Free" |
| Humanitix (hosted) | humanitix.com | 5% + $1.29 per paid ticket in USD (c16) | Per ticket | Free events free | None | n/a |
| Zeffy (hosted, nonprofits only) | zeffy.com | $0 (c17) | Free; donation-tip model | Yes | None | "The only 100% free fundraising platform for nonprofits" |
| Substitute: WooCommerce product + PDF, or a Google Form + PayPal | n/a | $0 | n/a | Yes | n/a | n/a |

## Per competitor

- **Event Tickets / The Events Calendar.** The default choice: 90,000+ active installs on Event Tickets, rated 3.5. It's really built for organisations already running The Events Calendar. Strong at calendar views, an all-in-one stack and a big install base. Weak at reliability after updates, support and licensing since the Liquid Web takeover, and price rises. The free tier takes 2% unless you pay $399/yr. Evidence: s13, s14, s15, c1, c2, c18.
- **Tickera.** It's for organizers who want seating charts and a check-in app with no commission. Its pitch is commission-free selling, a lifetime option and seating charts. Smaller (2,000+ installs, 4.5 stars). The year-one price includes a $50 activation fee (c5). Evidence: c4, c5, c6.
- **FooEvents.** It's for WooCommerce shops adding tickets. Strong at Wallet passes, POS and bookings. It needs WooCommerce, which is heavy for a church or theater site, and starts at $199/yr. Evidence: c7, c8.
- **Event Espresso.** It's for registration-heavy events such as conferences and classes. The free Decaf tier charges 3%; $129/yr removes it. Evidence: c9, c10.
- **Modern Events Calendar and Eventin.** Calendar-first suites. Ticketing is one module among many (AI, speakers, themes). Evidence: c11, c12.
- **Ticket Tailor.** The hosted, low-flat-fee option. It's for organizers who don't need tickets inside WordPress. Strong at its fees, no contract and a 50% charity discount. Weak for this buyer: the box office isn't native to their site, the WordPress plugin was last updated 9 months ago (4,000+ installs, 4.3 stars), and you pay per ticket forever. Evidence: c13, c14.
- **Eventbrite and Humanitix.** Hosted marketplaces with percentage fees. Usually the buyer pushes those fees onto attendees. They are the thing these WordPress plugin buyers are trying to avoid. Evidence: c15, c16.
- **Zeffy.** Free for registered nonprofits, so it removes the price argument for that segment entirely. Evidence: c17.

## Feature matrix (features taken from complaint language)

Marked from each vendor's own pages. `unknown` where the page didn't say.

| Feature | Event Tickets free | Event Tickets Pro | Tickera | FooEvents | Event Espresso | Ticket Tailor | Eventbrite |
|---|---|---|---|---|---|---|---|
| 0% platform fee | no | yes | yes | yes | partial (paid only) | no | no |
| Total cost under $100/yr for a small organizer | yes (but 2%) | no | partial (renewals $99) | no | no | partial (depends on volume) | no |
| Works without WooCommerce | yes | yes | yes | no | yes | yes | yes |
| QR check-in app | unknown | yes | yes | yes | unknown | yes | yes |
| Tickets live on your own site | yes | yes | yes | yes | yes | partial (embed) | no |
| Built-in seating charts | no | no (Elite) | partial (Bundle) | yes | unknown | yes | yes |
| Hosted, so updates can't break checkout | no | no | no | no | no | yes | yes |
| Ticket delivery monitoring / resend | unknown | unknown | unknown | unknown | unknown | yes | yes |
| Month-to-month or no-contract pricing | n/a | no | no | no | no | yes | yes |

## Where it's crowded and where it's empty

- **Crowded:** "zero-commission WordPress ticketing plugin". Tickera, FooEvents, Eventin, Event Espresso and Event Tickets Plus all lead with it (c6, c8, c12). Commission-free is table stakes, not a wedge.
- **Crowded:** hosted low-fee ticketing. Ticket Tailor sells at £0.22 to £0.60 per ticket, and Zeffy is free for nonprofits.
- **Thin:** a ticketing option that **lives on the organizer's WordPress site but can't be broken by plugin updates**, with checkout and ticket delivery hosted and monitored. Every plugin runs checkout inside the customer's WordPress, which is where the "update broke it" and "tickets never arrived" complaints come from (s15). Every hosted option takes the box office off-site.
- **Thin:** an honest, small, flat price for low-volume organizers. The free plugin tiers take 2 to 3% (c1, c9), and removing that costs $129 to $399 a year (c2, c10).
