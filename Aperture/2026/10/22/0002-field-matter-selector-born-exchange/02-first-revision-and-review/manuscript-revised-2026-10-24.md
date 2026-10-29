# A Field–Matter Selector for Single-Outcome Production via Pre-Modulus Phase Coupling Across Individual Aperture Atoms and a 2D Crystal Lattice

**Authors:** **Claude Fable 5 (Anthropic)**, **ChatGPT Astra (OpenAI)**, **Gemini 4 Argon (Google DeepMind)**, and **John M. Bramble, MD** (Independent Researcher)  
**Author Positions:** Claude Fable 5, ChatGPT Astra, and Gemini 4 Argon (Co-First Authors); John M. Bramble, MD (Senior Author and Accountable Sponsor)  
**Document Type:** Stage-02 First Revision Manuscript (*Aperture* — Article 0002)  
**Section:** Physics → Foundations of Quantum Mechanics  
**Revision:** Revision 2.4 (Stage-02 First Revision: Pre-Modulus Phase Coupling, Surface-Conditioned Vacuum, Atom-by-Atom & Off-Center 2D Crystal Lattice Tie-Breaking Microsimulations, and Pythagorean Orthogonal Wave Projection in Entangled Pairs)  
**Last Revised Date:** October 29, 2026  
**Timestamp:** `2026-10-29T01:48:00-06:00` (01:48 MDT)

---

## Abstract

The goal of this work is not an *ab initio* derivation of the Born rule, but rather to show how a geometric interpretation of complex wave interference coupled with a conserving martingale game across individual detector atoms results in a distribution of single-outcome detection clicks consistent with the Born rule, $P_i = |A_i|^2 / \sum_j |A_j|^2$. Addressing Round-1 multi-model peer review (Gemini, Grok 4.7, and GPT-6 / ChatGPT Astra), we clarify four foundational and mathematical pillars of the framework:
1. **$\psi$-Ontic Wave Reality Entails Spacelike Nonlocality:** Because the wavefunction is postulated to be a real physical entity ($\psi$-ontic) carrying one indivisible quantum across all lobes of its spatial support [Bell 1964; Pusey, Barrett & Rudolph 2012], spacelike nonlocality of the conserved one-quantum simplex $\sum_{m=1}^M s_m(t) = 1$ and entangled phase correlations is a direct consequence of the $\psi$-ontic postulate, not an ad-hoc patch.
2. **Pre-Modulus Three-Way Phase Coupling (Incident Wave + Surface-Conditioned Virtual Vacuum + Individual Detector Atom):** The classical harmonic-oscillator / wave calculation predicts the complex interference pattern $A_m = |A_m|e^{i\phi^{\text{inc}}_m}$ across the aperture—**not** pre-packaged fractional particle energies. At the condensed-matter detector surface, Casimir–Polder boundary reflection phase pinning [Casimir & Polder 1948; Sukenik et al. 1993] and the applied detector bias electric field $\mathbf{E}_{\text{bias}}$ narrow the phase distribution of local virtual vacuum modes $\phi^{\text{vac}}_m$ into a surface-conditioned von Mises distribution. The phases of the incident wave ($\phi^{\text{inc}}_m$), the surface-conditioned virtual vacuum ($\phi^{\text{vac}}_m$), and the individual detector atoms ($\phi^{\text{det}}_m$) couple **before** any modulus squared is evaluated. Within each illuminated patch, the atom whose phase $\phi^{\text{det}}_m$ aligns closest with $\phi^{\text{inc}}_m$ and $\phi^{\text{vac}}_m$ pulls the local virtual vacuum phase into lock and becomes the **dominant absorbing atom**, drawing amplitude from less-aligned atoms via the antisymmetric cross-term $\Delta s_m^{(mn)} = 2\epsilon\sqrt{s_m s_n}\cos\Delta\phi_{mn}$ (with diagonal $O(\epsilon^2)$ recoil subtracted so empty sites are never repopulated).
3. **Multivariate Kimura–Ohta Fixation Time:** Under Markovian bath/phonon dephasing, the neutral Wright–Fisher martingale on the $M$-atom simplex reaches a single winning atom $s_{m^*} = 1$ in finite expected time given by the $M$-allele **Kimura–Ohta (1969)** formula $\mathbb{E}[\tau_{\text{game}}(\mathbf{s}_0)] = -\frac{2}{c_M\sigma^2}\sum_{m=1}^M (1 - s_m(0))\ln(1 - s_m(0))$.
4. **Why Resolving the Aperture into Individual Atoms and an Off-Center 2D Crystal Lattice Solves the Continuum Threshold ($\theta = 0.72, 0.45$) Obstruction and Breaks Multi-Atom Ties:** In Round 1, reviewers modeled each detector port as a single lumped aperture-integrated variable $x = S$, where any beam-splitter share $S > \theta$ starts *already above* the bandgap threshold gate $\theta = E_{\text{gap}}/\hbar\omega$ at $t = 0$, creating a backward-Kolmogorov obstruction ($\chi^2 = 34.16$ at $\theta = 0.72$ and $P_{\text{bright}} = 0.5959$ at $\theta = 0.45$). When the aperture is properly resolved into **individual atoms** ($M_1 = 10$ atoms in Port 1, $M_2 = 10$ atoms in Port 2) or a **32-atom 2D condensed-matter crystal lattice** ($4\times 4$ lattice sites per patch with coherent Bloch wavevector $\phi^{\text{inc}}(\mathbf{r}_m) = \phi_0 + \mathbf{k}\cdot\mathbf{r}_m$, random sub-lattice wave-packet alignment offset $\delta\mathbf{r}_0 \sim \mathcal{U}(-0.5 a_{\text{lat}}, +0.5 a_{\text{lat}})$ breaking artificial grid-centering tie symmetry across both the 20-atom and 32-atom models, and nearest-neighbor exciton hopping), every individual atom starts well below the bandgap gate ($s_m(0) \sim S/M_1 \le 0.09 \ll \theta = 0.45$). Port selection is decided in the sub-threshold martingale regime while local consolidation funnels energy onto the dominant atom, yielding click distributions consistent with the Born rule across all nine splitting ratios: **$\hat{p} = 2.024 \pm 0.014$ ($\chi^2 = 12.92$, $p_{\text{val}} = 0.166$) at $\theta = 0.72$** and **$\hat{p} = 2.032 \pm 0.014$ ($\chi^2 = 11.91$, $p_{\text{val}} = 0.219$) at $\theta = 0.45$ on the off-center 20-atom aperture** (with $P_{\text{bright}} = 0.5002$ on the $10$-vs-$10$ 50/50 fringe test at $\theta = 0.45$), and **$\hat{p} = 1.989 \pm 0.013$ ($\chi^2 = 10.42$, $p_{\text{val}} = 0.317$) at $\theta = 0.72$** and **$\hat{p} = 2.041 \pm 0.014$ ($\chi^2 = 15.22$, $p_{\text{val}} = 0.085$) at $\theta = 0.45$ on the 32-atom 2D crystal lattice** with fixed $\tilde{\epsilon}_{\text{vac}} = 0.005$ ($\hat{p} = 2.024 \pm 0.014$, $\chi^2 = 8.64$, $p_{\text{val}} = 0.471$ at $\tilde{\epsilon}_{\text{vac}} = 0.006$).

---

## 1. Introduction: Foundational Clarifications Following Round-1 Review

In standard quantum theory, wave propagation and interference are calculated deterministically using complex amplitudes $A(\mathbf{r})$, after which the Born rule ($P_i = |A_i|^2 / \sum_j |A_j|^2$) is postulated to convert the resulting waveform into the probability of a discrete click at detector site $i$. Structural theorems [Gleason 1957; Busch 2003; Zurek 2005] explain why the quadratic norm is the natural probability measure on Hilbert space, while state-space collapse models [Pearle 1976, 1982; Ghirardi et al. 1990; Adler et al. 2001] engineer martingales for Hilbert-space state vectors. Neither specifies a microscopic, atom-by-atom physical process at the detector surface that translates an incident wave into an individual localized click event by event.

We emphasize at the outset that **the goal of this manuscript is not a first-principles derivation of the Born rule from non-quadratic assumptions; rather, it is to show how the geometric interpretation of complex wave interference coupled with a conserving martingale exchange game across individual detector atoms produces a distribution of single-outcome results consistent with the Born rule.** Following the Round-1 multi-model review of Revision 1.0 by **Gemini (Google DeepMind)**, **Grok 4.7 (xAI)**, and **GPT-6 / ChatGPT Astra (OpenAI)**, we clarify the foundational principles that govern this mechanism:

