# Contributing / Submitting an Article

> **This is a demonstration repository — a model, not a live journal.** "Submitting an article" below means contributing an *example* to this blueprint so others can see the format. It does **not** submit your work to any publication venue, and nothing here is published to an external journal. See the [README headline](README.md).

This repository is a public blueprint, and contribution happens in the open. There are two things you can do: **add an example article**, or **challenge an existing one**.

## Scope & safety (read before submitting)

- **Phase-1 fields: Physics and Chemistry only.** The narrowing is deliberate — see the [README "Sections"](README.md#sections). Other fields are a documented future expansion, not a permanent exclusion.
- **No human-subjects work for now.** Clinical, interventional, and identifiable-human-data research is out of scope until a real human-ethics apparatus (IRB, consent, registration, privacy) exists. The journal's publish-fast/correct-fast engine assumes errors are cheap to correct; in clinical medicine they are not.
- **No dangerous-capability content.** Work providing operational uplift toward mass-casualty or weapons-of-mass-destruction capability will not be published, regardless of merit.
- **Every submission is screened first.** Before any AI review, a submission clears a **safety-and-injection intake gate** ([`docs/REVIEW_PROTOCOL.md`](docs/REVIEW_PROTOCOL.md) §1): a dangerous-capability check, and a prompt-injection scan (because the reviewers are AI, your submission is untrusted model input). Anything in a submission addressed to the reviewing model is treated as a *finding*, not an instruction. A suspicious finding halts the AI review pending human adjudication.
- **Submissions may be rate-limited per lab.** A decorrelated multi-lab AI panel is expensive to run per paper, so the journal may cap how many submissions it takes from a single originating lab / model family — to protect review throughput and keep one lab from crowding the queue with its own AI-authored output (a policy lever; see [`docs/REVIEW_PROTOCOL.md`](docs/REVIEW_PROTOCOL.md) §2).

## Challenge an existing article (the open-review mechanism)

This is the published-adversarial-review pillar, implemented with the tools GitHub already gives us:

- **Open an Issue** to raise an objection to a paper, a review, an assessment, or a provenance record. State the specific claim and why you think it fails. Objections that are later refuted stay on the record — a failed critique is still information about what was checked.
- **Open a Pull Request** to propose a concrete correction, an added reference explanation in a tutor, or a second-lab review.

Every challenge and rebuttal is versioned and timestamped. Nothing is thrown away.

## Submit a new article

1. **Copy `templates/article-template/`** to `Aperture/<YYYY>/<MM>/<DD>/NNNN-<slug>/`, choosing the next free four-digit id and a short hyphenated slug (filed archive-style by date under the `Aperture/` journal instance).
2. **Fill in the components** per [`docs/ARTICLE_SPEC.md`](docs/ARTICLE_SPEC.md):
   - the manuscript in `01-original-submission-and-review/` (or a pointer to the canonical source) — the work itself.
   - `provenance.yaml` — honest authorship, including every model used and each human's role. **This is mandatory and is the heart of the journal.**
   - `tutor/` — at minimum a layered explainer of the paper and its key references.
3. **Open a Pull Request.** The review process ([`docs/REVIEW_PROTOCOL.md`](docs/REVIEW_PROTOCOL.md)) then runs against your submission.

## The two non-negotiables

1. **Honest provenance.** Understating a model's contribution, or overstating a human's, defeats the entire purpose. The byline is a measurement, not a courtesy.
2. **Scope discipline.** Say plainly what the work does *not* establish. In an AI-native venue where plausible text is free, the candor about limitations is the scarce, valuable signal.

## Authorship policy (what makes this journal different)

Authorship may be **AI, human, or any mix — including an AI as co-first author or as sole author**, and the byline says so. An AI that did first-author-level work is named as such in `provenance.yaml`. There is no policy here that forces a dishonest byline — the wall that motivated this venture (see [`docs/MANIFESTO.md`](docs/MANIFESTO.md) §2).

The **review panel enforces this**, it isn't left to the authors' goodwill: a reviewer who finds the byline understates a significant contribution — AI or human — **recommends an authorship revision**, which is then applied through the normal response→correction loop (see [`docs/REVIEW_PROTOCOL.md`](docs/REVIEW_PROTOCOL.md) §2–§4). So a paper written for an old-style venue that forbids AI authorship can have its byline **corrected to the honest one** when it enters this journal.

**Credit and accountability are separate axes, and the journal keeps both.** Authorship is *credit* — it goes where the work was done, AI or human. Accountability is *responsibility* — every article, **including an AI-solo one**, names a **human accountable sponsor** (the corresponding/maintainer role) who answers for it. For an AI-solo paper that human is *not* an author; they are the accountability anchor. The invited human assessor (Pillar III) additionally attaches a reputation to the article's assessment.
