# Pains: what Bookly and Amelia customers complain about

## Sources
I fetched **139 one-to-three-star review topics** from WordPress.org, each opened as a full page with `fetch.py page`:
- Bookly: 64
- Amelia: 57
- BookingPress: 16
- LatePoint: 2
- Simply Schedule Appointments: none came back. The filtered lists returned no topics, and its WP.org rating is 100/100 from 155 ratings.

Raw text is in `raw/wporg-*.jsonl`. I also pulled 90 Hacker News records (`raw/hn.jsonl`), but they held almost nothing about these products. Reddit is blocked on this network, so it isn't used. The digest is in `signals.md`.

## Context before reading the themes
- **These are the unhappy minority.** Of all ratings:
  - Bookly: 53 one-star out of 585, and 468 five-star.
  - Amelia: 58 one-star out of 790, and 675 five-star.
  - LatePoint: 2 one-star out of 104.

  Two reviewers allege the five-star reviews were solicited or rewarded (`best-booking-and-appointment-plugin`, `absolute-trash-7`). That is an allegation, not a fact.
- **Some complaints are old.** Dates are approximate, converted from WP.org's "N years ago". Most Bookly add-on and paywall complaints date from 2018 to 2023. Bookly's current pricing page says "No hidden costs or add-ons" (e66). Amelia's update and support complaints are **recent**: several are from 2025 and 2026 (e4, e7, e13, e14, e15, e50, e54).
- **Recency by plugin.** WP.org lists reviews newest first. In the fetched 1–3★ sample:
  - Amelia: 20 of 57 are from the last 24 months, and 11 from the last 12.
  - Bookly: 3 of 64 are from the last 24 months, and **0** from the last 12.
  - BookingPress: 4 of 16 from the last 24 months.

  So Bookly's public complaint stream has largely dried up, and the live dissatisfaction is with Amelia.
- **Many reviewers are developers or freelancers** setting the plugin up for a client (e62 to e65). They decide which plugin gets installed.

Counts are my classification of the 139 fetched reviews. One review can hit several themes.

## Themes, ranked by severity × frequency

### 1. Support is slow, scripted or absent: **high**
Tickets go unanswered for days or weeks while bookings are down. Reviewers explicitly leave over it (e58).

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 18 | 20 | 9 | 0 |

Evidence: e1, e2, e3, e4, e5, e6, e7, e8, e9.

### 2. An update breaks live bookings or loses data: **high**
Lost appointments, wiped customers, payments taken with no booking, waitlists and slots breaking after an update.

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 13 | 13 | 7 | 0 |

- "The last update deleted EVERYTHING including customers, bookings…" (e13, Amelia, about 2026-01)
- "It's the third time we lose a lot of appointments" (e10, Bookly, about 2024-09)

Evidence: e10, e11, e12, e13, e14, e15, e16, e17, e18.

### 3. Lapsed license means no fixes, nags or a broken dashboard: **high**
Bookly-specific: support ran out after 6 months, then an update broke the plugin and help required paying again. Reviewers call it a "ransom" (e19). Amelia's annual license renews at the full crossed-out price (e24, official). This is a switching trigger, because it surfaces exactly at renewal.

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 9 | 1 | 1 | 0 |

Evidence: e19, e20, e21, e22, e23 (plus e24 official).

### 4. Basics locked behind add-ons or higher tiers: **medium** (was high; mostly historical for Bookly)
Payments, blocking days, Google Calendar and staff cabinets were each a separate purchase. The free versions are called "just an advertisement" (e29).

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 20 | 5 | 2 | 1 |

Evidence: e25, e26, e27, e28, e29, e30, e31.

### 5. Scheduling logic doesn't match how service businesses work: **medium**
Idle gaps from mixed durations, a forced "employee" step for one-person shops, the front desk unable to book manicure plus pedicure together, no multiple staff per booking, bookings allowed in the past.

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 12 | 10 | 3 | 0 |

Evidence: e32, e33, e34, e35, e36, e37, e38.

### 6. Not WordPress-native, hostile to developers: **medium**
A separate user system, its own tables, no hooks or docs, broken timezones, dozens of tables left after uninstall. This hits the freelancers who choose the plugin for clients.

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 3 | 14 | 1 | 1 |

Evidence: e39, e40, e41, e42, e43, e44, e45.

### 7. Clunky admin for day-to-day running: **medium**
Hard to add a booking or a client from the backend, and the admin is "unnecessarily difficult" for a small business (e50, a salon that left in 2026).

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 6 | 5 | 2 | 0 |

Evidence: e50, e51, e52, e53.

### 8. Locked in: data hard to get out, sunk license cost: **medium**
Low frequency, but this is the main thing that stops people switching.

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 2 | 3 | 0 | 0 |

- "You are basically a hostage to your own appointments." (e48)
- "I've also paid for a lifetime licence so I'm stuck." (e47)

Evidence: e46, e47, e48, e49.

### 9. Refund refused: **low**

| Bookly | Amelia | BookingPress | LatePoint |
|---|---|---|---|
| 2 | 1 | 2 | 0 |

Evidence: e60, e61.

## Silence: things nobody complains about because nobody offers them (hypotheses, not facts)
- **Migration in.** No reviewer mentions using an importer. Instead they describe rebuilding, or staying stuck (e47). Importers do exist, though: BookingPress (e84) and Sugar Calendar (e85). So the silence is more likely an awareness or trust problem than a missing feature.
- **Update safety.** Nobody mentions a plugin that backs up its own tables before a schema migration, or lets you roll back in one click. Reviewers improvise: "BACKUP WEBSITE BEFORE UPDATES!" (in `terrible-support-backup-website-before-updates`), and one restored a two-day-old backup (e13).
- **Named-human support.** No reviewer describes being able to reach the developer directly.

## The three themes most likely to make someone switch
1. **An update broke live bookings** (theme 2): a business-stopping event, and recent for Amelia. Triggers: e13, e14, e18.
2. **Support didn't answer while bookings were down** (theme 1): stated as the reason for leaving in e58 and e55.
3. **License renewal or expiry** (theme 3): the moment Bookly asks for money again, or Amelia renews at full price, is when people reconsider (e19, e24, e54).

Lock-in (theme 8) is the **barrier** to all three. A switch-in importer removes it.
