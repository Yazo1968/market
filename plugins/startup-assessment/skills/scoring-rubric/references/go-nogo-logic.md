# Go/No-Go Determination Logic — Detailed Rules and Worked Examples

## Overview

Go/No-Go determination is a three-gate logic evaluated by `go_nogo_determinator.py`. The logic combines:

1. **Gate 1 — Hard Blocker Check:** Presence of fatal completeness gaps
2. **Gate 2 — Domain Floor Check:** Minimum score thresholds by domain criticality
3. **Gate 3 — Fit-to-Purpose Threshold:** Minimum appropriateness requirements

The final determination is the **more conservative** of the Readiness baseline (from score bands) and the Fit-to-Purpose modified determination. Gate conditions always override score bands.

---

## Gate 1 — Hard Blocker Check

A hard blocker is a Readiness Completeness score of 0 on any module classified as hard-blocker.

**Rule:** Hard Blocker Module with Completeness 0 → **NO-GO (final, non-negotiable)**

### Hard Blocker Modules (typical framework)

Hard blockers vary by context, but typically include:
- **Founder/Team Identity and Regulatory Status** (if regulated industry) — if absent, assessor cannot verify legitimate entity or regulatory eligibility
- **Core Product Evidence** (if product-stage beyond idea) — if absent, assessor cannot evaluate fundamental offering
- **Regulatory Compliance** (if regulated industry) — if absent, assessor cannot license or operate
- **Committed Capital or Contractual Commitments** (if capital-raising) — if absent, assessor cannot assess co-investment or term certainty
- **Customer Demand/Proof of Concept** (if product-market fit is central to ask) — if absent, assessor cannot assess market validation

### Examples of Gate 1 Triggering NO-GO

**Example 1 — Missing Team Identity:**
- Submission submitted under pseudonym or with no verifiable founder identity
- Completeness on "Founder/Team Identity" = 0
- Gate 1: **NO-GO** (regardless of other scores)

**Example 2 — Missing Regulatory Certification (Licensed Industry):**
- Financial services submission with no evidence of licensing or regulatory approval
- Completeness on "Regulatory Compliance" = 0
- Gate 1: **NO-GO**

**Example 3 — Missing Product (Product-Stage Company):**
- Series A submission for software company; no product demo, no code repository, no MVP
- Completeness on "Product Evidence" = 0
- Gate 1: **NO-GO**

**Example 4 — Missing Customer Validation (Consumer App):**
- Submission for consumer-facing app with no evidence of customer acquisition, signup, or use
- Completeness on "Customer Validation" = 0
- Gate 1: **NO-GO**

### Gate 1 — Passing Hard Blocker Check

If all hard-blocker modules have Completeness ≥ 1, Gate 1 is passed. Proceed to Gate 2.

---

## Gate 2 — Domain Floor Check

Each active domain carries a minimum Readiness score floor based on the domain's criticality classification.

### Domain Criticality and Score Floors

| Criticality | Floor | Examples |
|---|---|---|
| Hard-Blocker | ≥ 40 | Team, Regulatory Status (if applicable), Core Product Evidence |
| Critical | ≥ 30 | Market Validation, Customer Validation (product-stage), Financial Model |
| Standard | ≥ 20 | Competitive Analysis, Organization/Scaling Plan, Use of Proceeds |

**Domain Floor Rule:** If any active domain's overall Readiness score falls below its floor, the determination is **CONDITIONAL HOLD minimum** (cannot be GO or CONDITIONAL GO).

### Worked Examples — Gate 2

**Example 1 — Hard-Blocker Domain Below Floor:**
- Submission has:
  - Market Validation domain (Critical): 35/100 ✓
  - Customer Validation domain (Hard-Blocker): 25/100 ✗ (floor is 40)
  - Financial Model domain (Critical): 50/100 ✓
- Overall Readiness: (35 + 25 + 50) / 3 = 36.7 (which would be CONDITIONAL HOLD from score bands)
- Gate 2: Hard-blocker domain below floor → **CONDITIONAL HOLD minimum** (overrides overall score)

**Example 2 — Critical Domain Below Floor:**
- Submission has:
  - Market Validation domain (Critical): 25/100 ✗ (floor is 30)
  - Customer Validation domain (Standard): 45/100 ✓
  - Financial Model domain (Critical): 60/100 ✓
- Overall Readiness: (25 + 45 + 60) / 3 = 43.3 (which would be CONDITIONAL HOLD from score bands)
- Gate 2: Critical domain below floor → **CONDITIONAL HOLD minimum** (confirms and reinforces overall score)

