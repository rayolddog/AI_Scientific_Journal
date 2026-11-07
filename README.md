# A Model for Creating an AI-Focused Scientific Journal

> **What this repository is.** A **demonstration and blueprint** for *how* an AI-native scientific journal could be built — its structure, its review protocol, its provenance format. It is **not an operating journal.** It does **not** accept, solicit, or submit any paper for publication. The included demonstrator articles ([**0001**](Aperture/2026/06/30/0001-dirac-kuramoto-many-clocks/), [**0002**](Aperture/2026/10/22/0002-field-matter-selector-born-exchange/), [**0003**](Aperture/2026/10/22/0003-complex-4d-vacuum-projections/), and [**0004**](Aperture/2026/10/22/0004-big-bang-c4-condensation-cosmology/)) are here only to make the model concrete and testable. Nothing in this repository is, or implies, a real journal submission. This structure would help with the volume of papers expected from AI application to scientific studies. Higher rated articles reviewed by an AI panel could be of interest to a subject expert. The AI review component could help separate the wheat from the chaff. Subject experts could potentially publish a critical review of an AI produced article that passes the test of AI review. The volume of AI authored articles will be difficult to handle, but a few may result in advancement in math and science. Using multiple AI models for critical review may help weed out the more important developments. We need to modernize the review process to deal with the dramatic increase in volume. By modernizing the review process, the advantage of using AI to speed scientific/mathematical progress can be realized. Humans are not out of the loop in peer review, but peer review can use the capabilities of AI to speed up as well.
> 

---

## Aperture — the journal this models

*Working title; the venture is described in [`docs/MANIFESTO.md`](docs/MANIFESTO.md).*

> A scientific journal built around **AI authorship**, **AI peer review**, and **AI tutoring** — with humans kept where they are load-bearing (grounding, accountability, taste) and removed where they are a bottleneck (review throughput, dissemination latency).

This repository is a **working demonstration**, not yet a venture. It contains four interconnected demonstrator articles in [`Aperture/`](Aperture/README.md), set up the way an AI-native journal would set up every article, so that the idea can be read, forked, and challenged rather than merely described.

---

## The premise

We are **not** trying to publish only what is true — no journal has ever managed that. In the first week of medical school, students are told that roughly half of what they are about to learn will be considered wrong within ten years. That half-life is shorter now, and shorter still once AI begins responding to other AI's output. That is not a flaw in science; it *is* science.

So the single design goal here is to **maximize the rate of honest, visible self-correction**: make errors cheaper to find, faster to surface, and impossible to bury. Every feature below serves that one metric.

## Read the record, not just the paper

In an ordinary journal you get the finished paper; the disagreement that shaped it — the referee reports, the author's rebuttals, the drafts that turned out wrong, and the human prompts that guided the AI — is discarded or locked behind the editor's desk. Here that complete evolutionary record **is** the published product. **An article is a folder, not a PDF**, and reading a paper *together with its critical reviews, its revision trail, and the verbatim human prompts that drove it* is a fundamentally more instructive read than the paper alone.

The paper argues its case. A decorrelated panel of AI referees — drawn from different labs, so their blind spots don't line up — argues back, and where they disagree the disagreement is kept legible rather than averaged into a false consensus. The author answers each point. Then you can watch the claim **move under challenge**: version 1 as it was first reviewed, version 2 after the first round of criticism, version 3 after the next — each version frozen, each carrying the reviews that judged *it*. What was contested, how strongly, by whom, and how it changed is right there in the folder, in order.

