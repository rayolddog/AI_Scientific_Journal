# v3 — current revision (2026-06-30) · review pending

Manuscript: [`manuscript-second-revision-06-30-2026.md`](manuscript-second-revision-06-30-2026.md). This is the **standing current version** of Article 0001. It **has not yet been re-reviewed** — the round-2 reports stand on [version 2](../02-first-revision-and-review/), which is what those referees actually saw.

## What changed, and why

This revision answers the **decisive round-2 objection**. In round 2, GPT-5.5 ([`round2-reviewer-C-gpt-5.5.md`](../02-first-revision-and-review/review/round2-reviewer-C-gpt-5.5.md)) showed that the previous Appendix D's unconditional Lindblad dynamics give a *decaying* Bloch radius — the state tends to the maximally mixed state, **not** to two distinct pointer states — so it did not derive a bistable measurement attractor.

The rewrite (route (a)):

- **Withdraws** the unconditional-Lindblad "locked phase = outcome" claim.
- **Replaces** it with an explicit **conditional quantum-trajectory** calculation: the pointer is realigned to the einselected/QND $\sigma_z$ axis, so the unconditional state is a *mixture* of the two pointer states (weights $|\alpha|^2, |\beta|^2$), and a single **monitored** run purifies to a definite, Born-weighted pole.
- **Presents Born as consistent, not derived** — the weight enters via the standard unraveling (the second horn of §3.3/§8). The detector-bridge and outcome-selection problems are **conceded open**.
- **Softens** the matching in-text claim (§3.6) and the abstract to match.

The supporting numerics are [`../resolution/precession_radius_two_zeros.py`](../resolution/precession_radius_two_zeros.py) (run, safety-reviewed, checksum-pinned) — the full-density-matrix check GPT-5.5's round-2 report asked for.

## Standing / owed

- **Re-review owed.** No round-3 reports yet. Until then, the standing verdict is round 2's **unanimous major-revision**, judged against v2.
- **Reconciled downstream** (2026-06-30, *rescoped not retracted*): the [dispute-002 retirement path](../resolution/dispute-002-retirement-path.md) — K_eff and the cut location now sit in the manuscript; the SNIC exponents become the T6 *prediction* rather than a banked claim.
- The **final assessment** ([`../final-assessment.md`](../final-assessment.md)) is anchored to the reviewed version and is **not** auto re-scored against this revision; readers judge v3 against the standing round-2 review.

Per [`docs/REVIEW_PROTOCOL.md`](../../../../../../docs/REVIEW_PROTOCOL.md), a revision postdating the reviews it responds to does not alter those verbatim reports; the round-2 findings remain marked against v2 (disposition `revised-pending-rereview`), not "fixed."
