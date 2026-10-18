---
name: wedge-win-plan
description: Turn competitor weaknesses into specific moves that pull customers to you instead of them. Switching triggers, positioning in customers' own words, offers that win switchers, what to build first, where unhappy customers hang out, comparison pages, outreach scripts and trust signals, every move tied to evidence. Use for "how do I beat X", "steal customers from competitors", "how do I stand out", "positioning", "why would anyone pick us", "competitive strategy", or for an existing business that wants more customers.
---

# Wedge: win plan

Answers one question: why would a customer choose you over them, and how do you get in front of that customer at the right moment? Part of the Wedge pipeline. On its own, it's the core of the `compete` mode for existing businesses.

Inputs: `competitors.md`, `pains.md`, `gaps.md` and `critic.md`. For an existing business, also ask for its URL and fetch it with `fetch.py page` so the plan builds on what it already does.

## Build the plan

1. **Switching triggers.** Find the moments customers get fed up, from pains and reviews: a price hike or renewal, a support failure, a missing feature hitting a wall, an acquisition or rebrand, a forced migration or a growth stage the product can't handle. For each, note the trigger, the evidence, and the move: how you show up at that moment.
2. **Positioning.** Write one line that claims the spot competitors leave open: "The only <category> for <buyer> that <does what they complain nobody does>." Reuse customers' own words from quotes. Give 2 alternates.
3. **Offers that win switchers.** Pick 3 to 6 that address the top pains, such as:
   - free migration or import
   - matching the competitor's price for the rest of their contract
   - month-to-month with no contract
   - a public price that never changes on renewal
   - a named human for support
   - "fixed: <top complaint>" stated right on the pricing page

   Each one ties to a pain theme.
4. **Build first.** Rank 3 to 7 features by how much complaining they'd answer per unit of effort. Each one cites a pain theme.
5. **Where unhappy customers are.** List specific places with URLs: subreddits, forums, Facebook groups, review pages of competitors, "alternative to <X>" search results, and communities and directories for the buyer. Note why each place matters.
6. **Trust signals.** List what competitors fail to show: transparent pricing, real support hours, uptime, a data export promise, a guarantee. List which ones you can credibly show from day one.
7. **What to stop doing.** List the things competitors do that customers hate, and that a newcomer would be tempted to copy.

## Ready-made assets: `ideas/<slug>/assets/`

- `vs-<competitor>.md`: a fair comparison page draft. Don't invent claims about them; cite the pricing pages and docs.
- `outreach.md`: 2 short messages for people who publicly complained. Be helpful, not spammy, and follow each community's self-promotion rules.
- `ads.md`: 3 headlines and 3 descriptions written from customers' own words.
- `faq.md`: the top 6 objections, each with an honest answer.

## Output: `ideas/<slug>/win-plan.md`

Include every section above and its evidence IDs. Also include a **First 10 customers** plan: 5 to 10 concrete steps naming the exact place and the exact message. Run `state.py done <slug> win`.

## Rules

- Every move ties to a pain or trigger with evidence. A move with no evidence is cut, not softened.
- Check each community's rules before suggesting outreach there. Many forbid self-promotion, for example the WordPress.org support forums and most subreddits. Where it's forbidden, suggest helpful answers without links, or the person's own channels instead.
- Never suggest fake reviews, astroturfing, or misleading comparison claims. Beyond being wrong, it gets brands banned from the very communities they need.
