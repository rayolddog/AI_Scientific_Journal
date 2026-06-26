# Experiment / Falsification — standing call (Article 0001)

**Status:** `open-call`

> *Bell wrote the inequality; Aspect built the apparatus.* This file is a standing public invitation to the labs that could test the framework's one non-trivial physical commitment. Any result — confirming, refuting, or null — publishes here as part of the article's living record.

## The honest framing (read first)

The framework is, by the authors' own statement, **empirically equivalent to standard QM in its core**. Its single point of potential empirical contact is an **added, non-covariant preferred-frame postulate** that enters only at Stage 2 (measurement). So these tests probe **the postulate, not the framework's core** — and the manuscript (and Reviewer A, Concern 5) both stress that this postulate may already be in tension with precision Lorentz-violation bounds. The point of listing them is to make the postulate *answerable* rather than perpetually deferred.

Tests **T1–T5 probe the same preferred-frame postulate** through different channels. **T6 is categorically different** — it is the first test of the framework's **core measurement mechanism** (is the Heisenberg cut an Adler *locking bifurcation*?), and so carries weight against the framework's centre, not just its added postulate.

| Test | Channel / observable | Predicted signature | Regime / apparatus | Status |
|---|---|---|---|---|
| **T1** | Gravitational Bell effect vs **detector linewidth** | Bell/CHSH degradation correlated with linewidth under gravitational decoherence | entangled-pair Bell test with controlled detector linewidth | open-call |
| **T2** | **Sidereal** GHZ correlations | GHZ correlation modulation periodic with sidereal time (Earth rotating through the frame) | multi-party GHZ interferometry, long integration | open-call |
| **T3** | Aharonov–Bohm visibility vs **γ** (Lorentz factor) | AB interference visibility envelope dependent on velocity/γ | AB interferometry across kinematic regimes | open-call |
| **T4** | **MRI / NMR surface relaxation** (dissipation channel) | boundary-induced relaxation signature from vacuum locking at material surfaces | precision NMR/MRI relaxometry | open-call |
| **T5** | **LIGO sidereal quantum-noise** (dissipation channel) | sidereal anisotropy in interferometer quantum noise | gravitational-wave interferometer noise data | open-call |
| **T6** ⭐ | **Locking-threshold / Adler-cut** (core mechanism) | the record/reversibility boundary is a **SNIC bifurcation** at \|Δω\|=K_eff: critical slowing τ ∝ (K_eff−\|Δω\|)^(−½), sub-threshold phase slips at √(Δω²−K²), and the catch-and-reverse window edge **coincident** with the tongue — vs a smooth decoherence crossover (null) | circuit-QED transmon + tunable continuous readout (Minev/Murch–Siddiqi regime) | open-call |

**Canonical sources for the protocols:** T1/§6 of `PAPER_REVISED.md`; T3 → `AB_VISIBILITY_PAPER.md`; T5 → `LIGO_SIDEREAL_TEST_T5.md` (all in the source repository); **T6 → full spec at [`resolution/dispute-002-retirement-path.md`](resolution/dispute-002-retirement-path.md)** (the retirement path for the dispute-002 standing dissent).

> **Why T6 matters most.** T1–T5 test an *added postulate* the framework could shed without collapse; **T6 tests the framework's central claim** that measurement *is* a dissipative locking transition. A null on T6 falsifies the core; a positive result supplies the "new testable prediction" that would retire the dispute-002 reject-vs-accept split. It is also the only test derivable from a standard circuit-QED model with **no new physics postulated**.
>
> **Part I of T6 is done (2026-06-25).** The locking strength is *derived*, not assumed: **K_eff = 4χ²n̄/κ** from the transmon+readout master equation, with the cut a readout-power threshold **n̄_crit = κ\|Ω\|/(4χ²)**, and all three SNIC signatures validated numerically — see [`resolution/dispute-002-retirement-path.md`](resolution/dispute-002-retirement-path.md) (§Part I result) and [`resolution/dispute-002-partI-Keff.py`](resolution/dispute-002-partI-Keff.py).
>
> **Part II is a commit-ready protocol.** Full hand-to-a-lab spec at [`resolution/dispute-002-partII-protocol.md`](resolution/dispute-002-partII-protocol.md): a transmon under continuous σ_z readout + Rabi drive, four measurements (Arnold tongue → critical-slowing exponent ½ → √-law slips → **catch-and-reverse edge on the tongue**), pulse sequences, discrimination table, ~1 device-week on existing hardware. A **null falsifies the framework's core**; a positive result supplies the new testable prediction that retires the dispute-002 reject-vs-accept split. **This is the commitment to invite.**

## Where the bounds already stand

- **Free-precession channel: closed.** Existing spin-precession anisotropy limits constrain the relevant coefficient to roughly **bₙ < 6.7×10⁻³⁴ GeV** — tight enough to rule out that channel.
- **Dissipation channel (T4/T5): unprobed.** The framework's postulate enters through *dissipative* (Stage-2) dynamics, a channel the free-precession bounds do **not** cover. This is the live loophole — and therefore where an experimental commitment would be most decisive.

> ⚠️ Quantitative caveat: an order-of-magnitude estimate tying each predicted anisotropy to a specific bound is **owed** (Reviewer A, Concern 5) and not yet supplied. A committing lab should ask the authors for that estimate first.

## How to commit

A lab able to run any of these is invited to open an **Issue** or **Pull Request** committing to the test, with a protocol and timeline. The result is published here whatever it shows — a null result that closes the T4/T5 loophole is as valuable as a positive one. **T6 is the highest-leverage commitment**: it needs only existing circuit-QED hardware and tests the framework's core rather than its postulate. A continuous-measurement group is the natural lab — see the [T6 spec](resolution/dispute-002-retirement-path.md).
