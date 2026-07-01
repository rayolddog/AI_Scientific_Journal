# Aperture — the journal

*The **instance**. This folder is Aperture set up as an AI-native journal would set up every article. For the **blueprint** — what the journal is, why it is built this way, and how to read it — see the [repository front page](../README.md).*

Articles are filed archive-style by date, `Aperture/<year>/<month>/<day>/<id>-<slug>/`, so the layout reads like a live archive rather than a flat folder. (One article today; the structure is built for the throughput an AI-native pipeline is expected to produce, not for what is here now.)

---

## Submissions

| # | Title | Section | Versions | Standing verdict | Ranking |
|---|---|---|---|---|---|
| [**0001**](2026/06/30/0001-dirac-kuramoto-many-clocks/) | Two Regimes of the Chiral Mass Coupling — *Quantum Measurement as Bath-Induced Synchronization* | Physics → Foundations of QM | 3 (v1 → v2 → **v3**) | **Unanimous major-revision** (round 2) | **3 / 5** *"sound"* — split (see note) |

**Ranking note (0001).** The headline **3/5** is the modal read, **not an average**. Round-2 decorrelated overall rankings on the revised manuscript were **Gemini 3.1 Pro = 3** ("sound") and **GPT-5.5 Thinking = 1** ("serious reservations"); a same-family Claude Opus 4.8 re-score also landed at 3. GPT-5.5's **1 is carried as a standing dissent**, not averaged in — the spread (1…3) *is* the signal: the verdict converged to unanimous major-revision while the quality ranking stayed split, locating the residual disagreement on significance / publish-bar ([dispute-002](2026/06/30/0001-dirac-kuramoto-many-clocks/resolution/dispute-002-significance.md)), not on the facts. A fresh fully-decorrelated re-score of the current revision is **owed**. *(These fields are eventually generatable from each article's [`provenance.yaml`](2026/06/30/0001-dirac-kuramoto-many-clocks/provenance.yaml).)*

---

## How to read an article here

Open the article's own `README.md` for its index, then read the manuscript **together with the reviews that judged it** and follow it across its versions — that combined read is the point, and it is spelled out on the [repository front page](../README.md#read-the-record-not-just-the-paper). Every article carries, alongside the paper: the full published review panel (decorrelated across labs), the bounded resolution loop for disputes, the author's point-by-point response, runnable + checksum-pinned code, a recursive tutor, and an honest `provenance.yaml`.

## Scope

Phase-1 sections are **Physics** and **Chemistry**; the exclusions (human-subjects, dangerous-capability, value-adjudicated domains) and the reasoning are on the [front page](../README.md#sections) and in the [manifesto](../docs/MANIFESTO.md). This repository is a **demonstration**, not an operating journal: it accepts, solicits, and submits nothing.
