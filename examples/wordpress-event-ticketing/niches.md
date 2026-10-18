# Niche scout (scratch, deep)

## Seeds and sources (Reddit blocked on this network, so not used)

- **Hacker News, 23 seeds** (`raw/scout.jsonl`, 434 records): "I wish there was a tool for etsy sellers", "alternative to mailchimp too expensive", "is there a tool for tutors scheduling", "alternative to calendly", "still using excel for", "spreadsheet for small business inventory", "alternative to kajabi", "is there an app for teachers grading", "alternative to linktree", "podcast hosting too expensive", "alternative to zapier too expensive", "how do you all handle client onboarding freelance", "switched from quickbooks", "alternative to typeform", "newsletter platform too expensive substack alternative", "Shopify app too expensive", "alternative to hotjar", "wordpress plugin too expensive", "alternative to docusign", "is there a tool for online course creators", "alternative to gumroad fees", "help desk too expensive small team", "alternative to hubspot crm small business". Digest: `signals-scout.md`. HN signal was dominated by "Show HN: open-source alternative to X" launches (Calendly, DocuSign, Typeform, Hotjar, Linktree). That is supply, not unmet demand, so few niches came from it directly.
- **Marketplace low-star pages** (`raw/scout-shopify.jsonl`, `raw/scout-market.jsonl`): 1-star (and 1+2-star) review pages saved for 31 Shopify apps and 18 WordPress.org plugins (21 more guessed Shopify handles returned 404) across e-commerce ops, store design, digital goods, subscriptions, events, donations, LMS, membership, email, cookie consent, podcasting, backups and forms. The rating distributions on those pages are a cheap pain screen: an app whose 1-star share is 20%+ is a candidate.
- **App Store search** (`raw/scout-apps.jsonl`): teamsnap, music lesson studio, tutoring business, etsy seller. All mobile-first or marketplace-network businesses; dropped (see below).
- **Event ticketing deep-dive** (`raw/scout-events.jsonl`): all 60 1-star review threads linked from the Event Tickets and The Events Calendar review pages (`fetch.py links` then `pages --from`).

## Rating screen (from the fetched pages, not estimates)

