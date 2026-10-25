# Experiment / Falsification — Standing Call (Article 0003)

**Status:** `open-call`  
**Last Revised Date:** October 22, 2026 · **Timestamp:** `2026-10-22T22:15:00-06:00` · **Revision:** 2.7

> *Bell wrote the inequality; Aspect built the apparatus.* A theoretical claim is a **postulate** until a laboratory or observational collaboration tries to refute it. This file is a standing public invitation to test the falsifiable discriminators of Article 0003.

## What Would Verify or Falsify the Central Claims

Article 0003 models $3+1\text{D}$ Lorentzian spacetime as a real phase-locked slice of a complexified $\mathbb{C}^4$ two-spinor vacuum with imaginary coordinate fluctuations $y^a = \text{Im}(z^a)$ gapped at $M_{\text{Pl}}$ and internal chiral Zitterbewegung rotations occurring in the complex plane. Four experimental/observational discriminators test this framework:

| Test | Observable | Predicted Signature | Apparatus / Regime | Status |
|---|---|---|---|---|
| **P1** | Energy-dependent photon group velocity $\Delta v_g(E)/c$ in astrophysical gamma-ray bursts | **Quadratic Planck-scale dispersion:** $\omega^2 = c^2 k^2\big[1 - \xi(\hbar\omega / M_{\text{Pl}}c^2)^2\big]$ from virtual excitation of the gapped imaginary fiber $y^a$, with zero linear ($E/M_{\text{Pl}}$) LIV term | Fermi-LAT / CTA time-of-flight observations of TeV gamma-ray flares from high-redshift blazars and GRBs | `open-call` |
| **P2** | Sub-period interferometric visibility modulation in Dirac Zitterbewegung quantum simulators | **Phase-holonomy beats at $\omega_{\text{ZB}} = 2m_{\text{eff}}c_{\text{eff}}^2/\hbar$:** periodic visibility dips at odd half-multiples of $T_{\text{ZB}}$ when the unprojected imaginary velocity component $\dot{y}_{\text{ZB}}(t) = -c_{\text{eff}}\sin(\omega_{\text{ZB}}t)$ ismaximal | Trapped-ion (`40Ca+`) or ultracold-atom spin-orbit-coupled Dirac simulators [Gerritsma et al. 2010] with sub-cycle Ramsey phase readout | `open-call` |
| **P3** | Heralded single-photon click probability $P_A(S \mid \text{herald})$ in a cooperative vs. incoherent detector pair | **Quadratic Born-rule bow:** $P_A(S \mid \text{herald}) = \eta_A S + \kappa S(1-S)$ ($\kappa < 0$) when Port $A$ has sub-wavelength radiative phase correlation ($d < \lambda$) | Sub-wavelength 2D optical-lattice cold-atom mirror in Port $A$ paired against a standard SPAD/SNSPD in Port $B$ | `open-call` |
| **P4** | Cosmic birefringence and vacuum Cherenkov bounds on condensate phase gradients $\partial_\mu \Theta_0$ | **Constraint $\lvert\partial_\mu \Theta_0\rvert \lesssim 10^{-42}\text{ GeV}$:** any residual spatial/temporal gradient of the chiral condensate phase $\Theta_0$ induces a Carroll–Field–Jackiw Chern–Simons term rotating CMB polarization | Planck, ACT, Simons Observatory, and LiteBIRD CMB $EB$ polarization cross-spectra | `open-call` |

## How to Commit

Any laboratory or observational group able to run **P1–P4** is invited to open an Issue or Pull Request committing to the test, with a protocol and timeline.
