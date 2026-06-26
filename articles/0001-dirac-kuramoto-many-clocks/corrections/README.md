# Corrections — Article 0001

This folder makes the **review → correction** loop concrete and inspectable: the manuscript *as submitted to AI review*, and each correction made in response, frozen as artifacts so the demonstration is reproducible even as the source manuscript keeps evolving.

## The three demonstration artifacts

| Stage | Artifact |
|---|---|
| **1. As submitted for review** | [`paper-01-as-reviewed-2026-06-25.md`](paper-01-as-reviewed-2026-06-25.md) |
| **2. The reviews** | [`../review/`](../review/) — Fable 5 (Anthropic), Gemini 3.1 Pro (Google DeepMind), GPT-5.5 Thinking (OpenAI) |
| **3. The corrections** | this folder — one `.diff` per correction, plus the post-correction snapshot |

The "as submitted" snapshot is a verbatim copy of the canonical manuscript at git commit **`1602f31`** of the source repository (`PAPER_REVISED.md`, "Two Regimes of the Chiral Mass Coupling"). It is the exact version the **2026-06-25** reviews (Gemini 3.1 Pro, GPT-5.5 Thinking) read. *Fable 5* reviewed a slightly earlier snapshot (2026-06-12) — see the currency note in [`../review/reviewer-A-fable5.md`](../review/reviewer-A-fable5.md).

## Corrections applied so far

| # | Correction | Addresses | Files |
|---|---|---|---|
| **001** | De-load-bear the unpublished companion preprint **[26]** (Aharonov–Bohm visibility paper). Re-anchored the "MCI's preferred frame is detectable, Bohm's is not" claim (§7.3) to the in-paper §6 gravitational channel; recast the §7.3 / §7.4 / §8 citations of [26] as *separate work, not relied on here*. | Fable 5 **Concern #6** ("load-bearing reliance on an unrefereed companion"); GPT-5.5 **citation-integrity** flag (rubric 3/5) | [`correction-001-companion-citation.diff`](correction-001-companion-citation.diff) · [`paper-02-after-correction-001-2026-06-25.md`](paper-02-after-correction-001-2026-06-25.md) |
| **002** | Soften the *remaining* [26] citations: drop the incidental one at §3.7 (the claim rests on §2.4 alone), and move the §7.3 Aharonov–Bohm-phase result into a parenthetical marked *developed in separate work, not relied on here*. After this, **every in-text [26] citation is a forward-pointer** — none is load-bearing. | completes Fable 5 #6 / GPT-5.5 citation-integrity | [`correction-002-companion-citation.diff`](correction-002-companion-citation.diff) · [`paper-03-after-correction-002-2026-06-25.md`](paper-03-after-correction-002-2026-06-25.md) |
| **003** | State **"Horn 2"** for the Born measure explicitly (§3.3, cross-ref §8): name the fork — *derive from the dynamics* (→ basin geometry 50/50, flat in \|α\|², carries no amplitude info) vs *import \|α\|² as a quantum-equilibrium measure* (Bohm status) — and land on the second horn. The lock supplies registration + equivariance, **not** the weights; MCI is Born-*compatible*, never Born-*derivative*. | dispute-001 (3-lab convergence, resolved-by-calc); Fable 5 #2; GPT-5.5 #2 | [`correction-003-born-horn2.diff`](correction-003-born-horn2.diff) · [`paper-04-after-correction-003-2026-06-25.md`](paper-04-after-correction-003-2026-06-25.md) |
| **004** | The **remaining review recommendations**, applied as one batch: **(a) §3.7** demote the chiral 0/π binary — the EM-selected **which-path/position basis** is the register, σx is internal-clock only; **(b) §6.2** name the **H′ gauge defect** (coupling to absolute φ_bulk breaks U(1)/shift symmetry) and its repair (couple to the gradient ∂_μθ), reframe H′ as a falsification term; **(c) §8** correct **"spontaneous"→explicit** low-energy Lorentz violation (genuine SSB needs an Einstein-aether/khronometric VEV, not done here); **(d) §8** the sub-quantum **H-theorem is unproven** here, so \|ψ\|² is adopted as a postulate; **(e) minors** — §2.5 spatial-gradient bridge, §7.5 gloss "unhidden variable" as *local macroscopic reference*. | Fable 5 #3; Gemini #1–#4 + minors; GPT-5.5 #2–#4 | [`correction-004-remaining-recommendations.diff`](correction-004-remaining-recommendations.diff) · [`paper-05-after-correction-004-2026-06-25.md`](paper-05-after-correction-004-2026-06-25.md) |
| **005** | **Fold the K_eff derivation into the manuscript** as a new **Appendix D** (cross-ref §3.6): a self-contained driven–dissipative (circuit-QED) derivation — adiabatic elimination → measurement dissipator (Γ_φ = 8χ²n̄/κ) → *exact* reduction to the Adler equation φ̇ = Ω − K_eff sin2φ with **K_eff = 4χ²n̄/κ**; the cut as the readout-power threshold n̄_crit = κ\|Ω\|/(4χ²); SNIC critical exponent ½. §3.6 is upgraded from "an identification, not a derivation" to "realized concretely in Appendix D." | GPT-5.5 #1 ("Adler asserted, not derived") | [`correction-005-fold-keff-derivation.diff`](correction-005-fold-keff-derivation.diff) · [`paper-06-after-correction-005-2026-06-25.md`](paper-06-after-correction-005-2026-06-25.md) |

