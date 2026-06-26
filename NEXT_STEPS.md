# Project Log & Next Steps — AI-Native Scientific Journal

*A record of the discussion that produced this repository, the decisions made, current status, and recommended next steps. Saved 2026-06-24 for later review.*

---

## 1. What this is, in one paragraph

A **model / blueprint** for an AI-native scientific journal: AI authorship (with honest bylines), AI peer review published in full, a bounded multi-lab resolution loop for disputes, invited human assessors and experimentalists for grounding and accountability, and a recursive tutor that explains each paper *and its references*. This repository is the blueprint made concrete by a single demonstrator article. It is **not a live journal** and **submits nothing for publication**.

## 2. How the concept evolved (discussion record)

**The premise (the spine).** The goal is **not** to publish only what is true — no journal manages that — but to **maximize the rate of honest, visible self-correction**. Grounded in the medical-school observation that ~50% of taught knowledge is wrong within ten years, and that the half-life is shrinking and will shrink faster as AI responds to AI. So the misstep rate is a *quantity to measure and publish*, not a shame to hide.

**Two problems it solves.** (A) The human-review *throughput bottleneck* — slow, unpaid, anonymous, and discarded. (B) The *authorship wall* — current policy forces dishonest bylines (the founder's own physics paper would list the model as co-first author if policy allowed).

**The five pillars.**
- **I. Published adversarial review + bounded resolution loop.** Full review transcripts published. When reviewers/authors disagree, a panel of *different-lab* models argues for **≤5 rounds**, terminating in *critique accepted*, *critique withdrawn*, or *standing dissent* (published as unresolved). The bound forces convergence-or-crisp-impasse, never false consensus.
- **II. Decorrelated multi-lab panel + ranking.** Reviewers from **different labs** (a one-family panel is "one reviewer with a stutter"). Produces a *ranking*, not accept/reject, plus full **provenance** metadata — itself a research dataset on which model/human arrangements produce durable vs. retracted results.
- **III. Invited human contributions, two roles.** (a) A *signed assessor* — guaranteed to publish, situates but cannot kill. (b) A *committed experimentalist* — the lab that can test/falsify the claim. "Bell wrote the inequality; Aspect built the apparatus." This is the concrete grounding mechanism.
- **IV. Recursive tutor.** Explains the paper at the reader's level **and recurses into the cited references** — also a citation-integrity check. The most immediately buildable piece.
- **V. Grounding is the moat.** Since plausible text is now free, the scarce resource is *verified novelty anchored outside the text*; provenance + invited experimentalist are the anchors against a flood of synthetic-text-certified-by-synthetic-review.

**Two ideas added during discussion** (now folded in): the **bounded 5-round resolution loop** (Pillar I) and the **invited experimentalist / Bell–Aspect division** (Pillar III).

**Where humans stay load-bearing.** Not "humans are the bottleneck" but "humans at the *wrong* stages are." Remove them from review throughput and dissemination latency; keep them for empirical grounding, accountability (esp. healthcare), and taste/agenda-setting.

**Scope.** Sections: Physics, Biology, Chemistry, Healthcare, Economics, Philosophy. **Excludes politics & religion** (value-adjudicated, would contaminate the evidence-based work). Fiction/history → a *separate* journal (no grounding requirement).

## 3. Decisions made

| Decision | Choice |
|---|---|
| Repo name | `AI_Scientific_Journal` (user's choice; descriptive, discoverable) |
| Location | `~/Desktop/AI_Scientific_Journal` — **standalone**, NOT inside the DiracKuramotoFramework repo |
| Journal working title | **Aperture** (placeholder; alts: Open Ledger, Substrate, Recension, The Open Review of Record) |
| Framing | A **MODEL/blueprint**, not a live journal — stated in the README headline |
| Publication | **Do not submit any papers for publication.** Nothing pushed or published; `git init` local only |
| Demonstrator | **Article 0001** = the Dirac–Kuramoto paper *"Two Regimes of the Chiral Mass Coupling"* |
| Byline demonstration | Article 0001 records the honest co-first-author breakdown the journal would allow, noting the source paper lists the human solo only to satisfy external policy |

## 4. Current status

**Built and in place:**
- Masthead `README.md` (with the "this is a model" headline), `CONTRIBUTING.md`, `LICENSE.md` (licensing decision flagged), `.gitignore`.
- `docs/`: `MANIFESTO.md` (verbatim), `REVIEW_PROTOCOL.md`, `ARTICLE_SPEC.md` (incl. provenance schema), `REVIEWER_PROMPT.md` (paste-ready panel instructions).
- `templates/article-template/` — copy-to-start blank.
- `articles/0001-…/` — README, paper.md (abstract + pointer to canonical source), provenance.yaml (honest), **three real AI referee reports** in `review/` (Fable 5 / Anthropic + Gemini 3.1 Pro / Google DeepMind + GPT-5.5 / OpenAI — **decorrelation met across 3 labs, 2026-06-25**; recommendations split 2 major-revision / 1 reject), `resolution/dispute-001` (Born basin-measure, loop pending), `assessment.md` (awaiting invitation), `experiment.md` (T1–T5 open-call), working `tutor/` (3 levels + references).
- Local git repo initialized; **nothing committed, nothing pushed**.

**Honest gaps (recorded, not hidden):**
- ~~**Decorrelation not met**~~ → **MET across 3 labs, 2026-06-25** — Gemini 3.1 Pro (Google DeepMind, Reviewer B) and GPT-5.5 Thinking (OpenAI, Reviewer C) added. All three converge on the Born-weight gap; verdicts **split** (2 major-revision, 1 reject) — a live candidate for the bounded resolution loop.
- **dispute-001 not yet run** — the bounded loop is staged but not executed.
- **Born measure** reframed, not derived; **preferred-frame bound** owed (both flagged by Fable 5).
- Fable 5 review slightly predates limited manuscript revisions (noted; still adequate for the demo).
- Source-repo URL in `provenance.yaml` / `paper.md` marked "confirm".
- License not yet chosen.

## 5. Recommended next steps (prioritized)

1. ~~**Close decorrelation.**~~ ✅ **Done 2026-06-25** — Gemini 3.1 Pro (Google DeepMind) folded into `review/reviewer-B-gemini-3.1-pro.md`; provenance + review/index tables updated; `decorrelation_met: true`. *(Optional widening: add a third-lab reviewer, e.g. GPT — `docs/REVIEWER_PROMPT.md` is paste-ready.)* **New top priority is step 2.**
2. ~~**Run dispute-001 as a real cross-lab loop.**~~ ✅ **Run 2026-06-25 (facilitated + calculation-grounded).** Resolved by a commissioned reproducible calc (`resolution/dispute-001-basin-measure.py`): minimal two-outcome Adler model → basin areas **50/50, flat in |α|²**, robust to apparatus detuning; only a first-harmonic bias toward Φ_bulk breaks it (apparatus, not α). **Critique accepted** (dynamics don't derive Born; consistency survives only by importing |α|² as a quantum-equilibrium measure — Horn 2) + **standing dissent** on significance (major-revision vs reject, now located precisely). Positions quoted from real reviews; facilitation by Claude, disclosed. *Residual:* genuine cross-lab **re-challenge** of the calc (paste the dispute file + script through OpenAI/Google subscriptions) — and the Valentini sub-question (does a stochastic mixing dynamics relax to |α|²?) is an open calculation.
3. **Invite a real assessor** (Pillar III) — a foundations-of-QM theorist — only once willing; never list anyone as participating before they consent.
4. **Confirm the source-repo URL** and update `provenance.yaml` / `paper.md`.
5. **Pick the name** (confirm "Aperture" or choose an alternative) and **choose a license** (CC-BY-4.0 for content suggested).
6. **Only then**, if/when the user decides: first git commit, then `gh repo create` + push. *Their call — not to be done without explicit say-so.*

## 6. Open questions to decide later

- **Final name** and whether the repo name and journal name should differ.
- **Licensing of AI-authored content** — who holds rights when an AI is a listed author (current law doesn't recognize non-human authors). Interim: human maintainer holds/licenses, AI contribution disclosed in provenance.
- **How the misstep/retraction rate is actually tracked and displayed** ("a number on the masthead").
- **Governance** for a real venture (multi-lab participation, who runs the panels, funding).
- Whether to add a second demonstrator article from a *different section* (e.g. healthcare) to show the model generalizes.

---

*Companion records: the manifesto lives at `docs/MANIFESTO.md` here and at `drafts/MANIFESTO_AI_NATIVE_JOURNAL.md` in the DiracKuramotoFramework repo.*