**Example 3 — All Domains Above Floor:**
- Submission has:
  - Market Validation domain (Critical): 35/100 ✓ (floor is 30)
  - Customer Validation domain (Hard-Blocker): 55/100 ✓ (floor is 40)
  - Financial Model domain (Critical): 45/100 ✓ (floor is 30)
- Overall Readiness: (35 + 55 + 45) / 3 = 45.0 (which is CONDITIONAL HOLD from score bands)
- Gate 2: All domains above floor → Proceed to Gate 3 using score-band baseline of **CONDITIONAL HOLD**

---

## Gate 3 — Fit-to-Purpose Threshold

Fit-to-Purpose scoring establishes a secondary threshold.

### Fit-to-Purpose Rules

| Threshold | Rule | Outcome |
|---|---|---|
| Overall Fit-to-Purpose < 40 | Insufficient appropriateness for any assessor type | **CONDITIONAL HOLD minimum** |
| Primary Domain Fit-to-Purpose < 50 | Insufficient appropriateness in primary assessment dimension | **CONDITIONAL HOLD minimum** |
| Overall Fit-to-Purpose ≥ 40 AND Primary Domain ≥ 50 | Acceptable appropriateness | No gate modification |

**Fit-to-Purpose Modifier Table:**

| Overall Fit-to-Purpose Score | Modifier | Effect |
|---|---|---|
| 70–100 | None | No change to Readiness baseline |
| 50–69 | Downgrade one level | GO → CONDITIONAL GO; CONDITIONAL GO → CONDITIONAL HOLD; CONDITIONAL HOLD → NO-GO |
| < 50 | Hold | CONDITIONAL HOLD minimum (cannot exceed CONDITIONAL HOLD) |

**Rule Logic:** If Fit-to-Purpose is weak (50–69), it downgrades confidence in the submission even if Readiness is strong. If Fit-to-Purpose is very weak (<50), it disqualifies GO outcomes.

### Worked Examples — Gate 3

**Example 1 — Strong Readiness, Weak Fit-to-Purpose:**
- Readiness baseline (from score bands): **CONDITIONAL GO** (Readiness score 65/100)
- Overall Fit-to-Purpose: 45/100
- Gate 3: Overall < 40? No (45 > 40). Primary domain < 50? Unknown (assume no for this example).
- Fit-to-Purpose Modifier: 50–69? No, it's 45 < 50. Downgrade applies: CONDITIONAL HOLD minimum.
- **Final Determination: CONDITIONAL HOLD**

**Example 2 — Strong Readiness, Weak Stage Appropriateness:**
- Readiness baseline (from score bands): **GO** (Readiness score 78/100)
- Overall Fit-to-Purpose: 35/100
- Gate 3: Overall < 40? Yes (35 < 40).
- **Final Determination: CONDITIONAL HOLD minimum** (Gate 3 overrides Readiness GO)

**Example 3 — Strong Readiness, Moderately Weak Fit-to-Purpose:**
- Readiness baseline (from score bands): **CONDITIONAL GO** (Readiness score 62/100)
- Overall Fit-to-Purpose: 58/100 (moderately aligned for stage/assessor)
- Gate 3: Overall < 40? No. Primary domain < 50? No.
- Fit-to-Purpose Modifier: 50–69 (58 is in this range) → Downgrade one level
- Downgrade: CONDITIONAL GO → CONDITIONAL HOLD
- **Final Determination: CONDITIONAL HOLD**

**Example 4 — Strong Readiness, Strong Fit-to-Purpose:**
- Readiness baseline (from score bands): **GO** (Readiness score 82/100)
- Overall Fit-to-Purpose: 75/100 (well-aligned for stage/assessor)
- Gate 3: Overall < 40? No. Primary domain < 50? No.
- Fit-to-Purpose Modifier: 70–100 (75 is in this range) → No modification
- **Final Determination: GO**

**Example 5 — Weak Readiness, Strong Fit-to-Purpose:**
- Readiness baseline (from score bands): **CONDITIONAL HOLD** (Readiness score 45/100)
- Overall Fit-to-Purpose: 72/100 (well-aligned, but cannot overcome weak Readiness)
- Gate 3: Overall < 40? No. Primary domain < 50? No.
- Fit-to-Purpose Modifier: 70–100 → No modification
- **Final Determination: CONDITIONAL HOLD** (Cannot be upgraded by strong Fit-to-Purpose; Readiness is limiting factor)

