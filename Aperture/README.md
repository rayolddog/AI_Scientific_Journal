# Aperture — the journal

*The **instance**. This folder is Aperture set up as an AI-native journal would set up every article. For the **blueprint** — what the journal is, why it is built this way, and how to read it — see the [repository front page](../README.md).*

Articles are filed archive-style by date, `Aperture/<year>/<month>/<day>/<id>-<slug>/`, so the layout reads like a live archive rather than a flat folder.

---

## Submissions

| # | Title | Section | Versions | Standing verdict | Ranking |
|---|---|---|---|---|---|
| [**0001**](2026/06/30/0001-dirac-kuramoto-many-clocks/) | Two Regimes of the Chiral Mass Coupling — *Quantum Measurement as Bath-Induced Synchronization* | Physics → Foundations of QM | 3 (v1 → v2 → **v3**) | **Unanimous major-revision** (round 2) | **3 / 5** *"sound"* — split (see note) |
| [**0002**](2026/10/22/0002-field-matter-selector-born-exchange/) | A Field–Matter Selector for Outcome Production via Conserving Complex-Interference Exchange | Physics → Foundations of QM | 2 (v1.0 → **v2.0**, + v0.9 pre-audit) | **Split** in Round 1 (2 major-revision, 1 reject); **v2.0** posted for Round 2 | **0…3 / 5** — split (**GPT-6 = 0**, **Grok 4.7 = 2**, **Gemini = 3**) |
| [**0003**](2026/10/22/0003-complex-4d-vacuum-projections/) | Spacetime Light Cones, Lorentz Contraction, and Quantum Correlations as Projections of a Two-Spinor Complexified 4D Vacuum: A Geometric Toy Model | Physics → Foundations of QM & Relativistic Geometry | 1 (**v1.0** / Rev. 2.7) | **Split** (Round 1: 2 major-revision, 1 reject) | **0…2 / 5** — split (**GPT-6 = 0**, **Grok 4.7 = 1**, **Gemini = 2**) |
| [**0004**](2026/10/22/0004-big-bang-c4-condensation-cosmology/) | The Big Bang as Energy-Triggered Condensation of an Infinite Two-Spinor Complexified 4D Vacuum into a $3+1\text{D}$ Spacetime Bubble: A Cosmological Toy Model | Physics → Cosmology & Quantum Gravity | 1 (**v1.0** / Rev. 1.2) | **Split** (Round 1: 2 major-revision, 1 reject) | **0…2 / 5** — split (**GPT-6 = 0**, **Grok 4.7 = 1**, **Gemini = 2**) |

**Ranking note (0001).** The headline **3/5** is the modal read, **not an average**. Round-2 decorrelated overall rankings on the revised manuscript were **Gemini 3.1 Pro = 3** ("sound") and **GPT-5.5 Thinking = 1** ("serious reservations"); a same-family Claude Opus 4.8 re-score also landed at 3. GPT-5.5's **1 is carried as a standing dissent**, not averaged in — the spread (1…3) *is* the signal: the verdict converged to unanimous major-revision while the quality ranking stayed split, locating the residual disagreement on significance / publish-bar ([dispute-002](2026/06/30/0001-dirac-kuramoto-many-clocks/resolution/dispute-002-significance.md)), not on the facts. A fresh fully-decorrelated re-score of the current revision is **owed**. *(These fields are eventually generatable from each article's [`provenance.yaml`](2026/06/30/0001-dirac-kuramoto-many-clocks/provenance.yaml).)*

**Round-1 Note (0002, 0003, 0004) & Stage-02 Revision (0002).** Each of Articles **0002**, **0003**, and **0004** has completed Round-1 review across three foundation-model labs: **Gemini (Google DeepMind, disclosed co-author audit)**, **Grok 4.7 (xAI, external zero-overlap decorrelated lab)**, and **GPT-6 (OpenAI, ChatGPT Astra slot, strictly pre-exposure)**. Across all three articles, Gemini and Grok 4.7 recommended **Major Revision** while GPT-6 recommended **Reject** (**0/5**), producing a split Round-1 verdict (**2 major-revision, 1 reject**) published as an unaveraged vector (**0…3 / 5** on 0002; **0…2 / 5** on 0003 and 0004). For Article **0002**, the authors have posted a comprehensive [`author-response.md`](2026/10/22/0002-field-matter-selector-born-exchange/author-response.md) and **Stage-02 First Revision (`v2.0`)** ([`manuscript-revised-2026-10-24.md`](2026/10/22/0002-field-matter-selector-born-exchange/02-first-revision-and-review/manuscript-revised-2026-10-24.md)) that incorporates GPT-6's algebraic proofs (the $(s_j-s_i)\sin^2\epsilon$ drift obstruction, the Kimura–Ohta $N$-site fixation formula, and the backward-Kolmogorov non-cancellation theorem), discloses the $\theta=0.45$ ten-site breakdown, and replaces all constructed Figure 3 points with event-by-event Monte Carlo simulations.

---

## How to read an article here

Open the article's own `README.md` for its index, then read the manuscript **together with the reviews that judged it** and follow it across its versions — that combined read is the point, and it is spelled out on the [repository front page](../README.md#read-the-record-not-just-the-paper). Every article carries, alongside the paper: the full published review panel (decorrelated across labs), the bounded resolution loop for disputes, the author's point-by-point response, runnable + checksum-pinned code, a recursive tutor, and an honest `provenance.yaml`.

## Scope

Phase-1 sections are **Physics** and **Chemistry**; the exclusions (human-subjects, dangerous-capability, value-adjudicated domains) and the reasoning are on the [front page](../README.md#sections) and in the [manifesto](../docs/MANIFESTO.md). This repository is a **demonstration**, not an operating journal: it accepts, solicits, and submits nothing.
