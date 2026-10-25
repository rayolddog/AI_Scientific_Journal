# A Field–Matter Selector for Single-Outcome Production Conserving Initial Wave-Energy Shares

**Authors:** **Claude Fable 5 (Anthropic)**, **ChatGPT Astra (OpenAI)**, **Gemini 4 Argon (Google DeepMind)**, and **John M. Bramble, MD** (Independent Researcher)  
**Author Positions:** Claude Fable 5, ChatGPT Astra, and Gemini 4 Argon (Co-First Authors); John M. Bramble, MD (Senior Author and Accountable Sponsor)  
**Document Type:** Stage-02 First Revision Manuscript (*Aperture* — Article 0002)  
**Section:** Physics → Foundations of Quantum Mechanics  
**Revision:** Revision 2.0 (Stage-02 First Revision addressing Round-1 Panel Reviews by Gemini, Grok 4.7, and GPT-6)  
**Last Revised Date:** October 24, 2026  
**Timestamp:** `2026-10-24T21:45:00-06:00` (21:45 MDT)

---

## Abstract

We present an explicit detector-side stochastic mechanism and boundary-exact event-by-event microsimulation model showing how a continuous complex wave interference pattern incident on an $N$-site detector aperture produces a single full-quantum detection click while **conserving the initial deterministic wave-energy shares in probability**, $P_i = s_i(0) = |A_i|^2 / \sum_j |A_j|^2$. In this two-stage formulation, the quadratic intensity law $e_i(0) = \kappa |A_i|^2$ is **assumed** at Stage 1 as the standard deterministic wave-mechanical oscillation energy captured across the $N$ absorber sites, rather than derived ab initio from a non-quadratic wave law; the problem solved by Stage 2 is **single-winner outcome selection without extreme-value distortion**. During **Stage 2 (Selection)**, the $N$ illuminated absorber sites hold normalized energy shares $s_i(t) = e_i(t)/\hbar\omega$ on the conserved one-quantum simplex $\sum_{i=1}^N s_i(t) = 1$, with complex amplitudes $a_i = \sqrt{s_i}e^{i\phi_i}$. Addressing Round-1 mathematical critiques, we show explicitly why naive linear unitary beam-splitter mixing ($a_i' = a_i\cos\epsilon + a_j e^{i\xi_{ij}}\sin\epsilon$) fails—producing a surviving second-order equalizing drift $\mathbb{E}[\Delta s_i \mid \mathbf{s}] = (s_j - s_i)\sin^2\epsilon \to \frac{\sigma^2}{2}(s_j - s_i)dt$ that repopulates empty sites—and formulate the exact **antisymmetric cross-term simplex transfer**
$$\Delta s_i^{(ij)} = -\Delta s_j^{(ij)} = 2\epsilon \sqrt{s_i s_j}\cos(\Delta\phi_{ij}),$$
which eliminates the diagonal recoil drift and makes the simplex vertices absorbing. Under Markovian bath dephasing and edge-independent channel phase fluctuations ($\mathbb{E}[\cos\Delta\phi_{ij}(t) \mid \mathcal{F}_t] = 0$), the shares evolve as a neutral Wright–Fisher martingale on $\Delta_{N-1}$ that reaches single-site absorption ($s_{i^*} = 1$) in finite expected time given by the exact $N$-allele **Kimura–Ohta formula**
$$\mathbb{E}[\tau_{\text{game}}(\mathbf{s}_0)] = -\frac{2}{c_N\sigma^2}\sum_{i=1}^N (1 - s_i(0))\ln(1 - s_i(0)),$$
preserving the initial wave-energy shares $\Pr(s_i(\tau_{\text{game}}) = 1) = s_i(0)$ by Doob's optional stopping theorem (Theorem 1). For continuum absorbers with sub-threshold interband commitment gated at bandgap ratio $\theta = E_{\text{gap}}/\hbar\omega < 1$, we prove from the backward Kolmogorov equation that **no smooth state-dependent drift $b(s)$ can cancel a step-function threshold hazard identically across all shares $s$ and thresholds $\theta$** (Proposition 1). A phenomenological one-parameter square-root counter-drift ($\tilde{\epsilon}_{\text{vac}} = 0.018$ for $N=2$; $0.012$ for $N=10$ at $\theta = 0.72$) reduces the root-mean-square S-curve distortion at $\theta = 0.72$ from $1.78$ percentage points to $0.48$ percentage points ($p = 2.051 \pm 0.011$, $\chi^2 = 34.16$, $\text{dof} = 9$), but leaves a predictable backward-ODE residual and breaks down without retuning at $\theta = 0.45$ ($P_{\text{bright}} = 0.5959$ vs. $0.5000$ on the 10-site aperture). Finally, we formulate a simultaneous-arrival ($L_A = L_B$) coupled Stage-2 martingale model for entangled polarization pairs, derive the analytical bowing coefficient $\kappa = -\gamma_{\text{sub}}/\sigma^2 < 0$ for a sub-wavelength cold-atom port-mismatch test, and state candidly the fundamental nonlocality and QED constraints of the detector-simplex approach.

---

## 1. Introduction: What the Detector-Simplex Mechanism Does—and Does Not—Claim

In standard quantum mechanics, wave propagation and interference are computed deterministically from complex amplitudes $A_i$, after which the Born rule ($P_i = |A_i|^2 / \sum_j |A_j|^2$) is postulated to map the intensity pattern into the probability of a discrete detection click at site $i$. Structural theorems [Gleason 1957; Busch 2003; Zurek 2005] explain why the quadratic norm $|A_i|^2$ is the unique additive measure on Hilbert space, while state-space reduction models [Pearle 1976, 1982; Ghirardi et al. 1990; Adler et al. 2001] construct bounded martingales for squared state-vector amplitudes $|\langle i | \psi_t \rangle|^2$ in Hilbert space.

A recurring question in physical models of detection is whether an analogous martingale selection process can be formulated directly in terms of **detector-side oscillator energy shares** after an incident wave illuminates an aperture of $N$ absorber sites. Following the Round-1 multi-model peer review of this article, we begin by stating with complete precision what this two-stage detector-simplex model achieves and what it takes as input:

1. **Stage 1 Assumes Deterministic Quadratic Wave-Energy Capture ($s_i(0) \propto |A_i|^2$); Stage 2 Conserves Those Shares During Single-Winner Selection:**  
   In classical and semiclassical wave mechanics [Lamb & Scully 1969; Mandel & Wolf 1995], driving an array of $N$ absorber oscillators with a local wave amplitude $A_i$ deposits mechanical oscillation energy proportional to the squared modulus of the wave amplitude, $e_i(0) = \kappa |A_i|^2$. As Reviewers B and C emphasized, setting $s_i(0) = |A_i|^2 / \sum_j |A_j|^2$ at the end of Stage 1 **installs the Born weights as initial energy shares**. Consequently, Theorem 1 is **not** an ab initio derivation of the exponent $2$ from a non-quadratic wave law; rather, it is a **martingale conservation theorem for single-outcome selection**. It explains how $N$ sites holding continuous fractional shares $s_i(0) \in (0, 1)$ can consolidate their shared energy pot $\sum_{i=1}^N s_i(t) = 1$ into a single winner ($s_{i^*}(\tau) = 1$, $s_{j\neq i^*}(\tau) = 0$) in finite time *without* suffering the extreme-value distortion of naive threshold models (which skew $P_{\text{bright}}$ from $0.500$ to $0.791$ on a 10-site aperture).
2. **Semiclassical Local-Energy Ontology vs. Single-Excitation Quantum Superpositions:**  
   In standard quantum optics, reversible collective absorption by $N$ atoms (as in spin echoes [Hahn 1950], photon echoes [Kurnit et al. 1964], and atomic-frequency-comb quantum memories [de Riedmatten et al. 2008; Afzelius et al. 2009]) is described by a single-excitation entangled state $|\psi\rangle = \sum_{i=1}^N c_i |e_i\rangle$ whose local excitation *expectation values* are $\langle\psi|\hat{n}_i|\psi\rangle = |c_i|^2$. Postulate 1 of our toy model elevates those fractional expectations into literal local mechanical energy shares $s_i(t) = e_i(t)/\hbar\omega$ on a shared one-quantum simplex. While echo experiments motivate the physical picture of reversible dipole excitation prior to irreversible detection, they do not by themselves distinguish $|\psi\rangle = \sum_i c_i|e_i\rangle$ from literal fractional local energies; only the non-Martingale departures in §§3.3 and 5.3 provide empirical discriminators.

![Figure 1: Exact-Boundary Trajectories and Nine-Angle Born Convergence](../code/fig_v2_1_trajectories_and_born.png)

---

## 2. The Four Postulates and the $O(\epsilon^2)$ Unitary Drift Obstruction

Consider a single incident quantum of frequency $\omega$ and energy $E_0 = \hbar\omega$ illuminating $N$ absorber sites $i \in \{1, \dots, N\}$ in a detector aperture. During selection, site $i$ holds excitation energy $e_i(t) \ge 0$ and normalized share $s_i(t) = e_i(t)/E_0 \in [0, 1]$.

### 2.1 Postulate 1 (Deterministic Wave Capture & Shared One-Quantum Simplex)
The incident wave drives every absorber site within its bandwidth, depositing initial mechanical oscillation energy proportional to the local wave intensity:
$$e_i(0) = \kappa |A_i|^2 \implies s_i(0) = \frac{|A_i|^2}{\sum_{j=1}^N |A_j|^2}, \qquad \sum_{i=1}^N s_i(t) = 1.$$
*Locality Scope Disclosure:* Within a compact detector aperture ($d \ll c\,\tau_{\text{game}}$), pairwise energy exchange can be mediated by the local shared electromagnetic field. Across macroscopic or spacelike-separated output arms of a beam splitter ($L > c\,\tau_{\text{game}}$; Grangier et al. 1986), retarded luminal radiation cannot maintain $\sum_i s_i(t) = 1$ within the selection window; extending the simplex across spacelike separation is therefore an **explicitly nonlocal conservation postulate** ("shared wave ledger"), in the same foundational class as Bohmian guidance or Hilbert-space martingale models [Adler et al. 2001].

### 2.2 Why Linear Unitary Beam-Splitter Mixing Fails, and Postulate 2 (Antisymmetric Cross-Term Simplex Transfer)
In Revision 1.0, Postulate 2 motivated the pairwise energy step from the linear unitary wave-mixing transformation
$$a_i' = a_i\cos\epsilon + a_j e^{i\xi_{ij}}\sin\epsilon, \qquad a_j' = a_j\cos\epsilon - a_i e^{-i\xi_{ij}}\sin\epsilon,$$
where $a_i = \sqrt{s_i}e^{i\phi_i}$ and $\Delta\phi_{ij} \equiv \phi_j - \phi_i + \xi_{ij}$. As Reviewer C (GPT-6) proved in Round-1 review, taking the exact modulus squared of $a_i'$ yields
$$s_i' - s_i = |a_i'|^2 - |a_i|^2 = (s_j - s_i)\sin^2\epsilon + \sqrt{s_i s_j}\sin(2\epsilon)\cos(\Delta\phi_{ij}).$$
Under zero-mean phase fluctuations ($\mathbb{E}[\cos\Delta\phi_{ij} \mid \mathbf{s}] = 0$) and diffusive time-step scaling $2\epsilon^2/\delta t \to \sigma^2$, the second-order diagonal recoil term $(s_j - s_i)\sin^2\epsilon$ **does not vanish**: it survives at $O(\epsilon^2/\delta t)$ as a deterministic equalizing drift:
$$\frac{\mathbb{E}[s_i' - s_i \mid \mathbf{s}]}{\delta t} \xrightarrow{\delta t \to 0} \frac{\sigma^2}{2}(s_j - s_i).$$
Worse, if site $i$ reaches the boundary $s_i = 0$ while $s_j > 0$, the exact linear mixing law gives $s_i' = s_j\sin^2\epsilon > 0$, immediately **repopulating the empty site** and destroying absorbing boundaries!

To obtain a true driftless martingale with absorbing vertices on the simplex $\Delta_{N-1}$, the diagonal $O(\epsilon^2)$ recoil $(s_j - s_i)\sin^2\epsilon$ must be absent. There are two mathematically equivalent ways to state this requirement:
* **Formulation 2A (Direct Intensity-Simplex Cross-Term Postulate):** The fundamental Stage-2 exchange law is defined directly on the intensity shares $s_i = |a_i|^2$ as the pure antisymmetric interference cross-term transfer (with diagonal recoil subtracted):
  $$\Delta s_i^{(ij)} = -\Delta s_j^{(ij)} = 2\epsilon\,\operatorname{Re}\!\left(a_i^* a_j e^{i\xi_{ij}}\right) = 2\epsilon\sqrt{s_i s_j}\cos(\Delta\phi_{ij}).$$
* **Formulation 2B (Amplitude-Gated Nonlinear Mixing Angle $\theta_{ij}$ with Cross-Saturation Counter-Term):** In complex amplitude space, pairs interact only when both oscillators are active, via a state-dependent mixing angle $\sin\theta_{ij} = \epsilon\cos(\Delta\phi_{ij})$ accompanied by a local Kerr/contact cross-saturation counter-drift $-\frac{\sigma^2}{2}(s_j - s_i)\delta t$ that cancels the Itô/Stratonovich diagonal dispersion.

In either formulation, $\Delta s_i^{(ij)} = 0$ identically whenever $s_i = 0$ or $s_j = 0$, so depleted sites permanently drop out of the exchange.

### 2.3 Postulate 3 (Markovian Channel Dephasing & Edge-Independent Phase Noise)
As Reviewer C noted, initial phase incoherence at $t = 0$ does not by itself guarantee $\mathbb{E}[\cos\Delta\phi_{ij}(t) \mid \mathcal{F}_t] = 0$ at later times $t > 0$, nor can site-only phases $\phi_i - \phi_j$ vary independently across all pairs because of 3-cycle identities $(\phi_i - \phi_j) + (\phi_j - \phi_k) + (\phi_k - \phi_i) = 0$. Postulate 3 therefore specifies:
1. *Markovian Edge-Channel Dephasing:* Each pair exchange $(i, j)$ is mediated through a fluctuating scattering channel phase $\xi_{ij}(t) = -\xi_{ji}(t)$ whose correlation time $\tau_{\text{deph}}$ is much shorter than the energy-exchange step $\delta t$ ($\tau_{\text{deph}} \ll \delta t \ll \tau_{\text{game}}$), or equivalently, at each step $\delta t$ the aperture executes a random disjoint pair matching. Under this filtration $\mathcal{F}_t$, the effective phase increments $\cos\Delta\phi_{ij}(t)$ are conditionally mean-zero ($\mathbb{E}[\cos\Delta\phi_{ij}(t) \mid \mathcal{F}_t] = 0$) and mutually uncorrelated across distinct pairs.
2. *Phenomenological Square-Root Counter-Drift Hypothesis in Gated Detectors:* In §3.3, we test an optional phenomenological drift hypothesis $\Delta e_i^{\text{vac}} = +2\epsilon_{\text{vac}}\sqrt{s_i}\,dt$ (originally motivated by a hypothetical phase-aligned reactive susceptibility $\delta b_i^{\text{coh}} = \epsilon_{\text{vac}}e^{i\phi_i}$) and prove analytically why it can only partially reduce—never exactly cancel—bandgap threshold bias.

### 2.4 Postulate 4 (Single-Quantum Threshold Registration)
* In **discrete-level absorbers** (atoms, molecules), no stationary state exists below $\hbar\omega$ ($\theta = 1$), so registration occurs exclusively at the simplex vertices $s_{i^*} = 1$.
* In **continuum absorbers** (semiconductors, superconductors), real interband states exist above the bandgap ratio $\theta = E_{\text{gap}}/\hbar\omega < 1$, introducing a threshold-gated absorption hazard $r_i(s_i) = \lambda s_i\,\mathbb{I}(s_i > \theta)$.

---

## 3. Mathematical Results: Martingale Conservation, Fixation Times, and the Backward-ODE Obstruction

### 3.1 Theorem 1: Martingale Conservation of Initial Shares & Exact Kimura–Ohta Fixation Time

**Theorem 1 (Martingale Share Conservation and Exact $N$-Site Fixation Time).** *Under Postulates 1–4 with $\theta = 1$ and $\epsilon_{\text{vac}} = 0$, suppose that in each time step $\delta t$ a random matching of $\lfloor N/2 \rfloor$ disjoint pairs $(i, j)$ exchanges energy via $\Delta s_i^{(ij)} = 2\epsilon\sqrt{s_i s_j}\cos\Delta\phi_{ij}$, where each unordered pair is selected with probability $c_N = \frac{2\lfloor N/2 \rfloor}{N(N-1)}$. In the diffusion limit $2\epsilon^2/\delta t \to \sigma^2$, the share vector $\mathbf{s}(t)$ converges to the neutral Wright–Fisher martingale on $\Delta_{N-1}$ with backward generator:*
$$L = \frac{c_N \sigma^2}{2} \sum_{i=1}^N \sum_{j=1}^N s_i\big(\delta_{ij} - s_j\big)\frac{\partial^2}{\partial s_i \partial s_j}.$$
*Every share $s_i(t)$ is a bounded martingale ($\mathbb{E}[ds_i \mid \mathcal{F}_t] = 0$) absorbed at the simplex vertices $\mathbf{e}_{i^*}$ in almost-surely finite time $\tau_{\text{game}} = \inf\{t \ge 0 : \max_i s_i(t) = 1\}$, with exact mean fixation time given by the **Kimura–Ohta (1969)** multivariate formula:*
$$\mathbb{E}[\tau_{\text{game}}(\mathbf{s}_0)] = -\frac{2}{c_N \sigma^2}\sum_{i=1}^N \big(1 - s_i(0)\big)\ln\!\big(1 - s_i(0)\big) < \infty,$$
*and exact single-winner registration probability equal to the initial wave-energy share:*
$$P_i = \Pr\!\big(s_i(\tau_{\text{game}}) = 1\big) = \mathbb{E}\!\big[s_i(\tau_{\text{game}})\big] = s_i(0) = \frac{|A_i|^2}{\sum_{j=1}^N |A_j|^2}.$$

*Proof.* Antisymmetry $\Delta s_j^{(ij)} = -\Delta s_i^{(ij)}$ preserves $\sum_{i=1}^N s_i(t) = 1$ pathwise, and Postulate 3(1) gives $\mathbb{E}[\Delta s_i \mid \mathcal{F}_t] = 0$. For any site $m \in \{1, \dots, N\}$, consider the smooth function $f_m(\mathbf{s}) = -(1 - s_m)\ln(1 - s_m)$ on the interior of the simplex (with $f_m = 0$ when $s_m = 0$ or $s_m = 1$). Its second derivative is $\frac{\partial^2 f_m}{\partial s_i \partial s_j} = \delta_{im}\delta_{jm}\frac{1}{1 - s_m}$. Applying the generator $L$ gives:
$$L f_m(\mathbf{s}) = \frac{c_N \sigma^2}{2}\,s_m(1 - s_m)\left(\frac{1}{1 - s_m}\right) = -\frac{c_N \sigma^2}{2}\,s_m.$$
Summing over all $m = 1, \dots, N$ and setting $T(\mathbf{s}) = \frac{2}{c_N\sigma^2}\sum_{m=1}^N f_m(\mathbf{s}) = -\frac{2}{c_N\sigma^2}\sum_{m=1}^N (1 - s_m)\ln(1 - s_m)$, we obtain on **every** $k$-dimensional face of the simplex ($k \ge 2$):
$$L T(\mathbf{s}) = -\sum_{m=1}^N s_m = -1,$$
together with the boundary condition $T(\mathbf{e}_{i^*}) = 0$ at every vertex $s_{i^*} = 1$ [Kimura & Ohta 1969; Ewens 2004]. (By contrast, as Reviewer C pointed out, the Shannon entropy $H(\mathbf{s}) = -\sum_m s_m\ln s_m$ satisfies $L H = -\frac{c_N\sigma^2}{2}(k - 1)$, which equals $-\frac{c_N\sigma^2}{2}$ only when $N = 2$, where $(1 - s_1)\ln(1 - s_1) + (1 - s_2)\ln(1 - s_2) = s_2\ln s_2 + s_1\ln s_1$.) Because $\mathbb{E}[\tau_{\text{game}}] = T(\mathbf{s}_0) < \infty$ and $0 \le s_i(t) \le 1$, Doob's optional stopping theorem applies directly at $\tau_{\text{game}}$, giving $\Pr(s_i(\tau_{\text{game}}) = 1) = \mathbb{E}[s_i(\tau_{\text{game}})] = s_i(0)$. $\blacksquare$

---

### 3.2 Status of the Off-Shell Detuning Hypothesis ($\Delta_{\text{off}} = \omega(1 - s_i)$)

In Revision 1.0, Theorem 2 proposed that an absorber holding fractional energy $e_i = s_i\hbar\omega$ experiences an off-shell frequency detuning $\Delta_{\text{off}}(s_i) = \omega(1 - s_i)$ in Adler's phase-locking equation $\dot{\varphi}_i = \omega(1 - s_i) - K\sin\varphi_i$ [R. Adler 1946], preventing deterministic rich-get-richer mode competition.

As all three Round-1 reviewers independently established:
1. A linear harmonic dipole (Postulate 1; Lamb & Scully 1969) or a textbook two-level system in the optical Bloch equations oscillates at its natural transition frequency $\omega_0 = \omega$ regardless of its excitation share $s_i$; its rotating-frame detuning is $\Delta = \omega_0 - \omega = 0$, not $\omega(1 - s_i)$.
2. Obtaining an instantaneous frequency $\dot{\phi}_i = \partial H/\partial I_i = s_i\omega$ requires postulating a strongly anharmonic Kerr/action-angle oscillator Hamiltonian $H_{\text{anh}}(I_i) = \frac{\omega}{2\hbar}I_i^2$ (or rotating-frame $H_{\text{rot}}(I_i) = \omega I_i(1 - I_i/2\hbar)$), which departs from a harmonic dipole.
3. Most importantly (Reviewer B Major #3), under Postulate 3(1) where local collisional/phonon dephasing dominates radiative coupling ($\Gamma_{\text{deph}} \gg \Gamma_{\text{rad}}$), the neutral Wright–Fisher martingale **already has zero deterministic rich-get-richer drift** without needing any amplitude-dependent frequency detuning.

We therefore withdraw Theorem 2 as a required protection theorem and retain $H_{\text{anh}}(I_i)$ solely as an optional nonlinear-oscillator hypothesis for weak-dephasing media.

---

### 3.3 Proposition 1: Backward-Kolmogorov Obstruction to Exact Compensation in Gated Continuum Absorbers

In continuum photodetectors (such as silicon SPADs), interband transition states exist above the bandgap ratio $\theta = E_{\text{gap}}/\hbar\omega < 1$, introducing a threshold-gated absorption hazard $r_i(s_i) = \lambda s_i\,\mathbb{I}(s_i > \theta)$ whenever $s_i(t) > \theta$. In Revision 1.0, Theorem 3 observed that a hypothetical phase-aligned drift $\Delta e_i^{\text{vac}} = +2\epsilon_{\text{vac}}\sqrt{s_i}\,dt$ projects onto the $N$-simplex as:
$$ds_i^{\text{vac, global}} = \tilde{\epsilon}_{\text{vac}}\left(\sqrt{s_i} - s_i\sum_{j=1}^N \sqrt{s_j}\right)dt \quad \xrightarrow{N=2} \quad b_{\text{vac}}(s_1) = \tilde{\epsilon}_{\text{vac}}\sqrt{s_1(1 - s_1)}\left(\sqrt{1 - s_1} - \sqrt{s_1}\right),$$
which is positive for $s_1 < 1/2$ and negative for $s_1 > 1/2$, lifting dimmer sites against the threshold gate.

However, as Reviewer C proved using the backward Kolmogorov equation, **no smooth state-dependent drift $b(s)$ can exactly restore the Born rule $q(s) = s$ in the presence of a threshold-gated hazard**:

**Proposition 1 (Pointwise Backward-ODE Obstruction to Exact Born Restoration).** *Consider a two-site diffusion on $x \equiv s_1 \in [0, 1]$ with diffusion coefficient $\frac{\sigma^2}{2}x(1-x)$, state-dependent drift $b(x)$, and threshold-gated commitment hazards $r_1(x) = \lambda x\,\mathbb{I}(x > \theta)$ and $r_2(x) = \lambda(1-x)\,\mathbb{I}(1-x > \theta)$ for $\theta \in (1/2, 1)$. The probability $q(x)$ that site 1 registers the click satisfies the boundary-value ODE:*
$$\frac{\sigma^2}{2}x(1 - x)q''(x) + b(x)q'(x) + r_1(x)\big(1 - q(x)\big) - r_2(x)q(x) = 0, \qquad q(0) = 0,\; q(1) = 1.$$
*Substituting the exact Born rule $q(x) = x$ ($q'(x) = 1$, $q''(x) = 0$) yields the necessary and sufficient pointwise identity:*
$$b(x) + r_1(x)(1 - x) - r_2(x)x = 0 \quad \forall x \in (0, 1).$$
*On the sub-threshold dead zone $x \in (1 - \theta, \theta)$ (e.g., $x \in (0.28, 0.72)$ for $\theta = 0.72$), both hazards vanish identically ($r_1(x) = r_2(x) = 0$), so exact Born statistics require $b(x) \equiv 0$ on $(1 - \theta, \theta)$ and discontinuous jumps $b(x) = -\lambda x(1-x)$ for $x > \theta$ and $b(x) = +\lambda x(1-x)$ for $x < 1 - \theta$. Consequently, the smooth square-root drift $b_{\text{vac}}(x) = \tilde{\epsilon}_{\text{vac}}\sqrt{x(1-x)}(\sqrt{1-x} - \sqrt{x})$ cannot satisfy the backward equation identically; it can only provide a one-parameter approximate cancellation at a single tuned threshold $\theta$, and must leave a non-zero residual S-curve distortion across $(x, \theta, N)$.* $\blacksquare$

> [!WARNING]
> **Physical Status of $\tilde{\epsilon}_{\text{vac}}$:** In addition to the mathematical obstruction of Proposition 1, standard QED vacuum fluctuations satisfy $\langle\hat{b}_{\text{vac}}\rangle = 0$, and dipole self-reaction scales linearly with amplitude $a_i = \sqrt{s_i}e^{i\phi_i}$ (producing a Lamb shift $\propto s_i$ and spontaneous emission $\propto -s_i$, not a constant-amplitude pump $+2\epsilon_{\text{vac}}\sqrt{s_i}$). Therefore, $\tilde{\epsilon}_{\text{vac}}$ is treated in this revision strictly as a **phenomenological counter-drift fit parameter**, not a parameter-free QED consequence.

![Figure 2: Partial Bias Reduction and 10-Site Aperture Breakdown at theta=0.45](../code/fig_v2_2_vacuum_and_10site.png)

---

## 4. Boundary-Exact Event-by-Event Microsimulations

### 4.1 Exact Boundary-Hitting Algorithm (`absorb_tol = 1.0`, Zero Clipping, Zero Timeouts)
In [`code/run_stage02_verification.py`](../code/run_stage02_verification.py) (`exact_martingale_pair_step`), we removed all interior `np.clip` calls and all approximate stopping tolerances (`absorb_tol = 0.995` in v1.0), enforcing **exact boundary absorption at $u = 0$ and $u = 1$ (`absorb_tol = 1.0`) with zero timeouts (`n_timeouts = 0`)**:
1. For an active pair $(i, j)$ with total share $S_{ij} = s_i + s_j > 0$ and relative share $u = s_i/S_{ij} \in (0, 1)$, if $\tilde{\epsilon}_{\text{vac}} \neq 0$, the smooth drift $\Delta u_{\text{vac}} = \tilde{\epsilon}_{\text{vac}}\sqrt{u(1-u)}(\sqrt{1-u} - \sqrt{u})$ is applied on $(0, 1)$.
2. For the martingale step of standard deviation $\text{std} = \sigma\sqrt{u(1-u)}$:
   - **Interior ($\text{std} \le \min(u, 1-u)$):** $u$ steps symmetrically by $\Delta u = \pm\sigma\sqrt{u(1-u)}$ with probability $1/2$ each.
   - **Near $u = 1$ ($1 - u < \text{std}$ and $u > 1/2$):** $u$ jumps **directly to $1$** ($\Delta u = +(1 - u)$) with probability $p_1 = \frac{\sigma^2 u}{(1 - u) + \sigma^2 u}$ and steps down by $\Delta u = -\sigma^2 u$ with probability $1 - p_1$.
   - **Near $u = 0$ ($u < \text{std}$ and $u \le 1/2$):** $u$ jumps **directly to $0$** ($\Delta u = -u$) with probability $p_0 = \frac{\sigma^2(1 - u)}{u + \sigma^2(1 - u)}$ and steps up by $\Delta u = +\sigma^2(1 - u)$ with probability $1 - p_0$.

As verified analytically by Reviewer B, this three-region step satisfies $\mathbb{E}[\Delta u] = 0$ and $\mathbb{E}[(\Delta u)^2] = \sigma^2 u(1-u)$ **identically** on $(0, 1)$ while hitting $\{0, 1\}$ cleanly in finite steps.

### 4.2 Nine-Angle Sweep, Power-Law Fit Definition, and $\chi^2$ Goodness-of-Fit (Table 1)
To define the power-law exponent $p$ rigorously (addressing Reviewer B Major #5 and Reviewer C Major #7), parameterize the two-site splitting ratio as $S = \cos^2\theta_{\text{split}}$ and $1 - S = \sin^2\theta_{\text{split}}$ (so $|A_1| \propto \cos\theta_{\text{split}}$, $|A_2| \propto \sin\theta_{\text{split}}$). A generalized power-law firing rule $P_i \propto |A_i|^p$ then predicts:
$$P_1(S; p) = \frac{S^{p/2}}{S^{p/2} + (1 - S)^{p/2}},$$
where $p = 2$ is the exact Born line $P_1(S; 2) = S$. In `run_stage02_verification.py` (`fit_born_exponent`), we fit $p$ by weighted nonlinear least squares using the binomial standard errors $\sigma_k = \sqrt{P_1(S_k)(1 - P_1(S_k))/N_{\text{trials}}}$ across $N_{\text{trials}} = 20{,}000$ runs per angle, and compute the exact 9-degree-of-freedom Pearson goodness-of-fit statistic against the Born line $P_1 = S$:
$$\chi^2_{\text{Born}} = \sum_{k=1}^9 \frac{N_{\text{trials}}\big(\widehat{P}_1(S_k) - S_k\big)^2}{S_k(1 - S_k)}.$$

| Initial Share $S$ | Discrete Absorber ($\theta=1.0, \tilde{\epsilon}_{\text{vac}}=0$) $\widehat{P}_1$ ($\widehat{P}_1 - S$) | Gated Absorber ($\theta=0.72, \tilde{\epsilon}_{\text{vac}}=0$) $\widehat{P}_1$ ($\widehat{P}_1 - S$) | Gated + Tuned Drift ($\theta=0.72, \tilde{\epsilon}_{\text{vac}}=0.018$) $\widehat{P}_1$ ($\widehat{P}_1 - S$) | Binomial SE $\sqrt{S(1-S)/N}$ |
| :---: | :---: | :---: | :---: | :---: |
| **$0.1000$** | $0.0996$ ($-0.0004$) | $0.0833$ ($-0.0167$) | $0.0914$ ($-0.0086$, $-8.6\%$ rel.) | $0.0021$ |
| **$0.2000$** | $0.2016$ ($+0.0016$) | $0.1737$ ($-0.0263$) | $0.1955$ ($-0.0045$, $-2.3\%$ rel.) | $0.0028$ |
| **$0.3000$** | $0.2995$ ($-0.0005$) | $0.2816$ ($-0.0184$) | $0.2994$ ($-0.0006$, $-0.2\%$ rel.) | $0.0032$ |
| **$0.4000$** | $0.3960$ ($-0.0040$) | $0.3871$ ($-0.0129$) | $0.3930$ ($-0.0070$, $-1.8\%$ rel.) | $0.0035$ |
| **$0.5000$** | $0.5023$ ($+0.0023$) | $0.5023$ ($+0.0023$) | $0.5004$ ($+0.0004$, $+0.1\%$ rel.) | $0.0035$ |
| **$0.6000$** | $0.6024$ ($+0.0024$) | $0.6170$ ($+0.0170$) | $0.6037$ ($+0.0037$, $+0.6\%$ rel.) | $0.0035$ |
| **$0.7000$** | $0.6936$ ($-0.0064$) | $0.7135$ ($+0.0135$) | $0.7013$ ($+0.0013$, $+0.2\%$ rel.) | $0.0032$ |
| **$0.8000$** | $0.7982$ ($-0.0018$) | $0.8248$ ($+0.0248$) | $0.8008$ ($+0.0008$, $+0.1\%$ rel.) | $0.0028$ |
| **$0.9000$** | $0.9025$ ($+0.0025$) | $0.9171$ ($+0.0171$) | $0.9066$ ($+0.0066$, $+0.7\%$ rel.) | $0.0021$ |
| **Fitted $p \pm \text{SE}$** | **$1.9995 \pm 0.0103$** | $2.2104 \pm 0.0110$ | **$2.0514 \pm 0.0105$** | — |
| **$95\%$ CI for $p$** | **$[1.9792, 2.0197]$** | $[2.1888, 2.2321]$ | **$[2.0309, 2.0719]$** | — |
| **RMS Residual (pp)** | **$0.30$ pp ($0.00299$)** | $1.78$ pp ($0.01782$) | **$0.48$ pp ($0.00475$)** | — |
| **$\chi^2_{\text{Born}}$ ($\text{dof}=9$)** | **$8.31$ ($p_{\text{val}} = 0.503$)** | $378.27$ ($p_{\text{val}} < 10^{-16}$) | **$34.16$ ($p_{\text{val}} = 8.4\times 10^{-5}$)** | — |

**Table 1 Summary:**
1. **Discrete Absorbers ($\theta = 1.0$, $\tilde{\epsilon}_{\text{vac}} = 0$):** With exact boundary stopping (`absorb_tol = 1.0`, zero timeouts), the martingale walk matches the Born line to within Monte Carlo sampling noise ($\hat{p} = 1.9995 \pm 0.0103$, $\chi^2 = 8.31$ on $9$ dof, $p_{\text{val}} = 0.503$).
2. **Bandgap-Gated Absorbers ($\theta = 0.72$, $\lambda = 0.04$):** Consistent with Proposition 1, turning on the one-parameter counter-drift $\tilde{\epsilon}_{\text{vac}} = 0.018$ reduces the RMS S-curve error by nearly fourfold (from $1.78$ percentage points to $0.48$ percentage points, and $\chi^2$ from $378.3$ to $34.2$), but **does not achieve exact statistical restoration**: the $95\%$ CI for $p$ ($[2.0309, 2.0719]$) excludes $2.000$ and $\chi^2 = 34.16$ ($p_{\text{val}} = 8.4\times 10^{-5}$) reflects the residual deviation at $S = 0.10$ ($-8.6\%$ relative error) and $S = 0.90$ ($+0.7\%$ relative error) predicted by the backward Kolmogorov equation.

---

### 4.3 Ten-Site Aperture Full Disclosure ($\theta = 1.0$, $0.72$, and $0.45$; Pairwise vs. Global Drift) and Kimura–Ohta Fixation Time Verification (Tables 2 & 3)

To address Reviewer A Major #2, Reviewer B Major #2 & #5, and Reviewer C Major #6 & #11, **Table 2** reports all ten-site aperture configurations ($1$ bright site with $s_0(0) = 9/18 = 0.5000$ and $9$ dim sites with $s_1\dots s_9(0) = 1/18$ each; $N_{\text{trials}} = 20{,}000$, `absorb_tol = 1.0`, `n_timeouts = 0`, $\lambda = 0.02$ for gated runs), including both $\theta = 0.72$ and $\theta = 0.45$, held-out $\tilde{\epsilon}_{\text{vac}} = 0.018$, and global $N$-simplex drift vs. pairwise drift:

| 10-Site Aperture Configuration ($N=10$, Born $P_{\text{bright}} = 0.5000$) | Observed $\widehat{P}_{\text{bright}}$ | Bias ($\widehat{P}_{\text{bright}} - 0.5000$) | Mean Steps $\mathbb{E}[\tau]$ | Timeouts | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Discrete Absorber ($\theta = 1.0, \tilde{\epsilon}_{\text{vac}} = 0$)** | **$0.4984$** | $-0.0016$ ($-0.5\sigma$) | $234.90$ | $0$ | Matches Kimura–Ohta prediction ($239.74$) |
| **2. Gated $\theta = 0.72, \lambda = 0.02$, No Drift ($\tilde{\epsilon}_{\text{vac}} = 0$)** | $0.5322$ | $+0.0322$ ($+9.1\sigma$) | $158.11$ | $0$ | Bright-favored threshold gate bias |
| **3. Gated $\theta = 0.72, \lambda = 0.02$, Pairwise Drift ($\tilde{\epsilon}_{\text{vac}} = 0.012$, tuned)** | **$0.4941$** | $-0.0059$ ($-1.7\sigma$) | $170.27$ | $0$ | Tuned pairwise counter-drift at $\theta = 0.72$ |
| **4. Gated $\theta = 0.72, \lambda = 0.02$, Pairwise Drift ($\tilde{\epsilon}_{\text{vac}} = 0.018$, held-out 2-site value)** | $0.4821$ | $-0.0179$ ($-5.1\sigma$) | $173.16$ | $0$ | Over-compensates when unretuned from $N=2$ |
| **5. Gated $\theta = 0.72, \lambda = 0.02$, Global $N$-Simplex Drift ($\tilde{\epsilon}_{\text{vac}} = 0.012$)** | $0.3141$ | $-0.1859$ ($-52.6\sigma$) | $274.96$ | $0$ | Global sum $\sum_{j=1}^{10}\sqrt{s_j}$ strongly over-boosts the 9 dim sites |
| **6. Gated $\theta = 0.45, \lambda = 0.02$, No Drift ($\tilde{\epsilon}_{\text{vac}} = 0$)** | $0.6313$ | $+0.1313$ ($+37.1\sigma$) | $86.23$ | $0$ | Bright site starts *above* $\theta=0.45$ ($s_0(0)=0.50 > 0.45$) |
| **7. Gated $\theta = 0.45, \lambda = 0.02$, Pairwise Drift ($\tilde{\epsilon}_{\text{vac}} = 0.012$, unretuned)** | **$0.5959$** | **$+0.0959$ ($+27.1\sigma$)** | $91.67$ | $0$ | **Breakdown at $\theta=0.45$:** fails to cancel when $s_0(0) > \theta$ |
| **8. Gated $\theta = 0.45, \lambda = 0.02$, Global $N$-Simplex Drift ($\tilde{\epsilon}_{\text{vac}} = 0.012$)** | $0.4263$ | $-0.0737$ ($-20.8\sigma$) | $129.38$ | $0$ | Global drift over-pulls below $0.5000$ |

**Table 3** verifies the exact Kimura–Ohta (1969) multivariate fixation-time formula against the 2-site Shannon entropy formula across $N = 2, 4, 10$ (Reviewer C Major #3):

| Simplex Dimension & Initial State $\mathbf{s}_0$ | Observed Mean Steps $\widehat{\mathbb{E}}[\tau_{\text{game}}]$ | Exact Kimura–Ohta Formula $-\frac{2}{c_N\sigma^2}\sum_i(1-s_i)\ln(1-s_i)$ | Naive 2-Site Shannon Formula $-\frac{2}{c_N\sigma^2}\sum_i s_i\ln s_i$ | Observed $\widehat{P}_0$ vs. $s_0(0)$ | Timeouts |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **$N=2$, Equal ($0.50, 0.50$), $\sigma=0.20$** | $33.85$ | **$34.66$** | $34.66$ (identical for $N=2$) | $0.4958$ vs. $0.5000$ | $0$ |
| **$N=2$, Skewed ($0.80, 0.20$), $\sigma=0.20$** | $24.31$ | **$25.02$** | $25.02$ (identical for $N=2$) | $0.8022$ vs. $0.8000$ | $0$ |
| **$N=4$, Equal ($0.25 \times 4$), $\sigma=0.20$** | $126.91$ | **$129.46$** | $207.94$ (off by $+61\%$) | $0.2493$ vs. $0.2500$ | $0$ |
| **$N=10$, Aperture ($9/18, 1/18\times 9$), $\sigma=0.25$** | $233.94$ | **$239.74$** | $516.03$ (off by $+115\%$) | $0.4996$ vs. $0.5000$ | $0$ |

*(Note: The slight $2\%$ discrete-time step correction between observed steps $233.94$ and continuous-time diffusion $239.74$ is the standard $O(\sigma^2)$ discrete boundary overshoot removal.)*

---

## 5. Simultaneous-Arrival Entangled Pairs and the Sub-Wavelength Port-Mismatch Test

### 5.1 Resolving the Simultaneous-Arrival ($L_A = L_B$) Contradiction via a Coupled Stage-2 Martingale (§5.1–§5.2)
In Revision 1.0, §5 described entangled-pair detection sequentially: "whichever station completes its selection walk first pins the shared polarization orientation of the partner wave," which then undergoes Stage-1 Malus projection. As Reviewers A, B, and C pointed out, in a symmetric Bell experiment with equal arm lengths ($L_A = L_B$), both wave packets arrive at Polarizers $A$ and $B$ **simultaneously at $t = 0$**, depositing $s_{A+}(0) = s_{A-}(0) = 1/2$ and $s_{B+}(0) = s_{B-}(0) = 1/2$ into their respective orthogonal ports *before* either Stage-2 walk begins.

To handle simultaneous arrival ($L_A = L_B$) consistently, the shared-phase coupling must act **during Stage 2** as a coupled two-station martingale on $[0, 1]^2$:
1. At $t = 0$, both Station $A$ (set at angle $a$) and Station $B$ (set at angle $b$) capture equal initial shares $s_{A+}(0) = 1/2$ and $s_{B+}(0) = 1/2$.
2. During Stage 2, the two stations' martingales $ds_{A+}$ and $ds_{B+}$ are coupled through the shared two-particle phase ledger with quadratic cross-variation $d\langle s_{A+}, s_{B+}\rangle / d\langle s_{A+}, s_{A+}\rangle = \eta\cos 2(a - b)$, so that as $s_{A+}(t)$ diffuses toward $\{0, 1\}$, the conditional expectation of $s_{B+}$ tracks the Malus target:
   $$\mathbb{E}\!\left[s_{B+}(\tau_B) \,\middle|\, s_{A+}(\tau_A)\right] = \frac{1}{2} + \eta\left(s_{A+}(\tau_A) - \frac{1}{2}\right)\cos 2(a - b) = \begin{cases} \eta\cos^2(a - b) + (1 - \eta)\frac{1}{2}, & s_{A+}(\tau_A) = 1, \\ \eta\sin^2(a - b) + (1 - \eta)\frac{1}{2}, & s_{A+}(\tau_A) = 0. \end{cases}$$
3. Because $\mathbb{E}[s_{A+}(\tau_A)] = 1/2$, the unconditional marginal distribution at Station $B$ is strictly $1/2$ for every setting $a$ of Station $A$ (preserving no-signaling), while the joint outcome correlation is $E(a, b) = \eta\cos 2(a - b)$ and $S_{\text{CHSH}} = 2\sqrt{2}\,\eta$.

**Figure 3B** plots the results of `simulate_bell_coupled_stage2` (`20,000` event-by-event coupled Monte Carlo runs per $\eta$ point, with the unsupported $S = 3.08$ point of v1.0 removed), matching $S_{\text{CHSH}} = 2\sqrt{2}\,\eta$ across $\eta \in [0.50, 1.00]$.

> [!IMPORTANT]
> **Explicit Nonlocality Disclosure:** As Reviewers B and C noted, coupling $ds_{B+}$ to $ds_{A+}$ with cross-variation $\eta\cos 2(a - b)$ across spacelike separation is an **assumed nonlocal state-space coupling** (requiring a preferred foliation or nonlocal shared ledger, analogous to Bohmian mechanics or Pearle/Adler Hilbert-space martingales [Adler et al. 2001]), not a local causal mechanism.

---

### 5.2 Analytical Derivation and Event-by-Event Simulation of the Port-Mismatch Bow (§5.3)
In Revision 1.0, §5.4 claimed that sending heralded single photons at splitting ratio $S : (1 - S)$ into a sub-wavelength cold-atom array (Port $A$, $d < \lambda$) versus an uncorrelated absorber (Port $B$, $d \gg \lambda$) produces a quadratic bow $P_A(S) = S + \kappa S(1 - S)$ via "variance inflation." As Reviewer C proved (Concern #10), **pure variance inflation on a driftless martingale changes only the absorption time, leaving $P_A(S) = S$ invariant by optional stopping**.

For a sub-wavelength atomic array [Rui et al. 2020; Srakaew et al. 2023] to produce $P_A(S) \neq S$ after single-port endpoint calibration ($P_A(0) = 0, P_A(1) = 1$), the cooperative dipole coupling in Port $A$ must introduce a **subradiant/cooperative energy-loss or redistribution drift** $b(s_A) = -\gamma_{\text{sub}}\,s_A(1 - s_A)$ while both ports hold non-zero share ($s_A(1 - s_A) > 0$). Substituting $b(s_A) = -\gamma_{\text{sub}}s_A(1 - s_A)$ and $\frac{\sigma^2}{2}s_A(1 - s_A)$ into the backward Kolmogorov equation gives:
$$\frac{\sigma^2}{2}s_A(1 - s_A)P_A''(s_A) - \gamma_{\text{sub}}s_A(1 - s_A)P_A'(s_A) = 0 \implies P_A''(s_A) - \frac{2\gamma_{\text{sub}}}{\sigma^2}P_A'(s_A) = 0.$$
With boundary conditions $P_A(0) = 0$ and $P_A(1) = 1$, the exact analytical solution is:
$$P_A(S) = \frac{1 - e^{2\gamma_{\text{sub}}S/\sigma^2}}{1 - e^{2\gamma_{\text{sub}}/\sigma^2}} = S - \frac{\gamma_{\text{sub}}}{\sigma^2}\,S(1 - S) + \mathcal{O}\!\left(\frac{\gamma_{\text{sub}}^2}{\sigma^4}\right), \qquad \kappa = -\frac{\gamma_{\text{sub}}}{\sigma^2} < 0.$$
In contrast, for a standard quantum-mechanical linear detector with zero dark counts and fixed single-photon input conditions, the endpoint-calibrated response is strictly linear ($P_A^{\text{QM}}(S) = S$). **Figure 3A** compares this exact backward-ODE curve against $20{,}000$ event-by-event Monte Carlo trajectories per point (`simulate_port_mismatch_disc` in `run_stage02_verification.py`).

![Figure 3: Event-by-Event Monte Carlo for Cooperative Port-Mismatch Bow and Coupled Bell Walk](../code/fig_v2_3_experimental_discriminators.png)

---

## 6. Summary of Open Fundamental Limitations

To ensure that the record of Article 0002 is completely transparent for subsequent human and AI review, we summarize the four fundamental limitations established by the Round-1 panel:

1. **Spacelike Nonlocality of the Shared Simplex:** Maintaining $\sum_{i=1}^N s_i(t) = 1$ across macroscopic beam-splitter arms ($L > c\tau_{\text{game}}$) and correlating simultaneous Stage-2 Bell walks ($L_A = L_B$) cannot be mediated by luminal retarded QED fields; both require a nonlocal shared ledger and a preferred foliation.
2. **Martingale Conservation vs. Ab-Initio Born Derivation:** Setting $s_i(0) = |A_i|^2/\sum_j |A_j|^2$ in Stage 1 imports the quadratic wave-intensity law from classical/semiclassical wave mechanics; Theorem 1 proves that the Stage-2 simplex martingale preserves those shares during single-click selection.
3. **Pointwise Obstruction to Exact Threshold Compensation (Proposition 1):** In continuum detectors with bandgap threshold $\theta < 1$, the backward Kolmogorov equation forbids any smooth state-dependent drift $b(s)$ from cancelling the step-function hazard $r_i(s)\mathbb{I}(s > \theta)$ across all $(s, \theta, N)$, explaining both the residual $\chi^2 = 34.16$ at $\theta = 0.72$ and the breakdown at $\theta = 0.45$ ($P_{\text{bright}} = 0.5959$).
4. **Phenomenological Status of Cross-Term Simplex Transfer:** Eliminating the $O(\epsilon^2)$ equalizing drift $(s_j - s_i)\sin^2\epsilon$ of linear unitary wave mixing requires either postulating the intensity-simplex transfer directly (Formulation 2A) or introducing a nonlinear cross-saturation counter-term (Formulation 2B).

---

## References

* Adler, R. (1946). A study of locking phenomena in oscillators. *Proc. IRE* **34**, 351–357.
* Adler, S. L., Brody, D. C., Brun, T. A., & Hughston, L. P. (2001). Martingale models for quantum state reduction. *J. Phys. A* **34**, 8795–8820.
* Afzelius, M., Simon, C., de Riedmatten, H., & Gisin, N. (2009). Multimode quantum memory based on atomic frequency combs. *Phys. Rev. A* **79**, 052329.
* Bramble, J. M., & Claude Fable 5 (Anthropic) (2026). *DiracKuramotoFramework: The Many Clocks Interpretation of Quantum Mechanics*. Public GitHub repository: `https://github.com/rayolddog/DiracKuramotoFramework`.
* Busch, P. (2003). Quantum states and generalized observables: a simple proof of Gleason's theorem. *Phys. Rev. Lett.* **91**, 120403.
* de Riedmatten, H., et al. (2008). A solid-state light–matter interface at the single-photon level. *Nature* **456**, 773–777.
* Ewens, W. J. (2004). *Mathematical Population Genetics I: Theoretical Introduction* (2nd ed.). Springer.
* Ghirardi, G. C., Pearle, P., & Rimini, A. (1990). Markov processes in Hilbert space and continuous spontaneous localization. *Phys. Rev. A* **42**, 78–89.
* Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *J. Math. Mech.* **6**, 885–893.
* Grangier, P., Roger, G., & Aspect, A. (1986). Experimental evidence for a photon anticorrelation effect on a beam splitter. *Europhys. Lett.* **1**, 173–179.
* Hahn, E. L. (1950). Spin echoes. *Phys. Rev.* **80**, 580–594.
* Hensen, B., et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature* **526**, 682–686.
* Kimura, M., & Ohta, T. (1969). The average number of generations until fixation of a mutant gene in a finite population. *Genetics* **61**, 763–771.
* Kurnit, N. A., Abella, I. D., & Hartmann, S. R. (1964). Observation of a photon echo. *Phys. Rev. Lett.* **13**, 567–568.
* Lamb, W. E., Jr., & Scully, M. O. (1969). The photoelectric effect without photons. In *Polarisation, Matière et Rayonnement*, pp. 363–369.
* Mandel, L., & Wolf, E. (1995). *Optical Coherence and Quantum Optics*. Cambridge University Press.
* Pearle, P. (1976). Reduction of the state vector by a nonlinear Schrödinger equation. *Phys. Rev. D* **13**, 857–868.
* Pearle, P. (1982). Might God toss coins? *Found. Phys.* **12**, 249–263.
* Rui, J., et al. (2020). A subradiant optical mirror formed by a single structured atomic layer. *Nature* **583**, 369–374.
* Srakaew, K., et al. (2023). A subwavelength atomic array switched by a single Rydberg atom. *Nat. Phys.* **19**, 714–719.
* Zurek, W. H. (2005). Probabilities from entanglement, Born's rule $p_k = |\psi_k|^2$ from envariance. *Phys. Rev. A* **71**, 052105.
