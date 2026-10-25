# Extension Note: Shared-Phase Wave Pairs, Malus’s Law, and Why the First Detector Lock Must Entrain the Shared Phase

**Prepared for:** John M. Bramble, MD  
**Date:** October 14, 2026  
**Companion to:** *A Field–Matter Selector for Outcome Production via Conserving Complex-Interference Exchange* (`field_matter_selector_v1.0`)

---

## 1. Purpose of This Note

In standard treatments of quantum entanglement (and in earlier drafts of the selector paper), two-particle correlations are written in **probability / Hilbert-space matrix notation**: a joint coefficient matrix $c_{ij}$ is defined in configuration space, the first detection selects row $i$ with marginal probability $m_i = \sum_j |c_{ij}|^2$, and the second station’s probabilities are updated via Bayes’ conditional rule $P(j \mid i) = |c_{ij}|^2 / m_i$.

While mathematically convenient, that notation obscures the physical wave mechanism by moving the explanation back into probability space. This note records the purely **wave-mechanical formulation in 3D detector space**, answering three foundational questions:
1. How do entangled pair correlations and no-signaling arise from **classical Malus’s law ($\cos^2(a-b)$)** and **wave trigonometry** without invoking probability-space matrices $c_{ij}$?
2. Does this eliminate "spooky action at a distance," or where does the nonlocality reside?
3. Why must the first detector’s lock **actively shift (entrain/pin) the shared phase**, rather than the two waves simply carrying a passive, pre-set phase $\theta_0$ from the source?

---

## 2. Single-Event Wave Picture of an Entangled Pair (No Probability Space)

Suppose two waves $A$ and $B$ are created together in a single source excitation and travel to two spatially separated polarization analyzers: Polarizer $A$ (oriented at angle $a$) and Polarizer $B$ (oriented at angle $b$). Each polarizer splits its incident wave into two orthogonal output ports ($+$ along the polarizer axis, and $-$ along the perpendicular axis $+90^\circ$), where detector sites run the conserving complex-interference walk:
$$\Delta s_+ = -\Delta s_- = 2\epsilon \sqrt{s_+ s_-}\cos(\Delta\phi).$$

Instead of a Hilbert-space probability table $c_{ij}$, consider what the physical waves do in a single event:

1. **Creation with a Shared, Unpinned Phase Reference:**  
   Because waves $A$ and $B$ originate from the same atomic transition or parametric down-conversion vertex, their **relative phase/polarization difference is locked** ($\phi_A - \phi_B = 0$), while their **common absolute orientation is initially unpinned** (free to rotate, like a holographic wavefront prior to fixing the reference beam).
2. **At the First Detector to Lock (Say Station $A$):**  
   Because the pair’s common polarization orientation is unpinned relative to angle $a$, the two orthogonal output ports of Polarizer $A$ ($+$ at angle $a$, and $-$ at angle $a + 90^\circ$) receive equal initial wave energy ($s_+(0)_A = 0.5, s_-(0)_A = 0.5$). Station $A$’s local $\sqrt{s_+ s_-}\cos\Delta\phi$ walk runs with its local detector and vacuum phases until one port reaches $1$—locking onto either angle $a$ (port $+$) or angle $a + 90^\circ$ (port $-$), each occurring in $50\%$ of events.
3. **Entrainment of the Shared Phase Frame:**  
   When Station $A$’s absorber sites lock onto port $+$ (angle $a$), that lock **physically pins (entrains) the shared polarization orientation of the pair wave to angle $a$** ($\phi_A = a$). Because the pair wave maintains the rigid phase relation $\phi_A - \phi_B = 0$, the partner wave arriving at Station $B$ now has its polarization oriented along angle $a$ ($\phi_B = a$).
4. **Malus’s Law Projection at the Partner Station (Station $B$):**  
   When a wave polarized along angle $a$ passes through Polarizer $B$ oriented at angle $b$, **ordinary classical wave optics (Malus’s law, 1809)** dictates that the transmitted field amplitude along $b$ is $\cos(a - b)$ and the orthogonal field amplitude along $b + 90^\circ$ is $\sin(a - b)$.  
   By Postulate 1, the initial mechanical oscillator energies deposited in Station $B$’s $+$ and $-$ ports are simply the classical Malus wave intensities:
   $$s_+(0)_B = \cos^2(a - b), \qquad s_-(0)_B = \sin^2(a - b).$$
   Station $B$ then runs its own local $\sqrt{s_+ s_-}\cos\Delta\phi$ walk on those mechanical shares. By Theorem 1, Station $B$ registers $+$ in a fraction $\cos^2(a - b)$ of those events and $-$ in a fraction $\sin^2(a - b)$.

