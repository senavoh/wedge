# Gap ranking (idea mode: one opportunity, scored per scoring.md)
| Opportunity | pain | wtp | gap | fit | reach | build | total |
|---|---|---|---|---|---|---|---|
| Sync-health monitor alongside existing sync plugins, $79-149/yr | 7 | 4 | 4 | 6 | 6 | 5 | 54 (17.5+8+8+9+7.2+4) after critic; 58 before |

**Gap sentence:** WooCommerce stores with thousands of products that already use a sync or feed plugin can't tell when sync quietly stops, because the plugin dashboards and job logs report "no errors" while products stay unsynced or feeds go stale (e1 e2 e7 e8 e9 e10), and the free platform alerts only fire on big Google-side drops (e28), with nothing comparable found for Meta (e30 e31).

- pain 7: two high themes, different authors, 4 plugins, 3 sites (WP.org, wpde.org, GMC community), mostly 2026. Not 8+: posters did notice and asked for help; few say they left.
- wtp 4: stores pay for Pro feed plugins (e22-e26), a substitute. No evidence anyone pays for monitoring alone: the Shopify monitor apps show 0 reviews (e43), and the cheapest charges $4.99/mo (e42), far below $79-149/yr.
- competition_gap 5: Google side covered for free on large drops (e27 e28) and shown in Google for Woo's overview (e33). RexTheme shipped and then paused failed-run email alerts for its own feeds (e38 e39). Six 2026 WP.org entrants do local data audits with email alerts (e34 e37), all under 10 installs. A cross-plugin job and Meta-status monitor wasn't found.
- founder_fit 7: reading Action Scheduler and plugin meta is core Woo/PHP. Reading Merchant API or Meta catalog status needs OAuth and app review, a stretch at 15h/week.
- reachability 6: WP.org directory search plus forums (no advertising, e48), official WooCommerce Facebook group (e46), Woo Slack (e47), wpde.org (e9), Merchant Center community (e20). Places exist, but only WP.org shows volume, and the main one bans promotion.
- build_cost 6: local job monitor MVP takes weeks. Platform status reads (Google OAuth, Meta app review) take months to make reliable across 5 plugins' internals.

## After critic
- gap 4: CatalogCanary (e50 e62), vendor failure emails (e53 e38), Google push API (e55).
- fit 6: Meta App Review (e57).
- build 5: Google notifications need a hosted HTTPS endpoint, and Meta needs review.
- PIVOT (pain 7 >= 6; GO fails: total 54 < 65, wtp 4 < 6, unresolved high risks 1, 2, 4, 5, 7).
