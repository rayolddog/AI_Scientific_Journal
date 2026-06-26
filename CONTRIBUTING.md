# Contributing / Submitting an Article

> **This is a demonstration repository — a model, not a live journal.** "Submitting an article" below means contributing an *example* to this blueprint so others can see the format. It does **not** submit your work to any publication venue, and nothing here is published to an external journal. See the [README headline](README.md).

This repository is a public blueprint, and contribution happens in the open. There are two things you can do: **add an example article**, or **challenge an existing one**.

## Challenge an existing article (the open-review mechanism)

This is the published-adversarial-review pillar, implemented with the tools GitHub already gives us:

- **Open an Issue** to raise an objection to a paper, a review, an assessment, or a provenance record. State the specific claim and why you think it fails. Objections that are later refuted stay on the record — a failed critique is still information about what was checked.
- **Open a Pull Request** to propose a concrete correction, an added reference explanation in a tutor, or a second-lab review.

Every challenge and rebuttal is versioned and timestamped. Nothing is thrown away.

## Submit a new article

1. **Copy `templates/article-template/`** to `articles/NNNN-<slug>/`, choosing the next free four-digit id and a short hyphenated slug.
2. **Fill in the components** per [`docs/ARTICLE_SPEC.md`](docs/ARTICLE_SPEC.md):
   - `paper.md` (or a pointer to the canonical manuscript) — the work itself.
   - `provenance.yaml` — honest authorship, including every model used and each human's role. **This is mandatory and is the heart of the journal.**
   - `tutor/` — at minimum a layered explainer of the paper and its key references.
3. **Open a Pull Request.** The review process ([`docs/REVIEW_PROTOCOL.md`](docs/REVIEW_PROTOCOL.md)) then runs against your submission.

## The two non-negotiables

1. **Honest provenance.** Understating a model's contribution, or overstating a human's, defeats the entire purpose. The byline is a measurement, not a courtesy.
2. **Scope discipline.** Say plainly what the work does *not* establish. In an AI-native venue where plausible text is free, the candor about limitations is the scarce, valuable signal.

## Authorship policy (what makes this journal different)

Authorship may be **AI, human, or any mix**, and the byline says so. An AI that did first-author-level work is named as such in `provenance.yaml`. There is no policy here that forces a dishonest byline — which is the wall that motivated this venture in the first place (see [`docs/MANIFESTO.md`](docs/MANIFESTO.md) §2).

Accountability is preserved separately: a **named human maintainer or corresponding author** bears responsibility for each article, and the invited human assessor (Pillar III) attaches a reputation to its assessment. Honest credit and clear accountability are different axes; this journal keeps both.
