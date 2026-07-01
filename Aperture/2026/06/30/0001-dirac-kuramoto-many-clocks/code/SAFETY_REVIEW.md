# Code Safety Review — Article 0001 programs

**Scope:** *safety to run on a host machine* — **not** scientific correctness (that is the reviewers' and the resolution loops' job).
**Reviewer:** an independent AI agent (Claude, Anthropic), run as a dedicated code-safety pass on 2026-06-25, separate from the agent that assembled this folder. The 7th program, `resolution/precession_radius_two_zeros.py`, was added and reviewed on 2026-06-30 by a *separate* independent Claude agent (same single-lab caveat as below).
**Integrity:** this review certifies the exact bytes pinned in [`SHA256SUMS`](SHA256SUMS). If a checksum no longer matches, this review no longer applies — re-run it.

## Per-file assessment

| File | Verdict | Imports / side-effects | Notes |
|------|---------|------------------------|-------|
| `born_weights_check.py` | **SAFE** | `numpy` only; stdout only (no file writes) | 4000-trajectory Python loop × ~3000 steps — merely slow (~100 s here), bounded, not a DoS. |
| `finite_time_weights.py` | **SAFE** | `numpy` only; stdout only | Vectorized 40000-trajectory × 5000-step sim; modest bounded memory. |
| `phi_dissipative_check.py` | **SAFE** | `numpy` + `matplotlib` (Agg); stdout + one `savefig` to its own dir | matplotlib import wrapped in try/except; figure path pinned to script directory; bounded loops. |
| `kuramoto_sync.py` | **SAFE** | `numpy`, `pathlib`, `matplotlib` (Agg), `scipy.integrate`; stdout + one `savefig` to script dir | `plt.show()` present but is a no-op under Agg; path pinned to resolved script dir. |
| `resolution/dispute-001-basin-measure.py` | **SAFE-WITH-NOTES** | `numpy` + optional `matplotlib` (Agg); stdout + one `savefig` (relative filename) | Figure written to the **current working directory** via a fixed, benign filename (no traversal). Bounded vectorized RK4. |
| `resolution/dispute-002-partI-Keff.py` | **SAFE-WITH-NOTES** | `numpy`, `scipy.linalg`/`integrate`; optional `matplotlib` (Agg); stdout + one `savefig` (relative filename) | Same relative-figure note. Contains an `assert` (raises, never spawns). `eig`/`expm` on ≤28×28 matrices — trivial. |
| `resolution/precession_radius_two_zeros.py` | **SAFE-WITH-NOTES** | `numpy` + `matplotlib` (pyplot); stdout + one `savefig` (relative filename) | Same relative-figure note. No `plt.show()` (savefig only), so the backend is immaterial. Bounded Euler / Euler–Maruyama loops (20k steps × 400-ensemble, ~3 s, sub-MB); fixed seed `default_rng(7)`; no network/subprocess/eval/pickle/env/deletion. Reviewed 2026-06-30. |

## Overall verdict: **SAFE**

All seven scripts are safe to run. They are self-contained numerical-physics simulations whose only imports are `numpy`, `scipy`, `matplotlib` (non-interactive — either forced to the `Agg` backend or `savefig`-only with no `plt.show()`), and `pathlib`; their only side effects are printing to stdout and, in five cases, writing a single `.png` figure named after the script. There is **no** network, subprocess, shell, `eval`/`exec`, pickle, environment/credential, or filesystem-deletion activity anywhere, and no path traversal or unbounded/infinite loops — the heaviest scripts are merely slow (bounded Monte-Carlo loops), not denial-of-service risks. The only minor note: the three `resolution/` scripts write their figure to the current working directory via a relative filename rather than pinning it to the script's own directory; this is benign.

## Honesty note (decorrelation)

This is a **single AI safety reviewer, Claude-family** — the same caveat the article's scientific [reviews](../01-original-submission-and-review/review/) carry. For a safety pass matching the journal's decorrelation pillar, a second review from a different-lab model could be added here (the scripts are short; a few minutes each). The checksum file makes that cheap to do later against the exact same bytes.

## Re-verify before running
```
# from the article root:
shasum -a 256 -c code/SHA256SUMS    # must print OK for every file
```
If every line says `OK`, the programs are byte-identical to what this review covered.
