# Round 1 — original manuscript

Panel review of the **original submission** ([`../paper-01-as-reviewed-2026-06-25.md`](../paper-01-as-reviewed-2026-06-25.md)) per [`docs/REVIEW_PROTOCOL.md`](../../../../../../../docs/REVIEW_PROTOCOL.md). **Requirement: ≥2 reviewers from ≥2 different labs.** Round 2 (the revised manuscript) is in [`../../02-first-revision-and-review/review/`](../../02-first-revision-and-review/review/).

| Reviewer | Provider / lab | Recommendation | Report |
|---|---|---|---|
| **Fable 5** | Anthropic | Major revision (foundations venue) | [reviewer-A-fable5.md](reviewer-A-fable5.md) |
| **Gemini 3.1 Pro** | Google DeepMind | Major revision (four major concerns) | [reviewer-B-gemini-3.1-pro.md](reviewer-B-gemini-3.1-pro.md) |
| **GPT-5.5 Thinking** | OpenAI | **Reject** (speculative-foundations venue at best) | [reviewer-C-gpt-5.5.md](reviewer-C-gpt-5.5.md) |

## Decorrelation status: ✅ MET (3 labs)

Three reviewers from three different foundation-model families — **Fable 5** (Anthropic), **Gemini 3.1 Pro** (Google DeepMind), **GPT-5.5 Thinking** (OpenAI) — satisfy the **≥2 reviewers from ≥2 labs** requirement with margin. The payoff is sharp on two axes:

- **Convergence on the diagnosis.** All three, reviewing **independently**, land on the *same* load-bearing gap — whether the synchronization/locking dynamics can carry the Born weights, or instead predict the *wrong* statistics. They reach it from different directions: Fable 5 via the **basin measure**; Gemini via the **chirality of the measurement coupling** (§3.7); GPT-5.5 via both *plus* a demand that the **Adler equation itself be derived**. Three decorrelated families on one gap is strong evidence it is real.
- **Divergence on the verdict.** Recommendations **split** — two *major revision* vs one *reject* — a **ranking, not a binary**, with the disagreement kept legible. The convergence was sent through [dispute-001](../../resolution/dispute-001-born-basin-measure.md) and **resolved by calculation** (run 2026-06-25): the dynamics give 50/50, not |α|² — critique **accepted**, with a **standing dissent** on significance that locates the major-revision-vs-reject split precisely.

## On the reviews

All three are **genuine, unedited AI referee reports** produced at the author's request — dropped in verbatim, which is itself the demonstration: AI review cheap enough to publish in full.

- **Fable 5 (Anthropic), 2026-06-12** — **major revision** for a foundations/interpretation venue; judges the manuscript "serious, scholarly… not crankish," presses hardest on the Born-statistics question. A slightly earlier snapshot (limited revisions since); major concerns still standing.
- **Gemini 3.1 Pro (Google DeepMind), 2026-06-25** — **major revision**; four major concerns: equivariance / Born-weight preservation (§3.7), gauge-pathology of the $H'$ postulate (§6.2), explicit-vs-spontaneous symmetry breaking (§8), the sub-quantum H-theorem leap (§8). Verbatim excerpt (sections 4–6; 1–3 not captured — noted in the file header).
- **GPT-5.5 Thinking (OpenAI), 2026-06-25** — **reject** (harshest of the three); complete report (sections 1–8, with rubric scores). Independently calls the §3.7 chiral-channel self-critique "largely devastating," and demands the **Adler/Kuramoto reduction be derived from a microscopic Hamiltonian/Lindblad**. Rubric: Novelty 2, Internal-consistency 2, Evidential-grounding 2, Reproducibility 1, Citation-integrity 3.

## Supplementary review (not a panel member)

A fourth report — **[Gemini 3.5 Flash](reviewer-supplementary-gemini-3.5-flash.md)** (Google) — was also obtained. Because it is the **same lab/family as Reviewer B**, it **does not add decorrelation**; it is recorded *supplementary*, not as a fourth panel member. Two things make it worth keeping:

- **It independently corroborates the diagnosis** — reviewing on its own, it raises the *same four* major concerns and recommends **major revision** (a fourth model on the same gaps).
- **It exposes a rubric divergence** — it scored **Reproducibility 4.5/5** (crediting the public code) where Reviewer C (GPT-5.5) scored that dimension **1/5**. Same rubric, same paper, opposite read — surfaced, not averaged. (Its other scores: Novelty 3.5, Internal-consistency 3.0, Evidential-grounding 2.0, Citation-integrity 5.0.)

## Raw export

The original raw export of the collected reviews is archived at the submission base as [`../../_raw-reviews-export-2026-06-25.rtf`](../../_raw-reviews-export-2026-06-25.rtf) (it also contains the two round-2 reports). The markdown files here are the canonical record.
