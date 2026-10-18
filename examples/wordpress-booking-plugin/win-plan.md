# Win plan: taking customers from Bookly and Amelia

Verdict context: **PIVOT, 63/100**. **Amelia first:** its complaints are recent, while Bookly's are mostly from 2023 and earlier (see `pains.md`) (see `gaps.md` and `critic.md`). Don't fight Bookly and Amelia feature for feature, and don't pitch yourself as "a cheaper LatePoint". Win the people who are **already stuck**: a broken update, a silent support queue, or a renewal coming up. Be the safe way off.

Working name: **SteadySlots** (steadyslots.com came back "available" from `domain.py`; see `launch-kit.md`).

## 1. Switching triggers

| # | Trigger (the moment they're fed up) | Evidence | Your move |
|---|---|---|---|
| 1 | **An update broke bookings or wiped data** | e13, e14, e15, e10, e17, e18 | Publish a plain "Amelia/Bookly update broke my booking form: how to roll back safely" guide that helps whether or not they switch. It ends with the rescue offer: we restore you, or migrate you in 48 hours. |
| 2 | **Support went silent while bookings are down** | e4, e5, e6, e7, e58 | Publish a support promise you can keep: a named developer, Mon–Fri, first reply within 1 business day. Put it on the pricing page. |
| 3 | **License renewal or expiry** (Bookly support lapse, Amelia renewing at the full crossed-out price) | e19, e20, e21, e22, e24, e54, e55 | A "switch before you renew" offer: free done-for-you migration when they show a renewal notice, plus a renewal price locked for life. |
| 4 | **A freelancer's client is phoning them about broken booking** | e62, e63, e64, e65 | A freelancer and agency program: one free client migration, a multi-site license, and documented hooks so they can fix things themselves. |
| 5 | **Hitting a scheduling wall** (multi-service front-desk booking, idle gaps, forced "employee" step) | e35, e36, e32, e33, e34, e38 | Ship these specific fixes and write one short page per wall, e.g. "Book manicure + pedicure together from the admin". |

## 2. Positioning
**Main:** *"The WordPress booking plugin you can switch to without losing a single appointment, and that won't break your bookings on update."*

Alternates:
- *"Get off Bookly or Amelia this week. We move your customers, services and future appointments for you, and the developer answers your email."*
- *"Booking for salons, barbers, tutors and therapists that keeps working: on update, on renewal, and when you need help."*

These reuse customers' own words. They fear updates ("I'm concerned about installing further updates", e15), feel trapped ("You are basically a hostage to your own appointments", e48), and wait on support ("I wait for weeks…", e4).

## 3. Offers that win switchers
1. **Done-for-you migration from Bookly or Amelia**, with a written "no appointment lost" check: a before/after count of customers, services and future appointments. *(Pain: lock-in, e46, e47, e48.)* Self-serve importers exist (e84, e85), so the offer is the labour and the guarantee, not the code.
2. **Bookings never stop if your license lapses.** You lose updates and support, never the booking form. *(Pain: license expiry, e19, e22.)*
3. **One renewal price, the same as the price you paid, stated on the pricing page.** *(e24, e73.)*
4. **A named developer and a published reply time** (1 business day, Mon–Fri). *(Pain: support, e2, e4, e5.)*
5. **Automatic table backup and one-click rollback before every update.** *(Pain: updates, e13, e10.)*
6. **30-day refund, no argument.** *(Pain: refunds, e60, e61.)*

## 4. Build first (complaint answered per unit of effort)

| Rank | Feature | Why (pain theme) | Effort |
|---|---|---|---|
| 1 | Bookly + Amelia importer: customers, services, staff, future appointments. Dry run first, then a diff report | Lock-in, the barrier to every switch (e46, e47, e48) | Small–medium |
| 2 | Update safety: version the schema, snapshot your tables before each migration, one-click rollback, and never auto-run destructive migrations | Updates break bookings, high severity (e10, e13, e14) | Small–medium |
| 3 | Lapse-safe licensing: no kill switch, no dashboard lockout | License expiry (e19, e22, `it-used-to-be-so-great`) | Small |
| 4 | Solo mode: hide the employee and category steps when there's one provider | Scheduling for one-person shops (e34) | Small |
| 5 | Front-desk admin: create the client inside the booking screen, with multiple services in one appointment | Clunky admin, scheduling (e35, e51, e52) | Medium |
| 6 | Gap-free slot logic for mixed durations | Scheduling (e32, e33, e38) | Medium |
| 7 | WordPress-native: WP users for customers, documented hooks and filters, and an uninstall that removes every table | Not WP-native (e39, e40, e41, e43, e44, e49) | Medium; partly a design choice from day one |

## 5. Where unhappy customers are

