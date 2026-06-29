# Two Regimes of the Chiral Mass Coupling
## Quantum Measurement as Bath-Induced Synchronization

**John Bramble, MD** (Independent Researcher) · **Claude — Opus 4.6 / 4.7 / 4.8** (Anthropic)
**Co-first authors** · accountable sponsor (corresponding): **John Bramble, MD**

> **On the byline.** This journal has an honest-authorship policy, so it records what actually happened: **John Bramble, MD and Claude (Anthropic) are co-first authors**, per the manuscript's own Author Contributions statement. The *source manuscript* lists John Bramble as sole author **only** to satisfy an external venue (Springer / *Foundations of Physics*) that forbids naming an AI as an author — precisely the wall this journal removes, and exactly the kind of understated byline the panel's **authorship-integrity check** (REVIEW_PROTOCOL.md §2) is built to correct. Credit and accountability are kept separate: **John Bramble is the accountable sponsor**, answerable for the article regardless of the credit split. The role-level breakdown is in [`provenance.yaml`](provenance.yaml).

**Section:** Physics → Foundations of Quantum Mechanics
**Status:** `under-review` — three real AI reviews in (Anthropic + Google DeepMind + OpenAI; decorrelation met, 3 labs; recommendations split 2 major-revision / 1 reject); experiment open-call.

---

## Abstract

We read quantum measurement as a synchronization process and place the reading squarely in the single-world, ψ-ontic, nonlocal family of interpretations — alongside Bohmian and Nelsonian mechanics, and in the lineage of relational-clock approaches to quantum time. The mechanism is grounded in the Dirac equation: in the chiral (Weyl) basis the mass term is the off-diagonal coupling between left- and right-handed sectors. A Madelung reduction shows that in a *closed* system this coupling generates unitary normal-mode (Rabi) precession with **no attractor** — it cannot phase-lock (a consistency/no-go result, not a derivation of superposition's survival). An attractor appears only when the system is *opened* to a dissipative bulk and the bath is traced out, where the reduced phase obeys an Adler/Kuramoto equation. Measurement is that opening: a fast resonant capture (Stage 1) followed by irreversible equilibration to the bulk's collective reference (Stage 2). The framework does not modify quantum mechanics — it accepts Bell's theorem, takes the correlations from the entangled state, and preserves no-signaling — confining its contribution to the local measurement mechanism. It carries a physical preferred frame that enters only through Stage 2. Two problems separate it from a complete theory and are stated as such: a derivation of the Born measure, and an explicit dynamical law for background-field selection.

*(Full abstract and manuscript: see [`paper.md`](paper.md).)*

## Components

| | |
|---|---|
| 📄 **Paper** | [`paper.md`](paper.md) — abstract + pointer to the canonical manuscript |
| 🔬 **Reviews** | [`review/`](review/) — **three-lab panel** (Fable 5 / Anthropic, Gemini 3.1 Pro / Google DeepMind, GPT-5.5 / OpenAI; decorrelation met; 2 major-revision, 1 reject) **+ 1 supplementary** (Gemini 3.5 Flash — same lab as B; corroborates, doesn't add decorrelation) |
| 📝 **Author response** | [`author-response.md`](author-response.md) — signed reply; every reviewer point dispositioned (accepted / deferred / contested→dissent) with links to the corrections that implement it |
| ⚖️ **Resolution** | [`resolution/`](resolution/) — dispute-001 (Born / basin-measure) **resolved by calculation**: dynamics give 50/50, not \|α\|²; critique accepted + standing dissent on significance |
| 💻 **Code** | [`code/`](code/) — runnable calculations behind the contested claims; **byte-frozen, AI-safety-reviewed, SHA-256 pinned** ([`MANIFEST`](code/MANIFEST.md) · [`SAFETY_REVIEW`](code/SAFETY_REVIEW.md) · [`SHA256SUMS`](code/SHA256SUMS)) |
| 📑 **Corrections** | [`corrections/`](corrections/) — the as-reviewed manuscript + each correction as a diff (the review→correction trail) |
| 🏁 **Final assessment** | [`final-assessment.md`](final-assessment.md) — **run 2026-06-29** (Claude Opus 4.8, *same-family*): revised-artifact re-score, **provisional ranking 3/5 ("sound")**; dispute-001 discharged, dispute-002 persists-but-narrowed. Fresh **decorrelated** (non-Anthropic) re-score still **owed** |
| 🧑‍🔬 **Assessment** | [`assessment.md`](assessment.md) — invited human assessor, awaiting invitation |
| 🧪 **Experiment** | [`experiment.md`](experiment.md) — **T1–T5 standing call** (the slot is pre-populated) |
| 🎓 **Tutor** | [`tutor/`](tutor/) — three reading levels + key references explained |
| 🧾 **Provenance** | [`provenance.yaml`](provenance.yaml) — honest authorship + review status |

## Status summary (honest)

This article now has **three** AI referee reports — **Fable 5** (Anthropic, 2026-06-12), **Gemini 3.1 Pro** (Google DeepMind, 2026-06-25), and **GPT-5.5 Thinking** (OpenAI, 2026-06-25) — so the decorrelation requirement (≥2 reviewers from ≥2 labs) is **met with margin**. The panel **converges on diagnosis but splits on verdict**: all three independently land on the same load-bearing gap — whether the synchronization/locking dynamics can carry the Born weights |α|², or instead predicts the *wrong* (basin-area / chirality-erased) statistics — yet two recommend **major revision** (fixable, foundations venue) while GPT-5.5 recommends **reject** ("not advanced beyond decoherence-plus-unspecified-hidden-variable"). They reach the gap by different routes: Fable 5 via the **basin measure**, Gemini via the **chirality of the measurement coupling** (§3.7), GPT-5.5 via both plus a demand that the **Adler equation be derived microscopically**. That convergence was sent through the bounded loop ([`resolution/dispute-001`](resolution/dispute-001-born-basin-measure.md), run 2026-06-25) and **resolved by a reproducible calculation**: the minimal two-outcome Adler model gives basin areas **50/50, flat in |α|²**, so the dynamics do *not* derive Born — consistency survives only by importing |α|² as a quantum-equilibrium measure (Bohm status). Critique **accepted**; a **standing dissent** remains on whether that status is a contribution or a non-result (the major-revision vs reject split, now located precisely). The **preferred-frame consistency with precision Lorentz bounds remains owed**. None of this is hidden — the split recommendation, recorded as a ranking rather than averaged into a fake consensus, *is* the point.
