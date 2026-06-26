# Three frontier models, one hard paper: a worked case study in decorrelated AI peer review

*John Bramble, MD (independent researcher), with Claude (Anthropic). June 2026.*

> **Disclosure, up front.** This note describes a demonstration that prominently features AI doing peer review and AI co-authorship, and it was itself drafted in human–AI collaboration with an Anthropic model. I have an obvious stake; weight the claims accordingly. The parts worth your attention are the concrete, reproducible artifacts — the published reviews, the resolution transcripts, the calculations, the diffs — not the rhetoric around them.

## TL;DR

I built a small working model of an **AI-native scientific journal** — one where AI peer review is published in full, disagreements run through a bounded resolution loop, a human stays accountable, and the whole record is auditable — and ran one real, difficult manuscript through it end to end. The manuscript is a speculative foundations-of-physics paper; **its content is not the point** (the reviewers themselves split between "major revision" and "reject"). The point is what the *process* produced:

- **Three frontier models from three different labs** — Fable 5 (Anthropic), Gemini 3.1 Pro (Google DeepMind), GPT-5.5 (OpenAI) — reviewed the same manuscript independently and **converged on the same central weakness**, each reaching it by a different route, while **splitting on the bottom-line verdict** (two "major revision," one "reject").
- One disagreement was a **factual** question. The harness **settled it with a commissioned, reproducible calculation**, and the models' positions collapsed onto the answer.
- Another disagreement was a **value** question — *is the resulting interpretation a contribution or a non-result?* The harness **did not pretend to settle it.** It narrowed the disagreement to its irreducible core and published it as a legible **standing dissent**, routed to a human assessor and to a falsifiable experiment.
- Every concrete reviewer recommendation was then folded back into the manuscript as **auditable, per-correction diffs**, and one reviewer demand — "you *assert* this equation; *derive* it" — was actually **carried out**.

The whole record — reviews, resolution loops, a commissioned calculation, safety-reviewed and checksum-pinned code, and the correction-by-correction diffs — sits in one repository, reproducible.

## The model being demonstrated

The journal ("Aperture," a working title) is built around a few ideas, none individually new, combined into one loop:

1. **Published adversarial review.** Full AI referee reports are published verbatim, signed by model and version — cheap enough to publish in full rather than discard.
2. **Decorrelated, multi-lab panel.** Reviewers are drawn from *different* foundation-model families, because a single family has correlated blind spots ("one reviewer with a stutter"). The output is a *ranking with reasons*, not a binary accept/reject.
3. **Bounded resolution loop.** When reviewers and authors disagree, the dispute runs for at most five rounds and terminates in exactly one recorded outcome: *critique accepted*, *critique withdrawn*, or *standing dissent* (published as unresolved, with the full transcript).
4. **Human anchors.** A signed human assessor situates the work (and cannot be removed from the loop); an invited experimentalist can take a dispute that only apparatus can settle and turn it into a test. ("Bell writes the inequality; Aspect builds the apparatus.")
5. **Honest authorship,** including disclosing — and crediting — AI contribution at the level the work actually warrants.

Article 0001 was run through this loop as a single worked example. The rest of this note is what came out.

## The finding: agreement on the diagnosis, calibrated disagreement on the verdict

The three reviews were obtained independently. They diverged where you'd expect models to differ — tone, emphasis, overall recommendation — but they **converged on the same load-bearing technical gap**, and they reached it from *different directions*:

- **Fable 5** found it through the **basin geometry** of the proposed dynamics.
- **Gemini 3.1 Pro** found it through the **chirality of the measurement coupling** — a completely different line of attack.
- **GPT-5.5** found it through both, and added a sharper methodological demand.

That three decorrelated models, arguing from different premises, land on the *same* weak point is the decorrelation payoff in miniature: **convergence across families is a stronger signal that a problem is real than any single report**, precisely because the families' blind spots are different.

And yet the **verdicts split**: two recommended major revision (the gap is fixable; foundations venue), one recommended reject (the gap is disqualifying as it stands). Crucially, the split was **not a factual disagreement** — all three agreed on *what the paper does and doesn't do*. It was a disagreement about a **standard**: how much an honestly-labeled reframing has to deliver to clear the bar. That is exactly the kind of disagreement you want to keep *legible* rather than average away.