## Honest scope (important for the demonstration)

**Corrections 001–003 are applied so far**, across two issues:

- **001–002 — the unpublished-companion citation [26]** (citation integrity): now fully addressed in-text — **every [26] citation is a forward-pointer** to separate work, none load-bearing. The one residual is *outside* the manuscript: the reference still has no citable locator (the AB paper is not on arXiv/Zenodo); fixing that is "option 3" (post it and cite a DOI), the author's call.
- **003 — the Born measure** (dispute-001): the manuscript now states **"Horn 2" explicitly** — the synchronization dynamics do *not* derive Born (basin geometry is 50/50, flat in |α|²); |α|² is imported as a quantum-equilibrium measure (Bohm status); the lock supplies registration + equivariance, *not* the weights. Born-compatible, not Born-derivative. This sharpens, and names, concessions the manuscript already made diffusely across §3.3/§7.3/§8.

With corrections 001–005, **every concrete reviewer recommendation is applied** — including GPT-5.5 #1 ("the Adler equation is asserted, not derived"), now discharged by folding the derivation into the manuscript as **Appendix D** (correction 005). What remains is not text-level review fixes but two author/strategic decisions:

- **[26] locator** — post the AB companion to arXiv/Zenodo and cite a DOI ("option 3"); an author action, not an edit.
- **Repositioning** — leading the paper with the two survivors (cut-as-locking-threshold; single-world-as-occupied-basin) is a structural choice, not a reviewer fix; left to the author.

So this folder demonstrates **five review→correction cycles covering every concrete reviewer recommendation**, plus two remaining author-judgment items. Each further correction should be added here as `correction-00N-*.diff` with its own row above, so the loop stays legible.

## Reproduce / inspect

```
# each correction as a patch:
cat correction-001-companion-citation.diff      # §7.3 / §7.4 / §8 de-load-bearing
cat correction-002-companion-citation.diff      # §3.7 + §7.3 remaining cites
cat correction-003-born-horn2.diff              # §3.3 + §8 Born = Horn 2 (imported, not derived)
cat correction-004-remaining-recommendations.diff   # §2.5/§3.7/§6.2/§7.5/§8 batch
cat correction-005-fold-keff-derivation.diff         # §3.6 + new Appendix D (K_eff = 4χ²n̄/κ)
# the snapshot chain (as-reviewed -> after 001 -> ... -> 005):
diff paper-01-as-reviewed-2026-06-25.md         paper-02-after-correction-001-2026-06-25.md
diff paper-02-after-correction-001-2026-06-25.md paper-03-after-correction-002-2026-06-25.md
diff paper-03-after-correction-002-2026-06-25.md paper-04-after-correction-003-2026-06-25.md
diff paper-04-after-correction-003-2026-06-25.md paper-05-after-correction-004-2026-06-25.md
diff paper-05-after-correction-004-2026-06-25.md paper-06-after-correction-005-2026-06-25.md
```

*Snapshots captured 2026-06-25 by Claude Opus 4.8. The live, evolving manuscript remains `PAPER_REVISED.md` in the source repository; these are frozen copies for the journal record. Nothing here was committed or pushed without the author's instruction.*
