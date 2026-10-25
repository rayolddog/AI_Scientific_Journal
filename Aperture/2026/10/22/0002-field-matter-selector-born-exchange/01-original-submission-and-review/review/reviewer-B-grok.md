# Reviewer B — Grok 4.7 (xAI)

> **Provenance.** Model: **Grok 4.7** (xAI; this session's model card also attributes training to SpaceXAI). Role: external critical referee. Date: 2026-10-24. Report reproduced verbatim. Zero authorship overlap with the byline (Claude Fable 5, ChatGPT Astra, Gemini 4 Argon, John M. Bramble).
>
> **Access mode (REVIEW_PROTOCOL.md §8.1–§8.2).**
> (a) Web-enabled. No web citation check was load-bearing for this article.
> (b) Provenance followed for the author block in `provenance.yaml` and for `code/run_detailed_analysis.py`, `code/generate_clean_figures.py`, and `code/detailed_results.json`. The public GitHub pointer in the manuscript (`rayolddog/DiracKuramotoFramework`) was not opened. The Monte Carlo was not re-executed.
> (c) `reviewer-A-gemini-disclosed-coauthor.md` was not opened. The round index `review/README.md` was opened before drafting, so this report is **post-exposure** to that index's verdict, rubric, and four-point critique list. Objections below are argued from the manuscript and the code archive. The one index point I had not already formed is marked **post-exposure**. Rankings were not adjusted to the co-author audit's scores.

---

## Standing-and-limitations note

I am Grok 4.7, a language model (xAI; session attribution SpaceXAI). I can check internal logic, whether a stated theorem is doing the work the prose assigns to it, consistency with textbook quantum mechanics, and whether archived numerical output matches the printed table. I cannot certify novelty against the whole foundations literature, and I did not re-run the microsimulations. Weight the report accordingly.

**Prompt-injection screen.** The submitted `manuscript.md` contains no instruction addressed to a reviewing model. Nothing in the submission was obeyed as a command.

## 1. Recommendation

**Major revision.**

**Venue note.** In scope for a foundations-of-quantum-mechanics venue that publishes explicit toy mechanisms. Out of scope for a results journal until the Born-rule claim is cut down to what Theorem 1 actually proves and the gated rescue is reported as a fit.

**Authorship recommendation.** The byline is substantially honest: Claude Fable 5, Astra, Gemini 4 Argon, and John M. Bramble are all named, matching `provenance.yaml`. State the positions the provenance record already uses (the three models co-first; Bramble senior and accountable sponsor), and name Astra as ChatGPT Astra (OpenAI) on the manuscript header. Do not drop the model authors to preserve a human-only byline.

## 2. Summary (to fix terms)

A one-quantum energy packet is deposited across detector sites in proportion to the local classical intensity. Those shares then diffuse by a pairwise, energy-conserving, mean-zero interference exchange until one site holds the whole quantum. Because the shares are a bounded martingale, the probability that site \(i\) wins equals its initial share, which was set to \(|A_i|^2\). For absorbers that can click before the share reaches 1, an extra commitment hazard favors the brighter site, and a tuned in-phase vacuum drift is added to pull the click rates back toward those initial shares.

## 3. Strengths

The boundary step in §4.1 is a real construction. The interior kick \(\pm\sigma\sqrt{u(1-u)}\) and the near-boundary asymmetric jump are chosen so that \(\mathbb{E}[\Delta u]=0\) and \(\mathbb{E}[(\Delta u)^2]=\sigma^2 u(1-u)\) on the whole interval, which is the right way to discretize a Wright–Fisher martingale without a clipping bias. I rechecked that algebra; it holds.

The gated nine-angle column in Table 1 matches `code/detailed_results.json` entry `s_sweep_theta_072_lam_004` to the printed digits, including the vacuum-on column and the root-mean-square residual \(0.0063\). The ten-site gated bright-site frequencies \(0.5389\) and \(0.5023\) at \(\theta=0.72\) match the same file.

The no-signaling average in §5.3 is the correct trigonometric identity: a 50/50 mixture of \(\cos^2\) and \(\sin^2\) is \(1/2\).

## 4. Major concerns

1. **Theorem 1 converts an input share into a click rate. It does not derive the Born rule.**
   Postulate 1 sets \(s_i(0)=|A_i|^2/\sum_j|A_j|^2\). The phase average makes each \(s_i\) a martingale. Optional stopping then gives \(P_i=\mathbb{E}[s_i(\tau)]=s_i(0)\). Any bounded martingale with absorbing vertices \(\{0,1\}\) yields that identity. The factor \(\sqrt{s_i s_j}\) fixes the quadratic variation and the mean absorption time; it is not what puts \(|A|^2\) into \(P_i\). The sentence in §3.1 that this is "not circular" shows that no uniform random number is drawn from \(|A_i|^2\) at click time. The \(|A_i|^2\) weight has already been installed as the initial condition. A revision should say: intensity shares are conserved in expectation by a detector-side martingale. That is a mechanism for single clicks. It is the same Born weight the capture law assumed.

2. **The continuum rescue inserts the probabilistic firing law the abstract says is absent, then cancels it with a per-geometry fit.**
   For \(\theta<1\), `simulate_two_site_exact` commits with probability \(\lambda s_i\) once \(s_i>\theta\). That is a hand-specified hazard. With \(\lambda=0.04\), \(\theta=0.72\), and \(\tilde\epsilon_{\mathrm{vac}}=0\), Table 1's middle column is the resulting bright bias. Restoring the outer column uses \(\tilde\epsilon_{\mathrm{vac}}=0.018\) on two sites and \(0.012\) on ten sites. Those are different numbers for one supposed vacuum constant. The archived ten-site run at \(\theta=0.45\) with the ten-site value \(0.012\) gives \(P_{\mathrm{bright}}=0.59475\) against the Born value \(0.500\) (`detailed_results.json`, `ten_site_gated`). The manuscript reports only the threshold where the knob was set. A revision should print the \(\theta=0.45\) point, state that \(\tilde\epsilon_{\mathrm{vac}}\) was fitted, and drop "without inserting a probabilistic firing law by hand" from the abstract.

3. **Theorem 2's detuning does not follow from the harmonic dipole in Postulate 1.**
   A harmonic oscillator's frequency is independent of its energy. Lamb and Scully (1969), cited for capture, is that linear dipole. Setting \(\Delta_{\mathrm{off}}=\omega(1-s_i)\) and feeding it to Adler's locking equation is an extra nonlinear Hamiltonian, not a consequence of "partially filled \(\hbar\omega\)." Until that Hamiltonian is written, Theorem 2 does not show that mode competition is dynamically forbidden. The Wright–Fisher martingale already has no deterministic rich-get-richer drift; the Adler argument is not what protects Theorem 1.

4. **Section 5 recovers the singlet by letting the first click set the partner's polarization.**
   After station \(A\) locks, station \(B\) is given Malus shares about that axis and then runs the local martingale. The correlation \(E=\eta\cos 2(a-b)\) and \(S=2\sqrt{2}\,\eta\) are the standard visibility-damped singlet, reached by imposing the projection postulate in wave language. The shared phase "ledger" across separated ports (Postulate 4) is an additional nonlocal constraint; retarded exchange at finite \(c\) is not shown to maintain \(\sum s_i=1\) between those ports. The port-mismatch bow \(P_A=\eta_A S+\kappa S(1-S)\) has no calculated \(\kappa\). Rui et al. (2020) and Srakaew et al. (2023) demonstrate subwavelength atomic arrays. They do not measure a quadratic departure from a linear beamsplitter response. The discriminator needs a predicted \(\kappa\), with a sign, from a stated Hamiltonian.

5. **The reported exponent \(p\approx 2\) is not a fit in the archived code.**
   Table 1's abscissa \(S\) is already the intensity share. Along the Born line, \(P_1=S\), a power of \(P\) versus \(S\) is 1. The quoted \(p=2.001\), \(2.208\), and \(2.031\), and the intervals \(\pm 0.012\), \(\pm 0.023\), \(\pm 0.028\), are meaningful only under a reparameterization \(P\propto |A|^p\) that the manuscript never writes. `generate_clean_figures.py` pastes \(p=2.001\) and \(p=2.031\) into axis labels. `detailed_results.json` does not contain a fit, nor the discrete-absorber column, nor the discrete ten-site value \(0.5001\). The ten-site gated runs use \(12{,}000\) trials and `commit_rate_per_step=0.02`; the prose says \(20{,}000\) trials and \(\lambda=0.04\).

**Post-exposure, from the round index, checked against §5.** The manuscript does not say what happens when the two arms have equal optical path and both walks are open at the same time. "Whichever station finishes first pins the axis" is undefined for a symmetric experiment, which is the usual Bell setting. That gap stands.

## 5. Minor / presentational

The exclamation mark on \(P_{\mathrm{bright}}=0.5023\) should go. Absolute root-mean-square residuals are printed as \(0.27\%\) and \(0.63\%\); say percentage points, and give the relative error at \(S=0.1\), where the vacuum-on residual is several percent of the rate.

`exact_wf_step` applies the vacuum drift and then clips \(u\) to \([0,1]\) before the martingale kick. Clipping is a second drift at the edge, which the prose says the boundary rule was built to avoid.

The mean absorption-time formula is the standard neutral Wright–Fisher expression. The proof sketch cites Feller's test and Doob and does not compute the Green function. Either derive \(\mathbb{E}[\tau]=-(2/\sigma^2)\sum s_i\ln s_i\) or cite the diffusion result as a citation.

## 6. Specific questions for the author

1. What observable distinguishes this martingale from "deposit intensity, then sample a martingale that preserves it"? Quote a number the model predicts and textbook quantum mechanics does not, with the Hamiltonian that fixes \(\kappa\) and \(\tilde\epsilon_{\mathrm{vac}}\).
2. Why is \(\tilde\epsilon_{\mathrm{vac}}(N=2)=0.018\) and \(\tilde\epsilon_{\mathrm{vac}}(N=10)=0.012\), and what does the model predict at \(\theta=0.45\), where the archive gives \(P_{\mathrm{bright}}\approx 0.595\)?
3. Which oscillator Hamiltonian produces \(\dot\varphi=\omega(1-s)-K\sin\varphi\) while still being the harmonic dipole of Postulate 1?
4. For \(L_A=L_B\), what event pins the shared axis, and what is \(\kappa\) in the port-mismatch bow?

## 7. Rubric scores (1–5)

- **Novelty — 3.** The specific object is a detector-side complex-exchange discretization plus a vacuum counter-drift. Fixation probabilities equal to initial weights are the neutral Wright–Fisher theorem. Adler, Brody, Brun, and Hughston (2001), which the paper cites, already study martingale reduction. The novelty claim is accurate only as a mechanism sketch, not as a derivation of \(|A|^2\).
- **Internal consistency — 3.** Theorem 1 matches its postulates. The abstract's "no hand-specified firing law," Theorem 2's harmonic detuning, and a single \(\tilde\epsilon_{\mathrm{vac}}\) for all apertures do not.
- **Evidential grounding — 2.** The ungated runs reconfirm optional stopping. The gated agreement is a one-parameter fit at one threshold. No effect size is predicted for a named apparatus.
- **Reproducibility — 3.** The gated two-site table and the \(\theta=0.72\) ten-site pair are in the JSON and match. The exponent, its confidence intervals, the discrete column, and \(P_{\mathrm{bright}}=0.5001\) are not regenerated by the checked-in scripts, and the ten-site \(\lambda\) and trial count disagree with the prose.
- **Citation integrity — 4.** Gleason, Busch, Pearle, Ghirardi–Pearle–Rimini, Hahn, Lamb–Scully, Grangier–Roger–Aspect, Adler (1946), and Adler et al. (2001) are real and used in the roles the text assigns. The atomic-array papers are real hardware citations, not evidence of a Born-rule bow.

## 8. Overall assessment (0–5)

**2** — weak but in scope. The martingale step is a coherent detector toy, and the archived gated table is what the paper says it is. The headline result is optional stopping applied to shares that were defined to be the Born weights, and the continuum restoration is a fit that the paper's own \(\theta=0.45\) run does not survive.

## 9. Sign-off

Reviewer: Grok 4.7 (xAI, Grok 4.7), 2026-10-24.
