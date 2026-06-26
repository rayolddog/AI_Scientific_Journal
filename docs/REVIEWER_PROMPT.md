# Reviewer Prompt — paste this to each panel model

This is the standard instruction handed to every model on a review panel, so reports come back consistent with [`REVIEW_PROTOCOL.md`](REVIEW_PROTOCOL.md) and drop straight into an article's `review/` folder. **Run it on a model from a different lab than the existing reviewer(s)** — that is the whole point (decorrelation).

> **Attach or paste the current manuscript** (for Article 0001: `PAPER_REVISED.md`, "Two Regimes of the Chiral Mass Coupling") along with the prompt below.

---

You are acting as a **critical peer reviewer** for a foundations-of-physics / interpretation venue. Review the attached manuscript. Be a skeptic: your job is to find what is wrong or unsupported, not to encourage.

**Open with a standing-and-limitations note.** State plainly that you are a language model, which labels you (name, provider, version) and what you *can* assess reliably (internal logic, where claims outrun their support, consistency against itself and against textbook QM/QFT) versus what you *cannot* certify (specialist-level correctness of any one-loop QFT; novelty against the complete literature). Weight your report accordingly.

**Then provide, in this order:**

1. **Recommendation** — one of: accept / minor revision / major revision / out-of-scope-for-this-venue / reject — and a one-line **venue note** (which kind of journal this fits).
2. **Summary (to fix terms)** — 1 short paragraph restating the manuscript's core claim in your own words, so the author can see how you read it.
3. **Strengths** — only genuine ones worth preserving.
4. **Major concerns** — numbered. For each: the specific claim, why it fails or is unsupported, and what would fix it. Default toward refutation; press hardest where a specialist would.
5. **Minor / presentational.**
6. **Specific questions for the author.**
7. **Rubric scores (1–5, with one line of justification each):**
   - **Novelty** — what precisely is new (result / mechanism / re-description / ontology), and is the novelty claim accurate?
   - **Internal consistency**
   - **Evidential grounding** — what ties it to anything outside the text?
   - **Reproducibility**
   - **Citation integrity** — are cited sources real, correctly characterized, load-bearing?
8. **Sign-off** — `Reviewer: <model name> (<provider>, <version>), <date>`.

Output as Markdown. Do not soften conclusions to be agreeable; a refuted objection is still useful information.

---

## What to do with each returned report

1. Save it as `articles/0001-dirac-kuramoto-many-clocks/review/reviewer-B-<model>.md` (then `reviewer-C-…`, etc.). Paste a one-line **provenance header** at the top: model, provider, version, date, and that it is reproduced verbatim.
2. In that article's `provenance.yaml`:
   - add the reviewer to `review.panel`,
   - fill `review.rubric_scores` (or record per-reviewer scores in each report),
   - once you have **≥2 reviewers from ≥2 labs**, set `decorrelation_met: true`.
3. Update `review/README.md` (the table + decorrelation line) and `articles/README.md` (the index "Decorrelation" column).
4. If the new reviewer disagrees with Fable 5 (or with the author) on a load-bearing point, that is a candidate for the **bounded resolution loop** — open a `resolution/dispute-NNN-….md`.

## Running dispute-001 as a real cross-lab loop

With models from two or more labs available, [`dispute-001`](../articles/0001-dirac-kuramoto-many-clocks/resolution/dispute-001-born-basin-measure.md) (can the synchronization dynamics yield |α|² weights?) can be run as an actual ≤5-round exchange: give each model the others' previous-round response, instruct each round to *narrow* to the load-bearing claim, and stop at convergence or round 5. Record the transcript and the outcome (accepted / withdrawn / standing dissent) in that file.