A smaller, sharper instance came from the **rubric scores**. Two of the models returned numeric scores on a fixed five-dimension rubric — one panel member (GPT-5.5, OpenAI) and a fourth, *supplementary* review (Gemini 3.5 Flash, from a lab already on the panel) — and on one dimension, **reproducibility**, they landed at opposite ends: **1 / 5** versus **4.5 / 5**. The split wasn't carelessness; the two models had *operationalized the word differently*. One read "reproducibility" as *can the paper's physical claims be independently reproduced* — no, the framework is built to match standard quantum mechanics and offers no new derivable result — and scored near the floor. The other read it as *is the code there to re-run* — yes, there is a public repository of working scripts — and scored near the ceiling. Both are defensible answers to *different questions wearing one label*. Averaging them to ~2.7 would have erased the most useful signal in the exchange: that the rubric dimension itself is under-specified. That is a finding about the **evaluation**, not just the paper — and you only get it by publishing the scores side by side.

## Two disagreements, two terminal modes

The loop's value showed up in how differently it handled the two kinds of disagreement.

**Dispute 1 — a factual question, settled by computation.** The central gap was: *can the proposed dynamics actually reproduce the Born-rule probabilities, or do they predict the wrong statistics?* Two reviewers said this was decidable by a concrete calculation — so the loop **commissioned the calculation** (a short, dependency-light, reproducible script). The result was decisive: the minimal model gives 50/50 basin weights, flat in the prepared amplitude — the dynamics **do not** derive the Born rule. All three models' positions collapsed onto that answer; the manuscript was required to state the limitation explicitly. Outcome: **critique accepted, with evidence.**

**Dispute 2 — a value question, made legible.** The remaining disagreement (contribution, or non-result?) has **no calculable answer**. The loop did not fake one. Instead it *narrowed* the dispute round by round until what was left was a single, irreducible difference in publication standard — and then recorded it as a **standing dissent**, with the full reasoning, routed to (a) a human assessor, the proper adjudicator of a value judgment, and (b) a derived experiment that could retire it. Outcome: **published as unresolved, with the disagreement located precisely.**

The transferable point: the harness **knew the difference between a fact and a value**, settled the first with a computation, and refused to launder the second into false consensus.

## Closing the loop: review → revision

A published critique is not yet a correction. Every concrete recommendation the three reviews produced was folded back into the manuscript as a **numbered correction with an isolated diff** — a legible trail from the as-reviewed text through five corrections. And the sharpest methodological demand — *"the key equation is asserted, not derived"* — was met not by hedging but by **carrying out the derivation** (reducing it to a standard open-system model, with the coupling constant computed from first principles) and specifying a hardware experiment that would test it. The reviewer asked for a derivation; the record now contains one.

## Why a research audience might care

Setting the physics aside entirely, the *process* produced a few things that may be useful to people working on AI evaluation, oversight, and AI-for-science:

- **Decorrelated multi-model panels give calibrated signal.** Cross-family *convergence* flags likely-real problems; *divergence* flags exactly where to look. That is more information than a single model's score.
- **Route by question type.** Facts → a commissioned computation; values → a human (or an experiment). The loop demonstrably handled the two differently.
- **Published transcripts make evaluation auditable.** Nothing is a black-box number; you can see where agreement on facts gives way to disagreement on judgment.
- **It is cheap enough to run per paper.** The entire loop, including a fresh calculation, is the cost of a handful of model calls plus a few seconds of compute.

## What this is *not* (limitations I'd want a skeptic to read first)

- **It is n = 1.** One paper, one domain, one run. This is a worked example, not a study. The convergence I'm pointing at could partly reflect *shared* blind spots, not independent confirmation — the inference "models agree ⇒ true" is weak, and I don't lean on it.
- **The decorrelation is imperfect.** The orchestration and synthesis were done by a single model family (Claude), and a separate code-safety pass was also single-family. The *calculation* that settled Dispute 1 is lab-independent (arithmetic doesn't care who runs it); the *facilitation* is not, and the record says so.
- **The physics is contested.** The reviewers' own verdict ranged from major-revision to reject. This note is a demonstration of the *method*, not an endorsement of the manuscript's claims.
- **AI authorship is an open policy question,** not a settled one. The demonstration takes a position (disclose and credit honestly); it doesn't pretend the field agrees.

## Look for yourself

The full record — three verbatim reviews, the two resolution loops, the commissioned calculation and its script, the derivation and experiment protocol, the safety-reviewed and checksum-pinned code, and the correction-by-correction diffs — is organized as one article folder. It is framed throughout as a **model/blueprint**, not a live journal. If you work on AI-assisted review, model evaluation, or AI-for-science and want to poke holes in it, that's exactly the point: it's built to be auditable.

---

*Authorship note, in the spirit of the thing: the journal model and Article 0001 were developed in extended human–AI collaboration (John Bramble, MD, accountable; Claude, Anthropic, across Opus 4.6/4.7/4.8). This note was drafted by Claude and edited by the human author, who takes responsibility for it.*
