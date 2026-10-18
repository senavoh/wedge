# Win plan (for the pivot)

**What's being won:** small brick-and-mortar Shopify POS shops that are still stuck after Stocky. The offer is a one-time, fixed-price setup that gets purchase orders, receiving, labels and the year-end count working again on a free or cheap app. Working name: **Shelf Sorted**. This is a plan for a 7-day test, not for a company.

## 1. Switching triggers

| Trigger | Evidence | Move |
|---|---|---|
| Stocky shutdown, and read-only access ends Nov 29, 2026 | t1, t2, k1, k2 | Post a plain export checklist in the threads now, with a free 15-minute "what do I still need to grab?" call. The setup offer comes after. |
| First big receiving day on native POs ("triple the time") | e7, e8, e10 | Offer to build the vendor→supplier map and a reorder template, so the next PO takes minutes. |
| Year-end stock count (December/January) | e5, e28, e31 | "Year-end count ready" package in early December: barcode count set up and tested on a small section first. |
| Inventory Planner renewal or price hike | t3, t4, e19 | Only for small shops that IP itself turned away: set them up on a free or cheap tool instead. |

## 2. Positioning

**Main:** "Your back room, working again after Stocky. One flat fee, done with you in a week, by a shop owner who had to do it too."

Alternates:
- "Stop re-entering years of vendor data. We map it, import it and train your staff." (customers' words: e14, e13)
- "No new monthly bill. We set up the free tools properly." (answers e22, e25)

## 3. Offers that win switchers

- **Fixed price on the page, paid once** (pain: price, theme 4; e22, k6).
- **Vendor-to-supplier mapping done for you** (pain: data re-entry, theme 3; e15, e17).
- **Labels printing from your PO before we leave** (pain: labels, theme 6; e29, e30, e32).
- **Staff walkthrough, recorded so new hires can rewatch it** (pain: setup and support, theme 5; e33, e34).
- **Free 15-minute export check before Nov 29** (trigger: deadline; k1).
- **Money back if the first PO doesn't go through** (pain: setup time, theme 5; e34).

## 4. Build first (tiny, internal tools only)

1. **Vendor→supplier mapping sheet + CSV converter** (theme 3). It takes the Shopify product export plus any saved Stocky export and produces a supplier list. A few evenings with AI help.
2. **Setup checklist per tool** (Stockroom, EZstock, native POs) (theme 5).
3. **Label printer test kit** (theme 6): one page per common printer, confirmed to work.
4. **Booking page + Stripe payment link** (theme 4: price shown upfront).

No Shopify app gets built until 5 shops have paid.

## 5. Where unhappy customers are

| Place | URL | Why |
|---|---|---|
| "Stocky replacement?" thread | https://community.shopify.com/t/stocky-replacement/621332 | Active through Aug 2026. Merchants describe the exact PO and receiving pain [e7, e8]. |
| "Removing Stocky is a Material Retail Operations Risk" | https://community.shopify.com/t/removing-stocky-is-a-material-retail-operations-risk/589102 | Retail owners about to leave over data re-entry [e5, e13, e14]. |
| "Replacement to Stocky?" (Retail & POS) | https://community.shopify.com/t/replacement-to-stocky/587141 | Small shops asking for "count and adjust" without big-app costs [e23, e31]. |
| "Stocky Alternatives" | https://community.shopify.com/t/stocky-alternatives/632200 | A small shoe store asking "What do you recommend?" [e15, e16]. |
| "Stocky alternative recommendation" | https://community.shopify.com/t/stocky-alternative-recommendation/553677 | Shown in Related topics with activity on Oct 17, 2026 (raw/forum.jsonl). |
| "Stocky App Going Away after August 31 2026" | https://community.shopify.com/t/stocky-app-going-away-after-august-31-2026/587292 | 160+ posts (raw/forum.jsonl, page 7). |
| Stocky's own 1-star reviews | https://apps.shopify.com/stocky/reviews?ratings%5B%5D=1 | Named shops with the exact complaints (labels, counts, setup) [e28, e33, e35]. |

Reddit (r/shopify, r/smallbusiness) is likely relevant, but it was blocked on this network, so it's unverified here.

## 6. Trust signals

Competitors and freelancers mostly don't show these. All of them can be shown from day one:
- A fixed, public price.
- A real shop: "I run a Shopify home-goods store and buy inventory too." It's true, and you can link it.
- A written scope: what's done, what isn't, and how long it takes.
- A data promise: we work from your exports, test on one location, and change nothing in bulk without your sign-off.
- A money-back condition (the first PO works).

## 7. What to stop doing

Things competitors do that customers hate:
- Hiding the price behind a demo call (Inventory Planner [c8]; a developer in the thread notes this pattern [c14]).
- Locking people into annual contracts and raising the price at renewal [e20, e21].
- Pitching in threads without answering the question. The threads are already full of it (raw/forum.jsonl).
- Upselling the shop to a paid app it doesn't need. If native POs plus Stockroom is enough, say so.

## First 10 customers

1. **"Stocky Alternatives" thread:** reply to MurphysBootShop's "What do you recommend?" [e16] with a concrete answer for a small shoe store: tag-filtered POs, and which free tool does it. Disclose at the end that you offer setup help. No link unless asked.
2. **"Removing Stocky..." thread:** reply to the posts about re-entering vendor data [e13, e14] with the vendor→supplier CSV method, step by step.
3. **"Replacement to Stocky?" thread:** answer the "count and adjust" request [e23, e31] with the cheapest working stocktake path.
4. **"Stocky replacement?" thread:** answer the many-SKU PO complaint [e8] with a reorder-template tip.
5. **Post one new thread:** "Stocky read-only ends Nov 29: a 10-point export checklist from a shop owner." Pure help, no pitch [k1].
6. **Stocky 1-star reviewers** whose shops are named (e.g. labels [e29, e30], setup [e35]): find their public store contact page and send message A from `assets/outreach.md`. At most 10, and only where the store lists a contact form.
7. **Offer 3 "founding" setups at $99** (half price) in exchange for a written testimonial and permission to share the before/after.
8. **Your own network:** ask the suppliers you buy home goods from which other retail stockists use Shopify POS. Send message B.
9. **After each setup:** ask for one referral to a fellow shop owner.
10. **Log every objection** in a sheet. If "too expensive" comes up 3 or more times, test $149.

Assets: `assets/vs-stockroom.md`, `assets/vs-native-pos.md`, `assets/outreach.md`, `assets/ads.md`, `assets/faq.md`.
