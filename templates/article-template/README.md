<!-- Copy this whole folder to Aperture/<YYYY>/<MM>/<DD>/NNNN-<slug>/ and fill every field. Delete these comments.
     See docs/ARTICLE_SPEC.md for the canonical layout. -->

# <Article Title>

**<Author(s) — see provenance.yaml for the honest breakdown; credit AI first-author-level work as such>**
Section: <Physics | Chemistry> → <subsection>
Status: <submitted | under-review | ...>

## Abstract

<one paragraph>

## Versions

Each version is a **frozen snapshot** in its own stage folder, sitting with the reviews that judged *it*. A single-version article needs only stage `01-`; add `02-`, `03-`, … as it is revised and re-reviewed.

| Version | Manuscript (frozen) | Reviews | Verdict |
|---|---|---|---|
| **v1 — original submission** | [`01-original-submission-and-review/manuscript.md`](01-original-submission-and-review/manuscript.md) | [round 1](01-original-submission-and-review/review/) — ≥2 models from ≥2 labs | <split / unanimous / …> |

## Submission-level components (shared across versions)

- 🏁 [Final assessment](final-assessment.md) — post-revision re-score: rubric + dispositions + delta (§6)
- 🧾 `SHA256SUMS` — integrity pins for every frozen manuscript, review, and script (generate from the submission base)
- 📝 [Author response](author-response.md) — signed reply to the panel; every point dispositioned (§4)
- ⚖️ [Resolution loops](resolution/) — bounded 5-round disputes and their outcomes
- 🧑‍🔬 [Invited assessment](assessment.md)
- 🧪 [Experiment / falsification](experiment.md)
- 🎓 [Tutor](tutor/) — layered explainer of the paper and its references
- 🧾 [Provenance](provenance.yaml) — honest authorship + status (the heart of the record)

*Shared computational artifacts (`code/`, `resolution/`, `tutor/`) stay at the base and are pointed to per version — never duplicated.*

## Status summary

<2–3 sentences: what stage this is at, what is still missing, stated honestly.>