| Place | URL | Why it matters |
|---|---|---|
| Amelia 1–3★ reviews | https://wordpress.org/support/plugin/ameliabooking/reviews/?filter=1 (also `filter=2` and `filter=3`) | The most recent complaints (2025–2026), and several name a business or a freelancer. **Read only. WP.org forbids promoting here (e80).** |
| Bookly 1–3★ reviews | https://wordpress.org/support/plugin/bookly-responsive-appointment-booking-tool/reviews/?filter=1 | A long history of support, update and renewal complaints. Read only. |
| Specific threads worth studying | `new-version-is-glitchy-and-disappointing`, `amelia-did-not-meet-expectations`, `dont-support-multiple-services-booking-backend`, `doesnt-support-multiple-employees-per-appointment`, `support-unable-to-resolve-409-booking-error`, `not-a-safe-option-unexpected-bugs-everywhere` (all under https://wordpress.org/support/topic/) | Each one is a ready-made spec for a feature or an offer. Several authors are agencies with public sites (e64, e63). Contact them **through their own sites**, not the forum. |
| Amelia and Bookly support forums (unresolved topics) | https://wordpress.org/support/plugin/ameliabooking/unresolved/ · https://wordpress.org/support/plugin/bookly-responsive-appointment-booking-tool/unresolved/ | Live, unanswered problems: the trigger-1 moment. Answering genuinely, with no pitch, is allowed and builds reputation. |
| r/WPAmelia | https://www.reddit.com/r/WPAmelia/ | Amelia's own public community, linked from its help center. *Not fetched (Reddit is blocked here). Check its rules before posting.* |
| Amelia Discord | https://discord.gg/zx6HVQeCxB | Linked from Amelia's help center. Not checked. |
| Amelia feature board | https://features.wpamelia.com/ | Long-standing upvoted requests (a reviewer says multi-employee has been top ten "for years", e36). Returned 403 to the fetcher, so open it in a browser. |
| Bookly ideas board | https://ideas.booking-wp-plugin.com/ | The same for Bookly. Page is JS-rendered, so it wasn't fetched. |
| jobs.wordpress.net | https://jobs.wordpress.net/ | WP.org sends paid-fix requests here (guidelines page, e80 URL). It fits the rescue and migration service. |
| "Amelia alternative" / "Bookly vs" searches | e.g. Bookly's own blog runs "Bookly vs Amelia" and "Best LatePoint alternatives" posts | Vendors write these because people search for them. Your honest vs pages compete here. |

## 6. Trust signals
What competitors fail to show, per the reviews: renewal at the same price (e24), support that answers (theme 1), data that comes out (e46), clean uninstall (e43, e44), and features not pulled into paid add-ons (e28).

Credible from day one:
- The renewal price printed next to the first-year price.
- Support hours and a reply-time promise, with the developer's real name.
- An "Export everything (CSV + JSON)" button, and an uninstall that removes all tables. Both documented.
- A changelog entry for every release that says "what this update changes in your data", plus the rollback button.
- A 30-day refund.
- Public code or docs for hooks (optional: a public GitHub repo for the free version).

## 7. Stop doing (things a newcomer is tempted to copy)
- **License kill switches or dashboard lockouts** when support lapses (e22, `it-used-to-be-so-great`).
- **Moving an existing feature into a paid add-on in a minor update** (e28).
- **Asking for site credentials as the first support step** (e9). Ask for a system report or a staging copy instead.
- **Intro prices that jump at renewal** (e24, e73).
- **A separate user system and 50 custom tables** (e39, e43).
- **Asking for, or rewarding, 5-star reviews.** Reviewers notice and say so (`best-booking-and-appointment-plugin`, `absolute-trash-7`).
- **Refusing refunds behind marketplace rules** (e60, `read-dissatisfied-with-bookly`).

## Assets
- `assets/vs-bookly.md`: a fair comparison page.
- `assets/vs-amelia.md`: a fair comparison page.
- `assets/outreach.md`: two messages for people who publicly complained.
- `assets/faq.md`: six objections, answered honestly.

## First 10 customers
1. **Build the list (day 1).** From the Amelia and Bookly 1–3★ review lists above, take every review from the last 24 months. Note the reviewer handle, the problem, and whether they link a business or agency site. In the fetched sample, Amelia has 20 low-star reviews from the last 24 months (11 from the last 12). Bookly has only 3 from the last 24 months and 0 from the last 12. **Start with Amelia.**
2. **Contact reviewers who run agencies or businesses, through their own site's contact form, never on WP.org.** Use message A in `assets/outreach.md`. Start with the authors of `doesnt-support-multiple-employees-per-appointment` (agency, WooCommerce clients) and `support-unable-to-resolve-409-booking-error` (freelancer with a client).
3. **Offer 5 free done-for-you migrations** in exchange for an honest public review once they've used it for 30 days. The review must not be conditional on its rating.
4. **Publish the rollback guide** (trigger 1) and **"Migrating from Amelia without losing appointments"** on your site. Answer unresolved WP.org threads genuinely, with no links to your product unless a moderator allows it.
5. **jobs.wordpress.net:** watch for booking-plugin fix requests and quote a fixed price ($149 rescue or migration).
6. **r/WPAmelia and the Amelia Discord:** be useful for two weeks before you mention anything. Disclose that you build a competing plugin if you ever do.
7. **Freelancer program:** message 10 WP freelancers who review or post about booking plugins with message B ("one client migration free"). One freelancer can bring several client sites.
8. **List the free version on WordPress.org** once the importer and rollback work, with a readme that states the promises (lapse-safe, same renewal price, clean uninstall).
9. **Every migrated customer gets a 15-minute call.** Write down the exact words they use for why they left; that becomes your next landing copy.
10. **Pass bar for this list:** 3 paid migrations or 10 active installs from switchers within 30 days. Otherwise re-run the verdict (see `launch-kit.md` kill criteria).
