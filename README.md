# The design-lead standard

**An open scaffold for encoding a design practice — yours — so any AI model can execute it, audit against it, and get better at it with use.**

AI tools produce competent screens and generic judgment. They drift: invented components, made-up tokens, no process, no taste. The fix isn't reviewing harder — it's encoding. This scaffold is the empty vessel for doing that: a **constitution** (your rules), an **operating loop** (how work runs), a **harvest engine** (how your corrections become permanent law), and the **governance** that lets it grow without drifting away from you.

This is the *structure*, open and free. What you pour into it is yours.

## The three layers

| Layer | What it is | Who owns it |
| --- | --- | --- |
| **The standard** (this repo) | The empty structure: templates, conventions, tooling, governance | Open source (MIT) |
| **The canon** | A filled knowledge base: behavioral-science principles, pattern doctrine, intake protocols, validated fixtures | Licensed separately — see `CANON.md` |
| **Your voice** | Your aesthetic posture (§B), your harvested rules (§G), your takes | Yours, forever |

## Instantiate yours (three moves)

1. **Use this template** (button above) → your own private repo.
2. Open it in any capable AI tool and say: **"Read INSTANTIATE.md and onboard me."** The playbook interviews you, drafts your §B from your brand or taste, sets up your harvest inbox, your distribution channel, and your first validation run.
3. **Work.** Correct the AI's output in plain language. Every correction is a harvest candidate; ratified ones become your constitution. The practice gets more like you every week.

## What's in the box

```
INSTANTIATE.md          — the agent-executable onboarding playbook
CANON.md                — the contract for mounting a licensed canon
templates/
  RULES.md              — constitution skeleton (§A–G, writing conventions, samples)
  PROCESS.md            — the operating loop skeleton
  BOOT.md               — the one-page bootstrap skeleton
  AGENTS.md             — knowledge-base navigation contract
  MAINTENANCE.md        — growth governance (the autonomy ladder applied to the KB)
  USING.md              — the human operator's field guide skeleton
  fixtures/smoke-brief-template.md — your standing validation test
harvests/INBOX.md       — capture-anywhere, process-in-batch
tools/
  build_sealed_boot.py  — concatenates your boot into one paste-able file (+ a 10k tier for capped fields)
  publish_dist.py       — publishes your boot to your own public dist repo
  linkcheck.py          — internal link/anchor validator
```

## Design lineage

The standard generalizes a working practice built and validated in July 2026: cross-model sealed testing (a 12-box fixture, multiple models), a foreign-industry run against a third-party design system, and in-the-wild distribution where destination AIs self-installed the package from a URL. The reference implementation's public floor: [design-lead-dist](https://github.com/yorkchase/design-lead-dist).

## License

MIT — the scaffold is free to use, copy, and adapt. Canon content and any instance's voice layer are **not** part of this license; see `CANON.md`.

*Standard v0.1 · maintained by Chase York*
