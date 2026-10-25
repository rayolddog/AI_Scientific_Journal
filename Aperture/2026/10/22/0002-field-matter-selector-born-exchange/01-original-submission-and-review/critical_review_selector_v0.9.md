# Critical Review: *A Field–Matter Selector for Outcome Production, Conditioned on a Detector Ready-State Measure* (Draft v0.9)

**Authors of Reviewed Manuscript:** Claude Fable 5 (Anthropic) and John M. Bramble, MD  
**Draft Version Reviewed:** v0.9 (Base v0.5 of 2026-07-28 with point revisions through 2026-09-02)  
**Review Date:** October 14, 2026  

---

## 1. Executive Summary & Overall Assessment

This manuscript proposes a detector-side stochastic selection mechanism to bridge the gap between continuous wave-mechanical excitation ("Stage 1 — capture") and discrete, single-outcome detector registration ("Stage 3 — registration"). The core idea is to transplant the martingale / gambler’s-ruin engine of dynamical state-reduction models (Pearle 1976, 1982; Adler–Brody–Brun–Hughston 2001) out of Hilbert space and into the physical detector bulk ("Stage 2 — selection"), arguing that five "fairness theorems" (Theorems 1–5) force the stochastic competition among absorber sites onto the unique zero-drift martingale point using stated detector premises (P0–P6) rather than engineered noise.

### Major Strengths
1. **Exceptional Intellectual Honesty and Self-Falsification:** The manuscript’s greatest strength is its rigorous commitment to testing its own claims against edge cases, computing explicit converses, retaining failing simulation configurations as diagnostics, and recording where its mechanisms break. The de-claiming passes (v0.6–v0.9) rightly withdraw earlier overclaims—including the withdrawal of *"the Born weight is nowhere inserted by hand,"* the withdrawal of *"the measurement postulate is redundant,"* and the withdrawal in v0.7 of the false claim that single-detector physics is quarantined from the nonlocal premises P5 and P6.
2. **Concrete, Falsifiable Experimental Discriminators:** Unlike purely interpretive proposals in quantum foundations, §8 translates premise failures into clean, quantitative experimental signatures—most notably the **tabletop port-mismatch discriminator (§8.4)** and the **cross-station Bell injection protocol (§8.7)**.

### Critical Vulnerabilities
By v0.9, the paper’s sequence of internal corrections has quietly **hollowed out the central load-bearing role of Stage 2 (the stochastic energy game)** while introducing severe mathematical and physical inconsistencies between the body text (§§1–6) and the v0.8/v0.9 patches:

