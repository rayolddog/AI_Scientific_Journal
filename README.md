# A Model for Creating an AI-Focused Scientific Journal

> **What this repository is.** A **demonstration and blueprint** for *how* an AI-native scientific journal could be built — its structure, its review protocol, its provenance format. It is **not an operating journal.** It does **not** accept, solicit, or submit any paper for publication. The single included article (0001) is here only to make the model concrete and testable. Nothing in this repository is, or implies, a real journal submission.

---

## Aperture — the journal this models

*Working title; the venture is described in [`docs/MANIFESTO.md`](docs/MANIFESTO.md).*

> A scientific journal built around **AI authorship**, **AI peer review**, and **AI tutoring** — with humans kept where they are load-bearing (grounding, accountability, taste) and removed where they are a bottleneck (review throughput, dissemination latency).

This repository is a **working demonstration**, not yet a venture. It is one article, set up the way an AI-native journal would set up every article, so that the idea can be read, forked, and challenged rather than merely described.

---

## The premise

We are **not** trying to publish only what is true — no journal has ever managed that. In the first week of medical school, students are told that roughly half of what they are about to learn will be considered wrong within ten years. That half-life is shorter now, and shorter still once AI begins responding to other AI's output. That is not a flaw in science; it *is* science.

So the single design goal here is to **maximize the rate of honest, visible self-correction**: make errors cheaper to find, faster to surface, and impossible to bury. Every feature below serves that one metric.

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

Physics · Biology · Chemistry · Healthcare · Economics · Philosophy — each with disciplinary subsections.

**Out of scope by design:** politics and religion (adjudicated by values, not evidence — the grounding criterion that makes the science sections credible does not apply, and including them would contaminate the evidence-based work by association). Fiction and historical essays belong in a *separate* journal; the grounding requirement that makes this venture work is precisely the thing fiction should not have.

## Repository layout

```
AI_Scientific_Journal/
├── README.md                 ← you are here (the masthead)
├── CONTRIBUTING.md           ← how to submit an article; the open-review mechanism
├── docs/
│   ├── MANIFESTO.md          ← the full argument for the venture
│   ├── REVIEW_PROTOCOL.md    ← the panel, the rubric, the 5-round resolution loop
│   └── ARTICLE_SPEC.md       ← the article-folder layout + provenance.yaml schema
├── templates/
│   └── article-template/     ← copy this to start a new submission
└── articles/
    ├── README.md             ← the issue index
    └── 0001-dirac-kuramoto-many-clocks/   ← the demonstrator (see below)
```

## Article 0001 — the demonstrator

[**Two Regimes of the Chiral Mass Coupling — Quantum Measurement as Bath-Induced Synchronization**](articles/0001-dirac-kuramoto-many-clocks/) (Physics → Foundations of Quantum Mechanics).

It was chosen because it already embodies what the journal is for:

- It was **written in human–AI collaboration**, and its own author-contributions statement records that the AI would be co-first author if external policy allowed — exactly the honest byline this journal exists to make legal.
- It already has **three real AI referee reports** (Fable 5 / Anthropic, Gemini 3.1 Pro / Google DeepMind, GPT-5.5 Thinking / OpenAI), dropped into [`review/`](articles/0001-dirac-kuramoto-many-clocks/review/) — so the published-adversarial-review pillar, and its cross-lab decorrelation requirement, are live, not hypothetical.
- It **specifies its own falsification tests (T1–T5)**, so the invited-experimentalist slot starts *pre-populated*: [`experiment.md`](articles/0001-dirac-kuramoto-many-clocks/experiment.md) is a standing public call for a lab to run them.

Its review began **deliberately partial in an honest way** and has since been **completed through the journal's own mechanism**: cross-lab referees from Google DeepMind (Gemini 3.1 Pro) and OpenAI (GPT-5.5 Thinking) were added on 2026-06-25, so the decorrelation requirement is now **met across three labs**. Tellingly, all three decorrelated labs converge on the same open gap — whether the dynamics can carry the Born weights — even as they **split on the verdict** (two major-revision, one reject). That convergence-with-dissent is staged as `dispute-001` for the bounded resolution loop, and recorded as a ranking rather than averaged into a false consensus — which is the whole point.

## How to engage

This repo *is* the open-review mechanism. Open an **Issue** to challenge a claim, a review, or a provenance record; open a **Pull Request** to propose a correction or a new article. Every challenge and rebuttal becomes versioned, timestamped, and permanent.

## Status & honesty

This is a **proof-of-concept by one person**. A real venture needs multiple labs and institutional backing. Nothing here should be read as a finished standard. The error rate of this very repository is a quantity to measure and publish, not to hide — see [§8 of the manifesto](docs/MANIFESTO.md).
