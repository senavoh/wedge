# Pains: WordPress event ticketing for small organizers

## Corpus
- `raw/reviews.jsonl`: 625 WordPress.org review threads, every 1-, 2- and 3-star review linked from the review list pages (pages 1 to 6) of 8 plugins: The Events Calendar, Event Tickets, Events Manager, Tickera, Event Espresso, Eventin, Modern Events Calendar, Ticket Tailor. Collected with `fetch.py links` and then a single `fetch.py pages --from` (625 pages in about 5 min 20 s).
- `raw/scout-events.jsonl`: 60 more 1-star threads (Event Tickets and The Events Calendar).
- `raw/support.jsonl`: 24 unresolved support threads (Event Tickets and The Events Calendar).
- `raw/reviews-hn.jsonl`: 133 Hacker News items (eventbrite fees, eventbrite alternative, ticket tailor, event ticketing small venue, selling tickets wordpress).
- **842 records in total for this niche.** Digest: `signals.md` / `signals.json`. Themes below were counted with keyword rules over the first post of each of the 709 WordPress threads. Counts are approximate: a thread can hit several themes, and the rules miss phrasings they don't anticipate.

**Caveat on recency:** only 101 of the 709 WordPress threads are under 2 years old, and 56 of those are about The Events Calendar or Event Tickets. Much of the corpus is old, but the recent complaints focus on one vendor's post-acquisition behaviour (Liquid Web / Nexcess).

**Caveat on scope:** The Events Calendar has 344 of the 709 threads, and many are about the calendar, not ticketing. Ticket-specific failures (buyers who can't buy, or never get their tickets) are rare in the corpus (about 6 keyword hits) but severe.

## Themes (ranked by severity × frequency)

| # | Theme | Severity | Approx. threads | Per competitor (keyword hits) | Evidence |
|---|---|---|---|---|---|
| 1 | **Updates break the site, events or checkout** | high | 45 | Events Calendar 25, Events Manager 7, Event Tickets 6, Eventin 4, MEC 1, Event Espresso 1 | r1, r2, r3, r4, r5 |
| 2 | **Paid support doesn't answer** | high | 92 | Events Calendar 37, Events Manager 24, Event Tickets 16, Tickera 8, MEC 4, Eventin 3 | r6, r7, r8, r9, s14 |
| 3 | **Renewal price rises and licensing mess** | high | 57 | Events Calendar 21, Events Manager 11, Event Tickets 6, Eventin 6, MEC 4, Tickera 4, Event Espresso 2 | s13, s14, r9, r10, r12 |
| 4 | **Buyers can't buy, or don't get their tickets** | high (rare but event-ruining) | about 6 by keyword, plus scout threads | Event Tickets 3, Events Calendar 2, Eventin 1 | s15, r2, r13, r14, r15 |
| 5 | **Payment setup breaks, or surprise platform fees** | medium | 19 | Event Tickets 7, Events Manager 4, Events Calendar 3, Eventin 3 | r16, r17, r18, c1 |
| 6 | **Bloated, with upsell ads, for people who run 10 events a year** | medium | 63 (complexity) + 30 (upsell) | Events Calendar 36 + 17, Events Manager 8 + 4, Tickera 6 + 4 | r19, r20, r21, r11 |
| 7 | **Hosted options mean per-ticket fees and an off-brand embed** | medium | small (HN + Ticket Tailor's 8 reviews) | Eventbrite, Ticket Tailor | r22, r25, r23, r24 |
| 8 | **Performance and theme/CSS conflicts** | low to medium | 64 | Events Calendar 23, Events Manager 18, Event Tickets 7, Eventin 7 | (no quotes pulled; counted only) |

### Notes per theme
1. **Updates break things.** Every one of these plugins runs checkout inside the customer's own WordPress, so any plugin, theme or core update can take down ticket sales. "Updates frequently break existing installations." (r1). "The upgrade broke and we couldn’t sell a single ticket" (r2).
2. **Support.** People pay for the licence partly to get support, and then can't get it (r6, r8).
3. **Price and licensing.** The Events Calendar's Pro tier is now $399/yr (c2). A sole trader running "about 10 events per year" (r11) left over a 50% renewal increase (r10).
4. **Delivery.** "OVER 1000 tickets sold and 90% of our customers are emailing saying they DIDNT recieve their QR code" (s15). Rare in the corpus, but it's the failure that ends a relationship.
5. **Payments.** Stripe webhook validation trouble (r16). The free tier's 2% fee surprised people (r17, documented in c1).
6. **Bloat.** Small organizers say the product is "much more than I need" (r21) and object to ads injected into wp-admin (r20).
7. **Hosted trade-off.** Hosted tools fix reliability, but charge per ticket and look foreign on the site (r23). One buyer still wants hosted next time (r24): demand for reliability beats demand for "own it".

## Silence (hypotheses, not facts)
- Nobody in the corpus asks for **monitoring** ("tell me if checkout is broken before my customers do"). Possibly no product offers it, so nobody thinks to ask.
- Nobody praises a **flat, low, no-renewal-shock price for under 1,000 tickets a year**. Tickera's lifetime $399 is the closest.

## The three themes most likely to make someone switch
1. Updates breaking sales (1), combined with buyers not receiving tickets (4).
2. Renewal price rises and licensing chaos at The Events Calendar / Event Tickets (3).
3. Unanswered paid support (2).
