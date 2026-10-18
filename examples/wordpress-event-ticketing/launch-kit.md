# Launch kit: a test kit for the PIVOT (agency channel)

The verdict is PIVOT, so this kit exists to run the 7-day test that decides whether A′ deserves a build. It is not a launch.

## Name and domain
Checked 25 names with `domain.py --tlds com,app,co,io` (RDAP, 2026-10-17). Most `.co` and `.io` lookups returned "unknown" (the registry didn't answer), so this kit makes no claims about those TLDs.

| Finalist | .com | .app |
|---|---|---|
| **Stubhaven** (pick) | available | available |
| Stubpath | available | available |
| Tixhold | available | available |
| Tixsteady | available | available |
| Rippass | available | available |

Other names that came back available on `.app` only: stubdesk, ticketwell, steadygate, gatehold, seatsure, tixlog, stublocker, tiximo, stubforge, ticketgrove, wellgate. Taken on every TLD checked: doorlist, stubly. "Available" is RDAP's answer; confirm at a registrar and run a trademark search (USPTO / EUIPO) before buying.

## Pricing
- **Recommendation:** $29/month per agency, up to 10 client sites, no per-ticket fee from us, and the price locked for early-list members.
- **Competitor range:** $99 to $399/yr per site for plugins (c4, c10, c11, c2; Tickera renews at $99/yr), $29.99/mo for Ticket Spot (k3), and per-ticket fees for hosted tools (c13, c15, c16).
- **Rationale:** Tickera's $99/yr renewal sets a per-site anchor for agencies, so $29/mo across 10 sites undercuts plugins once an agency has 4 or more sites. The locked price answers the renewal-hike complaints (r9, r10).

## Cost to run (estimates; free-tier limits **not re-checked** this run)
| Item | Cost |
|---|---|
| Cloudflare Pages (landing + dashboard front end) | $0 |
| Supabase or Neon free tier (database) | $0 |
| Stripe Connect, direct charges on clients' own Standard accounts | Stripe's fees are paid by the client; check Connect pricing before building |
| Resend or Amazon SES (ticket email) | $0 to about $20/mo depending on volume |
| Domain (stubhaven.com) | about $10 to $20/yr at typical registrars (not checked) |
| **Total** | **about $0 to $25/mo**, well under the $1k budget |

## Landing page
`landing/index.html`: a single self-contained file (Google Fonts only) with light and dark themes, phone-width layout, real quotes from the evidence, and a `mailto:` waitlist placeholder (replace `hello@example.com` before publishing).

## 7-day validation test
- **Experiment:** reach WordPress agencies and freelancers who publicly reviewed events plugins (a1 to a5 and similar) through their **own** websites, publish two search pages, and run a $50 switch-intent ad test.
- **Pass bar:** 5 agencies agree to a call **and** 2 of them say they'd pay $29/mo or more (or ask for early access with payment), **or** 30 waitlist signups from agency domains.
- **Steps:**
  - Day 1: publish the landing page on Cloudflare Pages, plus assets/vs-event-tickets.md and the recovery checklist.
  - Day 2: list 40 agencies/freelancers from public WordPress.org reviews; email 20 via their own contact pages (assets/outreach.md, message 1).
  - Day 3: email 20 more; start a $50 Google Ads test on "the events calendar alternative" and similar terms (assets/ads.md).
  - Day 4: answer, without links, in agency communities whose rules allow it.
  - Days 5 to 6: hold calls; ask what they pay per client today and whether they'd pay a flat agency price.
  - Day 7: score against the pass bar.
- **Kill criteria:**
  - Fewer than 3 agencies agree to a call out of 40 contacted.
  - None say they'd pay a flat agency price.
  - Fewer than 10 waitlist signups after 7 days.
  - Calls show agencies are happy to push clients to Ticket Tailor or Zeffy (meaning no unmet need).
  - Ad CTR under 1% on switch-intent terms.
