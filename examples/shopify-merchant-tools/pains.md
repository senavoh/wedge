# Pains: inventory purchasing and receiving for small Shopify retailers

**Sources:** 1-, 2- and 3-star review pages for Stocky, Inventory Planner, Prediko, Stockroom, EZstock and Supremo (`raw/reviews.jsonl`, `raw/scout.jsonl`), plus six Shopify Community threads about Stocky's shutdown (`raw/forum.jsonl`). Stockroom, EZstock and Supremo had no 1- to 3-star reviews at all. `signals.md` has the automated digest. It's noisy here, because each review page is a single record and developer replies are mixed in, so the themes below were built by reading the reviews.

**How counts work:** per-competitor numbers are keyword-tagged low-star reviews, from 40 Stocky reviews, 20 Inventory Planner reviews and 4 Prediko reviews. They're rough, and one review can carry several themes. "Forum posts" are hand counts of merchant posts in the threads. Vendor posts are excluded.

## Ranked themes (severity × frequency)

### 1. "Shopify took away the tool we run the shop on." (high)
Stocky was neglected, stripped of features, then shut down. Some merchants are leaving Shopify POS over it.
- Counts: Stocky 11. Forum posts: 5 or more.
- Quotes: "it's been completely abandoned" [e1]; "only for them to deprecate features you rely on" [e2]; shut down Aug 31, 2026 [e3]; "Removing Stocky means we can't place orders, do year end stock takes..." [e5]; "We are trialing Lightspeed." [e6]; [e4]

### 2. "The native PO tool takes triple the time." (high)
The free substitute is slow for real orders with many SKUs, and it has no "fill shelves" reordering.
- Counts: Stocky 30 (keyword-broad). Shopify native POs: 6 forum posts.
- Quotes: [e7, e8, e9, e10, e11, e12]

### 3. "I have to re-enter years of vendor data." (high)
Suppliers can't be exported, and native POs force vendors to be re-created as suppliers.
- Counts: Shopify native POs: 4 forum posts.
- Quotes: [e13, e14, e15, e16, e17]

### 4. "I won't pay $100+ a month for what used to be free." (high)
Small shops resent new fees. The big tools price for bigger stores and raise prices.
- Counts: Stocky 11, Inventory Planner 12, Prediko 1. Forum posts: 6.
- Quotes: [e19, e20, e21, e22, e23, e24, e25, e26, e27]

### 5. "Nobody can help me set it up." (medium)
Support can't fix it, setup eats whole days, and real onboarding costs thousands.
- Counts: Stocky 14, Inventory Planner 13, Prediko 2.
- Quotes: [e33, e34, e35, e36, e37, e38]

### 6. "Labels and stock counts don't work." (medium)
Receiving labels and barcode counts break, so shops pay for extra apps.
- Counts: Stocky 13, Inventory Planner 2.
- Quotes: [e28, e29, e30, e31, e32]

### 7. "The numbers are wrong." (medium)
Sync breaks, forecasts miss seasonality, data has bugs.
- Counts: Stocky 4, Inventory Planner 12, Prediko 1.
- Quotes: [e39, e40, e41, e42]

## Silence (hypotheses, not facts)
- Nobody complains about Stockroom, EZstock or Supremo yet. They're new (the Stockroom reviews on its listing are from recent months, with reviewers saying "About 1 month" or "About 2 months" using the app), so silence here means nobody has had time to complain, not proof they're good.
- No app in the matrix advertises hands-on setup at a small-shop price. The only paid onboarding in the evidence is Inventory Planner's "$5000" training [e36].

## The three themes most likely to make someone switch
1. **Re-entering vendor and supplier data** (theme 3). It's what keeps shops stuck on bad native POs [e15, e16].
2. **Price resistance** (theme 4). Anything near $100/mo is out [e22, k6].
3. **Setup help** (theme 5). Shops lose days and then give up [e34, e35].

Themes 1 and 2 are real, but they describe Shopify's decision, and a dozen apps are already chasing that same pain.