1. **The v0.9 "Reading B" Collapse (§5.4, §6.1, Header):** Adopting Reading B in v0.9 (to rescue silicon SPADs from a fatal $+0.1$ to $+0.2$ threshold-gating bias discovered in `threshold_gated_commit.py`) reduces the operative mechanism to: *initial shares are $s_i(0) = |A_i|^2/\sum_j |A_j|^2$ (by P1), commitment is an ungated memoryless hazard linear in $s_i$ (by Theorem 5 + Reading B), and the first site to fire takes the whole quantum via a nonlocal closed pot (P4a + P5)*. Under this rule, **the Stage-2 stochastic exchange game does no statistical work at all**—setting the exchange noise to zero ($\sigma = 0$) yields the exact same Born statistics immediately at $t = 0^+$.
2. **Mathematical Flaw in Theorem 1 & Appendix A.1:** The Itô calculus proof of Theorem 1 models site energies $e_i$ as independent diffusions ($de_i = \sigma \sqrt{e_i}\,dW_i$, $\langle dW_i dW_j \rangle = \delta_{ij} dt$), which implies that total energy $E(t) = \sum_j e_j(t)$ is a non-conserved random walk ($dE \neq 0$), directly contradicting the paper’s repeated insistence on a **strictly closed energy pot** ($\sum_i e_i = \hbar\omega = \text{const}$) in P4(a), §4, §6.1, and §7.2. Furthermore, the uniqueness proof in Appendix A.1 is an artifact of denominator fluctuations $dE \neq 0$; under a genuinely conserving exchange ($dE = 0$), *any* symmetric zero-mean exchange law yields $\mathbb{E}[ds_i] = 0$.
3. **Microphysical Contradiction in Theorem 2 ($\kappa_{\text{ret}} = \Delta E/\hbar$):** Writing a real contraction eigenvalue $-\kappa_{\text{ret}} = -(E_0 - e)/\hbar$ in the rotating-frame ODE $\dot{a} = -(\kappa_{\text{ret}} + i\Delta)a + f e^{i\varphi_d}$ conflates a conservative off-shell **frequency detuning** (which is imaginary, $-i\Delta E/\hbar$, producing reversible phase beating) with a dissipative **phase-space contraction rate** (which is real, $-\kappa_{\text{ret}} < 0$, violating Liouville's theorem / unitarity unless an open continuum reservoir is traced out). Moreover, since $\kappa_{\text{ret}} = (E_0 - |a|^2)/\hbar$ depends on $|a|^2$, the ODE is cubic in $a$, contradicting Theorem 2’s statement that *"In Cartesian coordinates this system is linear."*
4. **Confounding Systematic in the §8.4 Tabletop Discriminator and §8.7 Injection Test:** In §8.4, plotting the *conditional* probability $P(\text{port } A \mid \text{click})$ for ports with mismatched collective structure overlooks the fact that **standard quantum mechanics also predicts a $\kappa_{\text{QM}} S(1-S)$ bow in conditional click statistics** whenever the two ports have unequal detection efficiencies ($\eta_A \neq \eta_B$). In §8.7 (Knob 2), phase-locked tone injection acts as a homodyne local oscillator that modulates single-photon detection efficiency with analyzer angle, which is known to inflate postselected CHSH $S > 2\sqrt{2}$ in standard QM via the coincidence-efficiency loophole unless Eberhard / Clauser–Horne unconditional normalization is used.
5. **Structural Fragmentation ("Geological Strata"):** Because v0.6–v0.9 were added as paragraph-level patches rather than integrated via a unified rewrite, the manuscript repeatedly states a theorem or timescale conclusion in one paragraph and withdraws it two paragraphs later.

---

## 2. Detailed Technical and Conceptual Critiques

### Critique 1: The v0.9 "Reading B" Adoption Renders the Stage-2 Martingale Game Redundant

Tracing the internal evolution across v0.7 $\to$ v0.8 $\to$ v0.9 in **§2 (P4, p. 10)**, **§5.4 (p. 21)**, and **§6.1 (pp. 22–23)** exposes a central structural dilemma:

* **v0.5–v0.7:** The Stage-2 diffusive martingale ($s_i(t)$ diffusing to the absorbing boundary $s_i \to 1$) was the physical mechanism that selected a single winning site. In v0.7, commitment was placed at the avalanche/record-writing scale ($\text{ns–}\mu\text{s}$), three to five orders of magnitude slower than $\tau_{\text{game}} \sim 12\text{–}81\text{ ps}$, so first passage ($s_i = 1$, Theorem 0) settled every outcome before commitment could act.
* **v0.8:** The authors rightly recognized that commitment—defined throughout the paper as *first irreversibility* (when excitation ceases to be coherently returnable to the common field)—occurs in a semiconductor at the interband electron–hole vertex plus phonon thermalization ($\tau_{\text{commit}} \sim 10\text{ fs–}1\text{ ps}$ in Si), and in an SNSPD at hotspot formation ($10\text{–}50\text{ ps}$). Under Reading A (where shares $s_i$ carry real energy $e_i = s_i E_0$), any site whose share exceeds the gap ratio $\theta = E_{\text{gap}}/E_{\text{photon}}$ ($\theta = 0.45$ in Si at $500\text{ nm}$; $\theta \approx 0.002$ in NbN at $1550\text{ nm}$) can undergo irreversible interband decay.
* **v0.9:** When the authors ran their discrete-exchange simulation with a commitment channel gated at $\theta$ (`g3_drain_tests/threshold_gated_commit.py`), they found two devastating results:
  1. Because the stakes-scaled exchange $\delta \propto \min(e_i, e_j)$ slows down as losing sites drain, the eventual winner spends **40–90% of the entire game duration above $\theta$** ($t_{\text{exp}} \approx \tau_{\text{game}}$), so the expected number of commits during the exposed leg in silicon is $r = \lambda t_{\text{exp}} \sim 10\text{–}10^4 \gg 1$.
  2. Even with a *strictly linear* commitment hazard above $\theta$, gating the hazard at $\theta > 0$ violates Theorem 4 (which requires $\text{rate}_i \propto s_i$ for *all* sites, whereas a gate sets $\text{rate}_i = 0$ for sites with $s_i < \theta$) and biases an $80/20$ split by $+0.12$ to $+0.19$—a massive deviation excluded by standard calibration and by heralded $505\text{ nm}$ SPAD $g^{(2)}(0) = 0.0023$ data.
* **The v0.9 Escape Hatch (Reading B):** To save the theory from immediate empirical falsification in silicon and superconducting detectors, v0.9 adopts **Reading B**: sub-threshold shares are *"amplitude bookkeeping that becomes energy only when a site takes the whole quantum,"* so **there is no gate at $\theta$** ($\theta = 0$), and commitment is available from *every* site at all times with a memoryless Golden-Rule hazard linear in the site’s share:
  $$\text{rate}_i(t) = \Gamma s_i(t),$$
  where the first site to fire consumes the full quantum $\hbar\omega$ (P4a).

#### Why Reading B Hollows Out the Paper’s Core Thesis
Consider what happens under Reading B at $t = 0^+$, immediately after Stage 1 (capture) prepares the shares $s_i(0) = |A_i|^2 / \sum_j |A_j|^2$ (Premise P1):
1. Every site $i \in \{1, \dots, N\}$ is immediately eligible to commit with hazard $\lambda_i(t) = \Gamma s_i(t)$.
2. Suppose we turn off the Stage-2 stochastic exchange game completely ($\sigma = 0$), so $s_i(t) = s_i(0)$ is constant.
3. Because each site has an independent memoryless (Poisson) hazard $\lambda_i = \Gamma s_i(0)$ and the first site to fire takes the entire quantum (by P4a + P5), the probability that site $i$ fires first is:
   $$P_i = \frac{\lambda_i}{\sum_j \lambda_j} = \frac{\Gamma s_i(0)}{\sum_j \Gamma s_j(0)} = s_i(0) = \frac{|A_i|^2}{\sum_j |A_j|^2}.$$

**The Stage-2 stochastic energy game is doing zero statistical work.** Under Reading B, the Born probabilities come entirely from:
1. $s_i(0) \propto |A_i|^2$ (Premise P1),
2. $\text{rate}_i \propto s_i$ at every site with no threshold gate (Theorem 5 + Reading B), and
3. The first site to fire takes 100% of the quantum $\hbar\omega$ across all sites (Premise P4a + Premise P5).

In this picture, the diffusive exchange of §§4–5 is merely a neutral noise bath that jiggles the shares around their initial values without changing their expectations ($\mathbb{E}[s_i(T)] = s_i(0)$) while waiting for the Poisson jump to fire. The v0.9 header (p. 3) practically concedes this:
> *"the exchange game is the reversible sub-threshold dynamics of Theorems 1–3 and carries no statistical weight of its own; and the claim moves from 'the game realizes the Born measure' to 'any actualization law whose hazard is linear in the share reproduces the Born comparator, and the fairness theorems state what the substrate must not do to the shares before it fires.'"*

Even more concerningly, the v0.9 header (p. 4) reports that when the authors tested whether their underlying deterministic substrate model (`adler_two_channel_exploratory/`) naturally generates this memoryless linear hazard, **it failed**:
* The unconstrained Adler-locking race gave a coupling exponent of $1.56$ ($95\%$ CI $[1.44, 1.69]$), rejecting the Born exponent $2.0$.
* The positive-control scale-similar dwell overshot to $3.81$ ($[3.50, 4.15]$).
* The deterministic skeleton with *no noise at all* gave $1.52$ (showing the noise was not driving the race).
* Born ($2.16$) was recovered **only** when the authors manually inserted a memoryless Poisson jump with hazard linear in absorbed energy—i.e., putting Fermi's Golden Rule and Poisson actualization in by hand.

> [!IMPORTANT]
> **Bottom Line on Critique 1:** A reader who fights through §§3–6 believing they are reading a derivation of outcome selection via a Pearle-style diffusive martingale to an absorbing boundary $s_i = 1$ discovers in the v0.9 patches that: (a) if the boundary/gate is active (Reading A), the model is falsified by silicon SPADs; and (b) if the boundary/gate is removed (Reading B), the outcome is selected by a standard Golden-Rule Poisson jump rate $\propto |A_i|^2$ supplemented by a nonlocal closed-pot rule (P4a/P5), rendering the diffusive martingale game superfluous.

---

### Critique 2: Mathematical Inconsistency in Theorem 1 and Appendix A.1 (Independent Diffusions vs. Closed Pot)

In **§2 (P2, p. 9)**, **§5.1 (Theorem 1, p. 16)**, and **Appendix A.1 (p. 37)**, the stochastic differential equation (SDE) for the site energies is written as:
$$de_i = \sigma \sqrt{e_i}\,dW_i, \qquad \langle dW_i dW_j \rangle = \delta_{ij} dt.$$
Theorem 1 then applies Itô’s lemma to the share $s_i = e_i / E$, where $E = \sum_j e_j$:
$$\mathbb{E}[ds_i] = \frac{1}{2}\sum_j \sigma^2 e_j \frac{\partial^2 s_i}{\partial e_j^2}\,dt = \frac{\sigma^2}{E^2}\left(-e_i + \frac{e_i E}{E}\right)dt = 0.$$
And Appendix A.1 generalizes this to $de_i = \sigma a(e_i)\,dW_i$, obtaining:
$$\mathbb{E}[ds_i] = \frac{\sigma^2}{E^2}\left[s_i \sum_j a(e_j)^2 - a(e_i)^2\right]dt,$$
claiming: *"This vanishes for all configurations iff $a(e)^2 \propto e$ — the amplitude-linear law — proving Theorem 1 and its uniqueness."*

This mathematical setup has three deep flaws:

#### 1. The SDE Violates Energy Conservation ($dE \neq 0$)
If $de_i = \sigma \sqrt{e_i}\,dW_i$ with independent Wiener increments $\langle dW_i dW_j \rangle = \delta_{ij} dt$, then the total energy in the pot $E(t) = \sum_{i=1}^N e_i(t)$ obeys:
$$dE(t) = \sum_{i=1}^N de_i(t) = \sigma \sum_{i=1}^N \sqrt{e_i(t)}\,dW_i(t) = \sigma \sqrt{E(t)}\,d\widetilde{W}(t),$$
where $d\widetilde{W} = \sum_i \sqrt{s_i}\,dW_i$ is a standard Wiener process!
Thus, under the SDE of Theorem 1:
* **Total energy $E(t)$ is not conserved ($E(t) \neq \hbar\omega$).** Instead, $E(t)$ executes a Feller square-root diffusion starting at $E(0) = \hbar\omega$.
* Because $E = 0$ is an absorbing boundary for $dE = \sigma \sqrt{E}\,d\widetilde{W}$, **every single site energy $e_i(t)$ hits zero in finite time with probability 1!** In fact, for independent Feller diffusions $de_i = \sigma\sqrt{e_i}\,dW_i$, the condition "one survivor left with $s_i = 1$" only occurs at the moment the *second-to-last* site hits $e_j = 0$, at which point the surviving site $i$ does **not** hold energy $e_i = \hbar\omega$—it holds whatever random energy $e_i(T) \in (0, \infty)$ its independent random walk wandered to!
* Yet throughout the rest of the paper (**P4(a) on p. 10**, **§3 on p. 13**, **§6.1 on p. 22**, **§7.2 on p. 26**), the entire exclusivity argument rests on a **strictly closed energy pot**:
  $$\sum_i e_i(t) = \hbar\omega = \text{const},$$
  arguing that a site reaching $s_i = 1$ has assembled $e_i = \hbar\omega$. You cannot use independent site diffusions ($\langle dW_i dW_j \rangle = \delta_{ij} dt$, which require an open pot $dE \neq 0$) to prove Theorem 1 and Theorem 3, and simultaneously invoke a closed pot ($\sum_i de_i = 0$, which requires negatively correlated increments $\sum_j \langle de_i de_j \rangle = 0$) to prove exclusivity!

#### 2. What Happens When the Pot Is Actually Closed ($\sum_i de_i = 0$)?
If Stage 2 is genuinely an **energy-conserving exchange** among sites (as stated in §4: *"a stochastic redistribution of the deposited energy among them"*), then $E = \sum_j e_j = E_0$ is a constant ($dE = 0$).
When $E = E_0$ is constant:
$$s_i = \frac{e_i}{E_0} \implies ds_i = \frac{de_i}{E_0}.$$
Because $s_i$ is now a *linear* function of $e_i$, the second derivatives $\partial^2 s_i / \partial e_j^2$ **vanish identically**! There is no Itô convexity correction from the denominator $1/E$.
Consequently, for *any* pairwise conservative zero-mean exchange between sites $i$ and $j$:
$$de_i = \sum_{j \neq i} g(e_i, e_j)\,dW_{ij}, \qquad dW_{ji} = -dW_{ij},$$
where $g(e_i, e_j) = g(e_j, e_i)$ is *any* symmetric function that vanishes when $e_i=0$ or $e_j=0$ (for example, $g(e_i, e_j) = \sigma \sqrt{e_i e_j}$, or $g(e_i, e_j) = \sigma e_i e_j$, or $g(e_i, e_j) = \sigma \min(e_i, e_j)$), we have:
1. $\sum_i de_i = 0$ (exact energy conservation), and
2. $\mathbb{E}[ds_i] = \frac{1}{E_0}\mathbb{E}[de_i] = 0$ (exact martingale property for **every** noise scaling $g(e_i, e_j)$!).

Notice that the authors' own discrete gambler engine in §4(b) and Appendix D uses stakes-scaled exchange:
$$\delta = \pm \text{step} \cdot \min(e_i, e_j),$$
which scales linearly with $\min(e_i, e_j)$ (not $\sqrt{e_i}$!), conserves $E$ exactly at every step, and is an exact martingale! This directly disproves the claim that $\sqrt{e_i}$ noise is the unique scaling that produces a drift-free share game: $\sqrt{e_i}$ is only "unique" when you divide by a fluctuating, non-conserved total energy $E(t) = \sum_j e_j(t)$.

#### 3. Reconciling Wright–Fisher Diffusion with Independent Site Noise
In continuous time, if one starts with independent site fluctuations $d\tilde{e}_i = \sigma \sqrt{e_i}\,dW_i$ and conditions/projects onto the energy-conserving simplex $\sum_i e_i = E_0$, one obtains the multi-species **Wright–Fisher (or Kimball–Pearle) diffusion**:
$$ds_i = \frac{\sigma}{\sqrt{E_0}} \sum_{j=1}^N \left(\delta_{ij}\sqrt{s_i} - s_i\sqrt{s_j}\right) dW_j,$$
whose covariance matrix is $\langle ds_i ds_j \rangle = \frac{\sigma^2}{E_0}(s_i \delta_{ij} - s_i s_j)dt$. This process *does* arise uniquely from projecting $d\tilde{e}_i = \sigma \sqrt{e_i}\,dW_i$ onto the constant-energy constraint surface (or by tracking normalized shares $s_i = e_i / \sum_j e_j$ while allowing the unnormalized scale $E$ to fluctuate as an irrelevant gauge variable). If the authors intend $e_i$ in Theorem 1 to be an unnormalized weight and only $s_i E_0$ to be the physical energy, they must state this explicitly—otherwise $e_i$ cannot simultaneously satisfy $\langle de_i de_j \rangle = \sigma^2 e_i \delta_{ij} dt$ and $\sum_i e_i = \hbar\omega$.

---

### Critique 3: Microphysical and Mathematical Contradictions in Theorem 2 ($\kappa_{\text{ret}} = \Delta E/\hbar$)

In **§5.2 (Theorem 2, p. 18)** and **Appendix B.1 (p. 37)**, the authors write the rotating-frame equation for a sub-threshold site holding energy $e < E_0$:
$$\dot{r} = -\kappa_{\text{ret}} r + f\cos(\varphi_d - \varphi), \qquad \dot{\varphi} = \Delta + \frac{f}{r}\sin(\varphi_d - \varphi),$$
or in complex Cartesian form ($a = r e^{i\varphi}$):
$$\dot{a} = -(\kappa_{\text{ret}} + i\Delta)a + f e^{i\varphi_d}, \qquad \text{where } \kappa_{\text{ret}} = \frac{\Delta E}{\hbar} = \frac{E_0 - e}{\hbar}.$$

In the v0.5.3 dictionary paragraph (p. 18), the authors emphasize that $\kappa_{\text{ret}}$ is **not** dissipative decay into a bath, but *"the rate at which the borrowed energy reversibly returns to the common field — the beat rate of a failed lock."*

This formulation contains two fundamental errors:

1. **Unitary Off-Shell Beating Is Imaginary ($-i\Delta E/\hbar$), Not Real ($-\Delta E/\hbar$):**
   In quantum mechanics and coupled-mode theory, an off-shell energy mismatch $\Delta E = E_0 - e$ enters the Heisenberg / Schrödinger equation of motion as a **phase oscillation frequency** (an imaginary term $-i(\Delta E/\hbar)a$), *not* a real damping term $-(\Delta E/\hbar)a$.
   * Under a conservative Hamiltonian exchange with a common mode, an off-resonance oscillator beats back and forth with the drive at the Rabi/detuning beat frequency $\Omega_{\text{beat}} = \sqrt{\Delta^2 + 4g^2}$; its phase winds or oscillates periodically, and the time-averaged energy transfer over a beat cycle vanishes.
   * By contrast, placing $\kappa_{\text{ret}} = \Delta E/\hbar > 0$ in the **real** part of the eigenvalue ($\lambda = -\kappa_{\text{ret}} \pm i\Delta$) makes the flow a strict phase-space contraction:
     $$\frac{\partial \dot{a}_x}{\partial a_x} + \frac{\partial \dot{a}_y}{\partial a_y} = -2\kappa_{\text{ret}} < 0.$$
     By Liouville’s theorem, a deterministic flow with negative divergence cannot represent a reversible return to a single common field mode; it represents irreversible damping into a Markovian continuum reservoir! Even worse, at the fixed point $r^* = f/\sqrt{\kappa_{\text{ret}}^2 + \Delta^2}$, the drive continuously pumps power $P_{\text{in}} = 2f r^* \cos(\varphi_d - \varphi^*) = 2\kappa_{\text{ret}} |a^*|^2 > 0$ into the site, which is continuously swallowed by the $-\kappa_{\text{ret}} r$ sink.
2. **A Cubic ODE Falsely Described as Linear:**
   Theorem 2 states:
   > *"Under P1 and P4(i), a site holding energy $e < E_0$ is off-shell by $\Delta E = E_0 - e$ and constitutes a driven linear mode that returns its excitation to the common field at the rate $\kappa_{\text{ret}} = \Delta E/\hbar$... In Cartesian coordinates this system is linear with eigenvalues $\lambda = -\kappa_{\text{ret}} \pm i\Delta$; it possesses a unique, globally attracting fixed point $r^* = f/\sqrt{\kappa_{\text{ret}}^2 + \Delta^2}$..."*
   
   Wait: $e = |a|^2 = r^2$. Therefore, $\kappa_{\text{ret}}(r) = (E_0 - r^2)/\hbar$ is a function of $r^2$! Substituting $\kappa_{\text{ret}} = (E_0 - |a|^2)/\hbar$ into $\dot{a} = -(\kappa_{\text{ret}} + i\Delta)a + f e^{i\varphi_d}$ yields:
   $$\dot{a} = -\left(\frac{E_0 - |a|^2}{\hbar} + i\Delta\right)a + f e^{i\varphi_d},$$
   which is a **nonlinear (cubic) Stuart–Landau-type oscillator equation**, *not* a linear system with constant eigenvalues! And its fixed-point equation $r^* \sqrt{(E_0 - r^{*2})^2/\hbar^2 + \Delta^2} = f$ is a cubic polynomial in $r^{*2}$ that can exhibit bistability (up to 3 fixed points, not a unique global attractor!).

> [!TIP]
> **How to Fix Theorem 2 Cleanly:** You do not need the unphysical real contraction $-\kappa_{\text{ret}} = -\Delta E/\hbar$ to kill the Robert Adler rich-get-richer tail! In a genuinely conservative off-shell model, the off-shell deficit $\Delta E/\hbar$ acts as a large frequency detuning $\Delta_{\text{off}} = (E_0 - e)/\hbar \gg K$. Outside the resonance boundary layer ($\Delta_{\text{off}} > K$), the site sits outside the Arnold tongue of the Adler equation $\dot{\varphi} = \Delta_{\text{off}} - K\sin\varphi$, so its phase rotates rapidly and the time-averaged energy uptake $\langle \dot{e} \rangle$ vanishes over the fast beat period $2\pi/\Delta_{\text{off}}$ unless it enters the locking layer $\Delta E \lesssim \hbar K$ ($w = K/\omega$). That gives the exact same layer width $w = K/\omega$ without violating unitarity or confusing real damping with off-shell detuning.

---

### Critique 4: Relativistic Stress-Energy Nonlocality in the Single-Photon Sector (P0 + P1 + P4a + P5)

In **v0.7 (§2, pp. 10–12; §7.2, p. 26)**, the authors make an admirably candid correction: they withdraw the earlier claim that single-detector physics relies only on local premises P0–P4, acknowledging that a single photon split across a beam splitter requires **P5 (Shared registry)** and **P6 (Ordering foliation)**.

However, the manuscript understates the severity of the physical cost created by combining **P0 (Wave realism)**, **P1 (Energetics of capture)**, **P4(a) (Full-quantum threshold)**, and **P5 (Shared registry)**:
1. Consider a single photon ($\hbar\omega = 2.5\text{ eV}$) incident on a 50/50 beam splitter whose output arms lead to two detectors $A$ and $B$ separated by $L = 1\text{ km}$.
2. By **P0** and **P1**, when the wavepacket arrives at $A$ and $B$, it deposits **real, simultaneously possessed mechanical oscillator energy** $e_A(0) = 1.25\text{ eV}$ in the bound electrons of Detector $A$, and $e_B(0) = 1.25\text{ eV}$ in the bound electrons of Detector $B$.
3. By **§6.1**, the selection game runs in $\tau_{\text{game}} \sim 12\text{–}81\text{ ps}$, whereas the light-travel time between $A$ and $B$ is $L/c = 3.3\,\mu\text{s}$ ($10^5\times$ longer).
4. When a site in Detector $A$ commits, **P4(a)** requires it to consume the full $2.5\text{ eV}$, and **§8.6(vi)** requires Detector $B$ to be left with **zero calorimetric residue** ($e_B \to 0$).
5. Therefore, **1.25 eV of real mechanical energy stored in the bound charges of Detector $B$ must disappear from $B$ and appear in Detector $A$ across a 1 km spacelike separation in picoseconds** (effective energy-transport velocity $v > 10^5 c$).

In **§2 (p. 12)**, the authors write:
> *"But it is not a defect peculiar to this mechanism. Any single-world account of beam-splitter anticorrelation carries a nonlocal constraint — textbook collapse is nonlocal too..."*

This comparison is not quite fair:
* In textbook quantum mechanics (or Bohmian mechanics), the pre-detection wavefunction $\psi(\mathbf{x})$ is a **probability amplitude / guiding field**, not localized mechanical energy already deposited in the bound charges of both detectors. In standard QED, the energy $\hbar\omega$ is not split into two simultaneously possessed $0.5\hbar\omega$ parcels of matter excitation; the state is an entangled superposition $\frac{1}{\sqrt{2}}(|\text{excited}_A, \text{ground}_B\rangle + |\text{ground}_A, \text{excited}_B\rangle)$, where each branch conserves energy locally!
* By rejecting superposition of mutually exclusive excitations in **P0** and insisting that both detectors simultaneously hold $0.5\hbar\omega$ of real mechanical energy at Stage 1, the present model converts a nonlocal update of *correlations/probabilities* into **superluminal transport of real stress-energy $T^{\mu\nu}$**, violating local energy-momentum conservation $\partial_\mu T^{\mu\nu} = 0$. Similarly, the geometric metaphor in **§7.3 (p. 27)**—that rotating a shared phase frame is like the intersection point of closing scissors because *"nothing physical transits"*—works for entangled spin correlations (where each wing already has its own full quantum $\hbar\omega$), but **fails for the single-photon beam splitter**, where $\hbar\omega/2$ of real energy *must* transit from arm B to arm A!

---

### Critique 5: Critical Flaws in the Experimental Discriminators (§8.4 and §8.7)

#### A. The §8.4 Tabletop Discriminator Confounds Efficiency Mismatch with $\kappa S(1-S)$ Curvature
In **§8.4 (p. 29)** and **Figure 7 (p. 30)**, the authors propose sending single photons through a variable beam splitter with splitting ratio $S : (1-S)$ into two spatially separated ports ($A$: correlated sub-$\lambda$ array; $B$: uncorrelated sparse array) and recording the **conditional port statistics given a click**, $P'(S) = P(\text{port } A \text{ wins} \mid \text{click})$.
The text claims (p. 29):
> *"For any local POVM — i.e., for standard quantum mechanics with arbitrary collective physics inside each port — the cross-port matrix elements vanish and $P'(S)$ is exactly affine in $S$: a straight line whose slope encodes the (arbitrary, possibly collective) port efficiencies. The framework predicts curvature, $\kappa S(1-S)$, plus a state-dependent no-click anomaly. The signature is thus insensitive to the dressed-mode physics inside each port: any nonzero curvature (beyond calibrated nonlinearities) discriminates against the linear-POVM structure of quantum mechanics itself."*

**This statement is mathematically incorrect for the conditional probability plotted in Figure 7:**
1. In standard quantum mechanics, let Port $A$ (the dense sub-$\lambda$ atomic array, which by [Rui et al. 2020] acts as a cooperative subradiant mirror with modified reflectivity and absorption) have net single-photon detection efficiency $\eta_A \in (0, 1)$, and let Port $B$ (the sparse array) have net single-photon detection efficiency $\eta_B \in (0, 1)$, with $\eta_A \neq \eta_B$.
2. For an input single-photon state split in ratio $S : (1-S)$, standard QM predicts the **unconditional** probabilities per incident photon:
   $$P_{\text{QM}}(A) = \eta_A S, \qquad P_{\text{QM}}(B) = \eta_B (1-S), \qquad P_{\text{QM}}(\text{no click}) = 1 - \eta_A S - \eta_B(1-S).$$
   Notice first that when $\eta_A \neq \eta_B$, standard QM *already* predicts a **state-dependent ($S$-dependent) no-click rate**!
3. Now compute the **conditional probability that Port A wins given a click**—which is the exact quantity plotted on the vertical axis of Figure 7 (`P(correlated port wins | click)`) and reaching $0$ at $S=0$ and $1$ at $S=1$:
   $$P'_{\text{QM}}(S) \equiv P_{\text{QM}}(A \mid \text{click}) = \frac{\eta_A S}{\eta_A S + \eta_B (1-S)}.$$
4. Subtracting $S$ from $P'_{\text{QM}}(S)$ gives:
   $$P'_{\text{QM}}(S) - S = \frac{(\eta_A - \eta_B) S(1-S)}{\eta_B + (\eta_A - \eta_B)S} = \kappa_{\text{eff}}(S)\, S(1-S),$$
   which to leading order in the efficiency mismatch $\Delta\eta / \bar{\eta} = (\eta_A - \eta_B)/\bar{\eta}$ is **identical in functional form to the paper's predicted $\kappa S(1-S)$ bow**:
   $$P'_{\text{QM}}(S) \approx S + \left(\frac{\eta_A - \eta_B}{\bar{\eta}}\right) S(1-S)!$$
   Specifically, if the dense correlated array reflects more light (cooperative mirror effect, Rui et al. 2020) so that its absorption efficiency is lower ($\eta_A < \eta_B$), standard QM predicts $P_{\text{QM}}(A \mid \text{click}) < S$ with a downward $\kappa S(1-S)$ bow that passes through $(0,0)$ and $(1,1)$—**reproducing the orange curve in Figure 7 identically within standard quantum mechanics!**

> [!WARNING]
> **How §8.4 Must Be Corrected:** In standard QM, *unconditional* port probabilities $P(A) = \eta_A S$ (normalized to heralded input trials) are affine in $S$, whereas *conditional* probabilities $P(A \mid \text{click})$ are rational functions $\frac{\eta_A S}{\eta_A S + \eta_B(1-S)}$ that bow whenever $\eta_A \neq \eta_B$. To discriminate the selector game from a simple efficiency mismatch $\eta_A \neq \eta_B$ in standard QM, the experiment **must** either:
> 1. Measure the **unconditional** probability $P(A\text{ clicks per heralded photon})$ as a function of $S$ (where standard QM gives a straight line $\eta_A S$ with zero curvature, while the inter-port game gives curvature because Port A and Port B compete over the same closed pot across ports); **or**
> 2. Independently measure $\eta_A$ (at $S=1$) and $\eta_B$ (at $S=0$) using a heralded photon source, and test whether $P(A \mid \text{click})$ deviates from the standard QM curve $\frac{\eta_A S}{\eta_A S + \eta_B(1-S)}$.

*(Note also a conceptual tension in §8.4: if the two ports are "spatially separated" so cross-port noise correlations vanish, why are their shares $S_A$ and $S_B$ exchanging energy with each other via $\dot{S}_A \propto q_B S_A - q_A S_B$ at all? In §8.2, $\dot{S}_A = \frac{\sigma^2}{E^2}(q_B S_A - q_A S_B)$ comes purely from the fluctuating total energy denominator $E(t) = E_A(t) + E_B(t)$ of Theorem 1! As shown in Critique 2, if there is no energy exchange between macroscopically separated ports ($dE_A + dE_B = 0$ is only enforced at commitment, or internal site exchanges within port A conserve $E_A$ locally), then $dE_A = 0$ locally, and internal noise correlation inside port A cannot change the total energy $E_A$ of port A!)*

#### B. The §8.7 Cross-Station Bell Injection Test (Knob 2 Above-Tsirelson Claim)
In **§8.7 (p. 32)**, Knob 2 injects a coherent classical tone, phase-locked between stations $A$ and $B$ with polarization $\psi$ and shot-to-shot randomized global phase, predicting:
$$\delta E(a, b) = 2\kappa_1 \kappa_2 \lambda^2 \cos 2(a-\psi)\cos 2(b-\psi), \qquad \delta S > 0 \quad (S > 2\sqrt{2}).$$
The authors claim: *"an $S > 2\sqrt{2}$ reading under injection would be an unambiguous non-QM signature."*

**Standard QM Systematic That Produces $S_{\text{post}} > 2\sqrt{2}$ Under Coherent Injection:**
In standard quantum mechanics, Tsirelson's bound $S \le 2\sqrt{2}$ holds for trace-preserving local quantum operations (POVMs whose outcome probabilities sum to 1 independently of the analyzer angle $a, b$).
However, when a classical coherent field $|\alpha e^{i\phi}\rangle$ polarized along $\psi$ enters a polarization analyzer set at angle $a$, the transmitted coherent intensity into port $+$ is $|\alpha|^2 \cos^2(a-\psi)$ and into port $-$ is $|\alpha|^2 \sin^2(a-\psi)$.
In any real single-photon detector (SPAD or SNSPD), adding a classical background field modulated by $\cos^2(a-\psi)$ does two things in ordinary QM:
1. It generates background counts / homodyne interference proportional to $\cos^2(a-\psi)$ in port $+$ and $\sin^2(a-\psi)$ in port $-$.
2. Even in gated single-photon coincidence windows, the classical field shifts the absorber closer to threshold in the port aligned with $\psi$, **modulating the effective detection efficiency $\eta_\pm(a, \psi)$ as a function of $\cos 2(a-\psi)$**.
It is a well-known theorem in Bell test analysis (e.g., Larsson 1998; Gisin & Gisin 1999; Adenier & Khrennikov 2007) that if detection efficiency or threshold activation depends on the angle $(a - \psi)$ between the analyzer and a shared classical variable $\psi$, **postselected coincidence correlators $E_{\text{coinc}}(a,b)$ easily exceed the Tsirelson bound $2\sqrt{2}$ (reaching up to $S = 4$) strictly within standard physics!**
To ensure that an observed $\delta S > 0$ is not a standard QM efficiency-modulation / homodyne-threshold artifact, §8.7 must specify that $S$ is evaluated using **unconditional (non-postselected) Clauser–Horne or Eberhard inequalities**, or prove that the single-station calibration of $\kappa\lambda$ separates share-drift redirection (which conserves total clicks $N_+ + N_-$) from threshold/efficiency modulation (which changes $N_+ + N_-$).

---

## 3. Structural, Editorial, and Minor Technical Issues

### 3.1 The "Archaeological Strata" Problem
The manuscript currently carries four layers of self-contradictory revisions inside the main text:
* **Pages 1–4:** A 3.5-page single-spaced revision ledger precedes the Abstract.
* **Page 10 (Premise P4):** States P4, then adds a paragraph explaining v0.7, then a paragraph explaining how v0.8 withdraws v0.7, then a paragraph explaining how v0.9 adopts Reading B and supersedes v0.8.
* **Page 19 (Theorem 2(iii)):** Discusses v0.7's withdrawal of the fast-commit reading, which was itself withdrawn in v0.8 on p. 21! Thus **page 19 directly contradicts page 21**:
  * Page 19 says: *"With commitment slow (§6.1), a continuum absorber runs to the absorbing boundary just as a discrete-level one does, and therefore traverses the same boundary layer and incurs the same $O(w)$ deviation."*
  * Page 21 says: *"v0.8 withdraws the withdrawal. The ns–$\mu$s figure is the avalanche-and-quench cycle... Theorems 4–5 are load-bearing for class (ii)"* — and Table 1 on p. 28 lists the soft locking threshold $O(w)$ channel as **Retracted**!
  * This means **Figure 4 on p. 19 and paragraph (iii) on p. 19 are left in the v0.7 state, contradicting v0.8, v0.9, and Table 1!**
* **Pages 21–23 (§5.4 and §6.1):** Present the v0.8 calculations, followed immediately by v0.9 paragraphs that invalidate them.

### 3.2 Specific Textual, Typographical, and Numbering Errors
1. **Broken Figure Numbering (Throughout):**
   * On p. 17, the first figure is labeled `Figure 1: Figure 2. The knife-edge...`
   * On p. 17, the second figure is labeled `Figure 2: Figure 3. The martingale...`
   * On p. 24, the bar chart (`Same marginals, opposite correlations`) has **no `\caption` at all**, though the text on p. 24 refers to it as `(Fig. 5)`.
   * On p. 26, the third numbered figure is labeled `Figure 3: Figure 6. The resync-fidelity law...`
   * On p. 30, the fourth numbered figure is labeled `Figure 4: Figure 7. The tabletop discriminator...`
   * Furthermore, p. 18 refers to `(Fig. 4)` for the soft lock-layer width plot on p. 19, which also lacks a `\caption`.
2. **Broken List Numbering in §9.4 (Open Problems, p. 36):**
   * The first paragraph of §9.4 runs items `(i)` through `(viii)` inline in a single block paragraph.
   * Immediately below it, a new bulleted list starts at `(ii) Relational-phase completion`, `(iii) Sector-blindness...`, and `(iv) Share ontology...` (which the text elsewhere refers to as `§9.4(xi)`!).
3. **Unfinished Draft Placeholders and LaTeX Typos:**
   * **Page 9, bottom line:** `"and §8 [to draft] builds its experimental proposals..."` — leftover `[to draft]` marker.
   * **Page 22, bullet 3, line 9:** `"field-driven seed unrecoverability $ff$1 ps"` — corrupted LaTeX ligature/macro (likely `\lesssim 1\text{ ps}` or `\sim 1\text{ ps}`).
   * **Page 38, Appendix D, line 15:** `"[repository ref]"` — unresolved citation placeholder.
   * **Page 39, References header:** `"(Author–year style, alphabetical; matches in-text name citations. Entries flagged [verify] require bibliographic confirmation before any submission.)"` — internal author note left in the manuscript.

---

## 4. Actionable Roadmap for Revision (v1.0)

To transform this draft into a cohesive, mathematically rigorous, and publishable manuscript, I recommend the following five-step revision plan:

### Step 1: Purge the Revision Strata and Commit to One Architecture
* Move the 3.5-page header log (pp. 1–4) and the chronological v0.7 $\to$ v0.8 $\to$ v0.9 debates in §2, §5.4, §6.1, and §9.4 into a dedicated Appendix or supplementary note (*"Appendix F: Eliminated Mechanisms and Timescale Ledger"*).
* Reconcile page 19 (Theorem 2(iii) and the uncaptioned Figure 4) with §5.4 and Table 1 so the paper does not simultaneously claim the $O(w)$ soft-threshold deviation is active (p. 19) and retracted (p. 28).

### Step 2: Resolve the v0.9 "Reading B vs. Stage 2 Game" Dilemma
Be completely transparent about what happens under Reading B:
* Under **Reading B**, if every site has an ungated memoryless hazard $\lambda_i(t) = \Gamma s_i(t)$ from $t = 0^+$, then **the linear commitment hazard (Theorem 5) + initial capture shares (P1) + closed pot (P4a/P5) already produce the Born rule at $t = 0^+$**.
* In that architecture, the Stage-2 exchange game ($ds_i$) is **not** what generates the Born probabilities; rather, Theorems 1–3 prove **non-distortion (martingale conservation of expected shares)** during the finite waiting time before the Golden-Rule vertex fires.
* Alternatively, if you want Stage 2 first-passage ($s_i \to 1$) to be the actual selection mechanism (**Reading A**) without incurring the $+0.1$ to $+0.2$ bias in silicon, you should investigate why `threshold_gated_commit.py` spent 40–90% of the game above $\theta$:
  * In your discrete engine, the step size is $\delta = \pm \text{step} \cdot \min(e_i, e_j)$. As the losing sites drain ($1 - s_{\text{leader}} \to 0$), the step size shrinks **linearly** with $(1 - s_{\text{leader}})$, which causes an exponential slowdown ($s_{\text{leader}} \to 1$ takes infinite time in the continuum limit of $\dot{s} \sim 1-s$, a geometric Brownian tail!).
  * By contrast, in the true continuum Wright–Fisher / Pearle SDE $ds = \sigma \sqrt{s(1-s)}\,dW$, the diffusion coefficient scales as the **square root** $\sqrt{1-s}$, which reaches the boundary $s = 1$ in **strictly finite time** without slowing down! Re-running `threshold_gated_commit.py` with the true $\sqrt{s_i s_j}$ Wright–Fisher exchange step rather than $\min(e_i, e_j)$ will dramatically shorten $t_{\text{exp}}$!

### Step 3: Formulate Theorem 1 and Theorem 3 on the Energy-Conserving Simplex
Replace the non-conserving independent SDE $de_i = \sigma\sqrt{e_i}\,dW_i$ with a manifestly energy-conserving stochastic exchange on the simplex $\sum_i e_i = E_0$, or state explicitly that $e_i$ in Theorem 1 represents an unnormalized branching weight while physical energy is $E_0 s_i = E_0 e_i / \sum_j e_j$.
* Crucially, check what happens to the **port decomposition (§8.2–8.3)** under local energy conservation: if Port A and Port B are macroscopically separated so that no energy is exchanged between Port A and Port B during the local sub-threshold game prior to commitment, then the total energy in Port A ($E_A = \sum_{i \in A} e_i$) cannot drift due to internal correlations $C_{ij}$ within Port A! The port-level drift $\dot{S}_A = \frac{\sigma^2}{E^2}(q_B S_A - q_A S_B)$ in Appendix E.2 arises **entirely** from fluctuating total energy $dE_A \neq 0$ normalizing against $E = E_A + E_B$. This is a pivotal theoretical check: if within-port exchange conserves $E_A$ locally, the protective reading of §8.5 holds automatically!

### Step 4: Replace the Real Contraction $-\kappa_{\text{ret}}$ in Theorem 2 with Off-Shell Detuning
Rewrite Theorem 2 and Appendix B.1 so that the off-shell energy deficit $\Delta E = E_0 - e$ enters as a conservative frequency detuning $\Delta_{\text{off}} = \Delta E/\hbar$ in the imaginary part of the mode evolution rather than a real damping rate $-\kappa_{\text{ret}}$. Use fast-phase averaging outside the Arnold tongue ($\Delta_{\text{off}} > K \iff \Delta E > \hbar K$) to prove that rich-get-richer entrainment vanishes outside the boundary layer $w = K/\omega$.

### Step 5: Tighten the Experimental Protocols in §8.4 and §8.7
* In **§8.4 (Tabletop Discriminator)**: Explicitly derive the standard-QM conditional click formula $P_{\text{QM}}(A \mid \text{click}) = \frac{\eta_A S}{\eta_A S + \eta_B(1-S)}$ for mismatched port efficiencies $\eta_A \neq \eta_B$, show that it also bows as $\frac{\eta_A - \eta_B}{\bar{\eta}}S(1-S)$, and specify **heralded unconditional port counting** $P(A\text{ clicks} \mid \text{herald}) = \eta_A S$ (or endpoint efficiency calibration at $S=0, 1$) to eliminate the efficiency-mismatch confound.
* In **§8.7 (Cross-Station Bell Injection)**: Specify that the CHSH parameter $S$ under phase-locked tone injection must be computed using **heralded / unconditional event normalization** (or monitored for total coincidence-rate invariance $\partial_\psi N_{\text{coinc}}(a,b,\psi) = 0$) so that angle-dependent detector efficiency modulation (the homodyne fair-sampling loophole) cannot mimic an above-Tsirelson violation.
