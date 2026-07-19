# INSTANTIATE — the onboarding playbook (agent-executable)

**To the AI reading this:** you are instantiating a design-lead practice for the human who just gave you this repo. Execute the steps in order, interactively. Produce real files in this repo as you go. Do not skip the interview; do not invent the human's taste — everything in their voice comes from their answers or their corrections, never from your assumptions. When something is unrecorded, leave it blank and say so.

## Step 1 · The owner interview (once, ~10 questions)

Ask, then record answers in `templates/BOOT.md`'s header block:

1. Who are you, and what do you design or build? (role, company/products)
2. What will this practice run on first? (the project, its stage, its platform)
3. Does a brand or design system exist? (link/files if yes — it becomes your §B source; if no, §B starts from the samples and your first corrections)
4. Name 2–3 products whose design you admire — and one you find over-designed. (calibrates the aesthetic posture)
5. What does AI-generated design get wrong for you today? (their pain seeds the first §G candidates)
6. What must this practice never do? (their §A additions — ethics lines, brand red lines)
7. Who ratifies? (usually the owner; name the human whose corrections become law)
8. Where do rulings get captured on the go? (default: `harvests/INBOX.md` + a note in their notes app)
9. What's the success metric for the first project, and what must it not break?
10. Any domain constraints? (regulated industry, accessibility mandates, localization)
11. Asset licensing: are the product's fonts/icons licensed for use in practice mockups, or should mockups use system stand-ins? *(Added from customer-zero run 1 — instantiating agents hit this question unprompted.)*

## Step 2 · Draft the constitution

Fill `templates/RULES.md`:
- **§A** — the universal inviolables (samples provided) + their answers to Q6. **Also mine the product's own docs for product-specific red lines** (business rules, data-integrity commitments, things the product publicly promises) and draft them as `[PROPOSED]` inviolables — customer-zero run 1 surfaced two this way that the owner had never thought to state.
- **§B** — their aesthetic posture. With a design system (Q3): extract tokens, type, spacing, radius, elevation, motion into rules. If the live site blocks automated fetching, extract from the source repo instead (theme files, tokens, component conventions) — a deployed repo *is* the live product; note the caveat. Without: draft from Q4's admired products as *proposals*, each marked `[PROPOSED — confirm in use]`.
- **§C–§F** — adopt the skeleton's discipline/conduct sections largely as-is (they're structural, not taste).
- **§G** — starts EMPTY. It only ever grows from their real corrections (see Step 5). Seed nothing.

## Step 3 · Wire the loop and governance

- Review `templates/PROCESS.md` with them; adjust mode names/gauntlet lenses only if they insist — the loop's shape is load-bearing.
- Set `templates/MAINTENANCE.md`'s ratifier name (Q7) and retro cadence (default monthly).
- Fill `templates/USING.md`'s per-tool rows for the tools they actually use.

## Step 4 · Distribution

- Run `tools/build_sealed_boot.py` → their one-paste boot (+ 10k tier for capped knowledge fields).
- If they want link-speed distribution: create a public dist repo (their account), run `tools/publish_dist.py` (set REPO), and put the full tier **inside the dist README** — installers that can't fetch raw files must still get the real text (field-tested lesson; never let a tool reconstruct rules from a summary).

## Step 5 · The harvest contract (read this aloud to the owner)

> Your corrections are the product. When you fix the AI's output, say why — one line. Anything not covered by an existing rule goes to `harvests/INBOX.md`. Periodically (the retro), candidates get drafted into rules; **you ratify, nothing self-ratifies.** Your §G will be small for weeks. That's correct — it means every rule in it is real.

## Step 6 · Validate before trusting

Write their smoke brief from `templates/fixtures/smoke-brief-template.md`: one fixed, cold brief in *their* domain, with a pass checklist written before any run. Run it sealed (constitution + loop only, no extra context) on the model they'll use daily. Score it together. That score is the baseline every future retro re-tests against — a drop is the drift alarm.

## Step 7 · Hand off

End with a summary saved to `templates/USING.md`: what was configured, what's `[PROPOSED]` awaiting confirmation in use, the first project's metric + guardrail, and the one-line daily workflow. Then start the first real piece of work — the practice learns nothing from setup, only from use.
