# Reviews — Article 0001

Panel review per [`docs/REVIEW_PROTOCOL.md`](../../../docs/REVIEW_PROTOCOL.md). **Requirement: ≥2 reviewers from ≥2 different labs.**

| Reviewer | Provider / lab | Recommendation | Report |
|---|---|---|---|
| **Fable 5** | Anthropic | Major revision (foundations venue) | [reviewer-A-fable5.md](reviewer-A-fable5.md) |
| **Gemini 3.1 Pro** | Google DeepMind | Major revision (four major concerns) | [reviewer-B-gemini-3.1-pro.md](reviewer-B-gemini-3.1-pro.md) |
| **GPT-5.5 Thinking** | OpenAI | **Reject** (speculative-foundations venue at best) | [reviewer-C-gpt-5.5.md](reviewer-C-gpt-5.5.md) |

## Decorrelation status: ✅ MET (3 labs)

Three reviewers from three different foundation-model families are now on record: **Fable 5** (Anthropic), **Gemini 3.1 Pro** (Google DeepMind), and **GPT-5.5 Thinking** (OpenAI). This satisfies the **≥2 reviewers from ≥2 labs** requirement with margin.

The decorrelation payoff is now sharp on two axes:

- **Convergence on the diagnosis.** All three labs, reviewing **independently**, land on the *same* load-bearing gap — whether the synchronization/locking dynamics can carry the Born weights, or instead predicts the *wrong* statistics. They reach it from different directions: Fable 5 via the **basin measure** of the Adler model; Gemini via the **chirality of the measurement coupling** (§3.7 — EM is non-demolition for position but not for the chiral scalar $\bar\psi\psi$); GPT-5.5 via the same two routes *plus* a sharper demand that the **Adler equation itself be derived** from a specified system–bath model rather than inserted. Three decorrelated families on one gap is strong evidence it is real.
- **Divergence on the verdict.** Recommendations **split**: two *major revision* (Fable 5, Gemini — fixable, foundations venue) versus one *reject* (GPT-5.5 — "not advanced beyond decoherence-plus-unspecified-hidden-variable"). This is the panel behaving exactly as designed: a **ranking, not a binary**, with the disagreement kept legible rather than averaged away. The substantive convergence was sent through [dispute-001](../resolution/dispute-001-born-basin-measure.md) and **resolved by calculation** (run 2026-06-25): the dynamics give 50/50, not |α|² — critique **accepted**, with a **standing dissent** on significance that locates the major-revision-vs-reject split precisely.

## On the reviews

All three are **genuine, unedited AI referee reports** produced at the author's request — dropped in verbatim, which is itself the demonstration: AI review cheap enough to publish in full.

- **Fable 5 (Anthropic), 2026-06-12** — **major revision** for a foundations/interpretation venue; judges the manuscript "serious, scholarly… not crankish," presses hardest on the Born-statistics question. A slightly earlier snapshot (limited revisions since), major concerns still standing.
- **Gemini 3.1 Pro (Google DeepMind), 2026-06-25** — **major revision**; four major concerns: equivariance / Born-weight preservation (§3.7), gauge-pathology of the $H'$ postulate (§6.2), explicit-vs-spontaneous symmetry breaking (§8), the sub-quantum H-theorem leap (§8). Verbatim excerpt (sections 4–6; 1–3 not captured — noted in the file header).
- **GPT-5.5 Thinking (OpenAI), 2026-06-25** — **reject** (harshest of the three); a complete report (sections 1–8, with rubric scores). Independently calls the §3.7 chiral-channel self-critique "largely devastating," and adds the demand that the **Adler/Kuramoto reduction be derived from a microscopic Hamiltonian/Lindblad** rather than asserted. Rubric: Novelty 2, Internal-consistency 2, Evidential-grounding 2, Reproducibility 1, Citation-integrity 3.