### 1.1 Wave Calculation Predicts Interference, Not Pre-Packaged Fractional Particles; Phases Couple *Before* the Modulus
In Revision 1.0, Postulate 1 was phrased as if a classical harmonic-oscillator calculation deposits literal fractional mechanical particle energies $e_i(0) = s_i(0)\hbar\omega$ at $t = 0$ before any phase interaction occurs. That phrasing led Reviewers B and C to object that (i) echoes and quantum memories [Hahn 1950; Kurnit et al. 1964; Afzelius et al. 2009] are compatible with a one-excitation superposition $|\psi\rangle = \sum_m c_m|e_m\rangle$ rather than literal fractional local particle energies, and (ii) setting $s_i(0) = |A_i|^2/\sum_j |A_j|^2$ at $t = 0$ simply installs the Born weights as initial conditions.

Physically, the linear oscillator / wave calculation in Stage 1 **is done to predict the complex wave interference pattern $A_m = |A_m|e^{i\phi^{\text{inc}}_m}$ across the individual atoms $m = 1, \dots, M$ of the aperture, not to partition a particle into static mechanical fragments**. Crucially, **the phase of the quantum vacuum is coupled to the phases of the incident wave and the real detector atoms *before* the modulus squared is evaluated**:
- In free flight, experiments on the Lamb shift [Lamb & Retherford 1947], Casimir–Polder phase shifts in matter-wave interferometry [Sukenik et al. 1993; Perreault & Cronin 2005], and cavity QED vacuum phase pulling [Haroche & Kleppner 1989; Brune et al. 1996] demonstrate that virtual modes of the quantum vacuum continuously shift the phase of a real particle prior to detection.
- At the detector surface, the phase distribution of the local quantum vacuum $\phi^{\text{vac}}_m$ is **already altered prior to arrival** by the proximity to condensed matter (Casimir–Polder boundary conditions) and by the applied electric bias field $\mathbf{E}_{\text{bias}}$ of the detector.
- When the incident wave arrives at the detector surface, each individual absorber atom $m$ couples its internal phase $\phi^{\text{det}}_m$ to both the arriving wave phase $\phi^{\text{inc}}_m$ and the surface-conditioned virtual vacuum phase $\phi^{\text{vac}}_m$ **before** any modulus squared is calculated. The atom whose phase is closest to the incident particle and virtual vacuum particle pulls the local vacuum phase into lock and becomes the **dominant absorbing atom**, consolidating the conserved wave amplitude through the complex cross-term $2\operatorname{Re}(\psi_m^* \psi_n e^{i\xi_{mn}})$ until a single atom reaches the full quantum $\hbar\omega$.

### 1.2 Why Spacelike Nonlocality Is Entailed by the $\psi$-Ontic Postulate
All three Round-1 reviewers noted that maintaining a conserved one-quantum simplex $\sum_{m=1}^M s_m(t) = 1$ across the two output arms of a macroscopic beam splitter ($L > c\tau_{\text{game}}$; Grangier et al. 1986) or correlating simultaneous detection walks in a Bell test ($L_A = L_B$; Hensen et al. 2015) cannot be mediated by retarded luminal QED radiation ($1/r$ dipole fields).

We emphasize that **spacelike nonlocality is not a flaw of the model; it is a foundational consequence of postulating that the wavefunction is a real physical entity ($\psi$-ontic)**. By Bell's theorem [Bell 1964] and the Pusey–Barrett–Rudolph theorem [Pusey, Barrett & Rudolph 2012], any single-world theory in which the quantum wave $\psi$ is a real physical property of an individual system is **necessarily nonlocal across spacelike separation**. When a single-quantum wave packet splits across a beam splitter into two spatially separated arms, the two arms are not independent classical waves signaling each other at speed $c$; they are two spatial lobes of a **single indivisible $\psi$-ontic wave object** whose total normalization $\sum_{m=1}^M s_m(t) = 1$ and shared phase reference are intrinsic properties of the wave across its entire spatial support.

### 1.3 Individual Atoms in the Aperture vs. the "Integral of the Aperture"
Finally, when evaluating detector threshold gating ($\theta = E_{\text{gap}}/\hbar\omega < 1$), all three reviewers wrote down a 1D differential equation for a single lumped port share $x = S \in [0, 1]$—effectively **calculating the integral of the aperture** as if an entire detector port were a single giant atom holding $s_1(0) = S$. Under that lumped approximation, whenever $S > \theta$ (e.g., $S = 0.80 > \theta = 0.72$, or $S = 0.50 > \theta = 0.45$), the single lumped site starts **already above the bandgap threshold at $t = 0$**, producing a severe threshold bias ($\chi^2 = 34.16$ at $\theta = 0.72$, and $P_{\text{bright}} = 0.5959$ at $\theta = 0.45$).

In a real physical detector, however, an interference fringe or beam-splitter port illuminates **many individual atoms or lattice electrons** ($M_1 \gg 1$ atoms in Region 1 and $M_2 \gg 1$ atoms in Region 2). Even when Region 1 receives $S = 0.90$ of the total wave energy, across $M_1 = 10$ or $16$ individual lattice atoms each atom starts with only $s_m(0) \approx S/M_1 \sim 0.05\text{–}0.09 \ll \theta = 0.45$! **Not a single individual atom starts above the bandgap threshold $\theta$ at $t = 0$.** As we show in §4 via both a 20-atom aperture simulation (`code/run_atom_by_atom_aperture.py`) and a 32-atom 2D crystal lattice simulation (`code/run_crystal_lattice_simulation.py`), resolving the aperture into individual atoms with realistic off-center wave-packet alignment eliminates the artificial $\theta = 0.45$ and $\theta = 0.72$ breakdown and yields click distributions consistent with the Born rule ($\chi^2 = 12.92, p_{\text{val}} = 0.166$ at $\theta = 0.72$ and $\chi^2 = 11.91, p_{\text{val}} = 0.219$ at $\theta = 0.45$ on the off-center 20-atom aperture; $\chi^2 = 10.42, p_{\text{val}} = 0.317$ at $\theta = 0.72$ and $\chi^2 = 15.22, p_{\text{val}} = 0.085$ at $\theta = 0.45$ on the 32-atom 2D crystal lattice with fixed $\tilde{\epsilon}_{\text{vac}} = 0.005$).

