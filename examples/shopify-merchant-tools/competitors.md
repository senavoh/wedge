# Competitors: inventory purchasing and receiving for small Shopify retailers

Deep dive on niche 1 (the Stocky gap). Listings and pricing were fetched with `fetch.py page` from each app's Shopify App Store page on 2026-10-17 (`raw/competitors.jsonl`). Pricing quotes are marked `official` in `evidence.jsonl`. They prove what each vendor says about itself, nothing more.

## The table

| Name | URL | Starting price | Model | Free option | Headline (quoted) | Evidence |
|---|---|---|---|---|---|---|
| Stocky (Shopify) | apps.shopify.com/stocky | "Included with Shopify POS Pro subscription" | Bundled | Only with POS Pro | Shut down Aug 31, 2026 | c12, e3 |
| Shopify native POs | Shopify admin | Included in admin | Bundled | Yes | Merchants: "brutally inadequate" | e7, e10 |
| Stockroom (MyWorks) | apps.shopify.com/stock-room | Free | Free (monetizes QuickBooks/Xero sync) | Yes, unlimited | "Unlimited purchase orders, inventory management & manufacturing." | c1, c2, c3 |
| EZstock | apps.shopify.com/ezstock | Free (5 POs/mo), Starter $19/mo | Flat tiers capped by POs/month | Yes | "Leaving Stocky? Upload your export..." | c6, c7, c17 |
| Supremo | apps.shopify.com/supremo | Free (100 products), Shelf $19/mo | Flat tiers capped by catalog size | Yes | "Restock On Time with Inventory Forecasting" | c4, c5 |
| Assisty | apps.shopify.com/assisty | Basic free (no POs); POs in Replenishment $39/mo | Tiered by Shopify plan | Partial | "Stocky alternative" | c10 |
| Stockie | apps.shopify.com/stockie | $4.99/mo (alerts); POs in Pro Plus $59.99/mo | Flat tiers | No | "Know what to reorder and when." | c11 |
| Prediko | apps.shopify.com/prediko | Starter $49/mo (stores up to $100k revenue) | Tiered by store revenue | Trial only | "AI Inventory Management & Planner." | c9, k5 |
| Inventory Planner (Sage) | apps.shopify.com/inventory-planner | Not public: "Contact us to get a quote." | Quote, annual contracts reported | No | "More time, more profit, less guesswork." | c8, e20 |
| Cogsy | apps.shopify.com/cogsy | $199/mo | Flat | Trial only | "The smarter way to manage inventory." | c13 |

Also pitched in the Shopify Community threads but not fetched individually: FyreTrail, Binly ($19 per its developer), Replenly ($20 per its developer), Logistified ($12 per its developer), Stock&Buy, Sumtracker, SKUSavvy (~$179 per its developer), Stock Control, Stock Take, Stock Transfer Pro, LabelCraft, SupplyWatch [c14, c15, c16]. These prices are what each developer posted about their own app. They're positioning, not verified facts.

## Competitor sketches

### Stocky (the incumbent being removed)
- **Really for:** POS Pro retailers who needed POs, receiving, counts and labels in one free tool.
- **Strong at:** being free with POS Pro and doing "90% of the lift" for some shops (forum, Gabe_Stillwater, raw/forum.jsonl).
- **Weak at:** neglected for years [e1, e4], features removed [e2], label printing broken [e29, e30], gated behind POS Pro [e26]. Now gone [e3].

### Shopify native purchase orders (the free substitute)
- **Really for:** shops whose purchasing is simple.
- **Strong at:** free and built in.
- **Weak at:** slow for many-SKU orders [e7, e8, e9]; no "fill shelves" reordering [e10]; suppliers can't be exported from Stocky into it, so vendors must be re-created as suppliers [e15, e17].

### Stockroom by MyWorks (the free replacement)
- **Really for:** any Stocky refugee who wants POs, receiving, counts and labels without a new bill.
- **Strong at:** free, unlimited POs, Stocky migration, labels [c1, c2, c3]. Rated 4.9 with 56 reviews and zero 1- to 3-star reviews on the pages fetched (raw/reviews.jsonl).
- **Weak at:** no complaints to mine yet. Its business model is selling accounting sync, so the free tier is a loss leader. That's a risk to it, but not an opening you can count on.

### EZstock, Supremo, Stockie, Assisty (cheap post-Stocky apps)
- **Really for:** small shops that want a Stocky clone with a low monthly fee.
- **Strong at:** public prices, Stocky import (EZstock, Assisty), free tiers (EZstock, Supremo) [c4 to c11, c17].
- **Weak at:** too new to judge. Supremo has 7 reviews and EZstock has 1, with no low-star reviews on the fetched pages.

### Prediko, Inventory Planner, Cogsy (forecasting suites)
- **Really for:** DTC brands with revenue to protect, not shop counters.
- **Strong at:** forecasting and multi-location planning.
- **Weak at:** price and contracts [e19, e20, e21], sync failures [e39, e41], forecasts that miss seasonality [e40], data bugs [e42].

## Feature matrix

Features come from what merchants complain about, not from vendor lists. Values come from each listing's text. `unknown` means the listing didn't say.

| | Free plan | Public price | Stocky import | Reorder suggestions | Partial receiving | Barcode stocktake | Labels on receive | POs under $25/mo | Hands-on setup |
|---|---|---|---|---|---|---|---|---|---|
| Shopify native POs | yes | yes | no | no | unknown | partial | unknown | yes | no |
| Stockroom | yes | yes | yes | yes | yes | yes | yes | yes | unknown |
| EZstock | yes | yes | yes | yes | yes | yes | unknown | partial | unknown |
| Supremo | yes | yes | unknown | yes | yes | yes | unknown | yes | unknown |
| Assisty | partial | yes | yes | yes | unknown | yes | unknown | no | unknown |
| Stockie | no | yes | unknown | yes | unknown | yes | unknown | no | unknown |
| Prediko | no | yes | yes | yes | unknown | yes | yes | no | partial |
| Inventory Planner | no | no | unknown | yes | unknown | unknown | unknown | no | partial |

## Where it's crowded and where it's empty

- **Crowded:** "POs plus receiving plus Stocky import, cheap." At least one free, well-rated option (Stockroom) and several at $12 to $20 [c3, c14, c15, c16]. A developer in the thread says it outright: the shutdown "pushed a bunch of small focused apps into this space" [c14].
- **Crowded:** migration tooling. Vendors give away Stocky converters and export scripts [k3, k4, k5].
- **Thin:** someone who actually does the setup for a small shop: maps vendors to suppliers, imports the history, gets the label printer working and trains staff. Self-serve apps leave that to the merchant [e15, e16, e34]. Paid onboarding exists only at the top end [e36]. A web search also turned up Fiverr gigs offering Stocky migration, but those pages returned HTTP 403 to `fetch.py`, so they are unverified here.
- **Empty and closing:** the API and export window. Stocky's API stopped on Aug 31 and read-only access ends Nov 29, 2026 [k1, k2].
