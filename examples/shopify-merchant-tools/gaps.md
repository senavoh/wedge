# Gaps: ranked

Scores use `references/scoring.md`. Every score cites evidence that `verify.py` marked `yes`.

## Candidate gap sentences

1. **Stocky replacement app:** "Small brick-and-mortar Shopify shops who lost Stocky can't get fast POs, receiving, labels and counts at a small-shop price, because every option is either the slow native tool or a forecasting suite priced for DTC brands." This was true in February 2026 [e7, e19, e22]. By October 2026 it no longer holds: Stockroom is free and unlimited [c1, c3], and EZstock and Supremo have free tiers [c4, c6].
2. **Small-merchant subscriptions:** "Small DTC brands who sell subscriptions can't get reliable renewals without percentage fees, because Recharge has no small tier and the cheap options break silently." Half true: Seal is free up to 50 subscriptions with 0% fees [o5].
3. **Wholesale for small makers:** "Small brands selling to boutiques can't get wholesale pricing and net terms that work reliably, because the apps break themes and pricing." Weakened by Shopify B2B, which now runs on Basic and up [w5].

## Scores

| # | Opportunity | Pain | WTP | Gap | Fit | Reach | Build | Total |
|---|---|---|---|---|---|---|---|---|
| 1 | Stocky replacement app for small POS retailers | 8 | 5 | 2 | 7 | 7 | 5 | **57** |
| 3 | Wholesale ordering for small makers | 6 | 6 | 3 | 6 | 5 | 4 | **51** |
| 2 | Subscriptions for small merchants | 7 | 6 | 3 | 4 | 5 | 3 | **50** |

Total = round(pain×2.5 + WTP×2 + gap×2 + fit×1.5 + reach×1.2 + build×0.8).

### 1. Stocky replacement app (57)
- **Pain 8:** shops say the shutdown leaves them unable to place orders or count stock, and some are leaving Shopify POS. Many authors across reviews and six threads [e1, e3, e5, e6, e7, e13].
- **WTP 5:** some pay for workaround apps ($35/mo for labels [e29, e30]), but the loudest voices cap spend at $100/mo or resent paying for anything that used to be free [e22, e25, k6]. A free option exists [c3]. That's "pay for a weak substitute", not "already pay competitors and complain about price".
- **Competition gap 2:** a free, 4.9-rated app covers POs, receiving, counts, labels and Stocky import [c1, c2, c3]. More than ten other apps are pitching in the same threads [c14, c15, c16].
- **Founder fit 7:** he's a merchant, and this is a CRUD-style embedded app. The build is fine; standing out is the hard part.
- **Reachability 7:** six public Shopify Community threads full of the exact buyers [e7, e15, t1], plus Stocky's own review page [e1].
- **Build cost 5:** an embedded Shopify app with POs, partial receiving, label printing and barcode counts is a few months at 10 hours a week.

### 3. Wholesale for small makers (51)
- **Pain 6:** lost orders and broken pricing, from different merchants across 3 apps [w1, w2, w4].
- **WTP 6:** merchants already pay $34.95 to $149/mo [w6, w7, w3].
- **Gap 3:** Shopify B2B is native on Basic and up [w5], and there are many apps.
- **Fit 6:** the founder could be his own first wholesale user, but pricing logic touches checkout and themes, which is where the bugs live.
- **Reach 5:** App Store review pages only. Reddit was blocked, so no verified community venues.
- **Build 4:** a few months, with checkout/theme risk.

### 2. Subscriptions (50)
- **Pain 7:** Recharge pricing and lock-in, Seal renewals breaking silently [o1, o2, o3, o4].
- **WTP 6:** they pay Recharge "$99 / month 1.49% + 19¢ per transaction" [o6] and complain about price.
- **Gap 3:** Seal is free up to 50 subscriptions, and its paid plans start at $5.95 [o5]. Shopify Subscriptions is free, though rated poorly [o7].
- **Fit 4:** billing failures cost merchants money and chargebacks. That's a bad first build for 10 hours a week.
- **Reach 5:** review pages only.
- **Build 3:** recurring billing edge cases.

## The winning gap, after re-reading the evidence

The app gap in #1 is closed. The pain that is still open in the same buyers is narrower, and it's a service, not software:

> **Small brick-and-mortar Shopify shops forced off Stocky can't get purchasing, receiving and labels running again without days of re-entering vendor and supplier data, because every replacement is self-serve software and Shopify's tools can't carry suppliers across.** [g1, g2, g3, g5, g6]

Who already pays for setup help: Inventory Planner customers pay "$5000" for training [g5]. Who won't pay monthly: the same small shops [e22, k6]. So the pivot is to sell a one-time setup, not a subscription.
