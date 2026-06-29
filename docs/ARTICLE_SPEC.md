# Article Specification

Every article is a directory under `articles/`, named `NNNN-<slug>/` (four-digit zero-padded id, then a short hyphenated slug). It contains the following.

## Required files

```
articles/NNNN-<slug>/
├── README.md          Article front page: title, byline, abstract, status, links to every component below.
├── paper.md           The work itself — or, if the manuscript is canonical elsewhere, the abstract + a clear pointer to the source.
├── provenance.yaml    Honest authorship + review + status metadata. MANDATORY. The heart of the journal.
├── review/            Reviewer reports (≥2 models, ≥2 labs) + a README index. See REVIEW_PROTOCOL.md §2–§3.
├── author-response.md The authors' signed reply to the panel — accepted / contested / deferred, per point. See REVIEW_PROTOCOL.md §4.
├── corrections/       Numbered review→correction diffs + post-correction snapshots + a README index.
├── resolution/        One file per disputed claim sent through the bounded resolution loop + a README index. See REVIEW_PROTOCOL.md §5.
├── final-assessment.md Post-revision re-scoring: rubric on the final artifact + dispute dispositions + initial→final delta. See REVIEW_PROTOCOL.md §6.
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
section: <Physics | Chemistry>          # Phase-1 scope. Human-subjects fields are out of scope (see README & REVIEW_PROTOCOL.md §1.1); other non-human-subjects fields are a documented future expansion.
subsection: <disciplinary subsection>
status: <submitted | under-review | revision | published | standing-dissent | retracted | screening-halted | safety-rejected>
date_submitted: YYYY-MM-DD

screening:                              # §1 intake gate — runs before any AI review; auditable
  safety_check: <passed | rejected>    # §1.1 dangerous-capability exclusion
  injection_scan: <passed | flagged | halted>   # §1.2 prompt-injection screening
  adjudicated_by: <human maintainer — required for any non-"passed" result>
  notes: <date; what was found (quoted inert; never reproduce dangerous content); the disposition>

authors:
  - name: <name>
    type: <human | ai>
    provider: <for ai: the lab; for human: omit>
    affiliation: <for human>
    roles: [<conception, formalization, numerical-verification, prose-drafting, validation, editorial, ...>]
    author_position: <co-first | first | second | ... | contributing>   # honest CREDIT (human or AI). An AI may be co-first or sole author. Independent of accountability.
    byline_note: <free text — e.g. "co-first author; source manuscript lists the human solo only to satisfy an external venue that bars AI authorship">

accountable_sponsor:                  # REQUIRED — the human who answers for the article. Accountability, NOT authorship.
  name: <human name>                  # for a human-authored paper, usually also an author; for an AI-solo paper, a non-author anchor
  affiliation: <…>
  is_author: <true | false>          # false when authorship is AI-solo — credit and responsibility have come apart, by design

review:
  panel:
    - reviewer: <model name>
      provider: <lab>
      report: review/<file>.md
      recommendation: <accept | minor-revision | major-revision | out-of-scope | reject>
      overall_assessment: <0–5 integer | null>   # coarse holistic score = the RANKING value (§3/§6); no decimals
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

author_response:                        # §4 — the authors' signed reply; every reviewer point dispositioned
  file: author-response.md
  status: <pending | published>

final_assessment:                       # §6 — post-revision re-score; a vector, never averaged
  file: final-assessment.md
  status: <pending | complete>
  fresh_decorrelated_reviewer: <true | false>   # did ≥1 lab not on the original panel re-score the final artifact?
  ranking: <0–5 integer | null>         # the published ranking — coarse overall on the final (or, for a clean pass, the initial) artifact; per-reviewer spread kept, not averaged
  clean_pass: <true | false>            # true = passed initial review with no recommended revisions → §4–§5 not required, initial overall is the ranking

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
