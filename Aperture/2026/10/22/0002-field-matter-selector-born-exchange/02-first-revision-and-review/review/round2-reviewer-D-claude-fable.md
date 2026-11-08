# Referee report: Argon manuscript, Revision 2.8 (with Synthesis & Phase-Memory / Whole-Quantum Addendum)

**Manuscript:** *A Field-Matter Selector for Single-Outcome Production via Pre-Modulus Phase Coupling Across Individual Aperture Atoms and a 2D Crystal Lattice*, Revision 2.8, 2026-10-31 10:35 MDT.
**Reviewer:** Claude Fable 5.1 (Anthropic), 2026-11-01. Same-family disclosure: a prior Claude model is a listed co-first author. This report was written without reference to that model's contributions and should be weighted as a same-family audit.
**Access record:** full manuscript text; all four simulation scripts named in the text; the three results JSON files; `experiment.md`; Round-2 Reviewer C report; Round-4 trio audit; the external Codex critique (`critique_Sol.md`). I did not rerun the simulation suite. One independent calculation was run (`checks/drift_bias_check.py`), followed by the 15-configuration pre-registered `tau_c` simulation suite (`tau_c_simulation/RESULTS.md`) and `03_Addendum_Phase_Memory.md` / `04_Experiment_Proposal.md`.

## 1. Verdict

**Major revision.** The manuscript contains a correct and carefully implemented neutral exchange process, a correct multi-site fixation-time identity, a useful observation about lumped-site threshold artifacts, and an unusually honest disclosure of unfavorable runs. Around that core it makes physical claims (pre-modulus phase coupling, a surface-conditioned vacuum, a QEC duality, Bell correlations from Pythagoras, early-time reversibility) that its own evidence does not support and in two cases contradicts. The Born rule enters as an initial condition and is preserved by a fairness postulate that is the Born rule restated. The compensating drift ε̃_vac breaks the martingale property the paper advertises and is tuned per configuration. The low-threshold residual bias is statistically significant once the manuscript's own replicate runs are pooled.

Scores on the protocol dimensions used by the journal:

