# Launch kit

The verdict is **PIVOT**, so this kit is built for the pivot: sell **migration and rescue off Amelia/Bookly** first, and use it to put your plugin on switchers' sites. It's a test, not a full launch.

## 1. Name and domain
I checked 35 names with `domain.py --tlds com,app,co,io` (and a second batch with `com,app`) through public RDAP. Many `.co` and `.io` lookups came back `unknown` (the registry didn't answer), so I only list domains that came back **available**.

| Finalist | Domain (status from domain.py) | Why |
|---|---|---|
| **SteadySlots** (pick) | steadyslots.com: **available**. steadyslots.app: **available** | Says the promise: bookings that stay put through updates and renewals |
| SwitchSlots | switchslots.com: **available** | Says the switch. Narrower once you're not only about migration |
| SlotKeep | slotkeep.app: **available** (.com taken) | Short. "Keep" speaks to the lock-in and lost-data fear |
| KeepBooked | keepbooked.app: **available** (.com taken) | Plain English for salon owners |
| BookingKeel | bookingkeel.com: **available** | Stable and steady, but harder to spell |

Taken or unclear: steadybook, keepslot, calmbook, switchbook, bookstead, quietbook and plainbook (.com and .app taken), safeslot.com, slotkeeper, staybooked.com. Confirm at a registrar before buying. Run a trademark search too (USPTO and EUIPO), because "Slots" names are common in gaming.

## 2. Pricing
- **Recommendation:** **$79/year, 1 site, every feature, unlimited staff, and the renewal price is the price you paid.** **$199/year for 10 sites** for freelancers. **Done-for-you migration: $149**, or free with the first year for the first 5 switchers.
- **Competitor range** (pricing pages fetched 2026-10-18, first-year sale → list):
  - Bookly Pro: $39 → $99/yr, or $99 → $129 lifetime.
  - LatePoint Starter: $79 → $99/yr, with every feature.
  - SSA: Plus $99 → $129/yr. Team features need Business at $399 → $499/yr.
  - BookingPress: Standard $89/yr.
  - Fresha: $19.95/month.
- **Rationale:** you can't undercut a $39 intro price, and you shouldn't try. Instead, fix the price complaints directly: renewal jumps (Amelia e24, LatePoint e73), tier gating (SSA e74) and lapse lockouts (e22). Charge separately for the migration labour, because that's the scarce thing.

## 3. Cost to run (monthly)
Fees were checked by web search on 2026-10-17. Confirm them on each vendor's pricing page.

| Item | Cost |
|---|---|
| WordPress.org plugin listing (free version) | $0 |
| Landing page on Cloudflare Pages or GitHub Pages | $0 |
| Email via domain forwarding (e.g. Cloudflare Email Routing) to your existing inbox | $0 |
| Domain steadyslots.com | ~$1/month (registrar price not checked; typical .com is ~$10–15/yr) |
| Payments and licensing: Lemon Squeezy (reported 5% + 50¢ per sale, plus surcharges on international and subscription payments) or Freemius (reported 4.7% + 2.3% WordPress surcharge, plus gateway fees) | $0 fixed, percentage per sale |
| Local test sites (LocalWP or Docker) for Bookly/Amelia migration testing | $0. You need copies of Bookly Pro and Amelia to test the importers against real schemas; budget about $100–250 one-time from their sale prices |
| **Total** | **≈ $1/month + payment fees + ~$100–250 one-time** (fits under $1k) |

## 4. Landing page
`landing/index.html` is a single self-contained file. It has:
- the positioning headline
- three pain-answer blocks
- the switcher offers
- a pricing teaser
- a `mailto:` waitlist (replace `you@example.com` with your own address)
- an honest FAQ

## 5. Seven-day validation test
**Experiment:** offer paid migration and rescue to people with a public, recent problem, and collect waitlist signups from the content.

**Pass bar:** **3 people agree to pay** for a $149 migration (or put down a deposit), **or** 25 waitlist signups with at least 5 replies saying yes to $79/yr. **Below 10 signups and 0 paid asks = kill or pivot again.**

| Day | Steps |
|---|---|
| 1 | Buy steadyslots.com. Deploy `landing/index.html`. List every Amelia and Bookly 1–3★ review from the last 24 months (links are in `win-plan.md`) and mark the ones whose authors publish a business or agency site. |
| 2 | Send message A (`assets/outreach.md`) to 15 reviewers through their own sites' contact forms. Never via WP.org. |
| 3 | Publish "Amelia update broke my booking form: how to roll back safely" on your site. Answer 5 unresolved WP.org threads genuinely, with no pitch. |
| 4 | Send message B to 10 WordPress freelancers or agencies. Watch jobs.wordpress.net for booking-plugin fix posts and quote $149. |
| 5 | Publish "Migrating from Amelia without losing appointments", plus `assets/vs-amelia.md` and `assets/vs-bookly.md`, after removing any bracketed promise that isn't true yet. |
| 6 | Join r/WPAmelia and the Amelia Discord. Read the rules. Help people, and disclose who you are if you mention your work. Do a migration dry run on a test copy of Amelia so you can quote real timings. |
| 7 | Count signups, replies and paid asks. Compare them against the pass bar and re-score willingness_to_pay in `gaps.md`. |

## Kill criteria
- Under 10 waitlist signups after 7 days and 25 direct messages.
- 0 people willing to pay for a migration or rescue at $149, or any price you name.
- More than half of the replies say "I already moved to LatePoint/SSA/Fresha". That means the switchers are already served.
- Reviewers you contact say the problem has since been fixed by the vendor (check the threads for vendor replies marked resolved).
- Migration dry runs take more than 4 hours each, which breaks the 15 h/week budget at a $149 price.
