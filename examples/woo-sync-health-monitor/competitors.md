# Competitors: sync-health monitoring for WooCommerce catalogs (WP.org API stats 2026-10-18)
| Name | What it watches | Alerts | Price | Traction |
|---|---|---|---|---|
| Google Merchant Center (free) | Google-side product status | Email on significant drop in active products, by default (e27, e28); account suspension email (e29) | free | built in |
| Google for WooCommerce (free) | Overview: active/expiring/pending/disapproved/not synced (e33) | none found | free | 800k installs |
| Meta Commerce Manager / Meta for WooCommerce (free) | Diagnostics view, manual check or build your own API integration (e30, e31); per-product validation box (e32) | no email alert found | free | 400k installs |
| Product Feed Manager by RexTheme | Its own feed runs | Added email alerts for failed/incomplete runs 2026-08-12 (e38), then temporarily disabled (e39) | freemium | 10k installs, 4.8 |
| Feed Health Monitor for WooCommerce | Local product data only, no feed gen (e35) | Admin email on new critical errors / score drop (e34) | free | 0 installs, launched 2026 |
| FeedProof, Merchant Feed Booster Lite, Suspension Shield, PodSync, PW Readiness Audit | Local pre-flight data audits; FeedProof connects to no external service (e36) | PodSync paid add-on emails when a passing product stops passing (e37); PW sells a paid Merchant API connector (e40) | free + paid add-ons | 0-10 installs each |
| Shopify-only: Feed Guard, Feed Sentinel, FeedKill Watch, FeedSiren | Merchant Center + store data | Yes (e41, e44); $4.99/mo (e42) | $5-20/mo | 0 reviews (e43) |
| Optmyzr (agencies) | Disapproval-count alerts inside a PPC suite | yes | from $209/mo (e45) | established |
- Crowded: local "will Google reject this?" product-data audits. Six WP.org plugins launched in 2026, none past 10 installs.
- Covered free: Google-side big drops in active products (e28).
- Thin: one monitor that reads the store's own sync jobs (Action Scheduler/WP-Cron for whichever plugin is installed) plus Meta-side status, and alerts. Closest is RexTheme, but only for its own feeds, and the feature is currently disabled.