| Dimension | Score | One-line reason |
|---|:---:|---|
| Novelty | 2/5 | Gambler's-ruin reduction is Pearle 1976/1982; atom resolution and the threshold analysis are new, the rest is not. |
| Internal consistency | 2/5 | "Martingale" vs ε̃ drift; "inert" κ_pull vs an ablation that varies with it; maximal-dephasing noise vs echo claims. |
| Evidential grounding | 1/5 | Outcome frequencies cannot discriminate any of the physical postulates (the paper's own Table 5). |
| Reproducibility | 4/5 | Code, seeds, and JSON match the tables; one checked χ² reproduces. Parameter selection after results is not documented as such. |
| Citation integrity | 3/5 | References are real (spot-checked); several are used to support claims they do not bear. |

## 2. Major findings

Each item gives the claim, the problem, the evidence, and a fix.

### M1. The Born weights are an input, and the title mechanism does not touch them

**Claim.** The abstract: a geometric interpretation of interference coupled with a martingale game "results in a distribution of single-outcome detection clicks consistent with the Born rule."

**Problem.** Postulate 1.3 normalizes the seeded weights within each patch so that Σ_{m∈r} s_m(0) ≡ S_r = Σ_{m∈r}‖A_m‖² identically. Theorem 1 then preserves S_r by Doob. The regional click probability therefore equals the regional wave intensity because it was set equal to it at t = 0 and nothing in the dynamics can change a martingale's expectation. The three-way phase coupling, the von Mises vacuum, and dominant-atom pulling affect only how S_r is distributed among the atoms of patch r.

**Evidence.** The manuscript's own ablation (Table 5): setting κ_pull = 0, κ_surf = 0, or α_seed = 0 changes P̂_patch1 by amounts within Monte Carlo noise. §2.2 item 2 proves why: the full-circle uniform phase kick added to φ_det at every step makes sgn cos Δφ an exact fair coin regardless of κ_pull or κ_surf. The paper has therefore proved that its headline physical ingredients are statistically inert at the level of the quantity it reports.

**Fix.** State the result as a conditional theorem (quadratic seed + fair exchange + vertex absorption ⇒ Born), and move the vacuum-phase story to a clearly labeled "candidate hypotheses" section whose only demonstrated effect is intra-patch tie-breaking. Retitle accordingly.

### M2. Fairness is the Born rule in disguise

**Claim.** §1.4: conservation plus conditional fairness, via Doob, "guarantees that the absorption probabilities match the initial shares."

**Problem.** True, and that is the problem. A conditionally fair exchange in energy share has fixation probabilities equal to initial shares; so postulating fairness is postulating Born. The paper gives no dynamical reason why a real detector's exchange should be fair. Every physical coupling it examines is unfair: linear unitary mixing yields an equalizing recoil (§2.2, Regime B); individual-atom threshold hazards yield a bright-favoring bias (§3.3, Tables 1 and 2); the surface-vacuum drift is an equalizing drift (M3). Fairness is restored each time by construction (recoil subtraction; ε̃ tuning).

**Evidence.** §2.2 subtracts the diagonal recoil by fiat with a one-sentence normal-ordering justification. §3.2 concedes that the de Broglie clock argument from Revision 1.0 does not supply a drift and falls back to "already has zero drift." The zero drift is an assumption of the kernel.

**Fix.** Say plainly that the model is a nonlinear stochastic reduction model in the Pearle (1976, 1982) and Adler-Brody-Brun-Hughston (2001) class, compare with those papers (both cited, neither compared), and identify the fairness postulate as the single assumption carrying the Born content.

### M3. The ε̃_vac drift contradicts the martingale claim and is tuned post hoc

**Claim.** Postulate 3.3: a "weak pairwise relative-share drift" from surface-vacuum susceptibility; §3.3: regional shares evolve as "a driftless martingale throughout the sub-threshold consolidation phase."

**Problem.** Δu_vac = ε̃ √(u(1−u)) (√(1−u) − √u) is positive for u < ½ and negative for u > ½: an equalizing drift applied to every Tier-B pair, including pairs that straddle the two ports (code: `run_crystal_lattice_simulation.py` Tier B block; `run_atom_by_atom_aperture.py` L174 onward). With ε̃ ≠ 0 the port share S_r is not a martingale. The theorem is correctly restricted to ε̃ = 0, but the abstract's θ = 0.45 results all use ε̃ > 0.

**Evidence.** (a) Independent calculation (`checks/`): for a two-site walk with σ = 0.25 the drift alone gives fitted exponents 1.950 (ε̃ = 0.005), 1.940 (0.006), 1.821 (0.018). The manuscript's own `gated_theta_072_vac_0006` run reports p̂ = 1.932. The drift is of the same order as the gating bias it cancels. (b) Values used: 0.018 (lumped θ = 0.72), 0.012 (lumped θ = 0.45, Table 2), 0.008 (5 vs 15), 0.006 (20-atom θ = 0.45), 0.005 (lattice). (c) Table 4 reports the lattice at θ = 0.45 with both ε̃ = 0.005 (χ² = 15.22) and ε̃ = 0.006 (χ² = 8.64); the text's claim of "a single fixed parameter" is undercut by its own footnote. (d) `experiment.md` E2 describes the physical prediction as a "competition" between gating and ε̃, i.e., the knob is now part of the physics.

**Fix.** Either (i) derive ε̃ from a stated surface susceptibility with explicit dependence on θ, material, and bias field, and pre-register it; or (ii) set ε̃ = 0 everywhere and report the uncompensated bias as the model's prediction, which is what E2 then falsifiably tests. Sol's exact compensating drift b_m = R s_m − r_m is the mathematically correct alternative and is nonlocal within the detector; if adopted, that nonlocality needs discussion.

### M4. The residual bias at θ = 0.45 is real and significant

**Claim.** Abstract: results at θ = 0.45 are "consistent with the Born rule," with "small residual deviations" noted.

**Problem.** The fitted-exponent CIs exclude 2 in both θ = 0.45 columns of Table 1. Table 2's 5-vs-15 configuration at ε̃ = 0 is +4.0σ. And the ablation table is a hidden replication study: rows 1 to 4 are, by the paper's own circular-convolution argument, the same distribution at the port level (rows 3 and 4 alter only intra-patch seeding), all with ε̃ = 0.005 and N = 12,000.

**Evidence.** Pooled rows 1 to 4: P̂ = 0.7080, SE = 0.0021, z = 3.84 against 0.7000. Including row 5 (ε̃ = 0, a different model) does not change the picture (z = 4.4). Sol's independent comparator reproduces the 5-vs-15 bias at 0.529 [0.519, 0.539]. The manuscript's explanation of the row 1 vs row 2 difference as "a 2.35σ Monte Carlo finite-sample fluctuation triggered by floating-point trajectory divergence" is wrong in mechanism: all six rows share `seed=7101`, and κ_pull changes the phase values pathwise (hence which trajectories see which signs) while leaving the distribution invariant. They are replicates, and replicates should be pooled, not explained away.

**Fix.** Report the pooled estimate. Replace "consistent with Born" at θ = 0.45 with "biased by +0.7 to +0.8 pp at S = 0.7 with ε̃ = 0.005." Then decide whether that is the model's prediction (E2) or a defect to be removed by a registration law that satisfies Sol's balance condition.

### M5. The phase seed is not a function on the circle

**Claim.** Postulate 1.3: the seed w_m(0) = ‖A_m‖²[1 + α cos(φ_det − ½(φ_inc + φ_vac))], "evaluated on the principal branch."

**Problem.** Adding 2π to φ_inc describes the same incident wave but flips the sign of the cosine. The quantity is not a function of the physical phases. The parenthetical defense (uniform marginal statistics are unchanged) is true and beside the point: a physical coupling must be well defined event by event. Verified at `run_atom_by_atom_aperture.py` L124 and `run_crystal_lattice_simulation.py` L166.

Also: the text calls the first-order expansion of ‖ψ_m(0)‖² "exact." Exactly, ‖1 + (α/2)e^{iχ}‖² = 1 + α cos χ + α²/4; after regional normalization this equals the first-order form with α replaced by α/(1 + α²/4). Immaterial (0.15 → 0.149) but not exact.

**Fix.** Use any integer-coefficient combination, e.g. Sol's ½[cos(φ_d − φ_i) + cos(φ_d − φ_v)], or Re[e^{i(2φ_d − φ_i − φ_v)}]. Outcome statistics will be unchanged, which is itself worth stating.

### M6. The noise model forbids the echoes the paper claims to accommodate

**Claim.** §3.1: the finite, variable fixation time "naturally accounts for" spin and photon echoes, AFC quantum memories, delayed-choice erasure, and Minev et al.'s mid-flight reversal.

**Problem.** Both simulation scripts add δη ~ U(−π, π) to every atom's phase at every step. That is the maximal-decoherence limit: no phase information survives a single step, so no rephasing protocol could ever re-emit anything. The two-timescale paragraph (inhomogeneous vs homogeneous dephasing) describes physics the model does not contain. The model also makes no quantitative prediction for echo visibility, retrieval efficiency, or the Minev reversal probability; "consistent with" here means only that both involve a finite time.

**Fix.** Either implement a finite-memory phase model (e.g. Ornstein-Uhlenbeck phases with correlation time τ_c) and compute an echo observable, or remove the reversibility claims and the associated eight citations from the abstract and §3.1.

### M7. The quantum-circuit section re-implements the classical walk and mislabels its controls

**Claim.** §4.6: a state-vector simulation shows "collapse" as continuous norm-conserving evolution with error correction OFF, reproducing Born with 100% fixation.

**Problem.** Regime C sets the pair rotation angle from u = ‖ψ_m‖²/(‖ψ_m‖² + ‖ψ_n‖²) (code L213 to 214). The gate is unitary at each step but its selection depends on the hidden state; this is the Rademacher martingale with a complex-vector container. The paper says so in the "Physical Hardware Distinction" paragraph, which then undercuts the section's framing. Regime B's angle is δϑ = ε cos Δφ (code L129), which is state-dependent too, so "state-independent linear iSWAP" is inaccurate. Regime A undoes a known sampled kick with its exact inverse; that is an oracle, not quantum error correction. The "duality with QEC" in §1.4 is a metaphor presented as a result.

**What is valuable here.** Regime B is a real negative control: genuine linear exchange plus dephasing spreads the excitation and never localizes. That is the correct physics of unitary quantum mechanics and shows that the selector's localization is produced by the state-dependent recoil subtraction, i.e. by a nonlinearity. Keep Regime B; say what it shows.

**Fix.** Rename the section "A state-vector representation of the exchange walk and a linear negative control." Drop the QEC duality or reduce it to one sentence of analogy. Sol's weak-measurement instrument (Kraus operators independent of the state) is the physically admissible benchmark if one is wanted.

### M8. The Bell derivation is circular

**Claim.** §5.2: Bell correlation and no-signaling "both follow simultaneously from Parseval/Pythagorean energy conservation."

**Problem.** §5.1 postulates the conditional law E[S_B+ | S_A+] = ½ + η(S_A+ − ½)cos 2(a − b). §5.2 then computes E(a,b) = η cos 2(a−b) from it. The Pythagorean identity contributes only the normalization of the postulated law. The fidelity η is a free parameter; S_CHSH = 2√2 η is quantum only at η = 1, which nothing in the model fixes. "Classical local hidden-variable particles can only produce a piecewise-linear correlation" is false in general: LHV models produce many correlation functions, all with S_CHSH ≤ 2. No-signaling is shown for the stated joint law at fixed settings; nothing is shown for settings changed during the walk or for timing interventions.

**Fix.** Present §5 as a postulated nonlocal conditional rule, as Sol does, and list the derivation of that rule from a joint SDE as the open problem it already is in §6.

### M9. The Bell-plus-PBR argument for necessary nonlocality is a non sequitur

**Claim.** §1.2: by Bell and PBR, "any single-world theory in which the quantum state is a real physical entity ... must be nonlocal across spacelike separation."

**Problem.** Bell's theorem implies nonlocality for any theory reproducing quantum correlations, ψ-ontic or not. PBR shows, under preparation independence, that models reproducing quantum predictions must be ψ-ontic; it adds nothing to the nonlocality conclusion. The chain as written suggests PBR strengthens the case for nonlocality, and it does not. Preparation independence is not mentioned.

**Fix.** Cite Bell alone for nonlocality; cite PBR, if at all, only for the ψ-ontic framing and name its assumption.

### M10. The fixation-time formula is correct, its attribution and its applicability are loose

**Claim.** Theorem 1 and E3: the "M-allele Kimura-Ohta (1969) formula" gives E[τ_game].

**Problem.** The identity L T = −1 with T = −(2/c_Mσ²) Σ(1−s_m)ln(1−s_m) is correct; I checked the generator calculation and Table 3 verifies it numerically for the all-to-all kernel. Two caveats. (a) Kimura and Ohta (1969) treat the fixation time of a single mutant, i.e. two alleles; the multi-allele mean absorption time is usually credited to Littler (1975), see Ewens (2004). Check the attribution. (b) Tier-A lattice bonds every third step change the generator; the lattice's mean steps (285 to 290) differ from the 20-atom aperture's (200 to 207) at the same σ. E3 as stated uses the all-to-all formula for a lattice detector, and no physical calibration of σ² per second is given, so E3 is not yet a prediction.

### M11. Statistical practice

- Non-rejection at p > 0.05 with N = 12,000 is not confirmation. The standard error at S = 0.5 is 0.46 pp, comparable to the residuals under discussion. Use ≥ 10⁵ trials per point and an equivalence margin.
- dof = 9 for χ²_Born assumes no parameter was chosen on the data. ε̃ was.
- The commitment probability per step is implemented as r_tot rather than 1 − e^{−r_tot} (both scripts). Harmless at λ = 0.02; note it.
- Table 2's "+37.6σ" and "+27.1σ" are σ of the binomial, not of anything physical; fine, but z-scores above 10 convey nothing and read as rhetoric.

### M12. Review process

The Round-4 trio audit (co-author models) scored this revision 5/5 "Accept, Exemplary" across the board and declared 100% of prior recommendations resolved, on the same day an external reviewer (Codex) scored it 1/5 with six substantive findings, most of which stand after my reading. Same-family audits should be labeled as such and should not count toward acceptance.

---

## 3. Summary of Addendum (`03_Addendum_Phase_Memory.md`), `tau_c` Simulation (`tau_c_simulation/RESULTS.md`), and Whole-Quantum Registration Note (`04_Experiment_Proposal.md`)

1. **The Geometric Reading of Complex Interference (`00_README_Synthesis.md`):**
   - $\|\psi\|^2 = (\mathrm{Re}\psi)^2 + (\mathrm{Im}\psi)^2$ reflects the fact that the energy of a harmonic mode is quadratic in its two orthogonal **phase-space quadratures** ($\cos\omega t$ and $\sin\omega t$), and the law of cosines $\|\psi_m + \psi_n\|^2 = \|\psi_m\|^2 + \|\psi_n\|^2 + 2\|\psi_m\|\|\psi_n\|\cos(\phi_m - \phi_n)$ is the interference term. Framing the two quadratures in phase space (rather than as transverse spatial planes along a null ray) is physically sound for both photons and massive matter waves.
2. **Timescale Hierarchy & Structured-Vacuum Scan (`tau_c_simulation/RESULTS.md`):**
   - Slow detector electron phase drift under fast, uniform, share-blind quantum vacuum phase fluctuations (`slowdet_fresh_theta1`, Configuration 14) reproduces the Born rule cleanly.
   - Any persistent phase memory ($\tau_c \gtrsim \tau_{\text{fix}}$) causes Stratonovich recoil equalization ($0\%$ fixation at $\theta = 1$), while any concentration of the vacuum phase around a surface reference ($\kappa_{\text{surf}} > 0$, governed by $x = [I_1(\kappa)/I_0(\kappa)]^2 / \epsilon_0$) or dominant-atom pulling ($\kappa_{\text{pull}} > 0$) breaks the Born rule unless $a(\kappa) \lesssim 0.15\,\epsilon_0$. Thus, the QED vacuum works as the "roll of the dice" precisely because its phase fluctuations are uniform and share-blind ($\kappa_{\text{surf}} = 0, \kappa_{\text{pull}} = 0$).
3. **Whole-Quantum Registration ($\theta = 1$, Note Added 2026-11-01 in `04_Experiment_Proposal.md`):**
   - Any incident photon that interacts at all is already above the gap ($\hbar\omega \ge E_{\text{gap}}$), or it would not be absorbed; a photon is absorbed **whole** ($\theta = 1$), with the excess energy $\hbar\omega - E_{\text{gap}}$ going into the photoelectron's kinetic energy / phonons (or radiated as a secondary photon in discrete QED transitions).
   - Whole-photon registration is the $\theta = 1$ case (exact Born linearity by Doob's theorem with $\tilde{\epsilon}_{\text{vac}} = 0$). Dropping fractional individual-threshold registration removes the bandgap bias and eliminates the need for the tuned $\tilde{\epsilon}_{\text{vac}}$ parameter.
