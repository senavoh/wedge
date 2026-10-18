# Critic pass

Role reset: a skeptical investor who has seen 1,000 "Shopify app" pitches, arguing against `gaps.md`. Searches run for this pass: "Shopify Stocky discontinued retirement 2026 replacement" (someone tried and died / free incumbent), "apps.shopify.com Stockroom purchase orders free app" (free incumbent), and "Stocky migration service done for you" (is the pivot already sold?). Pages were then fetched with `fetch.py` into `raw/`.

| Risk | Severity | Rebuttal / status |
|---|---|---|
| **A free incumbent already owns the app idea.** Stockroom is free and unlimited, rated 4.9 with no low-star reviews, and its developer posts in every thread [c1, c3]. EZstock and Supremo are free to start [c4, c6]. | High (for the app) | **Unresolved for the app.** This is why the app idea doesn't get a GO. The pivot uses these free apps instead of fighting them. |
| **Someone tried and died, and it was Shopify.** Stocky itself was a tool Shopify ran, starved and then killed [e1, e2, e3]. Shopify can change native POs at any time, and every app here sits downstream of that. | Medium | Partly rebutted. Native POs are still "brutally inadequate" for these buyers [e7, e8], and a setup service works whichever tool Shopify pushes. |
| **The window is closing.** The API stopped on Aug 31. Read-only access ends Nov 29, 2026 [k1, k2]. After that, "rescue my data" demand drops to zero. | High | **Unresolved.** Some of the pain outlives the deadline (slow native POs, re-entering vendors, broken labels [e7, e15, e30]), but nobody knows how many shops are still unsorted in October. The 7-day test has to answer this. |
| **The pain is real but nobody pays.** Shops cap spend at $100/mo and resent paying for anything that used to be free [e22, k6, k7]. | High | **Unresolved.** A one-time fee dodges the "another monthly bill" objection, but no evidence shows a small shop paying a stranger for setup. The only paid onboarding in the evidence is Inventory Planner's $5000 training, for bigger customers [e36]. |
| **Free migration help already exists.** Vendors give away Stocky converters and export scripts [k3, k4, k5]. One developer offers to personally walk merchants through his app's import (forum, raw/forum.jsonl). Fiverr gigs selling Stocky migration showed up in search, but returned HTTP 403 to fetch, so they're unverified here. | Medium | Partly rebutted. Free tools move files. They don't map vendors to suppliers, set up label printers or train staff, which is what merchants are still asking about months later [e15, e16, e34]. |
| **Copyable in a week.** Any app vendor or freelancer can offer "we set it up for you". | Medium | True. The defense is being a real merchant who answers in the threads, plus speed. It's a side-income service, not a moat business. |
| **Channel closed.** The Community threads are already full of vendors pitching. Another pitch reads as spam. | Medium | Partly rebutted. Merchants there ask direct questions ("What do you recommend?" [e16]). Answer helpfully first and disclose. See `win-plan.md`. |
| **Trust and liability.** Touching a shop's inventory can wreck its counts. | Medium | Rebuttal: work from exports, test in one location first, and get the owner's sign-off before any bulk write. |

## Verdict reasoning

- **App idea (#1):** total 57 < 65, WTP 5 < 6, and two high risks are unresolved, so it can't be GO. Pain is 8, which is ≥ 6, so the call is **PIVOT**, not KILL.
- **Pivot:** change the channel and the price, not the buyer. Sell a one-time, fixed-price "get your back room working again" setup to small Shopify POS shops, built on the free apps rather than against them. Run the 7-day test before building anything.
- **If the pivot test fails:** the next opportunity is wholesale ordering for small makers (51). It needs its own deep run first, because Shopify B2B on Basic [w5] may already cover it.
