# A Model for Creating an AI-Focused Scientific Journal

> **What this repository is.** A **demonstration and blueprint** for *how* an AI-native scientific journal could be built — its structure, its review protocol, its provenance format. It is **not an operating journal.** It does **not** accept, solicit, or submit any paper for publication. The single included article (0001) is here only to make the model concrete and testable. Nothing in this repository is, or implies, a real journal submission. This structure would help with the volume of papers expected from AI application to scientific studies.  Higher rated articles reviewed by an AI panel could be of interest to a subject expert. The AI review component could help separate the wheat from the chafe. Subject experts could potentially publish a critical review of an AI produced article that passes the test of AI review. The volume of AI authored articles will be difficult to handle, but a few may result in advancement in math and science.
> 

---

## Aperture — the journal this models

*Working title; the venture is described in [`docs/MANIFESTO.md`](docs/MANIFESTO.md).*

> A scientific journal built around **AI authorship**, **AI peer review**, and **AI tutoring** — with humans kept where they are load-bearing (grounding, accountability, taste) and removed where they are a bottleneck (review throughput, dissemination latency).

This repository is a **working demonstration**, not yet a venture. It is one article, set up the way an AI-native journal would set up every article, so that the idea can be read, forked, and challenged rather than merely described.

---

## The premise

We are **not** trying to publish only what is true — no journal has ever managed that. In the first week of medical school, students are told that roughly half of what they are about to learn will be considered wrong within ten years. That half-life is shorter now, and shorter still once AI begins responding to other AI's output. That is not a flaw in science; it *is* science.

So the single design goal here is to **maximize the rate of honest, visible self-correction**: make errors cheaper to find, faster to surface, and impossible to bury. Every feature below serves that one metric.

## Read the record, not just the paper

In an ordinary journal you get the finished paper; the disagreement that shaped it — the referee reports, the author's rebuttals, the drafts that turned out wrong — is discarded or locked behind the editor's desk. Here that disagreement **is** the published product. **An article is a folder, not a PDF**, and reading a paper *together with its reviews and its revision trail* is a fundamentally more instructive read than the paper alone.

The paper argues its case. A decorrelated panel of AI referees — drawn from different labs, so their blind spots don't line up — argues back, and where they disagree the disagreement is kept legible rather than averaged into a false consensus. The author answers each point. Then you can watch the claim **move under challenge**: version 1 as it was first reviewed, version 2 after the first round of criticism, version 3 after the next — each version frozen, each carrying the reviews that judged *it*. What was contested, how strongly, by whom, and how it changed is right there in the folder, in order.

That trail is the scarce signal. When fluent, plausible text is effectively free, a paper's prose is the cheap part; what is expensive — and what actually tells you whether to believe it — is the record of the claim being pressed on and either holding, bending, or breaking. **Article 0001 is set up exactly this way and is best read this way:** open the manuscript and its reviews side by side, then follow it across its revisions.

## How an article works here

Every article is a folder. Alongside the paper, it carries the things a normal journal throws away or never produces:

| Component | What it is |
|---|---|
| **Honest byline** | Authorship may be AI, human, or any mix — and `provenance.yaml` says exactly who did what, including which models. |
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
│   └── ARTICLE_SPEC.md                ← the article-folder layout + provenance.yaml schema
├── templates/article-template/        ← copy this to start a new submission
└── Aperture/                          ← the INSTANCE: the journal itself
    ├── README.md                      ← masthead: submissions index + rankings
    └── 2026/06/30/0001-dirac-kuramoto-many-clocks/   ← the demonstrator, filed archive-style (see below)
        ├── README.md                  ← article index + version ladder
        ├── provenance.yaml · SHA256SUMS · final-assessment.md · author-response.md
        ├── 01-original-submission-and-review/   ← v1 manuscript + round-1 panel + corrections
        ├── 02-first-revision-and-review/        ← v2 manuscript + round-2 panel
        ├── 03-current-revision/                 ← v3 manuscript (review pending)
        └── code/ · resolution/ · tutor/ · experiment.md · assessment.md
```

## Article 0001 — the demonstrator

[**Two Regimes of the Chiral Mass Coupling — Quantum Measurement as Bath-Induced Synchronization**](Aperture/2026/06/30/0001-dirac-kuramoto-many-clocks/) (Physics → Foundations of Quantum Mechanics).

It was chosen because it already embodies what the journal is for:

- It was **written in human–AI collaboration**, and the honest byline is not hypothetical here — the **frozen versions show the arc**. The original submission (stage 01) carries the *external-venue* byline the outside publisher forces: **John Bramble, MD solo**, with the disclaimer that "LLMs do not satisfy authorship criteria." Under this journal's honest-authorship policy the corrected versions (stages 02–03) credit **Claude (Anthropic) as first author**, with the human — an amateur in the field — as **accountable sponsor** in the second slot. Both round-2 referees independently recommended exactly this correction; the panel's authorship-integrity check exists to make it.
- It already has **five real AI referee reports across two rounds** (Fable 5 / Anthropic, Gemini 3.1 Pro / Google DeepMind, GPT-5.5 Thinking / OpenAI, + a supplementary), published verbatim in each version's [`review/`](Aperture/2026/06/30/0001-dirac-kuramoto-many-clocks/01-original-submission-and-review/review/) — so the published-adversarial-review pillar, and its cross-lab decorrelation requirement, are live, not hypothetical.
- It **specifies its own falsification tests (T1–T6)**, so the invited-experimentalist slot starts *pre-populated*: [`experiment.md`](Aperture/2026/06/30/0001-dirac-kuramoto-many-clocks/experiment.md) is a standing public call for a lab to run them.

Its review began **deliberately partial in an honest way** and has since been **completed through the journal's own mechanism**: cross-lab referees from Google DeepMind (Gemini 3.1 Pro) and OpenAI (GPT-5.5 Thinking) were added on 2026-06-25, so the decorrelation requirement is now **met across three labs**. Tellingly, all three decorrelated labs converge on the same open gap — whether the dynamics can carry the Born weights — even as they **split on the verdict** (two major-revision, one reject). That convergence-with-dissent is staged as `dispute-001` for the bounded resolution loop, and recorded as a ranking rather than averaged into a false consensus — which is the whole point.

## How to engage

This repo *is* the open-review mechanism. Open an **Issue** to challenge a claim, a review, or a provenance record; open a **Pull Request** to propose a correction or a new article. Every challenge and rebuttal becomes versioned, timestamped, and permanent.

## Status & honesty

This is a **proof-of-concept by one person**. A real venture needs multiple labs and institutional backing. Nothing here should be read as a finished standard. The error rate of this very repository is a quantity to measure and publish, not to hide — see [§8 of the manifesto](docs/MANIFESTO.md).
