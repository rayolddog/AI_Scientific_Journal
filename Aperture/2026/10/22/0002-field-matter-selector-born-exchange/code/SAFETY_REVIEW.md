# Code Safety Review — Article 0002 Programs

**Last Revised Date:** October 24, 2026 · **Timestamp:** `2026-10-24T22:50:00-06:00` · **Revision:** 2.1  
**Scope:** *Safety to run on a host machine* — **not** scientific correctness (which is evaluated by the decorrelated peer-review panel).  
**Integrity:** Certifies the exact bytes pinned in [`../SHA256SUMS`](../SHA256SUMS).

## Per-File Assessment

| File | Verdict | Imports / Side Effects | Notes |
|---|---|---|---|
| [`run_stage02_verification.py`](run_stage02_verification.py) | **SAFE** | `pathlib`, `json`, `numpy`, `scipy.optimize`, `scipy.stats`, `matplotlib` (`Agg` backend); writes `stage02_verification_results.json` and `fig_v2_1_*.png`..`fig_v2_3_*.png` strictly inside `code/` via `Path(__file__).resolve().parent` | Bounded Monte Carlo loops ($N_{\text{trials}} = 20{,}000$); portable relative paths; no environment variable mutation, network, or shell access. |
| [`run_atom_by_atom_aperture.py`](run_atom_by_atom_aperture.py) | **SAFE** | `pathlib`, `json`, `numpy`, `scipy.optimize`, `scipy.stats`; writes `atom_by_atom_aperture_results.json` strictly inside `code/` via `Path(__file__).resolve().parent` | Bounded Monte Carlo loops ($N_{\text{trials}} = 10{,}000$); portable relative paths; no environment variable mutation, network, or shell access. |
| [`run_crystal_lattice_simulation.py`](run_crystal_lattice_simulation.py) | **SAFE** | `pathlib`, `json`, `numpy`, `scipy.optimize`, `scipy.stats`; writes `crystal_lattice_results.json` strictly inside `code/` via `Path(__file__).resolve().parent` | Bounded Monte Carlo loops ($N_{\text{trials}} = 8{,}000$); portable relative paths; no environment variable mutation, network, or shell access. |
| [`run_tests.py`](run_tests.py) *(Stage-01 frozen)* | **SAFE-WITH-NOTES** | `numpy`, `matplotlib.pyplot`, `json`; writes to `/Users/john-bramble/.gemini/antigravity/scratch/selector_verification/results.json` | Preserved byte-for-byte from Stage 01. Contains hardcoded author scratch path (noted by Reviewers A and C). |
| [`run_detailed_analysis.py`](run_detailed_analysis.py) *(Stage-01 frozen)* | **SAFE-WITH-NOTES** | `os`, `numpy`, `matplotlib.pyplot`, `json`; sets `os.environ["MPLCONFIGDIR"] = "/tmp/mplconfig"` and writes to hardcoded author scratch/brain paths | Preserved byte-for-byte from Stage 01. Mutates `MPLCONFIGDIR` to `/tmp/mplconfig` and writes to hardcoded absolute paths (noted by Reviewer C Major #11). |
| [`generate_clean_figures.py`](generate_clean_figures.py) *(Stage-01 frozen)* | **SAFE-WITH-NOTES** | `os`, `json`, `numpy`, `matplotlib.pyplot`; sets `MPLCONFIGDIR=/tmp/mplconfig` and reads/writes hardcoded author paths | Preserved byte-for-byte from Stage 01. |
| [`generate_paper_figures.py`](generate_paper_figures.py) *(Stage-01 frozen)* | **SAFE-WITH-NOTES** | `os`, `json`, `numpy`, `matplotlib.pyplot`; sets `MPLCONFIGDIR=/tmp/mplconfig` and reads/writes hardcoded author paths | Preserved byte-for-byte from Stage 01. |

## Overall Verdict: **SAFE** (Stage-02 suite) / **SAFE-WITH-NOTES** (Stage-01 frozen scripts)

None of the scripts perform network activity, subprocess execution, shell invocation, `eval`/`exec`, `pickle`, or file deletion. In response to Reviewer C Major #11, the Stage-01 scripts are accurately classified as `SAFE-WITH-NOTES` (due to `os.environ["MPLCONFIGDIR"] = "/tmp/mplconfig"` and hardcoded absolute paths), while the Stage-02 script [`run_stage02_verification.py`](run_stage02_verification.py) uses strictly portable `pathlib.Path(__file__).resolve().parent` paths and makes zero `os.environ` modifications.
