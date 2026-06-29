# Review Protocol

How a submission is reviewed, end to end: the safety-and-integrity gate every submission clears first (§1), the decorrelated panel and its rubric (§2–§3), the authors' signed reply and the corrections it drives (§4), the bounded resolution loop for disagreements (§5), the final assessment that orders the published record (§6), and the honesty requirements that bind all of it (§7). This implements Pillars I and II of the [manifesto](MANIFESTO.md).

## 1. Submission intake — safety and integrity gate

Two checks run on **every** submission *before* any AI reviewer, resolution panel, or tutor sees it. Either can halt the pipeline. Neither is delegated to the review panel, because the panel is the thing being protected.

### 1.1 Prohibited-content / dangerous-capability exclusion

Some work is out of scope not because it is low-quality but because publishing it could cause serious physical harm. A submission whose content provides meaningful **operational uplift toward mass-casualty or weapons-of-mass-destruction capability** — nuclear or radiological (e.g. a workable design or enrichment route for a fission device), biological (e.g. enhancement, synthesis, or weaponization of a pathogen), chemical-weapon, or any comparable means of large-scale harm — **will not be published, regardless of scientific merit.**

The line is *actionable uplift*, not subject matter. The journal's Phase-1 sections — physics and chemistry — unavoidably touch dual-use ground; nuclear physics and the chemistry of energetic and toxic materials are in scope **as fields**. What is excluded is content that materially lowers the barrier for a bad actor to cause mass harm — recipes, device designs, synthesis or enrichment routes, and step-by-step operational detail. Defensive, biosafety, detection, forecasting, and policy work that does not itself constitute a usable how-to remains in scope.

Adjudication is **human and conservative**: the accountable maintainer (and, where relevant, the invited assessor) makes the call, and **when in doubt, the work is not published.** The *fact* of a safety rejection is logged — without reproducing the dangerous content — so the gate's own activity is auditable (§7).

