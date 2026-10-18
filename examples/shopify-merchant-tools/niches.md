# Niches: what could a small Shopify merchant build for other merchants?

Mode `expertise`, depth `quick`. Reddit is blocked on this network, so the scout used Shopify App Store 1- and 2-star review pages (fetched with `fetch.py page`, saved in `raw/scout.jsonl`), plus Shopify Community threads. Web search was used only to find app handles and threads.

## What was scanned

17 apps across 9 categories, 1-star and 2-star pages each (34 pages, roughly 260 individual low-star reviews). Rating counts below are copied from the fetched review pages.

| Category | App | Reviews | Rating | 1★ / 2★ / 3★ | Read |
|---|---|---|---|---|---|
| Inventory / POs | Stocky (Shopify) | 211 | 3.0 | 59 / 26 / 16 | Worst-rated app in the scan. Being shut down. |
| Inventory / POs | Inventory Planner by Sage | 155 | 4.3 | 13 / 4 / 3 | Price hikes, "too small" brush-offs |
| Inventory / POs | Prediko | 263 | 4.9 | 3 / 1 / 1 | Few complaints |
| Inventory sync | syncX Stock Sync | 929 | 4.7 | 45 / 10 / 13 | Feed reliability, support |
| Subscriptions | Recharge | 3,138 | 4.8 | 149 / 24 / 31 | Price, lock-in, no small tier |
| Subscriptions | Seal | 3,147 | 4.9 | 17 / 11 / 27 | Cheap, some broken renewals |
| Subscriptions | Shopify Subscriptions (listing) | 865 | 3.7 | 163 / 71 / 114 | Free first-party app, weak ratings |
| Wholesale / B2B | Wholesale Pricing Discount | 747 | 4.9 | 20 / 6 / 3 | Pricing not applied, theme breakage |
| Wholesale / B2B | Wholesale Gorilla | 317 | 4.8 | 11 / 5 / 8 | Upgrade gating, billing after uninstall |
| Wholesale / B2B | SparkLayer | 391 | 4.9 | 5 / 5 / 2 | Errors, setup complexity |
| Returns | Loop Returns | 447 | 4.6 | 30 / 6 / 3 | Onboarding, logins; aimed at bigger brands |
| Returns | ReturnGO | 407 | 4.9 | 7 / 0 / 0 | Few complaints |
| Bundles | Bundles.app | 324 | 4.9 | 4 / 1 / 1 | Few complaints |
| Bundles | Bundler | 2,737 | 4.9 | 19 / 9 / 34 | Free-plan bait, surprise charges |
| Product options | Easify | 3,160 | 4.9 | 39 / 8 / 11 | Add-on prices not charged (lost money) |
| Back in stock | Amp Back in Stock | 966 | 4.9 | 22 / 7 / 3 | Silent failures, cheap substitutes exist |
| Order editing | Cleverific | 233 | 4.6 | 15 / 8 / 2 | Most complaints are from 2014 to 2020 |

Not fetched: Notify-me (page loaded but the review structure did not parse into reviews), Preorder Now (reviews URL returned 404). Web search showed STOQ and Timesact preorder apps at roughly 97 to 98% five-star, so preorders were not pursued.

## Shortlist (3)

### 1. Inventory purchasing and receiving for small brick-and-mortar shops (the Stocky gap)
- **Buyer and job:** a small Shopify POS retailer (gift shop, shoe store, yarn shop) that orders from 20 to 50 vendors, receives boxes, prints shelf labels and counts stock once a year.
- **Signal:** the strongest in the scan. Stocky is the only app with a 3.0 rating and 28% one-star reviews, and Shopify is shutting it down (delisted Feb 2, 2026; gone Aug 31, 2026) [e3, t1]. Merchants say the native PO tool is far slower [e7, e8] and that they won't pay much to replace something that used to be free [e22, e25]. Inventory Planner tells small shops they are too small [e19]. Six Shopify Community threads fetched, with posts from many different merchants (and many vendors).
- **Who serves them now:** Shopify native POs, Stockroom (free), EZstock, Supremo, Stockie, Assisty, Prediko, Inventory Planner, plus about a dozen apps pitched in the forum threads (FyreTrail, Binly, Replenly, Stock&Buy, Logistified, SKUSavvy...).
- **Founder fit:** high. The founder runs a store, buys inventory and knows this workflow.

### 2. Subscriptions for small merchants
- **Buyer and job:** a small DTC brand (coffee, pet food, supplements) selling subscribe-and-save to under a few hundred subscribers.
- **Signal:** Recharge has 149 one-star reviews. Merchants say there is no small tier [o1], fees pass 10% of recurring revenue [o2], and they feel locked in [o3]. Seal users report renewals breaking silently [o4].
- **Who serves them now:** Recharge, Seal (free up to 50 subscriptions [o5]), Shopify Subscriptions (free, 19% one-star [o7]), Appstle, Loop, Bold.
- **Founder fit:** weak. Recurring billing, failed payments and chargebacks are high-stakes for a 10-hour-a-week builder.

### 3. Wholesale ordering for small makers
- **Buyer and job:** a small brand (home goods fits) selling to boutiques at wholesale prices with net terms.
- **Signal:** wholesale customers can't order when special pricing isn't applied [w1], net-terms customers are forced to pay at checkout [w4], one brand lost orders for two years [w2], and discounts are gated behind upgrades [w3].
- **Who serves them now:** Shopify B2B, now on Basic and up [w5], Wholesale Pricing Discount, Wholesale Gorilla ($34.95+ [w6]), SparkLayer ($49+ [w7]), Faire as a channel.
- **Founder fit:** medium. The founder could be his own first user, but pricing logic touches checkout and themes.

## Dropped, and why

- **Bundles:** loud complaints are about free-plan bait and surprise charges [d1], not missing capability. Hundreds of 4.9-star apps.
- **Back in stock:** buyers already find substitutes "for $45 a year" [d2]. Race to the bottom.
- **Product options:** real money lost to bugs, but the category is crowded, and one merchant says AI can code a replacement "in a few hours" [d3]. That cuts both ways: easy to build, hard to charge for.
- **Returns:** pain clusters around Loop's onboarding [d4], which is an enterprise sales problem, not a small-merchant product gap.
- **Order editing and preorders:** complaints are old or rare.
