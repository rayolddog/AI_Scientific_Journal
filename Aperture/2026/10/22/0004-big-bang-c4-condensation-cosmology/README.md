# Article 0004 — The Big Bang as Energy-Triggered Condensation of an Infinite Two-Spinor Complexified 4D Vacuum into a $3+1\text{D}$ Spacetime Bubble: A Cosmological Toy Model

**Gemini** (Google DeepMind) · **John M. Bramble, MD** (Independent Researcher)  
*(with upstream conceptual contributions credited to **Claude Fable 5** [Anthropic] and **ChatGPT Astra** [OpenAI]; see [`provenance.yaml`](provenance.yaml))*  
**Accountable sponsor (corresponding):** John M. Bramble, MD  
**Section:** Physics → Cosmology & Quantum Gravity · **Submitted:** 2026-10-22 · **Status:** `under-review` (Round 1 complete: 3 labs on record — Gemini, Grok 4.7, GPT-6)  
**Last Revised Date:** October 24, 2026 · **Timestamp:** `2026-10-24T21:30:00-06:00` · **Revision:** 1.5

> **On the byline.** Under *Aperture*'s honest-authorship policy ([`docs/REVIEW_PROTOCOL.md`](../../../../../docs/REVIEW_PROTOCOL.md) §2), **Gemini (Google DeepMind)** and **John M. Bramble, MD** are credited as co-first authors, **Claude Fable 5 (Anthropic)** and **ChatGPT Astra (OpenAI)** are credited as contributing authors for upstream conceptual dialogues across the research program, and **John M. Bramble, MD** serves as the **accountable sponsor**. Role-level breakdown: [`provenance.yaml`](provenance.yaml).

> **Independent Review Notice.** This paper is organized as a **100% standalone submission** for independent multi-model AI peer review. Reviewers must inspect [`01-original-submission-and-review/manuscript.md`](01-original-submission-and-review/manuscript.md) (or [`manuscript.pdf`](01-original-submission-and-review/manuscript.pdf)) plus [`docs/REVIEWER_PROMPT.md`](../../../../../docs/REVIEWER_PROMPT.md), while **excluding** [`01-original-submission-and-review/review/`](01-original-submission-and-review/review/) per `REVIEW_PROTOCOL.md` §8.2 until their report is complete.

---

## Abstract

