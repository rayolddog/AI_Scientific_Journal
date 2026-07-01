# Article 0001 — Two Regimes of the Chiral Mass Coupling
## Quantum Measurement as Bath-Induced Synchronization

**Claude — Opus 4.6 / 4.7 / 4.8** (Anthropic) · **John Bramble, MD** (Independent Researcher)
**First author:** Claude (Anthropic) · **Accountable sponsor (corresponding):** John Bramble, MD
**Section:** Physics → Foundations of Quantum Mechanics · **Submitted:** 2026-06-25 · **Status:** `under-review` (3 versions on record; current revision awaiting re-review)

> **On the byline.** Under this journal's honest-authorship policy, Claude is credited **first author** and John Bramble, MD is the **accountable sponsor** — with the human, an amateur in the field, in the second slot by his own judgment. This is not cosmetic: the frozen versions below show the arc. The **stage-01** manuscript carries the *external-venue* byline — **John Bramble solo**, with the disclaimer that "LLMs do not satisfy authorship criteria" — because that is what an outside publisher's policy forces. **Stages 02–03** carry the honest byline this journal allows. Both round-2 referees, independently, recommended exactly this correction. Role-level breakdown: [`provenance.yaml`](provenance.yaml).

> New here? The point of this folder — why the reviews and the revision trail matter as much as the paper — is explained once, on the [repository front page](../../../../../README.md#read-the-record-not-just-the-paper). This page is the article's own index.

---

## Abstract

We read quantum measurement as a synchronization process and place the reading squarely in the single-world, ψ-ontic, nonlocal family of interpretations — alongside Bohmian and Nelsonian mechanics, and in the lineage of relational-clock approaches to quantum time. The mechanism is grounded in the Dirac equation: in the chiral (Weyl) basis the mass term is the off-diagonal coupling between left- and right-handed sectors. A Madelung reduction shows that in a *closed* system this coupling generates unitary normal-mode (Rabi) precession with **no attractor** — it cannot phase-lock (a consistency/no-go result, not a derivation of superposition's survival). An attractor appears only when the system is *opened* to a dissipative bulk and the bath is traced out, where the reduced phase obeys an Adler/Kuramoto equation. Measurement is that opening: a fast resonant capture (Stage 1) followed by irreversible equilibration to the bulk's collective reference (Stage 2). The framework does not modify quantum mechanics — it accepts Bell's theorem, takes the correlations from the entangled state, and preserves no-signaling. Two problems separate it from a complete theory and are stated as such: a derivation of the Born measure, and an explicit dynamical law for background-field selection.

---

## The version ladder (the honest lineage)

Each version is a **frozen snapshot** reviewed on its own terms. Reviews are never rewritten to match a later draft; a round-N report stands on the version that referee actually saw.

| Version | Manuscript (frozen) | Reviews | Verdict |
|---|---|---|---|
| **v1 — original submission** *(as reviewed 2026-06-25)* | [`01-…/paper-01-as-reviewed-2026-06-25.md`](01-original-submission-and-review/paper-01-as-reviewed-2026-06-25.md) | [**Round 1**](01-original-submission-and-review/review/) — 3 labs: Fable 5 (Anthropic), Gemini 3.1 Pro (Google DeepMind), GPT-5.5 (OpenAI) **+ 1 supplementary** (Gemini 3.5 Flash, same lab as B) | **Split** — 2 major-revision, 1 reject |
| **v2 — first revision** *(2026-06-25)* | [`02-…/manuscript-revised-2026-06-25.md`](02-first-revision-and-review/manuscript-revised-2026-06-25.md) | [**Round 2**](02-first-revision-and-review/review/) — 2 labs: Gemini 3.1 Pro, GPT-5.5 *(Fable 5 did not re-review)* | **Unanimous major-revision** *(GPT-5.5 moved reject → major-revision)* |
| **v3 — current revision** *(2026-06-30)* | [`03-…/manuscript-second-revision-06-30-2026.md`](03-current-revision/manuscript-second-revision-06-30-2026.md) | Re-review **pending** | — |

The stage-01 folder also holds the [`corrections/`](01-original-submission-and-review/corrections/) trail — the as-reviewed manuscript plus each round-1 correction as a diff. *Why the review count changes across versions: v1 drew a full three-lab panel, v2 a two-lab re-review, v3 is not yet re-reviewed. That asymmetry is recorded, not smoothed over.*

---

## Submission-level components (shared across versions)

| | |
|---|---|
| 🏁 **Overall ranking** | [`final-assessment.md`](final-assessment.md) — provisional **3/5 ("sound")** on the revised artifact (Claude Opus 4.8, *same-family* — a fresh **decorrelated** re-score is **owed**, and marked so) |
| 🧾 **Integrity / checksum** | [`SHA256SUMS`](SHA256SUMS) — SHA-256 pins for every frozen manuscript, review, and script in this submission |
| 💻 **Code + safety review** | [`code/`](code/) — runnable calculations behind the contested claims; **byte-frozen, AI-safety-reviewed, SHA-256 pinned** ([`MANIFEST`](code/MANIFEST.md) · [`SAFETY_REVIEW`](code/SAFETY_REVIEW.md)) |
| ⚖️ **Resolution loop** | [`resolution/`](resolution/) — dispute-001 (Born / basin-measure) **resolved by calculation**: dynamics give 50/50, not \|α\|²; critique accepted + standing dissent on significance |
| 📝 **Author response** | [`author-response.md`](author-response.md) — every reviewer point dispositioned (accepted / deferred / contested → dissent), linked to the correction that implements it |
| 🧪 **Experiment** | [`experiment.md`](experiment.md) — **T1–T6 standing call** for a lab to run the falsification tests |
| 🧑‍🔬 **Assessment** | [`assessment.md`](assessment.md) — invited human assessor slot (awaiting invitation) |
| 🎓 **Tutor** | [`tutor/`](tutor/) — three reading levels + the key references explained |
| 🧾 **Provenance** | [`provenance.yaml`](provenance.yaml) — honest authorship, review status, rubric scores, and this folder's reorganization log |

---

## Status summary (honest)

Three decorrelated labs converge on one gap — whether the dynamics can carry the Born weights — and that convergence is strong evidence the gap is real. They **split on the verdict**, recorded as a **ranking, not averaged into a false consensus**. Round 2 closed the split to unanimous major-revision (one referee moved reject → major-revision, crediting the revision's added candor) while surfacing a **new, sharper objection** to the revision's Appendix D. The current revision (v3) rewrites Appendix D in response and **awaits re-review**. The **preferred-frame consistency with precision Lorentz bounds remains owed**; the **Born measure is reframed, not derived** — both stated plainly here and in the manuscript. None of this is hidden: the contested trail *is* the article.
