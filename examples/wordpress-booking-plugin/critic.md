# Critic pass

**Brief:** "You are a skeptical investor who has seen 1,000 of these. Find the strongest reasons the top opportunity fails."

I ran this myself, deliberately arguing against `gaps.md`, rather than with a separate agent. The checks that ran:
- Someone tried and died: a WP.org directory query, HN, and a web search for closed booking plugins.
- A free or loved incumbent: WP.org API ratings, LatePoint and SSA pricing, Fresha and Square.
- Copyable in a week: a web search for existing importers.
- The channel is closed: WP.org forum guidelines.

## Risks

### 1. A loved, cheap incumbent already exists for unhappy switchers: **high** (Unresolved)
LatePoint is rated 98/100 from 104 ratings, with 2 one-star reviews. It has every feature on every plan (e71) and starts at $79/yr (e72). SSA is 100/100 from 155 ratings and promises replies within one business day (e75). Someone leaving Bookly or Amelia over bugs and support already has a well-reviewed place to go.
- **Partial rebuttal:** neither LatePoint nor SSA advertises a done-for-you migration or an update-safety guarantee in fetched copy. SSA gates team scheduling to $399 to $499/yr (e74), which is steep for a 3-chair salon.
- **Unresolved:** nothing shows Bookly or Amelia users choose a newcomer over LatePoint.

### 2. Migration isn't empty, so an importer is copyable and already shipped: **high** (partly resolved by changing the angle)
- BookingPress imports from Amelia, Bookly, Booknetic and LatePoint (e84).
- Sugar Calendar imports from Amelia in "a few clicks" (e85).
- PW Amelia Migration exports and imports Amelia data (e86).

Any incumbent can add an importer in weeks.
- **Rebuttal:** importers exist, yet reviewers still describe being "stuck" (e47) and a "hostage" (e48). The missing piece looks like trust and labour, not code. The angle therefore moved from "has an importer" to a **done-for-you migration with a no-lost-bookings promise**. That's a service incumbents don't sell. Whether anyone pays for it is untested, which is why WTP is 5.

### 3. The directory is saturated, and newcomers stall: **high** (Unresolved)
A WP.org search for "appointment booking" returns 784 results. Recently updated small entrants sit at 70 to 2,000 installs: radius-booking 400, truebooker 600, gembooking 200, rox 1,000 (`raw/wporg-plugin-info.jsonl`). On HN, a "Show HN: Free appointment booking plugin for WordPress" (DaySchedule, 2023) got 1 point. Organic WP.org discovery won't carry a new plugin.
- **Partial rebuttal:** the plan below doesn't rely on directory discovery. It relies on the public complaint threads and on freelancers.

### 4. WordPress.org forums forbid the obvious channel: **medium**
"The forums are not a venue to promote your own (or others') plugins, themes, websites or services." (e80). You can't reply to complaint threads with a pitch.
- **Rebuttal:**
  - Many reviewers are freelancers or agencies with their own public sites (e62 to e65), so they can be contacted directly and politely.
  - Amelia has public Discord and Reddit communities linked from its help center (r/WPAmelia). Their self-promotion rules weren't checked.
  - "Bookly vs" and "Amelia alternative" content is fair game.

### 5. Buyers are leaving WordPress booking altogether: **medium** (Unresolved)
Salons can use SaaS: Fresha is $19.95/month for one person (e79), and Square has a solo tier, though its price wasn't captured because the page is JS-rendered. For a salon owner (not a freelancer), "stop running booking on WordPress" is a real alternative.
- **Unresolved:** no evidence in this run on how often that happens.

### 6. You'll inherit the same reviews: **medium**
Booking plugins break across thousands of hosting setups, caching plugins and timezones (e16, e45). Support is the top complaint (theme 1), and a 15 h/week founder promising one-day replies can become the next 1-star thread.
- **Rebuttal:**
  - Cap the customer count during the service phase.
  - Publish the support hours honestly. Don't promise 24/7.
  - Ship update safety as code (pre-migration table backup, one-click rollback) so there's less to support.

### 7. The famous Bookly complaint is stale: **medium** (resolved by not leading with it)
The add-on nickel-and-dime reviews are mostly from 2018 to 2023 (e25 to e28). Bookly's current pricing says "No hidden costs or add-ons" (e66), and Pro is $39 for the first year (e67).
- **Rebuttal:** the win plan leads with update safety, support and migration, which are recent and current for Amelia (e13, e14, e4, e7, e50). Add-on pricing appears only as a secondary point.

### 7b. Bookly's complaint stream has dried up: **medium** (resolved by targeting)
In the fetched sample, Bookly has 0 low-star reviews from the last 12 months and 3 from the last 24, against Amelia's 11 and 20. Bookly customers are a weaker target today than the old reviews suggest.
- **Rebuttal:** target Amelia first. Keep the Bookly importer for the renewal trigger.

### 8. Directory-guideline and trust risk: **low**
BookingPress was closed on WP.org for a guideline violation (e78, e83). Upsell nags, tracking and license kill-switches can get a listing pulled.
- **Rebuttal:** follow the plugin guidelines from day one. Never disable bookings on license lapse; that's a trust signal anyway (theme 3).

### 9. The pain is real, but will anyone pay a stranger to migrate? **high** (Unresolved)
Owners pay for the plugins, but no evidence was found of paying a third party to rescue or migrate. Reviewers fight over refunds (e60, e61), and WP.org pushes paid fixes to jobs.wordpress.net (in the guidelines text, e80's page).
- **Unresolved:** this is exactly what the 7-day test has to answer.

## Net
Three high-severity risks remain unresolved (1, 3 and 9), and risk 2 is only partly resolved. That alone blocks GO under `references/scoring.md`. The pain is real and recent, so the verdict is **PIVOT**, not KILL.
