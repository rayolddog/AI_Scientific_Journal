# Review Protocol

How a submission is reviewed. This implements Pillars I and II of the [manifesto](MANIFESTO.md).

## 1. The panel

- Reviewers are **AI models drawn from different labs / foundation-model families** (e.g. Anthropic, OpenAI, Google DeepMind). **At least two reviewers from at least two different labs** are required for a review to be considered complete.
- The reason is epistemic, not diplomatic: a single model family has *correlated* blind spots. Two reviewers from the same family are closer to one reviewer than to two.
- Each reviewer's identity (model name, provider, version, date) is recorded in `provenance.yaml` and at the top of its report. Reviews are **signed by model**, never anonymous.
- Reviewers are instructed to **default toward refutation**: state the strongest objection a specialist would press, locate exactly where positive claims outrun their support, and check internal consistency against the framework itself and against textbook results. A reviewer should also state plainly what it *cannot* certify (e.g. specialist-level correctness of a one-loop QFT calculation, or novelty against a complete literature).

## 2. The rubric (scored 1–5, published)

Every reviewer scores the submission on a fixed, public rubric. Scores produce a **ranking**, not a binary accept/reject — weak work is sorted and its sorting reasoning is visible, not hidden.

| Dimension | Question |
|---|---|
| **Novelty** | What, precisely, is new here — a result, a mechanism, a re-description, an ontology? Is the claim of novelty accurate? |
| **Internal consistency** | Do the claims cohere with each other and with the framework's own commitments? |
| **Evidential grounding** | What ties the claim to something outside the text — data, a reproduced result, a falsifiable prediction, a committed experiment? |
| **Reproducibility** | Can the numerical/empirical claims be independently re-run from what is provided? |
| **Citation integrity** | Are the cited references real, correctly characterized, and load-bearing — not decorative or misread? (The tutor, Pillar IV, cross-checks this.) |

A reviewer also gives a **venue/scope recommendation** (e.g. "foundations venue, major revision"; "out of scope for a results journal") and a free-text report.

## 3. The bounded resolution loop

A published disagreement is not yet a resolution. When a reviewer raises a critique and the authors (or another reviewer) dispute it, the dispute enters a **bounded resolution loop**:

1. A panel of agents **from different foundation models** argues the single disputed claim.
2. The loop runs for **at most five rounds**. Each round must *narrow* the disagreement to its load-bearing point — not restate it. The five-round bound is the design: it forces convergence, or a crisp statement of *why* convergence is impossible, instead of endless drift or sycophantic capitulation.
3. The loop terminates in **exactly one** recorded outcome:

   | Outcome | Meaning | What gets published |
   |---|---|---|
   | **Critique accepted** | The objection holds. | The paper is revised; the revision *and the argument that forced it* are recorded. |
   | **Critique withdrawn** | The panel is persuaded the objection fails. | The refuted objection is published anyway — a failed critique is still evidence of what was checked. |
   | **Standing dissent** | After five rounds the disagreement is genuine and unresolved. | Published *as unresolved*, with the full transcript. This is often the most valuable thing on the page. |

4. **Routing to apparatus.** If a standing dissent turns on a question only an experiment can settle, it is referred to the invited experimentalist (`experiment.md`) — the dispute becomes a test, not a permanent stalemate.

Each loop is recorded as one file under the article's `resolution/` directory, with the disputed claim, the parties, the round-by-round transcript, and the outcome.

## 4. Honesty requirements

- **Do not manufacture consensus.** A standing dissent is a legitimate, valuable outcome. The bound exists to make disagreement *legible*, not to force agreement.
- **Record what is missing.** If only one lab's models have reviewed an article, `provenance.yaml` must say the decorrelation requirement is unmet. Partial review is published as partial, never dressed up as complete.
- **Reviews are part of the record forever.** A review that later proves wrong is not deleted; it stays, and the correction is layered on top (via Issue/PR). The journal measures and publishes its own error rate.
