# Author Response to Panel Review — Article 0001

Per [`docs/REVIEW_PROTOCOL.md`](../../../../../docs/REVIEW_PROTOCOL.md) §4.

**Signed:** John Bramble, MD (accountable) · Claude (Anthropic, Opus 4.6/4.7/4.8) — matching the paper byline; see [`provenance.yaml`](provenance.yaml).
**Date:** 2026-06-28

> **Honesty note on this artifact.** §4 was added to the protocol *after* Article 0001 had already been corrected directly. This response is therefore a **retrospective consolidation** of dispositions that are already on the record — in [`corrections/`](01-original-submission-and-review/corrections/) (the diff trail) and [`resolution/`](resolution/) (the two disputes) — into the single signed document the protocol now requires. It introduces no new disposition; every row below links to the artifact that already implements it. Future articles produce this *before* revising.

The three-lab panel **converged on one load-bearing gap** — whether the synchronization/locking dynamics can carry the Born weights |α|² — and **split on the verdict** (Fable 5 and Gemini 3.1 Pro: major revision; GPT-5.5: reject). The convergence was settled by calculation; the split is preserved as a standing dissent. Point-by-point:

## Reviewer A — Fable 5 (Anthropic)

| # | Point | Disposition | Response | Links |
|---|---|---|---|---|
| A1 | The one claimed empirical advantage over Bohm is not established *in this paper* (it leans on the unrefereed companion). | **Accepted** | The advantage-over-Bohm claim was re-anchored to the in-paper §6 gravitational channel; the companion is no longer load-bearing. | [correction-001](01-original-submission-and-review/corrections/correction-001-companion-citation.diff) |
| A2 | Taken as dynamics, the picture appears to predict the *wrong* Born statistics — and this is checkable. | **Accepted (by calculation)** | Sent through the bounded loop and settled by a reproducible calc: basins are 50/50, flat in \|α\|². The paper now states **Horn 2** explicitly — \|α\|² is *imported* as a quantum-equilibrium measure, not derived. | [dispute-001](resolution/dispute-001-born-basin-measure.md) · [correction-003](01-original-submission-and-review/corrections/correction-003-born-horn2.diff) |
| A3 | After the paper's own concessions, locate precisely what is *new*. | **Accepted** | §3.7's chiral 0/π binary was demoted; the surviving novelty is located as the synthesis + single-world-as-occupied-basin + cut-as-measurable-locking-threshold. | [correction-004](01-original-submission-and-review/corrections/correction-004-remaining-recommendations.diff) |
| A4 | Im Σ = −½ K_eff cos Δ* (§3.6) is asserted, not demonstrated. | **Accepted** | The derivation was carried out and folded in as a self-contained **Appendix D** (driven–dissipative reduction → Adler, K_eff = 4χ²n̄/κ). | [correction-005](01-original-submission-and-review/corrections/correction-005-fold-keff-derivation.diff) |
| A5 | Preferred-frame consistency (§8) is a promissory note on a potentially fatal constraint. | **Deferred** | Acknowledged as still owed. The related "spontaneous→explicit" Lorentz-violation overclaim was corrected; the precision-bound consistency check remains an **open limitation**, stated as such. | [correction-004](01-original-submission-and-review/corrections/correction-004-remaining-recommendations.diff) |
| A6 | Load-bearing reliance on an unrefereed companion [26]. | **Accepted** | Every in-text [26] citation is now a non-load-bearing forward-pointer; the incidental §3.7 cite was dropped. | [correction-001](01-original-submission-and-review/corrections/correction-001-companion-citation.diff) · [correction-002](01-original-submission-and-review/corrections/correction-002-companion-citation.diff) |

## Reviewer B — Gemini 3.1 Pro (Google DeepMind)

| # | Point | Disposition | Response | Links |
|---|---|---|---|---|
| B1 | §3.7 chirality mismatch: EM couples via the vector current (chirality-preserving), acting on the wrong channel to register the scalar \|bar-ψψ\| weights — "largely devastating." | **Accepted** | The EM-selected **which-path/position basis** is named as the register; σx is internal-clock only. This is the same gap as A2/C2, reached via chirality. | [correction-004](01-original-submission-and-review/corrections/correction-004-remaining-recommendations.diff) · [dispute-001](resolution/dispute-001-born-basin-measure.md) |
| B2 | H′ gauge defect (§6.2): coupling to absolute φ_bulk breaks U(1)/shift symmetry. | **Accepted** | H′ named as a gauge-defective term, with the repair (couple to the gradient ∂_μθ) and reframing as a falsification term. | [correction-004](01-original-submission-and-review/corrections/correction-004-remaining-recommendations.diff) |
| B3 | §8 "spontaneous" Lorentz violation overclaims (genuine SSB needs an aether/khronometric VEV). | **Accepted** | Corrected to **explicit** low-energy Lorentz violation. | [correction-004](01-original-submission-and-review/corrections/correction-004-remaining-recommendations.diff) |
| B4 | Minor/presentational (§2.5 bridge, terminology). | **Accepted** | Folded into the batch (§2.5 spatial-gradient bridge; "unhidden variable" glossed as *local macroscopic reference*). | [correction-004](01-original-submission-and-review/corrections/correction-004-remaining-recommendations.diff) |

## Reviewer C — GPT-5.5 Thinking (OpenAI)

| # | Point | Disposition | Response | Links |
|---|---|---|---|---|
| C1 | The Adler equation is **asserted, not derived**. | **Accepted** | Discharged by **Appendix D** — the microscopic derivation the reviewer demanded. | [correction-005](01-original-submission-and-review/corrections/correction-005-fold-keff-derivation.diff) |
| C2 | Why should the basin measure equal \|α\|² rather than geometric basin volume? + non-demolition channel (Q3/Q4). | **Accepted (by calculation)** | Same as A2/B1: dynamics give 50/50; \|α\|² imported (Horn 2). | [dispute-001](resolution/dispute-001-born-basin-measure.md) · [correction-003](01-original-submission-and-review/corrections/correction-003-born-horn2.diff) |
| C3 | Citation integrity: self/companion references carry too much weight. | **Accepted** | Companion de-load-beared (see A6). | [correction-001](01-original-submission-and-review/corrections/correction-001-companion-citation.diff) · [correction-002](01-original-submission-and-review/corrections/correction-002-companion-citation.diff) |
| C4 | Novelty is mostly re-description; **recommendation: reject** (gap is disqualifying as it stands). | **Contested → standing dissent** | We accept the *factual* diagnosis (it is a reframing, not a new derived prediction) but contest that this disqualifies an honestly-labeled foundations synthesis with one testable structural idea. This is a **value disagreement about the publish bar**, not a factual one — narrowed and published as a standing dissent, routed to a human assessor and to experiment **T6**. | [dispute-002](resolution/dispute-002-significance.md) · [experiment.md](experiment.md) |

## Summary

- **Accepted:** A1, A2, A3, A4, A6, B1–B4, C1, C2, C3 — implemented across [corrections 001–005](01-original-submission-and-review/corrections/).
- **Deferred (recorded limitation):** A5 — preferred-frame precision-bound consistency still owed.
- **Contested → standing dissent:** C4 — the major-revision-vs-reject split, preserved as [dispute-002](resolution/dispute-002-significance.md), not averaged away.