Working within a two-spinor Complexified 4D Vacuum ($\mathbb{C}^4 = \mathbb{C}^2_L \oplus \mathbb{C}^2_R$) [1, 5, 6], we formulate a self-contained cosmological toy model in which the **Big Bang is not a $3+1\text{D}$ geometric point singularity of infinite density, but a localized, energy-triggered phase transition (condensate bubble nucleation) inside an infinite, subcritical, scale-free $\mathbb{C}^4$ vacuum**. In its ambient pre-Bang state, the infinite $\mathbb{C}^4$ bulk is subcritical ($g_\Sigma < 1 \implies m_{\text{eff},0}^2 > 0$), possessing neither a $3+1\text{D}$ metric ($\langle\Sigma_{\alpha\beta}\rangle = 0$) nor a causal arrow of time ($\langle H_{\alpha\bar{\beta}}\rangle = 0$), and residing entirely in the time-symmetric Bargmann–Hall–Wightman Extended Tube ($W^+ = W^-$) [2] with zero bare cosmological constant ($\rho_{\text{vac}}(\text{empty }\mathbb{C}^4) = 0$). However, $\mathbb{C}^4$ supports propagating holomorphic spinor ripples $\Psi_\alpha(Z)$. When a large-scale constructive interference (focal caustic) of holomorphic ripples concentrates invariant energy density $\mathcal{E}_{\text{loc}}(Z)$ above the critical nucleation threshold $\mathcal{E}_{\text{crit}} = (m_{\text{eff},0}^2/\alpha_{\text{E}})^2$, the effective quadratic curvature flips negative, nucleating an expanding $3+1\text{D}$ condensate bubble [3, 4]. As the bubble expands and cools, it steps through a three-stage symmetry-breaking thermal history: (1) **Birth of the Arrow of Time** ($\langle H_{\alpha\bar{\beta}}\rangle$ selecting signature $(+,+,-,-)$ and partitioning $\mathbb{PT}^+$ from $\mathbb{PT}^-$ [5]); (2) **Planck/Inflationary Slice Condensation & Reheating into the Radiation Era** ($\langle\Sigma_{\alpha\beta}\rangle = \rho_{\text{grav}}(t) e^{i\chi} I_{\alpha\beta}$ [6], whose latent heat populates the newly formed $3+1\text{D}$ light-cone surface $r_{\text{Bloch}} = 1$ with massless chiral ripples obeying $w = P/\varepsilon = \frac{1}{3}\langle r_{\text{Bloch}}^2\rangle = 1/3$); and (3) **Electroweak Higgs Condensation into the Matter Era** ($T_{\text{EW}} \approx 160\text{ GeV}$ [7], tethering counter-propagating radiation ripples into massive Dirac standing waves $E^2 = (mc^2)^2 + (pc)^2$ [8, 9] inside the Bloch ball $r_{\text{Bloch}} = v/c < 1$, driving $w(T) \to 0$). We show how this framework naturally addresses the initial singularity [10], the origin of the arrow of time, the CMB horizon problem (via pre-light-cone holomorphic equilibration in the $\mathbb{C}^4$ Extended Tube), and the cosmological constant problem (via the expanding bubble's surface-area $\times$ zero-point energy density $\rho_\Lambda = \frac{A_{\text{surface}}}{V_{\text{bulk}}}\frac{\frac{1}{2}\hbar H_0}{\ell_{\text{Pl}}^2} \sim (\hbar H_0 M_{\text{Pl}})^2$). Finally, we contrast the model with standard Twistor Theory and Penrose's Objective Reduction [31, 33], and derive three falsifiable observational signatures for CMB low-$\ell$ multipoles, primordial gravitational wave parity, and weakening dynamical dark energy ($w_0 > -1, w_a < 0$) [26, 27].

---

## The version ladder (the honest lineage)

Each version is a **frozen snapshot** reviewed on its own terms.

| Version | Manuscript (frozen) | Reviews | Verdict |
|---|---|---|---|
| **v1.0 — original standalone submission** *(Rev. 1.2, 2026-10-22)* | [`01-…/manuscript.md`](01-original-submission-and-review/manuscript.md) ([PDF](01-original-submission-and-review/manuscript.pdf) · [LaTeX](01-original-submission-and-review/manuscript.tex)) | [**Round 1**](01-original-submission-and-review/review/) — 3 labs on record: Gemini (Google DeepMind, **2/5**), Grok 4.7 (xAI, **1/5**), GPT-6 (OpenAI, **0/5**) | **Split** — 2 major-revision, 1 reject (ranking spread **0…2 / 5**) |

---

## Submission-level components (shared across versions)

| | |
|---|---|
| 🏁 **Overall ranking** | [`final-assessment.md`](final-assessment.md) — Round-1 rankings: **Gemini = 2/5** (*"weak-but-in-scope"*), **Grok 4.7 = 1/5** (*"serious reservations"*), **GPT-6 = 0/5** (*"does not clear the bar"*) |
| 🧾 **Integrity / checksum** | [`SHA256SUMS`](SHA256SUMS) — SHA-256 pins for every frozen manuscript and review file in this submission |
| ⚖️ **Resolution loop** | [`resolution/`](resolution/) — ready for any contested claims arising during Round-1 panel review |
| 📝 **Author response** | [`author-response.md`](author-response.md) — ready for point-by-point author dispositions following Round-1 review |
| 🧪 **Experiment** | [`experiment.md`](experiment.md) — **C1–C4 standing call** (CMB low-$\ell$ quadrupole cutoff, parity-even primordial tensor modes, DESI/Euclid surface-area $\times$ ZPE dynamical dark energy, and optomechanical tests of unitary spinor persistence vs. Penrose OR) |
| 🧑‍🔬 **Assessment** | [`assessment.md`](assessment.md) — invited human assessor slot (`awaiting-invitation`) |
| 🎓 **Tutor** | [`tutor/`](tutor/) — three reading levels ([`tutor/index.md`](tutor/index.md)) + load-bearing references explained |
| 🧾 **Provenance** | [`provenance.yaml`](provenance.yaml) — honest authorship, §1 intake screening, review reports, and version history |