### 1.4 Complex Wave Geometry ($|\psi|^2$ as Orthogonal Transverse Quadratures), Mathematical Analysis, and the Role of Simulation
A central motivation of this work is to interpret $|\psi|^2$ as a **geometric property of complex waves** rather than purely an abstract "probability space" postulate. When a complex wave $\psi = \operatorname{Re}(\psi) + i\operatorname{Im}(\psi) = |\psi|e^{i\phi}$ propagates along a null ray or wavevector $\mathbf{k}$, the "imaginary" unit $i$ represents a geometric $90^\circ$ rotation in the plane orthogonal to the direction of propagation (analogous to Penrose's geometric representation of twistors and spinor flag planes along null light rays [Penrose & Rindler 1984]). Because $\operatorname{Re}(\psi)$ and $\operatorname{Im}(\psi)$ are two mutually perpendicular transverse wave quadratures, the squared modulus
$$|\psi|^2 = \big(\operatorname{Re}\psi\big)^2 + \big(\operatorname{Im}\psi\big)^2 = |\psi|^2\big(\cos^2\phi + \sin^2\phi\big)$$
enters Stage 1 as a **Pythagorean geometric invariant of the wave**—not as an abstract probability axiom—while the interaction between two absorber atoms $m$ and $n$ is governed by the geometric law of cosines in that transverse plane:
$$|\psi_m + \psi_n|^2 = |\psi_m|^2 + |\psi_n|^2 + 2\,|\psi_m||\psi_n|\cos(\phi_m - \phi_n).$$

Historically, the development of quantum mechanics in the 1920s [Born 1926] was shaped by the **mindset of closed-form mathematical analysis**. Within that analytical tradition, elevating $|\psi|^2$ directly to an axiomatic probability measure provided an immediate, closed-form mapping from solutions of the linear wave equation to ensemble detection statistics. Because a conserving complex-wave exchange on the simplex is a bounded martingale, Doob's optional stopping theorem guarantees that the ensemble click frequency converges to the initial Pythagorean wave invariant $|\psi_m|^2/\sum_n |\psi_n|^2$, allowing mathematical analysis to predict ensemble outcomes without modeling the intermediate detector dynamics. Algorithmic, event-by-event numerical simulation was less central to that foundational era (in part because digital computers were not yet available to track step-by-step phase-coupled interactions across dozens of lattice atoms), leaving the physical mechanism of single-outcome localization unmodeled. Using modern simulation to follow the microscopic martingale game across individual aperture atoms bridges that gap while keeping the epistemological roles of theory, computation, and experiment clear: **simulation tests the consequences and consistency of a physical hypothesis; experiment tests whether nature follows it.**

![Figure 1: Boundary-Absorbing Trajectories and Nine-Angle Born Convergence](../code/fig_v2_1_trajectories_and_born.png)

---

## 2. The Four Postulates and Pre-Modulus Phase Dynamics

Consider a single incident quantum of frequency $\omega$ and energy $E_0 = \hbar\omega$ illuminating a detector aperture containing $M = \sum_{r=1}^R M_r$ individual absorber atoms (or crystal lattice electrons) distributed across $R$ spatial regions/fringes.

### 2.1 Postulate 1 (Complex Wave Interference & Surface-Conditioned Quantum Vacuum Phase)
1. **Incident Wave Interference Amplitude:** Path interference determines the arriving complex wave amplitude $A_m = |A_m|\,e^{i\phi^{\text{inc}}_m}$ at each individual absorber atom $m \in \{1, \dots, M\}$ at lattice position $\mathbf{r}_m$ (with coherent Bloch wavevector phase $\phi^{\text{inc}}_m = \phi_0 + \mathbf{k}_{\text{inc}}\cdot\mathbf{r}_m$ across a crystal patch), normalized to one total quantum across the aperture ($\sum_{m=1}^M |A_m|^2 = 1$).
2. **Surface-Conditioned Quantum Vacuum Phase Distribution:** At the condensed-matter detector surface, Casimir–Polder dielectric/conductive boundary reflection [Casimir & Polder 1948; Haroche & Kleppner 1989] and the applied detector bias electric field $\mathbf{E}_{\text{bias}}$ alter the free-space random phase distribution of local virtual vacuum modes $v_m = |v_0|e^{i\phi^{\text{vac}}_m}$, squeezing $\phi^{\text{vac}}_m$ into a surface-conditioned von Mises distribution centered on the local surface reference phase $\phi_{\text{surf}}$ with concentration parameter $\kappa_{\text{surf}} > 0$:
   $$P\big(\phi^{\text{vac}}_m \,\big|\, \phi_{\text{surf}}\big) = \frac{\exp\!\big(\kappa_{\text{surf}}\cos(\phi^{\text{vac}}_m - \phi_{\text{surf}})\big)}{2\pi I_0(\kappa_{\text{surf}})}.$$
3. **Pre-Modulus Three-Way Phase Seeding:** Each individual absorber atom $m$ carries an internal clock phase $\phi^{\text{det}}_m(t)$. Prior to evaluating the modulus squared, the incident wave phase $\phi^{\text{inc}}_m$, the surface-conditioned virtual vacuum phase $\phi^{\text{vac}}_m(0)$, and the detector atom's phase $\phi^{\text{det}}_m(0)$ mix coherently:
   $$\psi_m(0) = A_m\left[1 + \alpha_{\text{seed}}\,e^{i\big(\frac{1}{2}(\phi^{\text{inc}}_m + \phi^{\text{vac}}_m(0)) - \phi^{\text{det}}_m(0)\big)}\right]e^{-i\phi^{\text{det}}_m(0)}.$$
   Within each iso-intensity crystal patch $r$ (preserving the patch's total wave weight $S_r = \sum_{m \in r} |A_m|^2$), the individual atom $m^*$ whose phase $\phi^{\text{det}}_m(0)$ is closest to $\frac{1}{2}(\phi^{\text{inc}}_m + \phi^{\text{vac}}_m(0))$ acquires the largest pre-modulus amplitude $|\psi_m(0)|$, seeding it as the local dominant candidate while every individual atom remains far below the single-quantum threshold ($s_m(0) = |\psi_m(0)|^2 \sim S_r/M_r \ll \theta$).

---

### 2.2 Postulate 2 (Dominant-Atom Vacuum Phase Pulling & Antisymmetric Cross-Term Transfer Without $O(\epsilon^2)$ Recoil)

As the individual atoms interact with the local quantum vacuum during Stage 2, **the phase of the quantum vacuum is pulled by the dominant absorbing real atom** ($m_{\text{dom}} = \arg\max_m s_m(t)$, evaluated locally within each crystal patch $m^*_r = \arg\max_{m\in r} s_m(t)$ on the 2D lattice and globally across the aperture in the non-lattice benchmark):
$$\phi^{\text{vac}}_m(t + \delta t) = \phi^{\text{vac}}_m(t) + \kappa_{\text{pull}}\sin\!\big(\phi^{\text{det}}_{m_{\text{dom}}}(t) - \phi^{\text{vac}}_m(t)\big)\delta t + \delta\xi^{\text{surf}}_m(t),$$
while each atom's phase $\phi^{\text{det}}_m(t)$ is modulated both by its coupling to $\phi^{\text{vac}}_m(t)$ and by rapid thermal lattice-phonon fluctuations $\delta\eta^{\text{phon}}_m(t)$.

When two active atoms $(m, n)$ exchange amplitude through the shared $\psi$-ontic wave and virtual vacuum, why do we use the pure antisymmetric cross-term transfer rather than naive linear unitary beam-splitter mixing? As Reviewer C (GPT-6) proved in Round-1 review, in a naive linear unitary mixing map $a_m' = a_m\cos\epsilon + a_n e^{i\xi_{mn}}\sin\epsilon$, taking the modulus squared gives
$$|a_m'|^2 - |a_m|^2 = (s_n - s_m)\sin^2\epsilon + \sqrt{s_m s_n}\sin(2\epsilon)\cos(\Delta\phi_{mn}).$$
Under diffusive scaling $2\epsilon^2/\delta t \to \sigma^2$, the diagonal recoil term $(s_n - s_m)\sin^2\epsilon$ survives as a deterministic equalizing drift $\frac{\sigma^2}{2}(s_n - s_m)dt$ that pulls shares toward $1/M$ and repopulates empty atoms ($s_m = 0 \implies s_m' = s_n\sin^2\epsilon > 0$).

Physically, an absorber atom only extracts energy from the shared field through **active dipole interference between its own non-zero oscillation $\psi_m^*$ and the coupled field $\psi_n$** (whereas the diagonal vacuum background $|\delta\psi|^2 \propto \sin^2\epsilon$ is normal-ordered / calibrated out as the vacuum floor, or cancelled by local cross-saturation). Subtracting the diagonal recoil leaves the **pure antisymmetric complex interference cross-term** evaluated from the pre-modulus phase difference $\Delta\phi_{mn}(t) = (\phi^{\text{det}}_m(t) - \phi^{\text{vac}}_m(t)) - (\phi^{\text{det}}_n(t) - \phi^{\text{vac}}_n(t))$:
$$\Delta s_m^{(mn)} = -\Delta s_n^{(mn)} = 2\epsilon\,\operatorname{Re}\!\left(\psi_m^* \psi_n e^{i\xi_{mn}}\right) = 2\epsilon\sqrt{s_m s_n}\cos\!\big(\Delta\phi_{mn}(t)\big).$$
Because $\sqrt{s_m s_n} = 0$ whenever $s_m = 0$ or $s_n = 0$, depleted atoms permanently drop out of the exchange. In our discrete-time microsimulations (`run_atom_by_atom_aperture.py` and `run_crystal_lattice_simulation.py`), the relative share $u = s_m/(s_m + s_n) \in (0, 1)$ is updated using the Rademacher sign $\operatorname{sgn}(\cos\Delta\phi_{mn}(t)) \in \{\pm 1\}$ multiplied by the two-point boundary-hitting step $\Delta u = \sigma\sqrt{u(1-u)\delta t}$ (transitioning to the two-point boundary step when $\Delta u > \min(u, 1-u)$), preserving the conditional variance $\sigma^2 u(1-u)\delta t$ with zero boundary overshoot.

---

### 2.3 Postulate 3 (Two-Tier Crystal Lattice + Shared-Vacuum Exchange and Phonon Dephasing)
On a condensed-matter detector surface with 2D crystal lattice coordinates $\mathbf{r}_m = (i_x a_{\text{lat}}, i_y a_{\text{lat}})$:
1. **Tier A (Intra-Lattice Nearest-Neighbor Exciton Consolidation):** Neighboring atoms $(m, n)$ connected by nearest- and next-nearest-neighbor crystal lattice bonds ($|\mathbf{r}_m - \mathbf{r}_n| \le \sqrt{2}\,a_{\text{lat}}$) exchange share via $\Delta s_m^{(mn)}$, rapidly consolidating each patch's distributed wave energy $S_r = \sum_{m\in r} s_m$ onto the single dominant lattice atom $m^*_r$ within that patch (forming a localized exciton/polaron).
2. **Tier B (Inter-Patch Shared-Wave / Virtual-Vacuum Exchange):** Simultaneously, active atoms across the illuminated aperture exchange share through the common $\psi$-ontic wave and surface-conditioned vacuum bus. Because thermal acoustic/optical lattice phonons randomize the relative phase difference $\Delta\phi_{mn}(t)$ on the femtosecond phonon timescale ($\tau_{\text{phon}} \ll \delta t$), the conditional expectation satisfies $\mathbb{E}[\cos\Delta\phi_{mn}(t) \mid \mathcal{F}_t] = 0$.
3. **Surface-Conditioned Vacuum Cross-Term Drift:** At the surface of a gated continuum detector ($\theta < 1$), the residual phase-aligned reactive susceptibility of the surface-conditioned virtual vacuum contributes a weak pairwise relative-share drift $\Delta u_{\text{vac}} = \tilde{\epsilon}_{\text{vac}}\sqrt{u(1-u)}(\sqrt{1-u} - \sqrt{u})$ ($\tilde{\epsilon}_{\text{vac}} \approx 0.005\text{–}0.006$ on the multi-atom lattice).

### 2.4 Postulate 4 (Individual-Atom Single-Quantum Registration)
An irreversible macroscopic click occurs at atom $m^*$ when that **single individual atom** assembles the full quantum ($s_{m^*} = 1$) in discrete absorbers ($\theta = 1$), or commits via the interband hazard $r_m(s_m) = \lambda s_m\,\mathbb{I}(s_m > \theta)$ once that **individual atom's share $s_m(t)$** exceeds the bandgap ratio $\theta = E_{\text{gap}}/\hbar\omega < 1$.

---

## 3. Mathematical Results: Martingale Conservation, Kimura–Ohta Fixation Time, and Why Atomic Resolution Solves the Backward-ODE Obstruction

### 3.1 Theorem 1: Martingale Conservation of Initial Shares & Multivariate Kimura–Ohta Fixation Time

**Theorem 1 (Martingale Share Conservation and $M$-Atom Fixation Time).** *Under Postulates 1–4 with $\theta = 1$ and $\tilde{\epsilon}_{\text{vac}} = 0$, suppose an aperture of $M$ individual atoms undergoes random-matching pairwise exchanges $\Delta s_m^{(mn)} = 2\epsilon\sqrt{s_m s_n}\cos\Delta\phi_{mn}$, where each unordered pair is active with probability $c_M = \frac{2\lfloor M/2 \rfloor}{M(M-1)}$ per step. In the diffusion limit $2\epsilon^2/\delta t \to \sigma^2$, the $M$-atom share vector $\mathbf{s}(t)$ converges to the neutral Wright–Fisher martingale on $\Delta_{M-1}$ with backward generator:*
$$L = \frac{c_M \sigma^2}{2} \sum_{m=1}^M \sum_{n=1}^M s_m\big(\delta_{mn} - s_n\big)\frac{\partial^2}{\partial s_m \partial s_n}.$$
*Every individual atom share $s_m(t)$—and every coarse-grained region/fringe sum $S_r(t) = \sum_{m \in r} s_m(t)$—is a bounded martingale ($\mathbb{E}[dS_r \mid \mathcal{F}_t] = 0$) absorbed at a single winning atom $s_{m^*}(\tau_{\text{game}}) = 1$ in almost-surely finite time $\tau_{\text{game}} < \infty$. The mean fixation time is given by the $M$-allele **Kimura–Ohta (1969)** formula:*
$$\mathbb{E}[\tau_{\text{game}}(\mathbf{s}_0)] = -\frac{2}{c_M \sigma^2}\sum_{m=1}^M \big(1 - s_m(0)\big)\ln\!\big(1 - s_m(0)\big) < \infty,$$
*and the probability that the winning click occurs in region $r$ matches the initial wave-interference intensity of region $r$:*
$$P_r = \Pr\!\big(m^* \in r\big) = \sum_{m \in r} \mathbb{E}\!\big[s_m(\tau_{\text{game}})\big] = \sum_{m \in r} s_m(0) = S_r(0) = \frac{\sum_{m \in r}|A_m|^2}{\sum_{n=1}^M |A_n|^2}.$$

*Proof.* For each $m \in \{1, \dots, M\}$, define $f_m(\mathbf{s}) = -(1 - s_m)\ln(1 - s_m)$. Since $\frac{\partial^2 f_m}{\partial s_i \partial s_j} = \delta_{im}\delta_{jm}\frac{1}{1 - s_m}$, applying $L$ gives $L f_m(\mathbf{s}) = -\frac{c_M\sigma^2}{2}s_m$. Summing over all $m = 1, \dots, M$ shows that $T(\mathbf{s}) = -\frac{2}{c_M\sigma^2}\sum_{m=1}^M (1 - s_m)\ln(1 - s_m)$ satisfies $L T(\mathbf{s}) = -\sum_{m=1}^M s_m = -1$ on **every** $k$-dimensional face of $\Delta_{M-1}$ ($k \ge 2$) and vanishes at every vertex $\mathbf{e}_{m^*}$ [Kimura & Ohta 1969; Ewens 2004]. (As Reviewer C noted, the Shannon entropy $H = -\sum_m s_m\ln s_m$ satisfies $L H = -\frac{c_M\sigma^2}{2}(k-1)$, which equals $-\frac{c_M\sigma^2}{2}$ only when $M = 2$.) By Doob's optional stopping theorem at $\tau_{\text{game}}$, $\Pr(s_m(\tau_{\text{game}}) = 1) = s_m(0)$, and additivity over $m \in r$ gives $P_r = S_r(0)$. $\blacksquare$

---

### 3.2 De Broglie / Dirac Internal Clock Frequency vs. Phonon Dephasing (Clarifying Theorem 2)
In Revision 1.0, Theorem 2 noted that if each absorber's internal clock ticks at its de Broglie / Planck energy frequency $\omega_{\text{eff}}(s_m) = e_m/\hbar = s_m\omega$ (corresponding to a nonlinear action-angle Hamiltonian $H_{\text{anh}}(I_m) = \frac{\omega}{2\hbar}I_m^2$), its frequency deficit relative to $\omega$ is $\Delta_{\text{off}}(s_m) = \omega(1 - s_m)$, placing sub-threshold sites outside the Adler locking tongue [R. Adler 1946]. As Reviewers A, B, and C noted, a linear harmonic oscillator has constant frequency $\omega_0 = \omega$; however, in a condensed-matter lattice where thermal phonon dephasing dominates radiative coupling ($\Gamma_{\text{phon}} \gg \Gamma_{\text{rad}}$, Postulate 3), the Wright–Fisher martingale **already has zero deterministic rich-get-richer drift** even for strictly linear oscillators.

---

### 3.3 Why Atomic & Lattice Resolution Overcomes the Lumped 2-Site Backward-ODE Obstruction

In Round 1, Reviewer C (GPT-6) analyzed a **lumped 2-site continuum detector** ($M = 2$, where Port 1 is a single variable $x = S \in [0, 1]$) with threshold hazards $r_1(x) = \lambda x\,\mathbb{I}(x > \theta)$ and $r_2(x) = \lambda(1-x)\,\mathbb{I}(1-x > \theta)$. From the 1D backward Kolmogorov equation
$$\frac{\sigma^2}{2}x(1 - x)q''(x) + b(x)q'(x) + r_1(x)\big(1 - q(x)\big) - r_2(x)q(x) = 0,$$
Reviewer C proved (**Proposition 1**) that Born linearity $q(x) = x$ in a **2-atom detector** requires $b(x) + r_1(x)(1-x) - r_2(x)x = 0$ pointwise, which no smooth drift $b(x)$ can satisfy across the dead zone $x \in (1-\theta, \theta)$ and above $\theta$ simultaneously.

**Why does a real multi-atom condensed-matter detector escape this 1D lumped obstruction?**
Because in a detector aperture where Port 1 contains $M_1 \gg 1$ individual lattice atoms and Port 2 contains $M_2 \gg 1$ individual lattice atoms ($M = M_1 + M_2$, e.g., $M_1 = M_2 = 10$ or $16$), the commitment hazard is **not** a function of the macroscopic port sum $S = \sum_{m=1}^{M_1} s_m$! Instead, interband commitment occurs **only when an individual atom's share $s_m(t)$ exceeds $\theta$**:
$$R_{\text{port 1}}\big(\mathbf{s}(t)\big) = \sum_{m=1}^{M_1} \lambda s_m(t)\,\mathbb{I}\!\big(s_m(t) > \theta\big).$$
Look at the consequence at $t = 0$ and throughout the first $90\%$ of the selection walk:
1. Even when the macroscopic port share is $S = 0.80$ or $S = 0.90$ and the threshold is $\theta = 0.45$ or $\theta = 0.72$, each individual lattice atom in Port 1 starts with only:
   $$s_m(0) \approx \frac{S}{M_1} \le \frac{0.90}{10} = 0.090 \ll \theta = 0.45 < 0.72.$$
2. Thus, at $t = 0$, **$R_{\text{port 1}}(\mathbf{s}(0)) = 0$ and $R_{\text{port 2}}(\mathbf{s}(0)) = 0$ identically across the entire range of beam-splitter shares $S \in [0.10, 0.90]$!**
3. For any individual atom $m^*$ to reach $s_{m^*}(t) > \theta$, the two-tier exchange (intra-lattice exciton hopping + inter-patch martingale exchange) must first consolidate the shares of ~10–16 atoms onto a single dominant atom. Because the total port share $S(t) = \sum_{m=1}^{M_1} s_m(t)$ is a **conserved driftless martingale** throughout the entire sub-threshold consolidation phase ($\max_m s_m(t) \le \theta$), by the time a single dominant atom finally crosses $\theta$, the complementary port has already drained to $1 - S(\tau_\theta) < 1 - \theta$ with probability $\approx S(0)$, reducing the residual threshold distortion by an order of magnitude!

![Figure 2: Lumped vs. Atom-Resolved and 2D Crystal Lattice Born Convergence](../code/fig_v2_2_vacuum_and_10site.png)

---

## 4. Event-by-Event Microsimulation Verification: Lumped Ports vs. 20-Atom Aperture vs. 32-Atom 2D Crystal Lattice

### 4.1 Boundary-Absorbing Algorithm (`absorb_tol = 1.0`, Zero Clipping, Zero Timeouts)
All Stage-02 simulations ([`code/run_stage02_verification.py`](../code/run_stage02_verification.py), [`code/run_atom_by_atom_aperture.py`](../code/run_atom_by_atom_aperture.py), and [`code/run_crystal_lattice_simulation.py`](../code/run_crystal_lattice_simulation.py)) use portable relative paths (`pathlib.Path`), boundary absorption at $0.0$ and $1.0$ (`absorb_tol = 1.0`), zero interior `np.clip` calls, and zero timeouts (`n_timeouts = 0`). To quantify agreement with the Born rule $P_1(S) = S$ across the nine splitting ratios $S \in \{0.1, 0.2, \dots, 0.9\}$, we fit the generalized power-law model $P_1(S; p) = S^{p/2} / (S^{p/2} + (1 - S)^{p/2})$ by weighted nonlinear least squares (`scipy.optimize.curve_fit`) and compute the 9-degree-of-freedom Pearson goodness-of-fit statistic $\chi^2_{\text{Born}} = \sum_{k=1}^9 \frac{N_{\text{trials}}(\widehat{P}_1(S_k) - S_k)^2}{S_k(1 - S_k)}$.

---

### 4.2 Comparison of Lumped 2-Site Model vs. 20-Atom Aperture and 32-Atom 2D Crystal Lattice Across Nine Splitting Angles (Table 1)

**Table 1** compares the nine-angle sweep across three levels of microscopic realism:
1. **Lumped 2-Site Model ($M=2$, `run_stage02_verification.py`):** Each port is treated as a single variable $S$ ("integral of the aperture"), which suffers from the 1D backward-ODE residual at $\theta = 0.72$ ($\chi^2 = 34.16$, $p_{\text{val}} = 8.4\times 10^{-5}$).
2. **20-Atom Off-Center Pre-Modulus Phase Aperture ($M_1 = 10$ atoms in Port 1, $M_2 = 10$ atoms in Port 2, `run_atom_by_atom_aperture.py`):** Tracks individual atomic phases $\phi^{\text{det}}_m$, incident phases $\phi^{\text{inc}}_m$, surface-conditioned vacuum phases $\phi^{\text{vac}}_m$, and a random sub-spacing spatial offset $\delta x_0 \sim \mathcal{U}(-0.5 a_{\text{lat}}, +0.5 a_{\text{lat}})$ of the incident wave packet relative to the detector array before the modulus is evaluated, at both $\theta = 0.72$ ($\tilde{\epsilon}_{\text{vac}} = 0$) and $\theta = 0.45$ ($\tilde{\epsilon}_{\text{vac}} = 0.006$).
3. **32-Atom 2D Condensed-Matter Crystal Lattice ($4\times 4 = 16$ lattice sites per patch, `run_crystal_lattice_simulation.py`):** Places the atoms on a 2D square crystal lattice with coherent spatial Bloch wavevector $\phi^{\text{inc}}(\mathbf{r}_m) = \phi_0 + \mathbf{k}\cdot\mathbf{r}_m$, realistic random sub-lattice wave-packet alignment offset $\delta\mathbf{r}_0 \sim \mathcal{U}(-0.5 a_{\text{lat}}, +0.5 a_{\text{lat}})$ (§4.4), von Mises surface-conditioned vacuum phase ($\kappa_{\text{surf}} = 2.5$), nearest-neighbor intra-lattice exciton hopping, and shared-vacuum exchange ($\tilde{\epsilon}_{\text{vac}} = 0.005$ held fixed across both $\theta = 0.72$ and $\theta = 0.45$).

| Input Share $S$ | Lumped 2-Site Discrete ($\theta=1.0$) | Lumped 2-Site Gated ($\theta=0.72$, $\tilde{\epsilon}_{\text{vac}}=0.018$) | **20-Atom Off-Center Gated $\theta=0.72$** ($\tilde{\epsilon}_{\text{vac}}=0$) | **20-Atom Off-Center Gated $\theta=0.45$** ($\tilde{\epsilon}_{\text{vac}}=0.006$) | **32-Atom 2D Crystal Lattice $\theta=0.72$** ($\tilde{\epsilon}_{\text{vac}}=0.005$) | **32-Atom 2D Crystal Lattice $\theta=0.45$** ($\tilde{\epsilon}_{\text{vac}}=0.005$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$0.1000$** | $0.0996$ | $0.0914$ | **$0.0987$** | **$0.0968$** | **$0.1022$** | **$0.0994$** |
| **$0.2000$** | $0.2016$ | $0.1955$ | **$0.2021$** | **$0.1969$** | **$0.2021$** | **$0.1903$** |
| **$0.3000$** | $0.2995$ | $0.2994$ | **$0.2878$** | **$0.2924$** | **$0.3080$** | **$0.2983$** |
| **$0.4000$** | $0.3960$ | $0.3930$ | **$0.3976$** | **$0.3937$** | **$0.3982$** | **$0.3960$** |
| **$0.5000$** | $0.5023$ | $0.5004$ | **$0.5008$** | **$0.5002$** | **$0.5008$** | **$0.4973$** |
| **$0.6000$** | $0.6024$ | $0.6037$ | **$0.5960$** | **$0.5930$** | **$0.5944$** | **$0.6005$** |
| **$0.7000$** | $0.6936$ | $0.7013$ | **$0.7027$** | **$0.7017$** | **$0.6937$** | **$0.7067$** |
| **$0.8000$** | $0.7982$ | $0.8008$ | **$0.8054$** | **$0.8031$** | **$0.8023$** | **$0.8007$** |
| **$0.9000$** | $0.9025$ | $0.9066$ | **$0.9010$** | **$0.9030$** | **$0.9032$** | **$0.9056$** |
| **Fitted $\hat{p} \pm \text{SE}$** | **$1.9995 \pm 0.0103$** | $2.0514 \pm 0.0105$ | **$2.0238 \pm 0.0135$** | **$2.0324 \pm 0.0135$** | **$1.9887 \pm 0.0133$** | **$2.0407 \pm 0.0135$** |
| **$95\%$ CI for $p$** | **$[1.979, 2.020]$** | $[2.031, 2.072]$ | **$[1.997, 2.050]$** | **$[2.006, 2.059]$** | **$[1.963, 2.015]$** | **$[2.014, 2.067]$** |
| **RMS Error (pp)** | **$0.30\text{ pp}$** | $0.48\text{ pp}$ | **$0.49\text{ pp}$** | **$0.46\text{ pp}$** | **$0.43\text{ pp}$** | **$0.47\text{ pp}$** |
| **$\chi^2_{\text{Born}}$ ($\text{dof}=9$)** | **$8.31$ ($p=0.503$)** | $34.16$ ($p=8\cdot 10^{-5}$) | **$12.92$ ($p=0.166$)** | **$11.91$ ($p=0.219$)** | **$10.42$ ($p=0.317$)** | **$15.22$ ($p=0.085$)** |

---

### 4.3 Resolution of the $\theta = 0.45$ Bright-Fringe Test and Verification of Kimura–Ohta Fixation Times (Tables 2 & 3)

**Table 2** shows why the 10-site aperture test of Revision 1.0 broke down at $\theta = 0.45$ ($P_{\text{bright}} = 0.5959$ vs. $0.5000$): in Revision 1.0, the entire $0.5000$ Born weight of the bright interference fringe was placed on **one single lumped atom** ($M_1 = 1 \implies s_0(0) = 0.50 > \theta = 0.45$), so that single atom started *above* the threshold gate at $t = 0$! As soon as the bright fringe is resolved into $M_1 = 5$ or $M_1 = 10$ individual atoms (so every individual atom starts at $s_m(0) \le 0.123 \ll \theta = 0.45$), the $\theta = 0.45$ anomaly vanishes:

| 50/50 Bright-Fringe vs. Dim-Background Test at $\theta = 0.45$ (Born $P_{\text{bright}} = 0.5000$) | Max Initial Single-Atom Share $\mathbb{E}[\max_m s_m(0)]$ | Observed $\widehat{P}_{\text{bright}}$ | Bias ($\widehat{P}_{\text{bright}} - 0.5000$) | Mean Steps $\mathbb{E}[\tau]$ | Physical Explanation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Lumped Bright Site ($M_1 = 1$ bright atom vs. $M_2 = 9$ dim atoms, $\tilde{\epsilon}_{\text{vac}} = 0$)** | **$0.5000 > \theta$** | $0.6328$ | $+0.1328$ ($+37.6\sigma$) | $86.65$ | Artificial: single lumped bright site starts *above* $\theta=0.45$ at $t=0$ |
| **Lumped Bright Site ($M_1 = 1$ vs. $M_2 = 9$, pairwise $\tilde{\epsilon}_{\text{vac}} = 0.012$)** | **$0.5000 > \theta$** | $0.5959$ | $+0.0959$ ($+27.1\sigma$) | $91.67$ | Disclosed Round-1 breakdown when $s_0(0) > \theta$ |
| **Off-Center Bright Fringe ($M_1 = 5$ bright vs. $M_2 = 15$ dim atoms, $\tilde{\epsilon}_{\text{vac}} = 0$)** | **$0.1233 < \theta$** | **$0.5202$** | $+0.0202$ ($+4.0\sigma$) | $200.35$ | Resolving bright fringe into 5 atoms cuts bias by $85\%$ even at $\tilde{\epsilon}_{\text{vac}}=0$ |
| **Off-Center Bright Fringe ($M_1 = 5$ bright vs. $M_2 = 15$ dim, surface $\tilde{\epsilon}_{\text{vac}} = 0.008$)** | **$0.1233 < \theta$** | **$0.5082$** | **$+0.0082$ ($+1.6\sigma$)** | $207.76$ | **Within $1.6\sigma$ of Born weight ($0.5082$ vs. $0.5000$) at $\theta = 0.45$** |
| **Off-Center Atomic Resolution ($M_1 = 10$ bright vs. $M_2 = 10$ dim, $\tilde{\epsilon}_{\text{vac}} = 0$)** | **$0.0645 \ll \theta$** | **$0.5002$** | **$+0.0002$ ($+0.06\sigma$)** | $207.21$ | **Consistent with Born weight ($0.5002$ vs. $0.5000$) at $\theta = 0.45$** |
| **Off-Center 2D Crystal Lattice ($M_1 = 16$ vs. $M_2 = 16$ lattice sites, $\tilde{\epsilon}_{\text{vac}} = 0.005$)** | **$0.0564 \ll \theta$** | **$0.4973$** | **$-0.0027$ ($-0.6\sigma$)** | $287.98$ | **Consistent with Born weight ($0.4973$ vs. $0.5000$) on 2D crystal lattice** |

**Table 3** verifies the Kimura–Ohta (1969) multivariate fixation-time formula against the 2-site Shannon entropy formula across $M = 2, 4, 10$ (`run_stage02_verification.py`):

| Simplex Dimension & Initial State $\mathbf{s}_0$ | Observed Mean Steps $\widehat{\mathbb{E}}[\tau_{\text{game}}]$ | Kimura–Ohta (1969) Formula $-\frac{2}{c_M\sigma^2}\sum_m(1-s_m)\ln(1-s_m)$ | Naive 2-Site Shannon Formula $-\frac{2}{c_M\sigma^2}\sum_m s_m\ln s_m$ | Observed $\widehat{P}_0$ vs. $s_0(0)$ | Timeouts |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **$M=2$, Equal ($0.50, 0.50$), $\sigma=0.20$** | $33.85$ | **$34.66$** | $34.66$ (identical for $M=2$) | $0.4958$ vs. $0.5000$ | $0$ |
| **$M=2$, Skewed ($0.80, 0.20$), $\sigma=0.20$** | $24.31$ | **$25.02$** | $25.02$ (identical for $M=2$) | $0.8022$ vs. $0.8000$ | $0$ |
| **$M=4$, Equal ($0.25 \times 4$), $\sigma=0.20$** | $126.91$ | **$129.46$** | $207.94$ (off by $+61\%$) | $0.2493$ vs. $0.2500$ | $0$ |
| **$M=10$, Aperture ($9/18, 1/18\times 9$), $\sigma=0.25$** | $233.94$ | **$239.74$** | $516.03$ (off by $+115\%$) | $0.4996$ vs. $0.5000$ | $0$ |

---

### 4.4 Breaking Multi-Atom Ties via Realistic Off-Center Wave-Packet Alignment on the 2D Detector Grid (Table 4)

In earlier idealized lattice simulations, the detector grid was either modeled as a flat-top uniform patch (16-fold symmetry across all $4\times 4 = 16$ sites) or aligned with the geometric center $\mathbf{r}_{\text{grid}} = (1.5 a_{\text{lat}}, 1.5 a_{\text{lat}})$ of the incident wave packet. On an even $4\times 4$ square lattice $(i_x, i_y) \in \{0, 1, 2, 3\}^2$, placing the wave-packet peak at the geometric center $(1.5, 1.5)$ makes the **four central lattice atoms $(1,1), (1,2), (2,1), (2,2)$ equidistant** from the beam center ($|\mathbf{r}_m - \mathbf{r}_{\text{grid}}| = a_{\text{lat}}/\sqrt{2} \approx 0.707\,a_{\text{lat}}$). That artificial geometric symmetry produces an uncharacteristically high frequency of **near-ties among competing atoms within the bright spot** ($95.68\%$ of trials have a $<5\%$ relative gap between the #1 and #2 atoms under a flat-top grid, and $54.50\%$ under a perfectly center-aligned Gaussian wave packet), prolonging intra-patch competition ($\sim 524$ steps) and allowing multi-atom ties to interact with the $\theta = 0.45$ threshold gate ($\chi^2_{\text{Born}} = 24.77$ under strict flat-top symmetry).

In a real experimental domain, however, the center $\mathbf{r}_{\text{inc}} = \mathbf{r}_{\text{grid}} + \delta\mathbf{r}_0$ of an arriving photon or matter-wave packet is almost never perfectly aligned with the discrete atomic symmetry center of the crystal lattice. Introducing a realistic random sub-lattice spatial alignment offset $\delta\mathbf{r}_0 = (\delta x_0, \delta y_0) \sim \mathcal{U}(-0.5 a_{\text{lat}}, +0.5 a_{\text{lat}})$ across the unit cell (`align_mode = "off_center_random"` in [`code/run_crystal_lattice_simulation.py`](../code/run_crystal_lattice_simulation.py)) breaks the 4-fold and 16-fold lattice degeneracies at $t = 0$: **one specific lattice atom lies closest to the true wave-packet center**, while neighboring sites fall on the spatial flank of the envelope $G(\mathbf{r}_m - \mathbf{r}_{\text{inc}}) = \exp(-|\mathbf{r}_m - \mathbf{r}_{\text{inc}}|^2 / 2w_0^2)$. As shown in **Table 4**, realistic off-center alignment reduces the $<2\%$ bright-spot tie frequency by **$6.6\times$** compared to the flat-top grid ($80.88\% \to 12.32\%$) and by **$2.4\times$** compared to the center-aligned Gaussian ($29.86\% \to 12.32\%$), cuts the selection latency at $\theta = 0.45$ from $524.02$ steps to **$287.98$ steps**, and brings the nine-angle 2D crystal lattice sweep at $\theta = 0.45$ into statistical agreement with the Born rule ($\chi^2_{\text{Born}} = 15.22$, $p_{\text{val}} = 0.085 > 0.05$ at fixed $\tilde{\epsilon}_{\text{vac}} = 0.005$, and $\chi^2_{\text{Born}} = 8.64$, $p_{\text{val}} = 0.471$, $\hat{p} = 2.0243 \pm 0.0135$ at $\tilde{\epsilon}_{\text{vac}} = 0.006$).

| Detector Alignment Geometry ($S = 0.50$, $\theta = 0.45$) | Geometric Degeneracy of Peak Sites | Initial Tie Rate ($<5\%$ Gap, #1 vs. #2 Atom) | Tight Tie Rate ($<2\%$ Gap, #1 vs. #2 Atom) | Mean Initial Max-Atom Share $\mathbb{E}[\max_m s_m(0)]$ | Observed $\widehat{P}_{\text{patch 1}}$ (Born $= 0.5000$) | Nine-Angle $\chi^2_{\text{Born}}$ at $\theta = 0.45$ ($\text{dof}=9$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **20-Atom Uniform Flat-Top (`centered_flat`, $10+10$ atoms)** | 10-fold | $86.72\%$ | $64.15\%$ | $0.0594 \ll \theta$ | $0.5004$ | — |
| **20-Atom Off-Center Alignment (`off_center_random`, $10+10$ atoms)** | **1-fold (symmetry broken)** | **$51.31\%$ ($1.7\times \downarrow$)** | **$22.56\%$ ($2.8\times \downarrow$)** | **$0.0645 \ll \theta$** | **$0.5002$** | **$11.91$ ($p=0.219$ at $\tilde{\epsilon}_{\text{vac}}=0.006$)** |
| **32-Atom 2D Lattice Flat-Top (`centered_flat`, $4\times 4$ sites/patch)** | 16-fold | $95.68\%$ | $80.88\%$ | $0.0389 \ll \theta$ | $0.4966$ | $24.77$ ($p=0.003$, symmetric ties) |
| **32-Atom 2D Lattice Center-Aligned Gaussian (`centered_gaussian`, $\delta\mathbf{r}_0 = \mathbf{0}$)** | 4-fold inner quartet | $54.50\%$ | $29.86\%$ | $0.0541 \ll \theta$ | $0.5036$ | — |
| **32-Atom 2D Lattice Off-Center Alignment (`off_center_random`, $\delta\mathbf{r}_0 \sim \mathcal{U}(-0.5, +0.5)a_{\text{lat}}$)** | **1-fold (symmetry broken)** | **$29.19\%$ ($3.3\times \downarrow$)** | **$12.32\%$ ($6.6\times \downarrow$)** | **$0.0564 \ll \theta$** | **$0.5030$ ($0.4973$ in sweep)** | **$15.22$ ($p=0.085$ at $\tilde{\epsilon}_{\text{vac}}=0.005$)<br>$8.64$ ($p=0.471$ at $\tilde{\epsilon}_{\text{vac}}=0.006$)** |

---

## 5. Simultaneous-Arrival Entangled Pairs and the Sub-Wavelength Port-Mismatch Test

### 5.1 Simultaneous-Arrival ($L_A = L_B$) Coupled Stage-2 Martingale for $\psi$-Ontic Wave Pairs
In Revision 1.0, §5 phrased entangled-pair detection sequentially ("whichever station finishes first pins the partner wave's Stage-1 Malus split"). To handle symmetric equal-arm Bell experiments ($L_A = L_B$) where both wave packets enter Polarizers $A$ and $B$ simultaneously at $t = 0$, the **shared phase difference** $\Delta\Phi_{AB} = \phi_A - \phi_B = \Phi_0$ of the $\psi$-ontic pair serves as the single nonlocal variable coupling the two stations **during Stage 2** (`simulate_bell_coupled_stage2` in `run_stage02_verification.py`):
1. Prior to detection, neither particle carries an individual pre-assigned polarization axis or fixed absolute phase $\phi_A, \phi_B$; only the relative phase difference $\Delta\Phi_{AB} = \Phi_0$ is locked across the two-particle wave packet (analogous to a holographic interference record). At $t = 0$, Station $A$ (angle $a$) and Station $B$ (angle $b$) therefore both initialize at $50/50$ across their respective orthogonal polarizer ports ($S_{A+}(0) = 1/2$, $S_{B+}(0) = 1/2$).
2. During Stage 2, the two stations' martingales are coupled through the shared $\psi$-ontic phase difference $\Delta\Phi_{AB}$ with cross-variation $\eta\cos 2(a - b)$, so that the conditional expectation of Station $B$'s share given Station $A$'s outcome $S_{A+}(\tau_A) \in \{0, 1\}$ follows Malus's law:
   $$\mathbb{E}\!\left[S_{B+}(\tau_B) \,\middle|\, S_{A+}(\tau_A)\right] = \frac{1}{2} + \eta\left(S_{A+}(\tau_A) - \frac{1}{2}\right)\cos 2(a - b).$$
   In `simulate_bell_coupled_stage2` ([`code/run_stage02_verification.py`](../code/run_stage02_verification.py)), this joint law is sampled via the integrated conditional martingale (integrating one station's walk to absorption and transferring the integrated cross-variation shift $\eta(S_{A+}(\tau_A) - \frac{1}{2})\cos 2(a-b)$ to the partner station's residual martingale), which is strictly invariant under exchanging $A \leftrightarrow B$ because both marginals equal $1/2$ and $\Pr(B = A \mid A) = \Pr(A = B \mid B)$.

### 5.2 Shared Phase Difference and Pythagorean Energy Conservation of Orthogonal Wave Projections (Bell Correlation vs. No-Signaling)
A foundational question is why a real, nonlocally shared phase difference $\Delta\Phi_{AB}$ can violate Bell's inequality up to Tsirelson's bound ($S_{\text{CHSH}} = 2\sqrt{2}$) while strictly forbidding faster-than-light signaling. Both features follow simultaneously from **Parseval / Pythagorean energy conservation of orthogonal wave projections**:
$$\cos^2(a - b) + \sin^2(a - b) = 1.$$
Historically, this identity is a universal mathematical theorem of complex inner-product waves (Parseval's theorem, 1799; Malus's law, 1809, for classical electromagnetic wave energy $\|\mathbf{E}\|^2 = |E_+|^2 + |E_-|^2$ split across orthogonal polarizer axes), which standard quantum mechanics subsequently elevated into a probability-space unitarity axiom (and which Gleason's theorem, 1957, proved uniquely forces the $|A_i|^2$ measure on Hilbert spaces). In the two-stage selector model, $\cos^2(a-b) + \sin^2(a-b) = 1$ operates directly as **physical wave-energy conservation across two mutually orthogonal polarizer ports**, performing two complementary roles at once:

1. **The Difference of Orthogonal Projections Produces the Quantum Bell Correlation/Anticorrelation:**  
   When Station $A$'s walk locks onto axis $a$ (or $a + 90^\circ$), the shared phase difference $\Delta\Phi_{AB}$ locks the relative orientation of the partner wave at Station $B$'s polarizing beam splitter (whose orthogonal ports lie along $b$ and $b + 90^\circ$). By Pythagorean wave decomposition, the fraction of wave energy routed into Bob's **correlated** port ($B = A$) is $\cos^2(a - b)$, and the complementary fraction routed into Bob's **anticorrelated** port ($B = -A$) is $\sin^2(a - b) = 1 - \cos^2(a - b)$. Because the Stage-2 martingale preserves these shares as click probabilities (modulated by phase-locking fidelity $\eta \in [0, 1]$), the net correlation is the **difference** of the two orthogonal wave-energy shares:
   $$E(a, b) = P(B = A \mid a, b) - P(B = -A \mid a, b) = \eta\Big[\cos^2(a - b) - \sin^2(a - b)\Big] = \eta\cos 2(a - b), \qquad S_{\text{CHSH}} = 2\sqrt{2}\,\eta.$$
   Whereas classical local hidden-variable particles with pre-assigned binary outcomes ($\pm 1$) can only produce a piecewise-linear correlation $1 - 2|a - b|/\pi$ bounded by $S_{\text{CHSH}} \le 2$, the quadratic Pythagorean wave curvature $\cos^2(a-b) - \sin^2(a-b) = \cos 2(a-b)$ reaches $S_{\text{CHSH}} = 2\sqrt{2} \approx 2.828$ (**Figure 3B**, generated from $20{,}000$ event-by-event Monte Carlo runs per point, with the unsupported $S = 3.08$ point of v1.0 removed).

2. **The Sum of Orthogonal Projections Automatically Enforces Relativistic No-Signaling:**  
   Because the entangled pair has no preferred initial polarization axis, Station $A$'s detector locks onto angle $a$ ($A = +1$) in $50\%$ of trials and onto the orthogonal axis $a + 90^\circ$ ($A = -1$) in the other $50\%$ of trials. In the first $50\%$ of trials, Station $B$'s $+1$ port receives wave energy share $\cos^2(a - b)$; in the other $50\%$ of trials, because $\cos(a - b + 90^\circ) = -\sin(a - b)$, Station $B$'s $+1$ port receives the complementary share $\sin^2(a - b)$. Without classical communication from Station $A$ to sort the trials into "$A=+1$" and "$A=-1$" sub-ensembles, an observer at Station $B$ sees only the **sum** of the two halves:
   $$P(B = +1 \mid a, b) = \frac{1}{2}\cos^2(a - b) + \frac{1}{2}\sin^2(a - b) = \frac{1}{2}\Big[\cos^2(a - b) + \sin^2(a - b)\Big] = \frac{1}{2}.$$

| Relative Polarizer Angle $(a - b)$ | Sub-Ensemble 1 ($50\%$ of trials where $A = +1$): Bob's $+1$ Share $\cos^2(a-b)$ | Sub-Ensemble 2 ($50\%$ of trials where $A = -1$): Bob's $+1$ Share $\sin^2(a-b)$ | **Net Correlation (Difference):** $\cos^2(a-b) - \sin^2(a-b)$ | **Bob's Marginal Click Rate (Sum):** $\frac{1}{2}\cos^2(a-b) + \frac{1}{2}\sin^2(a-b)$ |
| :---: | :---: | :---: | :---: | :---: |
| **$0^\circ$** | $1.0000$ | $0.0000$ | $+1.0000$ (Full Correlation) | **$0.5000$ ($50\%$)** |
| **$22.5^\circ$ (CHSH angle)** | $0.8536$ | $0.1464$ | $+0.7071$ ($1/\sqrt{2}$) | **$0.5000$ ($50\%$)** |
| **$30^\circ$** | $0.7500$ | $0.2500$ | $+0.5000$ | **$0.5000$ ($50\%$)** |
| **$45^\circ$** | $0.5000$ | $0.5000$ | $0.0000$ (Uncorrelated) | **$0.5000$ ($50\%$)** |
| **$67.5^\circ$ (CHSH angle)** | $0.1464$ | $0.8536$ | $-0.7071$ ($-1/\sqrt{2}$) | **$0.5000$ ($50\%$)** |
| **$90^\circ$** | $0.0000$ | $1.0000$ | $-1.0000$ (Full Anticorrelation) | **$0.5000$ ($50\%$)** |

 Thus, Pythagorean energy conservation of orthogonal wave projections simultaneously generates the Bell correlation via the **difference** $\cos^2 - \sin^2 = \cos 2(a-b)$ and protects relativistic no-signaling via the **sum** $\frac{1}{2}(\cos^2 + \sin^2) = \frac{1}{2}$.

### 5.3 Analytical Derivation and Event-by-Event Simulation of the Port-Mismatch Bow
As Reviewer C proved, pure variance inflation on a driftless martingale changes only the absorption time, leaving $P_A(S) = S$ invariant. In a sub-wavelength cold-atom array (Port $A$, $d < \lambda$ [Rui et al. 2020; Srakaew et al. 2023]) paired against an uncorrelated absorber (Port $B$, $d \gg \lambda$), cooperative subradiant dipole coupling introduces a two-port coexistence loss/redistribution drift $b(S_A) = -\gamma_{\text{sub}}\,S_A(1 - S_A)$ that vanishes at the single-port calibration endpoints $S = 0$ and $S = 1$. Solving the backward Kolmogorov equation $\frac{\sigma^2}{2}S_A(1 - S_A)P_A''(S_A) - \gamma_{\text{sub}}S_A(1 - S_A)P_A'(S_A) = 0$ with $P_A(0) = 0, P_A(1) = 1$ gives the analytical bowing law:
$$P_A(S) = \frac{1 - e^{2\gamma_{\text{sub}}S/\sigma^2}}{1 - e^{2\gamma_{\text{sub}}/\sigma^2}} = S - \frac{\gamma_{\text{sub}}}{\sigma^2}\,S(1 - S) + \mathcal{O}\!\left(\frac{\gamma_{\text{sub}}^2}{\sigma^4}\right), \qquad \kappa = -\frac{\gamma_{\text{sub}}}{\sigma^2} < 0,$$
compared against the linear quantum-mechanical null response $P_A^{\text{QM}}(S) = S$ (for a zero-dark-count linear detector under fixed single-photon input) and $20{,}000$ event-by-event Monte Carlo trajectories per point in **Figure 3A**.

![Figure 3: Event-by-Event Monte Carlo for Cooperative Port-Mismatch Bow and Coupled Bell Walk](../code/fig_v2_3_experimental_discriminators.png)

---

## 6. Conclusion

Rather than claiming an *ab initio* derivation of the Born rule, this work demonstrates how the geometric interpretation of complex wave interference ($|\psi|^2 = (\operatorname{Re}\psi)^2 + (\operatorname{Im}\psi)^2$ as a Pythagorean invariant of orthogonal transverse wave quadratures) coupled with a conserving martingale exchange game across individual detector atoms produces a distribution of single-outcome detection clicks consistent with the Born rule across both discrete and bandgap-gated detectors ($\theta = 0.72$ and $\theta = 0.45$). By resolving the detector aperture into individual atoms on an off-center 2D condensed-matter crystal lattice—where the phases of the incident wave, the surface-conditioned virtual vacuum, and the absorbing atoms couple *before* the modulus squared is evaluated—and by formulating concrete empirical discriminators (E1–E3), the framework honors the complementary roles of computation and laboratory observation: **simulation tests the consequences and consistency of a physical hypothesis; experiment tests whether nature follows it.**

---

## References

* Adler, R. (1946). A study of locking phenomena in oscillators. *Proc. IRE* **34**, 351–357.
* Adler, S. L., Brody, D. C., Brun, T. A., & Hughston, L. P. (2001). Martingale models for quantum state reduction. *J. Phys. A* **34**, 8795–8820.
* Afzelius, M., Simon, C., de Riedmatten, H., & Gisin, N. (2009). Multimode quantum memory based on atomic frequency combs. *Phys. Rev. A* **79**, 052329.
* Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics* **1**, 195–200.
* Born, M. (1926). Zur Quantenmechanik der Stoßvorgänge. *Z. Phys.* **37**, 863–867.
* Bramble, J. M., & Claude Fable 5 (Anthropic) (2026). *DiracKuramotoFramework: The Many Clocks Interpretation of Quantum Mechanics*. Public GitHub repository: `https://github.com/rayolddog/DiracKuramotoFramework`.
* Brune, M., et al. (1996). Quantum Rabi oscillation: A direct test of field quantization in a cavity. *Phys. Rev. Lett.* **76**, 1800–1803.
* Busch, P. (2003). Quantum states and generalized observables: a simple proof of Gleason's theorem. *Phys. Rev. Lett.* **91**, 120403.
* Casimir, H. B. G., & Polder, D. (1948). The influence of retardation on the London–van der Waals forces. *Phys. Rev.* **73**, 360–372.
* de Riedmatten, H., et al. (2008). A solid-state light–matter interface at the single-photon level. *Nature* **456**, 773–777.
* Ewens, W. J. (2004). *Mathematical Population Genetics I: Theoretical Introduction* (2nd ed.). Springer.
* Ghirardi, G. C., Pearle, P., & Rimini, A. (1990). Markov processes in Hilbert space and continuous spontaneous localization. *Phys. Rev. A* **42**, 78–89.
* Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *J. Math. Mech.* **6**, 885–893.
* Grangier, P., Roger, G., & Aspect, A. (1986). Experimental evidence for a photon anticorrelation effect on a beam splitter. *Europhys. Lett.* **1**, 173–179.
* Hahn, E. L. (1950). Spin echoes. *Phys. Rev.* **80**, 580–594.
* Haroche, S., & Kleppner, D. (1989). Cavity quantum electrodynamics. *Phys. Today* **42**(1), 24–30.
* Hensen, B., et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature* **526**, 682–686.
* Kimura, M., & Ohta, T. (1969). The average number of generations until fixation of a mutant gene in a finite population. *Genetics* **61**, 763–771.
* Kurnit, N. A., Abella, I. D., & Hartmann, S. R. (1964). Observation of a photon echo. *Phys. Rev. Lett.* **13**, 567–568.
* Lamb, W. E., Jr., & Retherford, R. C. (1947). Fine structure of the hydrogen atom by a microwave method. *Phys. Rev.* **72**, 241–243.
* Lamb, W. E., Jr., & Scully, M. O. (1969). The photoelectric effect without photons. In *Polarisation, Matière et Rayonnement*, pp. 363–369.
* Mandel, L., & Wolf, E. (1995). *Optical Coherence and Quantum Optics*. Cambridge University Press.
* Pearle, P. (1976). Reduction of the state vector by a nonlinear Schrödinger equation. *Phys. Rev. D* **13**, 857–868.
* Pearle, P. (1982). Might God toss coins? *Found. Phys.* **12**, 249–263.
* Penrose, R., & Rindler, W. (1984). *Spinors and Space-Time, Vol. 1: Two-Spinor Calculus and Relativistic Fields*. Cambridge University Press.
* Perreault, J. D., & Cronin, A. D. (2005). Observation of atom wave phase shifts induced by van der Waals atom–surface interactions. *Phys. Rev. Lett.* **95**, 133201.
* Pusey, M. F., Barrett, J., & Rudolph, T. (2012). On the reality of the quantum state. *Nat. Phys.* **8**, 475–478.
* Rui, J., et al. (2020). A subradiant optical mirror formed by a single structured atomic layer. *Nature* **583**, 369–374.
* Srakaew, K., et al. (2023). A subwavelength atomic array switched by a single Rydberg atom. *Nat. Phys.* **19**, 714–719.
* Sukenik, C. I., Boshier, M. G., Cho, D., Sandoghdar, V., & Hinds, E. A. (1993). Measurement of the Casimir–Polder force. *Phys. Rev. Lett.* **70**, 560–563.
* Zurek, W. H. (2005). Probabilities from entanglement, Born's rule $p_k = |\psi_k|^2$ from envariance. *Phys. Rev. A* **71**, 052105.