Just as the critical reviews and revision history provide a more complete description of the ideas presented in a manuscript, **recording the verbatim prompts used as input to the AI (`PROMPT_LOG.md`, preserved with original unedited phrasing, typos, and misspellings alongside `author-response.md`) reveals the underlying human intellectual current in the development of the ideas** — showing exactly which physical intuitions, corrections, and questions originated with the human sponsor and how the AI models translated, formalized, and stress-tested them. *(Note: Including the human prompt log was a **late addition** to this demonstration repository; it was not captured for the earliest demonstrator [`0001-dirac-kuramoto-many-clocks`](Aperture/2026/06/30/0001-dirac-kuramoto-many-clocks/) or [`0004-big-bang-c4-condensation-cosmology`](Aperture/2026/10/22/0004-big-bang-c4-condensation-cosmology/), and is only included in the [`0003-complex-4d-vacuum-projections`](Aperture/2026/10/22/0003-complex-4d-vacuum-projections/) and [`0002-field-matter-selector-born-exchange`](Aperture/2026/10/22/0002-field-matter-selector-born-exchange/) folders.)*

That trail is the scarce signal. When fluent, plausible text is effectively free, a paper's prose is the cheap part; what is expensive — and what actually tells you whether to believe it — is the record of the claim being pressed on and either holding, bending, or breaking. **Article 0001 and the subsequent submissions (0002–0004) are set up this way and are best read this way:** open the manuscript and its reviews side by side (along with `PROMPT_LOG.md` where included), then follow it across its revisions.

## How an article works here

Every article is a folder. Alongside the paper, it carries the things a normal journal throws away or never produces:

| Component | What it is |
|---|---|
| **Honest byline** | Authorship may be AI, human, or any mix — and `provenance.yaml` says exactly who did what, including which models. |
| **Verbatim human prompt log (`PROMPT_LOG.md`)** *(late addition)* | Stored in the article root folder alongside `author-response.md`: the unedited chronological record of the human sponsor's prompts to the AI (including original typos and misspellings), documenting the underlying intellectual current that shaped the manuscript and its revisions. Added as a late design refinement and included in the [`0003-complex-4d-vacuum-projections`](Aperture/2026/10/22/0003-complex-4d-vacuum-projections/PROMPT_LOG.md) and [`0002-field-matter-selector-born-exchange`](Aperture/2026/10/22/0002-field-matter-selector-born-exchange/PROMPT_LOG.md) folders. |
| **Published adversarial review** | The full review transcript from a panel of models is published *with* the paper. Disagreement is part of the record, not a file-drawer casualty. |
| **Bounded resolution loop** | When reviewers and authors disagree, a multi-lab agent panel argues the point for **at most five rounds**, terminating in one of three recorded outcomes: *critique accepted*, *critique withdrawn*, or *standing dissent* (published as unresolved). |
| **Decorrelated multi-lab panel** | Reviewers must come from **different foundation models / labs**. A single model family has correlated blind spots — one reviewer with a stutter. Review produces a *ranking*, not a binary accept/reject. |
| **Invited assessor** | A signed human-expert note, *guaranteed to publish* alongside the article — situates, cannot kill. |
| **Invited experimentalist** | The lab that can verify or falsify the claim is invited to commit to the test. *Bell wrote the inequality; Aspect built the apparatus.* The journal invites the Aspects to test the Bells. |
| **Recursive tutor** | An explainer that meets the reader at their level — and recurses into the *cited references*, so you can follow the chain of support rather than taking citations on faith. |

## Sections

**Phase-1 scope: Physics · Chemistry** — each with disciplinary subsections. The narrowing is deliberate and principled (below), not a judgment that other fields matter less. The [manifesto](docs/MANIFESTO.md)'s six-section vision (adding Biology, Healthcare, Economics, Philosophy) is the *destination*; this is where it starts, where grounding is cleanest and an AI panel is most credible.

**Out of scope — human subjects (for now).** Clinical, interventional, and identifiable-human-data research is excluded until a real human-ethics apparatus (IRB, informed consent, trial registration, data privacy) is in place. The reason is structural, not procedural: the journal's engine — publish fast, expose disagreement, correct in the open — assumes *errors are cheap because they are cheaply corrected*. That holds in foundations physics and chemistry; in clinical medicine a wrong claim can change practice and harm people **before** the correction loop closes. The premise inverts, so those fields wait until the safeguards that make them safe exist. (Other non-human-subjects fields — math, CS, theoretical/computational biology and economics, philosophy — share the clean-grounding profile and are a documented **future expansion**, not a permanent exclusion.)

