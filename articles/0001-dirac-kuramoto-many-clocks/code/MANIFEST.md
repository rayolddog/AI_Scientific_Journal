# Computation — Article 0001

The article's runnable calculations, bundled so the contested claims can be **reproduced from the journal folder alone** — directly addressing the reproducibility dimension (GPT-5.5 scored it **1/5**).

Two kinds of program live in this article:
- **Journal-generated** — written during the adversarial-review loops (in [`../resolution/`](../resolution/)): they *settle* disputes.
- **Author verification (frozen)** — copied byte-for-byte from the source repository, limited to the scripts behind the **contested** claims. The rest of the paper's code is **not** mirrored here (to avoid drift) — it stays in the source repo; see "Not bundled" below.

Every program here is **safety-reviewed** ([`SAFETY_REVIEW.md`](SAFETY_REVIEW.md)) and **checksum-pinned** ([`SHA256SUMS`](SHA256SUMS)).

## Programs

| Program | Backs which claim | Origin | Runs? (2026-06-25) | Safety | sha256 |
|---|---|---|---|---|---|
| `born_weights_check.py` | Born **not derived** — trajectories give 0.852/0.148 ≈ Born 0.85/0.15, but basin volume is **50/50** and \|α\|² enters only via the noise (dispute-001) | source `code/` | ✅ (~100 s) | SAFE | `aa2ff1cf3bea` |
| `finite_time_weights.py` | finite-time / attractor-strength does **not** rescue Born; predicts small falsifiable deviations (dispute-001) | source `code/` | ✅ | SAFE | `6c52cbf97301` |
| `phi_dissipative_check.py` | the `sin 2φ` second harmonic survives the dissipative reduction → bistable 0/π pointer (§3.7 / RESULTS_PHASE_DISSIPATIVE) | source `code/` | ✅ (writes fig) | SAFE | `cdbcaf6c0c46` |
| `kuramoto_sync.py` | Kuramoto/Adler phase-lock of the internal clock to a bulk reference (the core mechanism) | source `tests/` | ✅ (writes fig) | SAFE | `829a609616f5` |
| `../resolution/dispute-001-basin-measure.py` | the bounded-loop calc that resolved dispute-001 (basin measure = 50/50, flat in \|α\|²) | journal-generated | ✅ (~4 s) | SAFE-w/-notes | `2c38c87bec7b` |
| `../resolution/dispute-002-partI-Keff.py` | **K_eff = 4χ²n̄/κ** derived from the transmon+readout model; SNIC exponent ½ (T6 Part I) | journal-generated | ✅ (~10 s) | SAFE-w/-notes | `923dc0f108f1` |

"Runs?" = I executed it in this folder on 2026-06-25 and it exited 0. Figures (`*.png`) are regenerated on run and are **not** checksummed (matplotlib output is not bit-reproducible); only the source programs are pinned.

## Integrity — verify before running
```
# from the article root:
shasum -a 256 -c code/SHA256SUMS     # every line must say OK
```
A failing line means the program differs from the safety-reviewed, as-recorded version — do not trust the safety review for it until re-reviewed.

## Reproduce
```
pip install numpy scipy matplotlib       # the only dependencies
python3 code/born_weights_check.py        # ~100 s; prints the Born verdict
python3 code/finite_time_weights.py       # fast
python3 code/phi_dissipative_check.py     # writes phi_dissipative_check.png
python3 code/kuramoto_sync.py             # writes kuramoto_sync.png
python3 resolution/dispute-001-basin-measure.py
python3 resolution/dispute-002-partI-Keff.py
```

## Not bundled (by design)
The paper's full numerical suite — emergent-fields derivations (`honeycomb_emergence.py`, `weyl3d_emergence.py`, `statistics_emergence.py`), the wider Born/noise studies, the hardware/Qiskit experiment scripts, etc. — remains in the **source repository** (`code/`, `tests/`) and is pointed to from [`../provenance.yaml`](../provenance.yaml), not copied here. Only the scripts behind the *disputed* claims are frozen into this folder; if a future dispute leans on another script, freeze it here the same way (copy byte-for-byte → run → safety-review → add to `SHA256SUMS` and the table above).

*Assembled 2026-06-25 by Claude Opus 4.8. Programs frozen byte-for-byte from the source repo; independent safety review by a separate Claude agent; nothing committed or pushed without the author's instruction.*
