# Article Specification

Every article is a directory under `articles/`, named `NNNN-<slug>/` (four-digit zero-padded id, then a short hyphenated slug). It contains the following.

## Required files

```
articles/NNNN-<slug>/
├── README.md          Article front page: title, byline, abstract, status, links to every component below.
├── paper.md           The work itself — or, if the manuscript is canonical elsewhere, the abstract + a clear pointer to the source.
├── provenance.yaml    Honest authorship + review + status metadata. MANDATORY. The heart of the journal.
├── review/            Reviewer reports (≥2 models, ≥2 labs) + a README index. See REVIEW_PROTOCOL.md.
├── resolution/        One file per disputed claim sent through the bounded resolution loop + a README index.
├── assessment.md      The invited human expert's signed assessment (or the open invitation while pending).
├── experiment.md      The invited experimentalist's standing call: what test would verify/falsify the claim, its status, the result when in.
└── tutor/             The recursive tutor: a layered explainer of the paper AND its cited references.
```

A `paper.pdf` may accompany or replace `paper.md`. Figures/data live in subfolders as needed.

## `provenance.yaml` schema

This is the journal's defining artifact. It records *who did what* and *what state the article is in*, honestly.

```yaml
article_id: "NNNN"
slug: <hyphenated-slug>
title: <full title>
section: <Physics | Biology | Chemistry | Healthcare | Economics | Philosophy>
subsection: <disciplinary subsection>
status: <submitted | under-review | revision | published | standing-dissent | retracted>
date_submitted: YYYY-MM-DD

authors:
  - name: <name>
    type: <human | ai>
    provider: <for ai: the lab; for human: omit>
    affiliation: <for human>
    roles: [<conception, formalization, numerical-verification, prose-drafting, validation, editorial, ...>]
    corresponding: <true | false>     # humans only; accountability anchor
    byline_note: <free text — e.g. "would be co-first author under honest-authorship policy">

review:
  panel:
    - reviewer: <model name>
      provider: <lab>
      report: review/<file>.md
      recommendation: <accept | minor-revision | major-revision | out-of-scope | reject>
      date: YYYY-MM-DD
  decorrelation_met: <true | false>    # are there ≥2 reviewers from ≥2 labs?
  rubric_scores:                        # 1–5; null until scored. Record per-reviewer in their report.
    novelty: <n | null>
    internal_consistency: <n | null>
    evidential_grounding: <n | null>
    reproducibility: <n | null>
    citation_integrity: <n | null>
  resolution_loops:
    - dispute: resolution/<file>.md
      status: <pending | accepted | withdrawn | standing-dissent>

assessment:
  invited_assessor: <name | null>
  status: <awaiting-invitation | invited | received | declined>
  file: assessment.md

experiment:
  status: <open-call | committed | in-progress | result-in>
  file: experiment.md
  tests: [<short ids>]

tutor:
  entry: tutor/index.md

source:                                 # if the manuscript is canonical elsewhere
  canonical_manuscript: <filename or title>
  source_repository: <url>

provenance_meta:
  record_created: YYYY-MM-DD
  created_with: <model that scaffolded this record>
```

## Status values

| Status | Meaning |
|---|---|
| `submitted` | In the repo, review not yet started. |
| `under-review` | Panel review in progress. |
| `revision` | A critique was accepted; authors are revising. |
| `published` | Review complete (decorrelation met), assessment in, status stable. |
| `standing-dissent` | Carries at least one unresolved dispute, published as such. |
| `retracted` | Withdrawn; the record and the reason stay visible. Retractions are counted, not erased. |

## The rule behind the spec

If a field would be embarrassing to fill in honestly — "only one lab reviewed this," "Born measure not derived," "assessor not yet invited" — **fill it in honestly anyway.** The embarrassing-but-true entry is the product. A journal that hides its gaps is just a slower version of the thing this one replaces.
