# Signal digest

363 records from hn (259), github (104)

| Category | Hits | Distinct sources |
|---|---|---|
| missing | 27 | 22 |
| bugs | 25 | 21 |
| lockin | 15 | 13 |
| price | 11 | 9 |
| switching | 5 | 5 |
| complexity | 2 | 2 |
| wish | 0 | 0 |
| support | 0 | 0 |

## Competitor mentions

| Name | Mentions | Top pains |
|---|---|---|
| Let's Encrypt | 57 | lockin 6, bugs 3, missing 2 |
| Uptime Kuma | 23 | missing 9, bugs 1 |
| UptimeRobot | 2 | bugs 1 |
| Better Stack | 0 | - |
| StatusCake | 0 | - |
| updown | 0 | - |
| HetrixTools | 0 | - |
| Cert Spotter | 0 | - |
| TrackSSL | 0 | - |
| Red Sift | 0 | - |

## missing

- "Add SSL Certificate checks for General TCP ports ### ⚠️ Please verify that this feature request has NOT been suggested before." ([github](https://github.com/louislam/uptime-kuma/issues/1079), 2021-12-19)
- "[X] I checked and didn't find similar feature request ### 🏷️ Feature Request Type New Notification, New Monitor ### 🔖 Feature description Say you have an application running on a TCP port using an SSL Certificate that will expire eventually." ([github](https://github.com/louislam/uptime-kuma/issues/1079), 2021-12-19)
- "Notify when SSL/TLS certificate changes ### ⚠️ Please verify that this feature request has NOT been suggested before." ([github](https://github.com/louislam/uptime-kuma/issues/4143), 2023-12-01)
- "Customizable Alerts for Certificate Expiration: ### 🏷️ Feature Request Type Certificate expiry ### 🔖 Feature description Allow users to configure notifications for certificate expiration: Example: Notify 60, 30, 15, and 5 days before the expiration date." ([github](https://github.com/louislam/uptime-kuma/issues/5358), 2024-11-18)
- "🏷️ Feature Request Type Dashboard, Status-page, Certificate expiry ### 🔖 Feature description A dashboard that gives the status of all the HTTPs monitors without having to manually add/build them into it." ([github](https://github.com/louislam/uptime-kuma/issues/4962), 2024-07-25)

## bugs

- "Back Story: I built the basic tool kit for my previous startup - we were doing SEO and had very slow page speed across a wide variety of pages, so I ran lighthouse on an instance every day and put the results in the database and on a chart." ([hn](https://news.ycombinator.com/item?id=39974850), 2024-04-08)
- "Slow Performance alerts - if a page goes below a certain performance threshold, alert you 3." ([hn](https://news.ycombinator.com/item?id=39974850), 2024-04-08)
- "This tool keeps track of your SSL certificates in one dashboard and sends alerts before they expire, eliminating downtime risks and SEO penalties that can harm your business." ([hn](https://news.ycombinator.com/item?id=37408368), 2023-09-06)
- "Time lost, money spent, website glitches, and unhappy visitors complaining when their browsers say the website is not secure." ([hn](https://news.ycombinator.com/item?id=2556658), 2011-05-17)
- "A little while ago two major, yet easily avoidable problems occurred, resulting in downtime, lost revenue, stress, and unhappy clients: 1." ([hn](https://news.ycombinator.com/item?id=2560954), 2011-05-18)

## lockin

- "For contrast, **`aisstream.io`** itself is fine — valid through 26 Aug 2026 — so this looks isolated to the `stream.` subdomain's auto-renewal rather than a site-wide issue." ([github](https://github.com/aisstream/issues/issues/236), 2026-07-20)
- "This is most likely a failed auto-renewal of certbot or whatever Let's Encrypt agent runs your renewal cron." ([github](https://github.com/aisstream/issues/issues/189), 2026-05-20)
- "Just check expiration of the active certificate; if it’s under a threshold (say 1 week, assuming you auto-renew it when it’s 3 weeks to expiry; still serving a cert when it’s 1 week to expiration is enough signal that something went wrong) then you alert." ([hn](https://news.ycombinator.com/item?id=46407333), 2025-12-28)
- "I think I received about 15 'we're disabling email notifications soon' emails over the past several months - one of which was interesting, but none were needed, as I'd originally set this up, per documentation, to auto-renew every 30 days." ([hn](https://news.ycombinator.com/item?id=44642480), 2025-07-22)
- "Furthermore, their autorenew should have been failing loud and clear, everyone should know from metrics or logs… but nobody noticed anything." ([hn](https://news.ycombinator.com/item?id=46406880), 2025-12-28)

## price

- "My calc: SES pricing is around $0.1 per 1,000 emails." ([hn](https://news.ycombinator.com/item?id=43701747), 2025-04-16)
- "Pricing: It's free, but considering a paid version." ([hn](https://news.ycombinator.com/item?id=37408368), 2023-09-06)
- "I am interested to hear if anyone has had similar problems, whether people 'get' the idea of Silo, and finally would be willing to pay for this simple product (pricing at http://getsilo.com/plans)." ([hn](https://news.ycombinator.com/item?id=2556658), 2011-05-17)
- "Show HN: Uptime monitoring is table stakes I'm trying to disrupt the insane pricing of uptime monitoring." ([hn](https://news.ycombinator.com/item?id=47736853), 2026-04-12)
- "I made this after getting frustrated with overpriced monitoring tools that were too heavy for simple projects and didn’t offer helpful features like EC2 instance control or intelligent alerts." ([hn](https://news.ycombinator.com/item?id=43953014), 2025-05-11)

## switching

- "We moved from AWS to Hetzner, saved 90%, kept ISO 27001 with Ansible Earlier this year I led our migration off AWS to European cloud (Hetzner + OVHcloud), driven by cost (we cut 90%) and data sovereignty (GDPR + CLOUD Act concerns)." ([hn](https://news.ycombinator.com/item?id=44335920), 2025-06-21)
- "It's an alternative to either treating DNS as "set and forget", or doing manual checks / DIY scripts." ([hn](https://news.ycombinator.com/item?id=45720670), 2025-10-27)
- "AFAIK it only forces the browser to use HTTPS and never plain HTTP for that domain, but if you switch from a legit Let's Encrypt to a legit ZeroSSL cert, HSTS won't care about it; only the browser if you have a not-trusted certificate from another CA (or self-signed)." ([hn](https://news.ycombinator.com/item?id=45120607), 2025-09-03)
- "vault agent certificate renewal troubles Have decided to replace our CA with Vault but I'm now facing 2 issues: 1." ([github](https://github.com/hashicorp/vault/issues/26367), 2024-04-11)

## complexity

- "The problem: Most uptime tools I tried were either too complex, too expensive, or bundled with features I didn’t need." ([hn](https://news.ycombinator.com/item?id=45394922), 2025-09-27)
- "However, I agree that, unless you really know what you're doing, x509 is too complicated for that." ([hn](https://news.ycombinator.com/item?id=25382508), 2020-12-11)