| Product | Ecosystem | Rating | Reviews | 1-star |
|---|---|---|---|---|
| Shopify Search & Discovery (Shopify's own) | Shopify | 2.6 | 512 | 107 |
| Shopify Bundles (Shopify's own) | Shopify | 2.8 | 568 | 130 |
| Event Tickets and Registration | WordPress | 3.5 | 235 | 70 |
| SendOwl | Shopify | 3.5 | 91 | 23 |
| Shopify Order Printer (Shopify's own) | Shopify | 3.6 | 380 | 172 |
| Shopify Subscriptions (Shopify's own) | Shopify | 3.7 | 865 | 163 |
| The Events Calendar | WordPress | 4.2 | 2,459 | 328 |
| Marketplace Connect | Shopify | 4.1 | 2,128 | 308 |
| Paid Shopify alternatives checked (Searchanise, Rapid Search, Doofinder, Order Printer Pro, Bundler, Simple Bundles, Seal, Filemonk, Sky Pilot) | Shopify | 4.7 to 4.9 | 414 to 3,147 | 2 to 59 |

The pattern: Shopify's own free apps are hated, but each one already has a loved paid alternative rated 4.7+. In WordPress events, the incumbents themselves are the weak ones.

## Shortlist (7)

### 1. Small organizers selling event tickets from their own WordPress site  <- top pick
- **Buyer and job:** community theaters, clubs, churches, small venues and workshop hosts who run a WordPress site and want to sell tickets there with QR check-in, without Eventbrite.
- **Signal:** 60 1-star threads on Event Tickets (3.5 stars) and The Events Calendar (328 1-star reviews). Recurring themes: price rises and a licensing mess after the Liquid Web / Nexcess takeover, missing ticket emails, broken Stripe. Evidence: s13, s14, s15.
- **Who serves them now:** Event Tickets (+ Plus), The Events Calendar Pro, Tickera, Events Manager, Modern Events Calendar, FooEvents; hosted: Eventbrite, Ticket Tailor, Humanitix.
- **Founder fit:** a WordPress plugin plus a small hosted check-in web app. Weeks of work, $0 to $50/mo to run, sold through the free WordPress.org directory.

### 2. Shopify merchants whose site search broke after the 2026 Search & Discovery changes
- **Buyer and job:** small-catalog Shopify stores that relied on free native search (SKU lookups, synonyms).
- **Signal:** 107 1-star reviews, many dated Sept to Oct 2026. Evidence: s1, s2, s3.
- **Who serves them now:** Shopify Search & Discovery, Searchanise, Rapid Search, Doofinder, Boost, Klevu.
- **Founder fit:** fine, but loved paid apps start around $9 to $19/mo (per comparison blogs, unverified), so the gap is thin.

### 3. Shopify merchants printing invoices and packing slips
- **Signal:** Order Printer has 172 1-star reviews out of 380. Evidence: s4, s5.
- **Who serves them now:** Shopify Order Printer, Order Printer Pro (4.9, 2,989 reviews), Sufio (4.9).
- **Founder fit:** easy build, but a loved incumbent covers it. It also sits next to the existing invoicing example.

### 4. Shopify merchants building bundles with variants
- **Signal:** Shopify Bundles is rated 2.8 (130 1-star). Evidence: s6, s7.
- **Who serves them now:** Shopify Bundles, Simple Bundles (4.9), Bundler (4.9), Fast Bundle.
- **Founder fit:** moderate build, crowded with loved apps.

### 5. Small Shopify subscription merchants
- **Signal:** Shopify Subscriptions has 163 1-star reviews (3.7). Evidence: s8, s9.
- **Who serves them now:** Shopify Subscriptions, Recharge (4.8), Seal (4.9), Appstle, Loop.
- **Founder fit:** payments edge cases and a crowded market. Hard for 10 hours a week.

### 6. Shopify sellers of digital files and license keys
- **Signal:** SendOwl's 2025 price change (3.5 stars) and regressions in Shopify Digital Products. Evidence: s10, s11, s12.
- **Who serves them now:** Shopify Digital Products (free), Sky Pilot (4.8), Filemonk (4.9), FetchApp, SendOwl.
- **Founder fit:** easy build, but the free native app plus loved Filemonk and Sky Pilot leave little room.

### 7. WordPress site owners whose free cookie banner went paid
- **Signal:** Complianz and CookieYes moving features behind paywalls. Evidence: s16, s17.
- **Who serves them now:** Complianz, CookieYes, Cookiebot, iubenda, Borlabs, Real Cookie Banner.
- **Founder fit:** easy build, but the complaint is "it should be free" (low willingness to pay), and it carries legal-compliance liability.

## Dropped, and why
- **SaaS "alternative to X" (Calendly, DocuSign, Typeform, Zapier, Hotjar, Linktree):** HN is full of open-source and indie clones already (e.g. s18). The demand is real, but it's a red ocean.
- **Translation (Weglot, Langify, Translate & Adapt):** crowded with 4.5+ apps.
- **Product reviews (Judge.me at 5.0 with 48,706 reviews, Loox at 4.9):** a loved incumbent.
- **Etsy and marketplace sync (Marketplace Connect, 308 1-star):** real pain, but a heavy multi-API build that overlaps the existing Shopify inventory example.
- **LMS, membership and donations (Tutor LMS, LearnDash, PMPro, GiveWP, Charitable at 4.9):** heavy builds or a loved free incumbent.
- **Podcasting, tutoring, sports team apps:** low pain (Seriously Simple Podcasting 4.7) or mobile/network-effect businesses that don't fit 10 hours a week.
- **Appointment booking:** already covered by an existing example (Bookly/Amelia). Event ticketing is a different job (selling seats for a dated event, check-in at the door), but it sits in the same WordPress ecosystem. That adjacency is noted.

## Pick for the competitor map
Niche 1 (WordPress event ticketing for small organizers). It is the only shortlisted niche where the incumbents themselves are rated poorly and customers name a specific trigger (the takeover-era price rises and licensing breakage) that pushes them to leave. The Shopify niches all have a loved paid app at 4.7+ already filling the gap.