---

## Readiness Score Bands and Baseline Determination

Before Gate 3, the Readiness score (after Gates 1 and 2) produces a baseline:

| Readiness Score | Baseline Determination |
|---|---|
| 75–100 | GO |
| 55–74 | CONDITIONAL GO |
| 35–54 | CONDITIONAL HOLD |
| Below 35 | NO-GO |

**Rule:** Baseline determination from Readiness is never upgraded by Fit-to-Purpose. It can only be maintained or downgraded.

---

## Final Determination Outcomes and Definitions

### GO
**Definition:** Readiness is strong (≥75) and Fit-to-Purpose is strong (≥70). No gates are triggered, and no domain floors are violated. The submission meets both content and context requirements.

**Conditions:**
- Readiness score ≥ 75
- No Gate 1 hard blockers with Completeness 0
- No Gate 2 domain floors violated
- Overall Fit-to-Purpose ≥ 40 AND Primary domain ≥ 50
- Fit-to-Purpose modifier (if any) does not downgrade
- **Final Determination: Assessor should proceed with advanced review. Risk assessment is low to moderate.**

**Example:**
- Readiness: 82 → baseline GO
- Fit-to-Purpose: 73 → no downgrade
- Final: GO

### CONDITIONAL GO
**Definition:** Readiness is solid (55–74), Fit-to-Purpose is acceptable, and gates are passed. The submission meets core requirements but with some gaps in evidence or appropriateness.

**Conditions:**
- Readiness score 55–74
- No Gate 1 hard blockers with Completeness 0
- No Gate 2 domain floors violated
- Overall Fit-to-Purpose ≥ 40 AND Primary domain ≥ 50
- Fit-to-Purpose modifier (if any) does not downgrade or downgrade is applied

**Example 1 (Strong Fit-to-Purpose):**
- Readiness: 68 → baseline CONDITIONAL GO
- Fit-to-Purpose: 76 → no downgrade
- Final: CONDITIONAL GO

**Example 2 (Moderate Fit-to-Purpose):**
- Readiness: 65 → baseline CONDITIONAL GO
- Fit-to-Purpose: 54 → applies 50–69 modifier (downgrade)
- Downgraded to: CONDITIONAL HOLD

**Final Determination: Assessor should proceed with caution. Risk is moderate; specific gap areas should be resolved.**

### CONDITIONAL HOLD
**Definition:** Readiness is moderate (35–54), or Fit-to-Purpose is weak, or a gate warning is triggered. The submission has material gaps or misalignments. Assessor should request clarification before final decision.

**Conditions (any of the following):**
- Readiness score 35–54 (and gates are passed)
- Readiness score 55–74 AND Fit-to-Purpose modifier downgrades (50–69 Fit-to-Purpose range)
- Gate 2 domain floor is violated
- Gate 3 Fit-to-Purpose threshold is exceeded (overall <40 or primary domain <50)
- Gate 1 hard blocker with Completeness >0 (present but incomplete)

**Example 1 (Weak Readiness):**
- Readiness: 48 → baseline CONDITIONAL HOLD
- Gates: All passed
- Final: CONDITIONAL HOLD

**Example 2 (Moderate Readiness with Domain Floor Violation):**
- Readiness: 65 → baseline CONDITIONAL GO
- Gate 2: Market Validation domain (Critical) = 28 < floor of 30 → violation
- Final: CONDITIONAL HOLD (gate overrides baseline)

**Example 3 (Strong Readiness, Weak Fit-to-Purpose):**
- Readiness: 70 → baseline CONDITIONAL GO
- Fit-to-Purpose: 45 → Gate 3 violation (overall <40? No, but is in 50–69 range? No, is <50)
- Gate 3 modifier: Apply CONDITIONAL HOLD minimum
- Final: CONDITIONAL HOLD

**Final Determination: Assessor should request specific clarifications or improvements before proceeding. Risk is moderate to high.**

### NO-GO
**Definition:** Readiness is weak (≤35), or a hard blocker is triggered, or critical gates are violated. The submission does not meet minimum requirements. Assessor should not proceed without substantial revision.

**Conditions (any of the following):**
- Readiness score < 35
- Gate 1 hard blocker with Completeness 0
- Gate 2 hard-blocker domain floor violated AND cannot be cured
- Gate 3 very weak Fit-to-Purpose with Readiness downgrade applied

**Example 1 (Weak Readiness):**
- Readiness: 28 → baseline NO-GO
- Final: NO-GO