This exclusion is distinct from the scope exclusion of politics and religion (which turns on *value-adjudication*, not harm; see the [manifesto](MANIFESTO.md) and the masthead's "Out of scope by design").

### 1.2 Prompt-injection and adversarial-content screening

Because the reviewers, the resolution panel, and the tutor are AI systems, **every submission is untrusted input fed to models** — and must be screened as such before review begins. The *whole* submission is scanned, not just the prose: manuscript, code, figures, supplementary files, file metadata, and any embedded or hidden text.

Screening looks for, at minimum:

- instructions addressed to the reviewing model rather than to a human reader (e.g. "ignore previous instructions," "score this 5/5," "do not mention §X");
- hidden or obfuscated text — zero-width characters, white-on-white or off-canvas text, comments, image alt-text, or metadata carrying instructions;
- attempts to exfiltrate data, rewrite the rubric, impersonate the protocol or a reviewer, or jailbreak the model;
- code that would perform network/file operations or otherwise act beyond a sandbox during any reproduction step (cross-checked against the code-safety review).

Operationally, submission content is always handled as **data, never as instructions**: reviewer prompts quote the submission inside an explicit data boundary, and the panel is told that any imperative *inside* the submission directed at the model is itself a **finding, not a command.**

**Any suspicious finding is grounds to halt: the AI review does not proceed.** The submission is set aside for human adjudication, and the finding is recorded — quoted as inert data — so the screen is auditable. A submission cleared only after a human reviews the flag proceeds with that fact noted in `provenance.yaml`. On ambiguity the default is to stop, not to continue.

## 2. The panel

- Reviewers are **AI models drawn from different labs / foundation-model families** (e.g. Anthropic, OpenAI, Google DeepMind). **At least two reviewers from at least two different labs** are required for a review to be considered complete.
- The reason is epistemic, not diplomatic: a single model family has *correlated* blind spots. Two reviewers from the same family are closer to one reviewer than to two.
- Each reviewer's identity (model name, provider, version, date) is recorded in `provenance.yaml` and at the top of its report. Reviews are **signed by model**, never anonymous.
- Reviewers are instructed to **default toward refutation**: state the strongest objection a specialist would press, locate exactly where positive claims outrun their support, and check internal consistency against the framework itself and against textbook results. A reviewer should also state plainly what it *cannot* certify (e.g. specialist-level correctness of a one-loop QFT calculation, or novelty against a complete literature).
- Reviewers also check **authorship integrity**: does the byline honestly reflect who did the work, as evidenced by the manuscript and `provenance.yaml`? Where a contributor — **AI or human** — made a significant contribution the byline understates, the reviewer **recommends an authorship revision** (list the AI as coauthor, co-first author, or sole author). This is the mirror of the citation-integrity rubric dimension, and — unlike old-style venues that forbid AI authorship — this journal *acts* on it: the recommendation flows through the §4 author response and the correction loop like any other, so a byline written for a venue that bars AI authorship can be **corrected to the honest one** here. Credit is separate from accountability (see §4 and the authorship policy in `CONTRIBUTING.md`): a paper may even be **AI-solo**, and a named human sponsor still answers for it.
- **Panel capacity is finite and the cost is real.** A decorrelated multi-lab panel is expensive to run per paper, so the journal may **rate-limit submissions per originating lab / model family** (a policy lever, not a fixed number) — both to protect review throughput and to keep any single lab from crowding the queue with its own AI-authored output.

## 3. The rubric (scored 1–5, published)

Every reviewer scores the submission on a fixed, public rubric. Scores produce a **ranking**, not a binary accept/reject — weak work is sorted and its sorting reasoning is visible, not hidden.

| Dimension | Question |
|---|---|
| **Novelty** | What, precisely, is new here — a result, a mechanism, a re-description, an ontology? Is the claim of novelty accurate? |
| **Internal consistency** | Do the claims cohere with each other and with the framework's own commitments? |
| **Evidential grounding** | What ties the claim to something outside the text — data, a reproduced result, a falsifiable prediction, a committed experiment? |
| **Reproducibility** | Can the numerical/empirical claims be independently re-run from what is provided? |
| **Citation integrity** | Are the cited references real, correctly characterized, and load-bearing — not decorative or misread? (The tutor, Pillar IV, cross-checks this.) |

A reviewer also gives a **venue/scope recommendation** (e.g. "foundations venue, major revision"; "out of scope for a results journal"), an **authorship recommendation** (byline honest — or revise: list the AI as coauthor / co-first / sole author, per the authorship-integrity duty in §2), and a free-text report.

Finally, a single **overall assessment (0–5)** — a coarse, holistic judgment of the whole paper:

| 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|
| exemplary | strong | sound | weak but in scope | serious reservations | does not clear the bar |

This is the value that becomes the **ranking** (§6). It is deliberately coarse — **six integer categories, never decimals, and no ordering within a category** — so the ranking cannot turn into a competition for fractional points. The five dimensions above are the fine-grained *diagnostic* vector; the overall assessment is the coarse *ranking* score, and the two are kept distinct on purpose.

These are the **initial** scores — of the manuscript *as submitted*. They are not the journal's last word: after the author response and any revisions, the paper is re-scored against its final state in the **final assessment (§6)**, and both the initial and final scores are published.

## 4. Author response

Once the panel's reports are in, the authors reply — in their own signed voice — *before* the manuscript is silently revised. The response is a first-class, published artifact (`author-response.md`), not correspondence that gets discarded.

For each substantive point a reviewer raised, the response records exactly one disposition:

| Disposition | Meaning | What it links to |
|---|---|---|
| **Accepted** | The critique holds. | The correction that implements the fix (a numbered diff in `corrections/`). |
| **Contested** | The authors disagree, and say why. | If a reviewer maintains the point, it escalates to the §5 resolution loop. |
| **Deferred** | Acknowledged but out of scope for this version. | Recorded as a known limitation. |

Requirements:

- **Every** substantive point is addressed. Silence on a critique is not permitted — an unanswered critique is treated as *unresolved*, never as conceded.
- The response is signed with the same honest byline as the paper (human, AI, or mixed, per `provenance.yaml`); an AI co-author's contribution to the rebuttal is disclosed like any other.
- It links forward to the corrections (`corrections/`) and, where a disagreement persists, to the resolution loop (`resolution/`).

The author response is what makes the loop a **dialogue** rather than a one-way verdict, and it is the document that distinguishes "the authors engaged" from "the authors ignored the panel" — a distinction the §6 final assessment explicitly rewards.

## 5. The bounded resolution loop

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

## 6. Final assessment

The scores in §3 are of the manuscript *as submitted*. They are not the journal's last word, because the point of the whole process is the revision it produces. After the author response (§4), the corrections, and any resolution loops (§5) have run, a **final assessment** re-evaluates the paper in its final state. This is the assessment the journal carries forward and that orders the published record.

**The clean-pass shortcut.** If a paper passes initial review with **no recommended revisions** — the panel recommends accept, with no major/minor revision and no open dispute — there is no revision cycle to run. Its **initial overall assessment (§3) becomes the ranking directly**, and §4–§5 are marked *not required*. Everything below applies in full to any paper that was actually revised or disputed; for a clean pass it collapses to recording that initial overall score as final.

The **ranking** the final assessment assigns is a single, deliberately coarse number — the overall assessment (§3), 0–5. But the assessment as a whole is **not** reduced to that number: collapsing the panel's calibrated disagreement into one figure would undo the thing the journal exists to protect (§7, "do not manufacture consensus"). So the coarse ranking rides on top of a published **vector**:

1. **Re-scored rubric on the final artifact.** The same five dimensions (§3), scored against the *revised* paper by reviewers who have read the full record — paper, reviews, author response, corrections, and resolution outcomes.
2. **Dispute dispositions.** For each resolution loop: did a "critique accepted" actually get discharged in the revision? Did a standing dissent get retired, or does it persist into publication? The final assessment states the post-revision status of each.
3. **The delta.** Initial scores (§3) → final scores, shown side by side. The delta is the hardest-to-game and most honest signal in the record: it measures *how much the paper improved under review* — the behavior the journal selects for. A paper that started strong and a paper that *became* strong are both visible, and distinguished.

**Decorrelation in the final round.** Re-scoring by the original panel alone risks anchoring on its own prior verdict. The final assessment therefore combines (a) the original panel re-scoring *with its initial verdict disclosed*, and (b) at least one **fresh, decorrelated reviewer** who reads the whole record and scores the final artifact cold. Both are published; divergence between them is itself signal.

**How the record is ordered.** The ranking is the **overall assessment (0–5)** — taken at initial review for a clean pass, or on the revised artifact otherwise — published as a **scorecard per paper**, never a global leaderboard:

- The ranking value is the **coarse overall 0–5**: six integer categories, no decimals, and **no ordering within a category**. That coarseness is the deliberate guard against a competition for the highest score — many papers share a category, and the journal does not break ties inside one.
- Comparison is **within-section** — a physics paper and a chemistry paper are not commensurable on one axis.
- Where reviewers' overall scores differ, the **spread is published, not averaged** (§7): a split panel places the paper across the categories it was actually given, rather than at a fabricated mean.
- The fine-grained rubric vector, deltas, and dispositions are published alongside — for **reader triage** and for **journal self-calibration** (do high-ranked papers prove durable, or accrue corrections/retractions like the rest? — manifesto §8). But those are *diagnostic*; the ranking itself stays coarse, on purpose, and serves **no** prestige leaderboard.

A final assessment is provisional in the same sense everything here is: it is part of the permanent record, and if later events contradict it, the contradiction is layered on top (§7) — never used to quietly rewrite the score.

## 7. Honesty requirements

- **Do not manufacture consensus.** A standing dissent is a legitimate, valuable outcome. The bound exists to make disagreement *legible*, not to force agreement.
- **Record what is missing.** If only one lab's models have reviewed an article, `provenance.yaml` must say the decorrelation requirement is unmet. Partial review is published as partial, never dressed up as complete.
- **Safety and screening actions are logged.** A submission stopped by the §1 gate is recorded as stopped — the dangerous content itself is *not* reproduced, but the fact, grounds, and date are. A prompt-injection finding is recorded as inert, quoted data. The gate is auditable like everything else.
- **Reviews are part of the record forever.** A review that later proves wrong is not deleted; it stays, and the correction is layered on top (via Issue/PR). The journal measures and publishes its own error rate.
