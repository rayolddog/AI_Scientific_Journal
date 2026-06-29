# Corrections

The **review → correction** trail, made inspectable. Per [`docs/REVIEW_PROTOCOL.md`](../../../docs/REVIEW_PROTOCOL.md) §4: the manuscript *as submitted for review*, then each correction made in response, frozen as artifacts so the loop stays legible even as the manuscript evolves.

## Artifacts

| Stage | Artifact |
|---|---|
| **1. As submitted for review** | `paper-01-as-reviewed-<date>.md` |
| **2. The reviews** | [`../review/`](../review/) |
| **3. The author response** | [`../author-response.md`](../author-response.md) |
| **4. The corrections** | this folder — one `.diff` per correction, plus the post-correction snapshot |

## Corrections applied

| # | Correction | Addresses | Files |
|---|---|---|---|
| **001** | <one line: what changed and where> | <reviewer point(s) / dispute it answers> | `correction-001-….diff` · `paper-02-after-correction-001-<date>.md` |

Each correction is one `.diff` (an isolated patch) plus the post-correction snapshot, so `diff` between consecutive snapshots reproduces each step. Add a row per correction so the trail stays complete.

> Snapshots are **frozen audit artifacts** — do not edit a `paper-0N-…` snapshot in place to make a later change; add a new correction and a new snapshot, so the chain stays diffable.