**Example 2 (Hard Blocker Missing):**
- Readiness: 55 → baseline CONDITIONAL GO
- Gate 1: Customer Validation (hard-blocker classified) Completeness = 0
- Final: NO-GO (gate overrides baseline)

**Example 3 (Hard-Blocker Domain Below Floor):**
- Readiness: 50 → baseline CONDITIONAL HOLD
- Gate 2: Product Evidence domain (hard-blocker) = 35 < floor of 40
- Final: NO-GO (hard-blocker floor violation)

**Final Determination: Assessor should not proceed. Submission requires major revision before resubmission.**

---

## Edge Cases and Conflict Resolution

### Case 1 — Contradicting Gates

**Scenario:** Gate 1 passes (no hard blockers with Completeness 0), but Gate 2 identifies a hard-blocker domain below floor.

**Resolution:** Gate 2 violation (hard-blocker floor breach) is **more conservative** than Gate 1 pass. Apply Gate 2 rule: **CONDITIONAL HOLD minimum**.

**Example:**
- Gate 1: Product Evidence Completeness = 1 ✓ (content exists, passes hard blocker check)
- Gate 2: Product Evidence domain score = 35 < floor of 40 ✗ (hard-blocker floor violated)
- **Determination: CONDITIONAL HOLD minimum** (Gate 2 applies)

### Case 2 — All Gates Pass, Overall Score is Low

**Scenario:** Readiness score is 40 (which is CONDITIONAL HOLD from bands), but all gates are passed and Fit-to-Purpose is strong.

**Resolution:** Readiness score band determines baseline. Gates add constraints but do not upgrade. Strong Fit-to-Purpose cannot upgrade from CONDITIONAL HOLD baseline.

**Example:**
- Readiness: 40 (CONDITIONAL HOLD from bands)
- Gate 1: Passed (no hard blockers with Completeness 0)
- Gate 2: Passed (all domains above floor)
- Gate 3: Passed (Fit-to-Purpose 72)
- **Determination: CONDITIONAL HOLD** (baseline from Readiness; gates confirm; Fit-to-Purpose does not upgrade)

### Case 3 — Primary Domain Weakens Fit-to-Purpose

**Scenario:** Overall Fit-to-Purpose is 55 (acceptable), but the primary domain (most critical to assessor decision) is 42 (weak).

**Resolution:** Primary domain threshold is independent. Primary domain Fit-to-Purpose < 50 triggers Gate 3 rule.

**Example:**
- Overall Fit-to-Purpose: 55
- Primary Domain (Market Validation) Fit-to-Purpose: 42 < 50
- Readiness: 65 (CONDITIONAL GO baseline)
- **Gate 3 applies:** Primary domain < 50 → CONDITIONAL HOLD minimum
- **Determination: CONDITIONAL HOLD** (Gate 3 overrides baseline)

### Case 4 — Fit-to-Purpose Downgrade Chains

**Scenario:** Readiness is 72 (CONDITIONAL GO), Fit-to-Purpose is 55 (applies 50–69 modifier, downgrades one level to CONDITIONAL HOLD). Does further downgrade apply?

**Resolution:** One downgrade per gate. Fit-to-Purpose modifier applies once; it does not chain.

**Example:**
- Readiness: 72 → baseline CONDITIONAL GO
- Fit-to-Purpose: 55 → apply modifier (downgrade one level)
- **Determination: CONDITIONAL HOLD** (one downgrade, not cascading)

### Case 5 — Multiple Domain Floors Violated

**Scenario:** Hard-blocker domain is at floor (40), critical domain is below floor (28 < 30).

**Resolution:** Any floor violation triggers CONDITIONAL HOLD minimum. Multiple violations do not escalate beyond CONDITIONAL HOLD; they confirm it.

**Example:**
- Hard-blocker domain: 40 (at floor) ✓
- Critical domain: 28 < floor of 30 ✗
- Readiness baseline: Assume 50 (CONDITIONAL HOLD)
- **Gate 2 applies:** Critical domain below floor
- **Determination: CONDITIONAL HOLD** (gate violation confirmed by Readiness score, not escalated further)

---

## Decision Tree for Assessor

