# Gaps ranked (scoring.md weights)
| # | Opportunity | pain | wtp | gap | fit | reach | build | total |
|---|---|---|---|---|---|---|---|---|
| 1 | Throttled catalog sync for large-catalog stores (Meta + Google) | 8 | 6 | 4 | 7 | 5 | 5 | 61 (60.5) |
| 2 | Product add-ons / options plugin | 5 | 7 | 3 | 9 | 5 | 6 | 57 (56.8) |
| 3 | Booster lifetime-holder replacement | 4 | 6 | 4 | 8 | 4 | 3 | 49 (49.2) |

**Winning gap:** WooCommerce stores with thousands of products that sell through Facebook/Instagram and Google Shopping can't keep their catalog in sync without stalling or overloading their server, because the official plugins run heavy, unthrottled sync jobs, and the paid feed plugins that claim to handle large catalogs still draw "feed gets stuck" complaints.

## #1 reasoning
- pain 8: different authors, 3 vendors, recent (e1 ~Aug 2026, e2 ~Jun 2026), plus silent sync failures (e10-e14); Meta 315/481 1-star ratings.
- wtp 6: stores pay for feed plugins (AdTribes $249.50/yr Business, e40; "bought the Pro version" in e20 thread), and complain about license changes/refunds (e19, e20, e23), not about paying. But the official sync is free (e42), which caps it.
- gap 4 (lowered from 5 after critic: CTX markets large catalogs e46, WebToffee ships batch + scheduled Meta sync e48 e49): covered, but badly: well-rated paid alternatives exist (Product Feed PRO 4.7/1,070, CTX 4.6/837) and switchers name them (e24-e27), yet stuck/slow feeds on big catalogs appear in their reviews too (e4, e5, e6, e9). Not empty.
- fit 7: PHP/Woo/Action Scheduler work; Meta/Google API churn and Meta app review are a stretch.
- reach 5: only verified gathering place is WP.org support/reviews of 4 plugins, where self-promo is banned; woocommerce.com marketplace is a gated channel. Reddit not checkable.
- build 5: an MVP feed generator is weeks; reliable Meta Catalog Batch API + Google Content API sync at 50k SKUs is months.
## #2: pain 5 (complaints mostly 2016-2022: e29, e30, e31; e28 2022), wtp 7 (paid $79/yr official; price-rise complaint e28), gap 3 (ThemeHigh 4.9 with 5 one-star of 219, APF 4.8, cheap), fit 9, reach 5, build 6.
## #3: pain 4 (e32-e34, older, one vendor), wtp 6, gap 4 (no evidence on per-module alternatives), fit 8, reach 4 (buyers hidden), build 3 (100+ modules).