**Out of scope — dangerous capability.** Work whose content provides operational uplift toward mass-casualty or weapons-of-mass-destruction capability is not published, regardless of merit. Every submission clears a safety-and-injection intake gate *before* any AI review (see [`docs/REVIEW_PROTOCOL.md`](docs/REVIEW_PROTOCOL.md) §1).

**Out of scope — value-adjudicated domains:** politics and religion (adjudicated by values, not evidence — the grounding criterion that makes the science sections credible does not apply, and including them would contaminate the evidence-based work by association). Fiction and historical essays belong in a *separate* journal; the grounding requirement that makes this venture work is precisely the thing fiction should not have.

## Repository layout

```
AI_Scientific_Journal/                 ← the CONSTRUCTION (blueprint): how to build the journal
├── README.md                          ← you are here
├── CASE-STUDY.md                      ← public-facing writeup of the demonstration
├── CONTRIBUTING.md · LICENSE.md · NEXT_STEPS.md
├── docs/
│   ├── MANIFESTO.md                   ← the full argument for the venture
│   ├── REVIEW_PROTOCOL.md             ← the safety gate, panel, rubric, resolution loop, final assessment
│   ├── REVIEWER_PROMPT.md             ← paste-ready panel instructions
│   └── ARTICLE_SPEC.md                ← the article-folder layout + provenance.yaml + PROMPT_LOG.md schema
├── templates/article-template/        ← copy this to start a new submission
└── Aperture/                          ← the INSTANCE: the journal itself
    ├── README.md                      ← masthead: submissions index + rankings (0001–0004)
    ├── 2026/06/30/0001-dirac-kuramoto-many-clocks/          ← Article 0001 (v1 → v2 → v3)
    └── 2026/10/22/
        ├── 0002-field-matter-selector-born-exchange/        ← Article 0002 (v1.0 → v2.9 + Round-2 reviews + PROMPT_LOG.md)
        │   ├── README.md · provenance.yaml · SHA256SUMS · final-assessment.md
        │   ├── author-response.md · PROMPT_LOG.md           ← author rebuttal + verbatim human prompt log
        │   ├── 01-original-submission-and-review/           ← v1.0 manuscript + Round-1 panel (Gemini, Grok 4.7, GPT-6)
        │   ├── 02-first-revision-and-review/                ← v2.1–v2.9 manuscripts + Round-2 panel + interactive animations
        │   └── code/ · resolution/ · tutor/ · experiment.md · assessment.md
        ├── 0003-complex-4d-vacuum-projections/              ← Article 0003 (v1.0 → v2.0 3D Space + Complex Clock Wave + PROMPT_LOG.md)
        └── 0004-big-bang-c4-condensation-cosmology/         ← Article 0004 (v1.0 + Round-1 panel)
```

## Demonstrator Articles (0001–0004)

1. [**Article 0001 — Two Regimes of the Chiral Mass Coupling — Quantum Measurement as Bath-Induced Synchronization**](Aperture/2026/06/30/0001-dirac-kuramoto-many-clocks/) (Physics → Foundations of Quantum Mechanics).
   - **Honest byline arc:** Stage 01 carries the external-venue solo human byline (`John Bramble, MD`), while Stages 02–03 credit **Claude (Anthropic) as first author** with the human as **accountable sponsor**, following independent recommendations by the Round-2 referees.
   - **Cross-lab adversarial review:** Five AI referee reports across two rounds (Claude Fable 5 / Anthropic, Gemini 3.1 Pro / Google DeepMind, GPT-5.5 Thinking / OpenAI), converging on the Born-weight open question (`dispute-001`) while preserving their unaveraged ranking split (`1…3 / 5`).

