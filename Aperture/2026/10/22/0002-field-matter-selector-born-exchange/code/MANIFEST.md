# Computation Manifest — Article 0002

**Last Revised Date:** October 24, 2026 · **Timestamp:** `2026-10-24T22:50:00-06:00` · **Revision:** 2.1

The runnable event-by-event microsimulation scripts and data files behind both **Stage 01** ([`../01-original-submission-and-review/manuscript.md`](../01-original-submission-and-review/manuscript.md)) and **Stage 02** ([`../02-first-revision-and-review/manuscript-revised-2026-10-24.md`](../02-first-revision-and-review/manuscript-revised-2026-10-24.md)) of Article 0002, bundled so every numerical claim across both versions can be **reproduced directly from this article folder**.

Every program here is **safety-reviewed** ([`SAFETY_REVIEW.md`](SAFETY_REVIEW.md)) and **checksum-pinned** in the article's root [`../SHA256SUMS`](../SHA256SUMS).

## Stage-02 Verification & Atom-Resolved Microsimulation Suite (Current Revision v2.1 — 2026-10-24)

| File | Role / Claim Verified | Dependencies | Runs? | Safety |
|---|---|---|---|---|
| [`run_stage02_verification.py`](run_stage02_verification.py) | Complete Stage-02 baseline verification suite: exact boundary stopping (`absorb_tol = 1.0`, zero clipping, zero timeouts), weighted nonlinear least-squares power-law fit $P_1(S; p)$ and $\chi^2_{\text{Born}}$, Kimura–Ohta (1969) $N$-site fixation-time verification ($N=2,4,10$), full 10-site lumped disclosure at $\theta=1.0, 0.72, 0.45$, and genuine event-by-event Monte Carlo generation for Stage-02 Figures 1–3 (`fig_v2_1_*.png`, `fig_v2_2_*.png`, `fig_v2_3_*.png`). Strictly portable relative paths (`pathlib.Path`). | `numpy`, `scipy`, `matplotlib`, `json`, `pathlib` | ✅ (~8 s) | **SAFE** |
| [`stage02_verification_results.json`](stage02_verification_results.json) | Frozen JSON output of `run_stage02_verification.py` (exact numbers in Stage-02 Tables 1, 2, and 3) | — | Data file | **SAFE** |
| [`run_atom_by_atom_aperture.py`](run_atom_by_atom_aperture.py) | Atom-by-atom pre-modulus phase-coupled microsimulation (`M1=10`, `M2=10` individual atoms across 9 angles at $\theta=1.0, 0.72, 0.45$, plus 50/50 bright-fringe resolution test at $\theta=0.45$). Verifies pre-modulus 3-way phase coupling ($\phi^{\text{inc}}_m, \phi^{\text{vac}}_m, \phi^{\text{det}}_m$) and shows that resolving an aperture into individual atoms keeps $s_m(0) \sim S/M_1 \ll \theta$, eliminating the lumped backward-ODE obstruction ($\chi^2_{\text{Born}} = 5.59, p_{\text{val}} = 0.7801$ at $\theta=0.72$ with $\tilde{\epsilon}_{\text{vac}}=0$; $\chi^2_{\text{Born}} = 8.52, p_{\text{val}} = 0.4826$ at $\theta=0.45$). | `numpy`, `scipy`, `json`, `pathlib` | ✅ (~6 s) | **SAFE** |
| [`atom_by_atom_aperture_results.json`](atom_by_atom_aperture_results.json) | Frozen JSON output of `run_atom_by_atom_aperture.py` (exact numbers in Stage-02 §2.3, §4.3, Table 1, and Table 2) | — | Data file | **SAFE** |
| [`run_crystal_lattice_simulation.py`](run_crystal_lattice_simulation.py) | 2D condensed-matter crystal lattice microsimulation ($4\times 4 = 16$ lattice sites per detector patch, $N=32$ atoms total) with coherent Bloch wavevector $\phi^{\text{inc}}(\mathbf{r}_m) = \phi_0 + \mathbf{k}\cdot\mathbf{r}_m$, von Mises surface-conditioned quantum vacuum phases ($\kappa_{\text{surf}} \in \{0, 2.5, 6.0\}$), and nearest-neighbor tight-binding exciton hopping ($\theta=0.72$ and $\theta=0.45$). | `numpy`, `scipy`, `json`, `pathlib` | ✅ (~8 s) | **SAFE** |
| [`crystal_lattice_results.json`](crystal_lattice_results.json) | Frozen JSON output of `run_crystal_lattice_simulation.py` (exact numbers in Stage-02 §2.3, §4.3, Table 1, and Table 2) | — | Data file | **SAFE** |

## Stage-01 Historical Scripts & Data (Frozen as Reviewed in Round 1 — 2026-10-22)

> **Immutability Note:** The Stage-01 scripts and JSON outputs below are preserved **byte-for-byte** as inspected by Reviewers A, B, and C during Round-1 review. Note that as documented in Reviewer A Minor #2 and Reviewer C Major #11, the historical Stage-01 scripts contain hardcoded output paths into `/Users/john-bramble/.gemini/antigravity/scratch/selector_verification/`; use [`run_stage02_verification.py`](run_stage02_verification.py) for portable standalone execution.

| File | Role / Claim Verified (Stage 01) | Dependencies | Safety |
|---|---|---|---|
| [`run_tests.py`](run_tests.py) | Stage-01 initial 6-test comparison suite (`results.json`) | `numpy`, `json` | **SAFE-WITH-NOTES** (hardcoded output path) |
| [`run_detailed_analysis.py`](run_detailed_analysis.py) | Stage-01 9-angle and 10-site suite (`detailed_results.json`, `absorb_tol = 0.995`) | `numpy`, `matplotlib`, `json` | **SAFE-WITH-NOTES** (sets `MPLCONFIGDIR=/tmp/mplconfig`, hardcoded output path) |
| [`generate_clean_figures.py`](generate_clean_figures.py) | Stage-01 Figures 1 and 2 (`fig_clean_1_trajectories_and_born.png`, `fig_clean_2_vacuum_and_10site.png`) | `numpy`, `matplotlib`, `json` | **SAFE-WITH-NOTES** (hardcoded paths) |
| [`generate_paper_figures.py`](generate_paper_figures.py) | Stage-01 Figure 3 (`fig3_experimental_discriminators.png` — contained constructed points replaced in Stage 02) | `numpy`, `matplotlib`, `json` | **SAFE-WITH-NOTES** (hardcoded paths) |
| [`results.json`](results.json) | Frozen Stage-01 JSON output of `run_tests.py` | — | **SAFE** |
| [`detailed_results.json`](detailed_results.json) | Frozen Stage-01 JSON output of `run_detailed_analysis.py` | — | **SAFE** |

## Reproduce Stage 02 from Scratch

```bash
pip install numpy scipy matplotlib
cd Aperture/2026/10/22/0002-field-matter-selector-born-exchange/code
python3 run_stage02_verification.py
```
