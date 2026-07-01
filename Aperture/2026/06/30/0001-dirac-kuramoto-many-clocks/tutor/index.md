# Tutor — *Two Regimes of the Chiral Mass Coupling*

A layered explainer. Read the level that fits you; drop down a level whenever a term loses you.

---

## Level 1 — for a non-specialist (e.g. a physician)

**The problem.** Quantum theory says an unmeasured particle is in a *superposition* — several possibilities at once. But every time we look, we find exactly one outcome. The equations that govern the particle never actually pick one. That gap — between "many possibilities evolving smoothly" and "one definite result" — is the **measurement problem**, the oldest open wound in quantum mechanics.

**The usual answers, and their costs.** *Copenhagen* says the superposition "collapses" when measured, but never says how (a rule with no mechanism). *Many-Worlds* says every possibility happens, in separate branching universes (keeps the math clean at the cost of unobservable parallel worlds).

**This paper's picture.** Imagine every particle carries a tiny internal **clock** (a phase). Measurement is not a magic collapse and not a branching of worlds — it is the particle's clock **synchronizing** to the enormous "clock" of the measuring device, the way one out-of-step metronome on a shared table falls into rhythm with thousands of others. One world, no collapse, no branches — just synchronization. The device is so much larger that the particle has no choice but to fall into step, and *which* step it falls into is the measured outcome.

**A key subtlety the paper is careful about.** A free, untouched particle does **not** synchronize — its clock just precesses smoothly, preserving the superposition. Synchronization (and hence a definite outcome) switches on **only** when the particle is coupled to a big dissipative environment — a detector. The authors prove the "off" state mathematically, which is why they call it *two regimes*: closed (no locking) vs. open (locking = measurement).

**What it honestly does not do.** It does **not** explain *why* the long-run odds of outcomes follow the famous **Born rule** (probability = amplitude squared) — that is flagged as unsolved. And it does **not** claim any new experimental prediction for its core; one candidate test exists but probes an *extra* assumption, not the main idea.

---

## Level 2 — for an adjacent-field scientist

**The starting identification.** Write the Dirac equation in the **chiral (Weyl) basis**, where a spin-½ particle splits into left- and right-handed (L, R) components. The **mass term is the off-diagonal coupling** between them — it is the only thing connecting L and R. The paper reads that coupling strength as **K = m**.

**Closed regime (no attractor).** Do a **Madelung reduction** (write each component as amplitude × phase). In a *closed* system the L↔R coupling produces unitary **normal-mode precession** (Rabi-like oscillation) — and crucially it has **no attractor**: the phase difference does not get pulled toward any locked value. This is a *no-go* result, not a derivation: a coupling that superficially looks like a Kuramoto synchronizer is shown to have an off-switch.

**Open regime (Adler/Kuramoto locking).** **Open** the system to a dissipative bath and trace it out. Now the reduced phase obeys an **Adler/Kuramoto equation** — and an **attractor appears**. The system phase-locks. That switch — closed→open — *is* measurement.

**Two stages.** Measurement = (Stage 1) a fast **resonant capture**, then (Stage 2) **irreversible equilibration** to the bath's collective reference. The paper maps these onto the **real vs. imaginary parts** of an effective action / self-energy: Stage 1 ↔ reactive (Re), Stage 2 ↔ absorptive (Im). The "Heisenberg cut" becomes a vivid image: the dressed mass pole **leaving the real axis**.

**Where it sits.** Single-world, ψ-ontic (the wavefunction is real/physical), and nonlocal — same family as **Bohm** and **Nelson**. It carries a **physical preferred frame**, but only through Stage 2 (measurement); the unitary dynamics stay Lorentz-covariant.

**The two debts (stated as such):** (1) the **Born measure** is reframed (for equal-energy channels), not derived; (2) there is no explicit **dynamical law** for how the background selects an outcome — which is also where the nonlocality hides.

---

## Level 3 — for a specialist (skip to the contested steps)

What is genuinely new is **an organizing identification plus an ontological proposal**, *not* new dynamics — the paper concedes that irreversibility-as-amplification (Bohr, Wheeler, DLP), einselection (Zurek), the influence functional, the Schwinger rate, Kramers–Kronig, and the Adler linearization are all *adopted*. The contested steps a referee will press (see [the Fable 5 review](../01-original-submission-and-review/review/reviewer-A-fable5.md)):

1. **Born statistics (highest leverage).** If outcome selection is genuinely a basin-of-attraction story, the weights are fixed by basin geometry + the invariant measure on backgrounds, with no evident reason to equal |α|². Either derive the measure (and risk computing basin-area/equal weights — internal falsification) or admit it is an imported postulate. Staged as [dispute-001](../resolution/dispute-001-born-basin-measure.md).
2. **Im Σ = −½ K_eff cos Δ\*** (§3.6) is asserted, not demonstrated — needs one bath model where both sides are computed independently and shown to agree.
3. **Preferred-frame bounds** (§8) — a plausibility argument ("gravitationally suppressed"), not a bound against SME / clock-comparison limits at 10⁻¹⁷; possibly make-or-break.
4. **Advantage-over-Bohm** (observable frame) is deferred to an unrefereed companion [26]; within this paper the frame is as undetectable as Bohm's.

---

## Key references, explained

*What each load-bearing source actually shows, and why this paper leans on it. (A reference that can't be explained was probably misused — this list is also the citation-integrity check.)*

- **Dirac equation, Weyl (chiral) basis** — the relativistic wave equation for spin-½. In the chiral basis it splits into coupled L/R Weyl equations whose only coupling is the mass. *This is the entire foundation: "mass = L↔R coupling, K = m" is a re-reading of standard Dirac structure, not a modification of it.*
- **Kuramoto (1975), coupled-oscillator synchronization** — the canonical model of how populations of phase oscillators spontaneously lock. *Supplies the "synchronization = measurement" metaphor and, in the open regime, the actual locking equation.*
- **Adler equation** — the one-oscillator phase-locking equation (injection locking). *The reduced open-system phase obeys it; its attractor is the locked outcome.*
- **[2,3] Bohm (1952), pilot-wave mechanics** — a ψ-ontic, deterministic, explicitly nonlocal interpretation with a real guiding wave. *The closest cousin; the paper positions MCI as same-family but with a physical (not undetectable) preferred frame.*
- **[19] Nelson (1966), stochastic mechanics** — derives the Schrödinger equation from a Brownian (stochastic) process on configuration space. *Cited as the stochastic-dynamics sibling and a route the framework gestures toward for statistics.*
- **[29,36] Relational-clock / quantum time (Page–Wootters, Connes–Rovelli thermal time)** — time/dynamics emerges from correlations with a clock subsystem rather than an external parameter. *Grounds the "every particle is a clock" ontology in an existing lineage.*
- **[14] Superconducting-qubit catch-and-reverse** — an experiment reversing a partial measurement. *Used as a concrete exhibit of the reversible→irreversible boundary the two-stage picture is about.*
- **Penrose–Diósi objective reduction** — gravitationally-induced collapse with timescale τ ≈ ℏ/E_G. *The framework's gravitational-decoherence channel echoes this; placed as a relative, not a rival.*
- **[26] Bramble (2026), companion preprint** — ⚠️ **unrefereed and not independently verifiable.** Several distinctive claims (physicalized guidance field, AB phase from zero-frequency locking, non-suppressed kinematic frame coupling) lean on it. *Flagged by Reviewer A as a self-containment problem (Concern 6): claims that depend on it should be internalized or softened.*