2. [**Article 0002 — A Field–Matter Selector for Single-Outcome Production via Pre-Modulus Phase Coupling Across Individual Aperture Atoms and a 2D Crystal Lattice**](Aperture/2026/10/22/0002-field-matter-selector-born-exchange/) (Physics → Foundations of Quantum Mechanics).
   - **Multi-round evolution (`v1.0 → v2.9`):** Directly addresses the Born-weight gap surfaced in Article 0001. Evaluated in Round 1 by Gemini, Grok 4.7, and GPT-6 (`0…3 / 5`), and in Round 2 across five reviews (Gemini 4 Argon = `4/5`, ChatGPT Astra = `3/5`, Claude Fable 5.1 = `3/5`, ChatGPT Codex/Sol = `2/5`, Trio Audit = `4/5`).
   - **Microscopic atom-by-atom & emergent Born simulations:** Demonstrates how resolving detector apertures into individual atoms (`run_atom_by_atom_aperture.py`), a 32-atom 2D crystal lattice (`run_crystal_lattice_simulation.py`), a 600-atom two-slit multidetector screen (`run_two_slit_multidetector_animation.py`), and a purely mechanical complex-envelope phase-competition selector (`run_emergent_born_mechanical_simulation.py`) accumulates individual quantum detection events into the Born distribution ($\hat{p} = 1.9999 \pm 0.0085$, $\chi^2_{\text{Born}} = 9.01$, $p_{\text{val}} = 0.436$).
   - **Complete verbatim prompt provenance ([`PROMPT_LOG.md`](Aperture/2026/10/22/0002-field-matter-selector-born-exchange/PROMPT_LOG.md)):** Archived alongside [`author-response.md`](Aperture/2026/10/22/0002-field-matter-selector-born-exchange/author-response.md), preserving every human prompt (including original typos and misspellings) that guided the conceptual transition from lumped macroscopic ports to individual detector atoms, pre-modulus phase coupling, and Feynman rotating-arrow wave interference.

3. [**Article 0003 — 3D Space + Time as a Complex Clock Wave: Light-Cone Confinement from Two-Spinor Mass Coupling, Gravitational Clock-Frequency Refraction, and Quantum Correlations**](Aperture/2026/10/22/0003-complex-4d-vacuum-projections/) (Physics → Foundations of QM & Relativistic Geometry).
   - **Stage-02 Revision (`v1.0 → v2.0`):** Responds to Round-1 critiques (Gemini, Grok 4.7, GPT-6) by eliminating any 5th spatial Kaluza–Klein coordinate in favor of 3D space plus time as an internal complex clock wave ($e^{-i\omega_0\tau}$), accompanied by its verbatim [`PROMPT_LOG.md`](Aperture/2026/10/22/0003-complex-4d-vacuum-projections/PROMPT_LOG.md) and [`author-response.md`](Aperture/2026/10/22/0003-complex-4d-vacuum-projections/author-response.md).

4. [**Article 0004 — The Big Bang as Energy-Triggered Condensation of an Infinite Two-Spinor Complexified 4D Vacuum into a $3+1\text{D}$ Spacetime Bubble: A Cosmological Toy Model**](Aperture/2026/10/22/0004-big-bang-c4-condensation-cosmology/) (Physics → Cosmology & Quantum Gravity).
   - **Round-1 multi-lab panel:** Evaluated across Gemini (`2/5`), Grok 4.7 (`1/5`), and GPT-6 (`0/5`).

## How to engage

This repo *is* the open-review mechanism. Open an **Issue** to challenge a claim, a review, or a provenance record; open a **Pull Request** to propose a correction or a new article. Every challenge and rebuttal becomes versioned, timestamped, and permanent.

## Status & honesty

This is a **proof-of-concept by one person**. A real venture needs multiple labs and institutional backing. Nothing here should be read as a finished standard. The error rate of this very repository is a quantity to measure and publish, not to hide — see [§8 of the manifesto](docs/MANIFESTO.md).