---

## 3. Why "No-Signaling" Is Pure Wave Trigonometry

In this wave-mechanical picture, why does rotating Polarizer $A$ to any angle $a$ never change the single-station click rate at Station $B$?

* In the **$50\%$ of events** where Station $A$ locks onto its $+$ port (angle $a$), the partner wave is pinned to angle $a$, so Station $B$’s $+$ port receives mechanical wave energy:
  $$s_+(0)_B^{(+)} = \cos^2(a - b).$$
* In the **other $50\%$ of events** where Station $A$ locks onto its $-$ port (angle $a + 90^\circ$), the partner wave is pinned to angle $a + 90^\circ$, so Station $B$’s $+$ port receives mechanical wave energy:
  $$s_+(0)_B^{(-)} = \cos^2(a + 90^\circ - b) = \sin^2(a - b).$$
* Averaging over both equally frequent outcomes at Station $A$, the mean mechanical wave energy delivered to Station $B$’s $+$ port is governed by the elementary trigonometric identity:
  $$\bar{s}_+(0)_B = \frac{1}{2}\cos^2(a - b) + \frac{1}{2}\sin^2(a - b) = \frac{1}{2}\big[\cos^2(a - b) + \sin^2(a - b)\big] = \frac{1}{2},$$
  which is **identically $0.50$ for every possible angle $a$**!

Thus, **no-signaling is not a probability-space postulate**—it is the Pythagorean trigonometric identity $\cos^2\theta + \sin^2\theta = 1$ of two orthogonal wave projections.

---

## 4. Where Does the Nonlocality Reside? (No Propagating Force vs. Shared Wave Frame)

Does this picture eliminate "spooky action at a distance"? It separates two things that are usually conflated:

1. **No Propagating Force or Energy Transfer Between Stations:**  
   In an entangled pair, Station $A$ already holds its own full quantum $\hbar\omega$ and Station $B$ already holds its own full quantum $\hbar\omega$. When Station $A$ locks, **no energy, momentum, or force beam travels through space from $A$ to $B$**, and Station $B$’s total energy ($\cos^2(a-b) + \sin^2(a-b) = 1$) never changes.
2. **Nonlocality Resides in the Shared Phase Frame of the Wave:**  
   However, the two waves cannot be treated as completely separate objects after leaving the source. They remain a **single, phase-connected wave excitation** ($\phi_A - \phi_B = 0$) spanning the distance between $A$ and $B$. Locking the phase reference at one end pins the shared phase frame of that extended wave object.

---

## 5. Mathematical Proof: Why the First Lock MUST Shift/Entrain the Shared Phase

A natural question is: *Does the first detector's interaction actually have to shift/pin the shared phase, or could the two waves simply leave the source with a shared phase $\theta_0$ that passively guarantees a similar interference pattern at both detectors (outside of the local quantum vacuum and detector phases)?*

