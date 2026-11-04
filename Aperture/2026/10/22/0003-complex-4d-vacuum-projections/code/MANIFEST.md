# Computation & Figure Manifest — Article 0003

**Last Revised Date:** November 4, 2026 · **Revision:** Stage-02 v2.0

This directory contains the reproducible figure-generation scripts and figures for the Stage-02 revised manuscript ([`../02-first-revision-and-review/manuscript-revised-2026-11-02.md`](../02-first-revision-and-review/manuscript-revised-2026-11-02.md)).

| File | Role / Section Illustrated | Dependencies | Runs? | Safety |
|---|---|---|---|---|
| [`generate_feynman_peaks_troughs_diagram.py`](generate_feynman_peaks_troughs_diagram.py) | Generates [`fig_v2_1_feynman_arrows_peaks_troughs_two_slit.png`](fig_v2_1_feynman_arrows_peaks_troughs_two_slit.png) (**Figure 1** in §4.1): Superposition of Feynman's path arrows $e^{iS/\hbar}$ on the wave peaks ($\Phi = 0^\circ, \uparrow$) and wave troughs ($\Phi = 180^\circ, \downarrow$) for two straight least-action paths ($\delta S = 0$) from Slit 1 and two from Slit 2 vs. curved non-least-action paths (`C1, C2`, $\delta S \neq 0$). | `numpy`, `matplotlib` | ✅ (~2 s) | **SAFE** |
| [`generate_feynman_action_rarity_diagram.py`](generate_feynman_action_rarity_diagram.py) | Generates [`fig_v2_2_feynman_action_curve_and_path_rarity.png`](fig_v2_2_feynman_action_curve_and_path_rarity.png) (**Figure 2** in §4.1): Calculated action parabola $\Delta S(h)/\hbar \propto h^2$, Cornu spiral $\int e^{iS(h)/\hbar}\,dh$, 1st Fresnel stationary-action tube, and $1/h^2$ suppression of curved non-least-action paths. | `numpy`, `scipy`, `matplotlib` | ✅ (~2 s) | **SAFE** |
| [`generate_feynman_diagram_wave_comparison.py`](generate_feynman_diagram_wave_comparison.py) | Generates [`fig_v2_3_feynman_diagram_to_wave_peaks_troughs.png`](fig_v2_3_feynman_diagram_to_wave_peaks_troughs.png) (**Figure 3** in §5.1): Translation of a QED Feynman diagram into equations and 3D wave peak ($\uparrow$) and trough ($\downarrow$) interference, illustrating Feynman's 1949 analytic-Fourier / human-calculator shortcut vs. computer FFT wavefront + force-carrier martingale calculation. | `numpy`, `matplotlib` | ✅ (~2 s) | **SAFE** |
| [`fig_v2_1_feynman_arrows_peaks_troughs_two_slit.png`](fig_v2_1_feynman_arrows_peaks_troughs_two_slit.png) | Figure 1 PNG embedded in `02-first-revision-and-review/manuscript-revised-2026-11-02.md` | — | Image | **SAFE** |
| [`fig_v2_2_feynman_action_curve_and_path_rarity.png`](fig_v2_2_feynman_action_curve_and_path_rarity.png) | Figure 2 PNG embedded in `02-first-revision-and-review/manuscript-revised-2026-11-02.md` | — | Image | **SAFE** |
| [`fig_v2_3_feynman_diagram_to_wave_peaks_troughs.png`](fig_v2_3_feynman_diagram_to_wave_peaks_troughs.png) | Figure 3 PNG embedded in `02-first-revision-and-review/manuscript-revised-2026-11-02.md` | — | Image | **SAFE** |