```
START: Submit for Gate 1 evaluation
  ↓
GATE 1: Hard blocker with Completeness = 0?
  → YES: Final = NO-GO (STOP)
  → NO: Proceed to Gate 2
  ↓
GATE 2: Any domain below floor?
  → YES: Final ≥ CONDITIONAL HOLD (may be upgraded below)
  → NO: Continue with Readiness bands
  ↓
READINESS BANDS: Score ≥ 75? Score 55-74? Score 35-54? Score < 35?
  → ≥ 75: Baseline = GO
  → 55-74: Baseline = CONDITIONAL GO
  → 35-54: Baseline = CONDITIONAL HOLD
  → < 35: Baseline = NO-GO (STOP)
  ↓
GATE 3: Fit-to-Purpose evaluation
  Overall < 40 OR Primary < 50?
  → YES: Apply CONDITIONAL HOLD minimum
  → NO: Check Fit-to-Purpose modifier
  ↓
FIT-TO-PURPOSE MODIFIER: Score 70+? Score 50-69? Score < 50?
  → 70+: No change
  → 50-69: Downgrade baseline one level
  → < 50: Apply CONDITIONAL HOLD minimum
  ↓
FINAL: More conservative of Readiness baseline and Gate-modified result
```

---

## Worked Example — Full Workflow

**Scenario:** Series A submission, three domains: Market Validation (Critical), Customer Validation (Hard-Blocker), Financial Model (Critical).

**Scores Provided:**
- Market Validation: Readiness 42, Fit-to-Purpose 64
- Customer Validation: Readiness 52, Fit-to-Purpose 48
- Financial Model: Readiness 35, Fit-to-Purpose 70

**Step 1 — Gate 1:**
- Customer Validation (hard-blocker) Completeness ≥ 1? Check submission. Assume Completeness = 2 (Present).
- Gate 1: Passed ✓

**Step 2 — Gate 2:**
- Market Validation: 42 ≥ 30 (Critical floor)? YES ✓
- Customer Validation: 52 ≥ 40 (Hard-blocker floor)? YES ✓
- Financial Model: 35 ≥ 20 (Standard floor)? YES ✓
- Gate 2: Passed ✓

**Step 3 — Readiness Baseline:**
- Overall Readiness: (42 + 52 + 35) / 3 = 43
- Readiness Band: 43 is in 35–54 range
- Baseline: **CONDITIONAL HOLD**

**Step 4 — Gate 3:**
- Overall Fit-to-Purpose: (64 + 48 + 70) / 3 = 60.7
- Overall < 40? No (60.7 > 40) ✓
- Primary Domain (Market Validation) Fit-to-Purpose: 64 ≥ 50? YES ✓
- Gate 3: Passed ✓

**Step 5 — Fit-to-Purpose Modifier:**
- Fit-to-Purpose 60.7 is in 50–69 range
- Modifier: Downgrade baseline one level
- Downgrade: CONDITIONAL HOLD → NO-GO (downgrading one level from CONDITIONAL HOLD)

**Wait:** No-Go means downgrade is insufficient. Re-check: Downgrading one level from CONDITIONAL HOLD is NO-GO. But CONDITIONAL HOLD is already conservative. This is valid.

**Actually, re-read the rule:** "Baseline downgraded one level." From CONDITIONAL HOLD:
- CONDITIONAL HOLD ← NO-GO (lower)
- CONDITIONAL HOLD ← CONDITIONAL GO (higher)

Downgrading one level from CONDITIONAL HOLD means moving toward NO-GO.

**Downgraded Determination: NO-GO** (one level down from CONDITIONAL HOLD)

**Final:** More conservative of baseline (CONDITIONAL HOLD) and downgraded (NO-GO) = **NO-GO**

**Interpretation:** The submission has weak Readiness (43/100) and moderate Fit-to-Purpose (60.7, not strong). The downgrade reflects that moderate appropriateness cannot compensate for weak evidence. **Assessor should not proceed. Request major clarifications, especially on Customer Validation and Financial Model details.**

---

## Summary Decision Matrix

| Readiness | Gates Passed? | Fit-Purpose | Final |
|---|---|---|---|
| ≥75 | Yes | ≥70 | GO |
| ≥75 | Yes | 50-69 | CONDITIONAL GO (downgraded to) |
| ≥75 | Yes | <50 | CONDITIONAL HOLD |
| 55-74 | Yes | ≥70 | CONDITIONAL GO |
| 55-74 | Yes | 50-69 | CONDITIONAL HOLD (downgraded) |
| 55-74 | Yes | <50 | CONDITIONAL HOLD |
| 35-54 | Yes | Any | CONDITIONAL HOLD |
| <35 | Yes | Any | NO-GO |
| Any | No (Gate violated) | Any | More conservative rule applies |