Here is the exact mathematical proof showing why a **passive (unshifted) source phase $\theta_0$ fails**, and why **entrainment (shifting/pinning the shared phase to the first polarizer's axis $a$)** is required.

### Case A: Passive Source Phase $\theta_0$ (No Shift Upon First Lock)
Suppose the two waves leave the source with a common polarization angle $\theta_0 \in [0, 2\pi)$, and nothing shifts $\theta_0$ when the first detector interacts.
1. At Polarizer $A$ (angle $a$), the wave interference pattern gives initial shares:
   $$s_+(0)_A = \cos^2(a - \theta_0), \qquad s_-(0)_A = \sin^2(a - \theta_0).$$
2. At Polarizer $B$ (angle $b$), the wave interference pattern gives initial shares:
   $$s_+(0)_B = \cos^2(b - \theta_0), \qquad s_-(0)_B = \sin^2(b - \theta_0).$$
3. Each detector then runs its own local $\sqrt{s_+ s_-}\cos\Delta\phi$ walk driven by its own independent detector and quantum vacuum phases. By Theorem 1, for a given source angle $\theta_0$, Station $A$ registers $+$ with frequency $\cos^2(a - \theta_0)$ and Station $B$ registers $+$ with frequency $\cos^2(b - \theta_0)$ independently.
4. Averaging over all source phases $\theta_0 \in [0, 2\pi)$ gives the joint coincidence rate:
   $$P_{\text{passive}}(++ \mid a, b) = \frac{1}{2\pi}\int_0^{2\pi} \cos^2(a - \theta_0)\cos^2(b - \theta_0)\,d\theta_0 = \frac{1}{4} + \frac{1}{8}\cos 2(a - b),$$
   which yields the correlation function:
   $$E_{\text{passive}}(a, b) = P(++) + P(--) - P(+-) - P(-+) = \frac{1}{2}\cos 2(a - b) \implies S_{\text{CHSH}} = \sqrt{2} \approx 1.414.$$

**Why Case A Fails Physically (Look at $a = b$):**  
Suppose both polarizers are set to the **exact same vertical angle** ($a = b = 0^\circ$), and a pair leaves the source with $\theta_0 = 45^\circ$.
* Then Station $A$ gets $\cos^2(45^\circ) = 0.50$ and Station $B$ gets $\cos^2(45^\circ) = 0.50$.
* Because the local vacuum and detector phases at $A$ and $B$ are independent, in half of those runs Station $A$'s walk goes to $+$ while Station $B$'s walk goes to $-$!
* Across all $\theta_0$, when $a = b$, the two stations only agree **$75\%$ of the time** ($E(a, a) = 0.50$), whereas experimentally (and in quantum mechanics) aligned polarizers on $|\Phi^+\rangle$ agree **$100\%$ of the time** ($E(a, a) = 1.00$)!

### Case B: Active Entrainment / Pinning of the Shared Phase by the First Lock
Now contrast Case A with what happens when the source locks only the **relative phase difference** $\phi_A - \phi_B = 0$, and the first detector to complete its walk **shifts/entrains the common phase orientation into alignment with its winning polarizer axis** ($a$ or $a + 90^\circ$):
1. When Station $A$ locks onto port $+$ (angle $a$, occurring in $50\%$ of trials), the shared phase is shifted to $\phi_A = \phi_B = a$.
2. Now look at $a = b$: at Station $B$, the wave arrives with $\phi_B = a = b$, so its Malus interference pattern across Station $B$'s two ports is:
   $$s_+(0)_B = \cos^2(a - a) = \cos^2(0) = 1, \qquad s_-(0)_B = \sin^2(0) = 0.$$
3. Because $s_-(0)_B = 0$, the complex interference step at Station $B$ is $2\epsilon\sqrt{s_+ s_-} = 2\epsilon\sqrt{1 \times 0} = 0$! **Even though Station $B$ has its own random detector and vacuum phases, a port with zero wave amplitude cannot fluctuate away from zero.** Station $B$ is therefore guaranteed to register $+$ **$100\%$ of the time** when $a = b$!
4. For general angles $(a, b)$, this gives the exact quantum coincidence rate:
   $$P_{\text{entrained}}(++ \mid a, b) = \frac{1}{2}\cos^2(a - b) = \frac{1}{4} + \frac{1}{4}\cos 2(a - b) \implies E(a, b) = \cos 2(a - b), \quad S_{\text{CHSH}} = 2\sqrt{2} \approx 2.828.$$

---

## 6. Summary Comparison Table

| Feature | Passive Source Phase ($\theta_0$ Not Shifted by First Lock) | Shared-Phase Entrainment (First Lock Shifts $\phi_{\text{shared}} \to a$) |
| :--- | :---: | :---: |
| **What the source fixes** | Absolute polarization angle $\theta_0 \in [0, 2\pi)$ | Relative phase $\phi_A - \phi_B = 0$ (common angle free) |
| **Effect of first detector lock at $a$** | Local only; partner wave remains at $\theta_0$ | Entrains shared phase so partner wave is at angle $a$ |
| **Partner station initial shares** | $\cos^2(b - \theta_0)$ and $\sin^2(b - \theta_0)$ | $\cos^2(a - b)$ and $\sin^2(a - b)$ (Malus's Law) |
| **Same-angle correlation $E(a, a)$** | $0.50$ ($75\%$ agreement — **falsified**) | **$1.00$ ($100\%$ agreement — matches experiment)** |
| **General correlation $E(a, b)$** | $\frac{1}{2}\cos 2(a - b)$ | **$\cos 2(a - b)$** |
| **CHSH Parameter $S$** | $\sqrt{2} \approx 1.414$ | **$2\sqrt{2} \approx 2.828$** |
