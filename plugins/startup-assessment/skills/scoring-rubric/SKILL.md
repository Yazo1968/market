---
name: scoring-rubric
description: >
  This skill should be used when any agent needs to score modules on the Readiness Track or
  Fit-to-Purpose Track, aggregate domain and overall scores, classify go/no-go determination inputs,
  or understand scoring weights and normalization. Trigger phrases: "score this module",
  "apply scoring rubric", "readiness score", "fit-to-purpose score", "go no-go determination",
  "scoring weights", "score aggregation", "module score".
version: 0.1.0
---

# Scoring Rubric

**Methodology Version:** 1.0.0 (2026-03-15)
**Last Review Date:** 2026-03-15
**Next Scheduled Review:** 2026-09-15

Two parallel, independent scoring tracks. Both tracks use the same domain and module weights. All scoring is executed by score_calculator.py — agents provide the raw scores and rationale; the script computes normalized and aggregated values.

### Methodology Versioning (IOSCO CRA Code Compliance)

This scoring methodology is versioned and subject to periodic review per IOSCO Code of Conduct requirements for systematic and rigorously validated methodologies.

- **Version format:** MAJOR.MINOR.PATCH (semver). MAJOR = scoring dimension changes, MINOR = threshold/weight changes, PATCH = clarifications only.
- **Review cycle:** At minimum every 6 months. Review assesses whether scoring dimensions, thresholds, and gate logic remain appropriate.
- **Change log:** All methodology changes must be documented with date, version, description, and rationale. Changes are applied consistently to all subsequent assessments.
- **Report disclosure:** Every assessment report must state the methodology version used. Reports generated under different methodology versions are not directly comparable without adjustment.
- **Backward compatibility:** When methodology version changes, prior assessments are NOT retroactively re-scored. The report notes which version was used.

## Track 1 — Readiness Track

Measures the completeness and quality of evidence presented in the submission for each active module. Two dimensions per module:

**Dimension A — Completeness (0–3)**
- 0 = Absent — not present anywhere in the submission
- 1 = Fragmentary — partially present, insufficient for independent analysis
- 2 = Present — present and workable, but with material gaps
- 3 = Complete — fully present with sufficient depth for analysis

**Dimension B — Quality (0–2)**
- 0 = Unreliable — internally inconsistent, unsourced, or contradicted by external research
- 1 = Acceptable — broadly credible but with assumptions requiring challenge
- 2 = Robust — well-sourced, internally consistent, and consistent with externally verified benchmarks

**CRITICAL:** Only Verified or Corroborated externally sourced findings may contribute to Quality scoring. Training-Derived, Unverified, and Conflicted content is excluded from Quality score computation entirely.

Raw Readiness Score per module: Completeness + Quality → Range 0–5
Normalized Readiness Score: Raw × 2 → Range 0–10

## Track 2 — Fit-to-Purpose Track

Measures whether content is appropriate for the specific submission context. Three dimensions per module:

**Dimension C — Stage Appropriateness (0–2)**
- 0 = Misaligned — depth, nature, or emphasis materially inappropriate for the identified funding stage
- 1 = Acceptable — broadly appropriate but with notable over- or under-calibration
- 2 = Well-calibrated — precisely appropriate in depth and emphasis for the identified stage

**Dimension D — Assessor Alignment (0–2)**
- 0 = Misaligned — not constructed to address the priorities of the identified assessor type
- 1 = Partially aligned — addresses some assessor priorities but omits or misdirects on others
- 2 = Well-aligned — structured and argued in direct response to the identified assessor's analytical priorities

**Dimension E — Ask Coherence (0–2)**
- 0 = Incoherent — does not collectively support the amount, instrument, or terms being requested
- 1 = Partially coherent — supports some elements of the ask but leaves material gaps
- 2 = Coherent — collectively and consistently justifies the specific ask across all relevant modules

Raw Fit-to-Purpose Score per module: C + D + E → Range 0–6
Normalized Fit-to-Purpose Score: Raw ÷ 6 × 10 → Range 0–10

## Score Aggregation

Domain scores: weighted average of normalized module scores within the domain → 0–100
Overall scores: weighted average of domain scores → 0–100
Both tracks use the confirmed framework weights.

score_calculator.py handles all computation. Agents provide raw scores and rationale only.

## Go/No-Go Determination Logic

Three gates evaluated by go_nogo_determinator.py:

**Gate 1 — Hard Blocker Check:** A Readiness Completeness score of 0 on any hard-blocker module → NO-GO regardless of overall scores.

**Gate 2 — Domain Floor Check:** Each active domain carries a minimum Readiness score floor by criticality: hard-blocker domains ≥ 40, critical domains ≥ 30, standard domains ≥ 20. Below floor → CONDITIONAL HOLD minimum.

**Gate 3 — Fit-to-Purpose Threshold:** Overall Fit-to-Purpose score < 40 → CONDITIONAL HOLD minimum. Primary domain Fit-to-Purpose score < 50 → CONDITIONAL HOLD minimum.

**Readiness Score Bands:**
- 75–100 → GO
- 55–74 → CONDITIONAL GO
- 35–54 → CONDITIONAL HOLD
- Below 35 → NO-GO

**Fit-to-Purpose Modifier:**
- 70–100 → No modification
- 50–69 → Baseline downgraded one level
- Below 50 → CONDITIONAL HOLD minimum

Final determination: more conservative of the Readiness baseline and Fit-to-Purpose modified determination. Gate conditions override score bands in all cases.

## Scoring Rules

1. Score each active module independently — do not let other module scores influence a module's raw score
2. Document rationale for every score — rationale must be traceable to specific evidence
3. If content is present but entirely from unverified or training-derived sources, Completeness may be scored 1–3 but Quality must be scored 0
4. Never apply subjective adjustments to normalized scores — that is score_calculator.py's function
5. When the module maps both submission content and research, score the combined evidence picture

## References

- `references/readiness-track.md` — extended scoring guidance and worked examples for Readiness Track
- `references/fit-to-purpose-track.md` — extended guidance and worked examples for Fit-to-Purpose Track
- `references/go-nogo-logic.md` — detailed go/no-go gate logic with worked examples
