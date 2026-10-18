# Gaps, ranked (scoring.md weights)

| # | Opportunity | pain | wtp | gap | fit | reach | build | total |
|---|---|---|---|---|---|---|---|---|
| 1 | Receive-to-label workflow for Stocky refugees on native POs | 8 | 5 | 2 | 7 | 7 | 6 | 58 |
| 2 | Better barcode label app (Retail Barcode Labels refugees) | 6 | 4 | 2 | 8 | 7 | 8 | 54 |
| 3 | Subscriptions for Bold / Shopify Subscriptions refugees | 6 | 5 | 2 | 4 | 6 | 3 | 45 |

Winner gap: POS Pro retailers who lost Stocky can't get labels printed for exactly what they just received on a Shopify purchase order, because native POs have no label path and Shopify's Retail Barcode Labels makes them re-add every product by hand (e8-e12).

Reasoning for #1:
- pain 8: threats to leave POS or Shopify (e2, e5), many authors across App Store and Community (e1-e9).
- wtp 5: Stocky came bundled with POS Pro (e31). Merchants will pay, but with low ceilings: "$40 per month is insulting" (e20), nothing over $100 (e21), conditional (e22, e23).
- gap 2 (lowered from 3 after the critic: free label printing exists inside free PO apps, e41, e47; FyreTrail prints only what was delivered, e42): already covered well and cheaply. EasyScan has POs plus unlimited labels at $9.99, rated 5.0 (e32). LabelCraft labels incoming transfers (e33), PML does POs and transfers (e34), Alfred has labels (e36), another dev shipped PO labels (e37), Binly is $19 (e35), and native POs plus Quick count are free (e29, e30).
- fit 7: Remix + Polaris + Admin GraphQL is the job. $2k and 20 h/week are enough for a narrow app.
- reach 7: 10+ active Community threads (e1-e11), Stocky and RBL review pages, App Store search for "Stocky alternative". Devs post app showcases there (e40).
- build 6: weeks for the narrow wedge. It depends on reading received quantities from native POs; the API is new.
#2 is capped by loved free or cheap incumbents (ReFo 5.0/572, Yanet 4.9/456; Shopify itself points to them, e39) and a low price ceiling (e24).
#3 has strong incumbents (Appstle 5.0/9,042, Seal 4.9, Loop 5.0) and a heavy payments support load.

Pre-critic verdict: PIVOT (total 60). Post-critic: gap lowered to 2, total 58. Still PIVOT: under 65, with 3 unresolved high-severity critic risks.
