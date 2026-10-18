---
name: wedge-launch-kit
description: Take a chosen opportunity to a testable launch. A name with a verified-available domain, pricing based on real competitor prices, a cheapest-possible stack with monthly cost, a one-page landing page with waitlist, and a 7-day validation test with a pass bar and kill criteria. Use for "name my business", "find a domain", "make a landing page", "how do I validate this", "how much will this cost to run", "how should I price this".
---

# Wedge: launch kit

Turns a GO into something real that can prove or kill demand within a week. Part of the Wedge pipeline; it also works on its own. Run it only on an opportunity the user has chosen.

Scripts are in the `wedge` skill's `scripts/` folder, usually `../wedge/scripts/`.

## 1. Name and domain

1. Generate 20 to 30 names that are short (one or two words, under 12 letters), easy to say and spell, and hint at the job or the feeling of the gap. Mix real words, compounds and coined words.
2. Check them in batches: `domain.py name1 name2 ... --tlds com,co,io,ai --handles`.
3. Present 5 finalists with a confirmed-available domain. Never call a domain available unless `domain.py` returned "available". Remind the user to confirm at a registrar and run a quick trademark search (USPTO TESS or EUIPO).

## 2. Pricing

Anchor to the price ranges in `competitors.md`. Recommend one launch price and a model (flat, per seat or usage) that directly fixes a pricing complaint, such as "no per-tech fees" or "price locked for life". Give the reasoning in two lines.

## 3. Cost to run

Choose the cheapest stack that's good enough and list each item with its monthly cost, free tiers first. Typical options: Cloudflare Pages, Vercel or GitHub Pages for hosting; Supabase or Neon free tiers for a database; Stripe or Lemon Squeezy for payments; Resend or SES for email. Free tiers change, so check current limits with a quick search and say when you checked.

## 4. Landing page: `ideas/<slug>/landing/index.html`

One self-contained HTML file with no build step, deployable to any static host:
- The headline is the positioning line from `win-plan.md`.
- 3 benefit blocks, each answering a top pain in customers' words.
- A "Why switch" block built from the switcher offers.
- A pricing teaser.
- A waitlist form. Default to a `mailto:` or a Formspree, Tally or Google Forms endpoint the user fills in. Never collect data to a place the user didn't choose.
- An honest FAQ.

Make it look designed, not templated: choose real typography, a restrained palette and generous spacing, and make sure it works at phone width.

## 5. Seven-day validation test

Write one experiment with a numeric pass bar, for example: "Post in r/<sub> and 2 named communities, list on <directory>, DM 20 people who complained. Pass = 40 waitlist signups or 5 people asking to pay. Below 15 signups = kill or pivot." Then list:
- the steps for each day
- 3 to 5 kill criteria

## Output: `ideas/<slug>/launch-kit.md`

Include the finalists with domain status, pricing, cost table, the test and the kill criteria, and link `landing/index.html`. Run `state.py done <slug> launch`.
