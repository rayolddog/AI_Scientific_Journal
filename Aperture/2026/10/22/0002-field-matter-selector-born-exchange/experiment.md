# Experiment / Falsification — Standing Call (Article 0002)

**Status:** `open-call`  
**Last Revised Date:** October 22, 2026 · **Timestamp:** `2026-10-22T22:20:00-06:00` · **Revision:** 1.0

> *Bell wrote the inequality; Aspect built the apparatus.* A theoretical claim is a **postulate** until a laboratory with equipment tries to refute it. This file is a standing public invitation to experimental quantum optics and single-photon detector groups to test the falsifiable discriminators of Article 0002.

## What Would Verify or Falsify the Central Claims

Standard quantum mechanics predicts that for any local POVM, the unconditional click fraction in Port $A$ of a heralded single-photon beam splitter with splitting ratio $S \in (0, 1)$ is strictly linear in $S$ ($P_A(S \mid \text{herald}) = \eta_A S$), independent of the internal radiative correlation length of Port $A$ vs. Port $B$, and independent of the ratio $\theta = E_{\text{gap}}/\hbar\omega$ in continuum semiconductor/superconducting absorbers. By contrast, the conserving complex-interference selector makes three concrete, falsifiable predictions:

| Test | Observable | Predicted Signature | Apparatus / Regime | Status |
|---|---|---|---|---|
| **E1** | Heralded single-photon click probability $P_A(S \mid \text{herald})$ across 9 beam-splitter ratios $S \in [0.1, 0.9]$ | **Quadratic port-mismatch bow:** $P_A(S \mid \text{herald}) = \eta_A S + \kappa S(1 - S)$ with $\kappa < 0$ when Port $A$ is a sub-wavelength cold-atom array ($d < \lambda \implies c_A > 0$) paired against an uncorrelated absorber Port $B$ ($c_B \approx 0$) | Sub-wavelength 2D optical-lattice atomic mirror [Rui et al. 2020; Srakaew et al. 2023] in Port $A$ vs. standard SPAD/SNSPD in Port $B$; $10^6$ heralded photon trials per $S$ | `open-call` |
| **E2** | Fitted Born exponent $p$ and S-curve residual $\Delta P_1(S) = P_1(S) - S$ vs. bandgap ratio $\theta = E_{\text{gap}}/\hbar\omega$ | **Threshold-gating S-curve modulation:** tuning photon energy $\hbar\omega$ relative to $E_{\text{gap}}$ shifts the competition between sub-threshold gating ($\theta < 1$, bright-favored $p > 2$) and the non-random vacuum cross-term drift $\tilde{\epsilon}_{\text{vac}}\sqrt{s_1 s_2}(\sqrt{s_2} - \sqrt{s_1})$ | Wavelength-tunable heralded single-photon source illuminating cryogenic semiconductor SPADs or superconducting nanowire detectors near the gap edge $\theta \in [0.60, 0.98]$ | `open-call` |
| **E3** | Mean single-photon detection latency $\mathbb{E}[\tau_{\text{game}}(S)]$ vs. splitting ratio $S$ | **Shannon-entropy latency profile:** $\mathbb{E}[\tau_{\text{game}}(S)] = -\frac{2}{\sigma^2}[S\ln S + (1-S)\ln(1-S)]$, peaking at equal splitting $S = 0.50$ and decreasing toward $S \to 0, 1$ | Picosecond time-correlated single-photon counting (TCSPC) with sub-picosecond jitter SNSPDs across variable beam-splitter ratio $S$ | `open-call` |

## How to Commit

Any laboratory able to run **E1**, **E2**, or **E3** is invited to open an Issue or Pull Request committing to the test, with a protocol and timeline. Confirming, refuting, or null results publish here as part of the article's permanent record.
