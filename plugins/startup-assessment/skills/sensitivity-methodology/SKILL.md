---
name: sensitivity-methodology
description: >
  This skill should be used by the sensitivity-agent when conducting sensitivity analysis
  on a locked assessment determination. Covers methodology selection logic, execution
  procedures for all three methodology types, and robustness classification.
  Trigger phrases: "sensitivity analysis", "robustness check", "flip-point", "scenario analysis",
  "Monte Carlo", "methodology selection", "determination stability".
version: 0.1.0
---

# Sensitivity-Methodology Skill

## 1. Overview

### Purpose

The sensitivity-methodology skill enables the sensitivity-agent to conduct rigorous analysis on locked assessment determinations. After the assessor completes the full assessment (/assess phase) and reviews the determination outcome, the sensitivity phase (/sensitivity command) tests the robustness and stability of that determination.

### When This Skill Is Used

- Triggered after /assess is complete and the assessor reviews the determination
- Applies to all determination outcomes: GO, CONDITIONAL GO, CONDITIONAL HOLD, NO-GO
- Runs before the /recommend phase, which depends on sensitivity findings
- Occurs once per assessment cycle (locked determination prevents re-running /assess)

### What It Produces

1. **sensitivity-analysis.json** — machine-readable output feeding the /recommend phase
2. **HTML sensitivity report** — interactive methodology summary and detailed results
3. **PDF sensitivity report** — archivable assessment record
4. **Path B availability determination** — rules-based logic tied to robustness classification
5. **Next-phase prompt** — guidance for /recommend phase based on robustness findings

---

## 2. Methodology Selection Logic

### Determination-Type Methodology Mapping

The methodology options presented to the assessor vary by determination type. The sensitivity-agent presents 2–3 options; the assessor selects one for execution.

#### GO Determination (Readiness 75–100 + Adequate Fit)

**Appropriate methodologies:**
- **Boundary/Flip-Point Analysis** — How close is the determination to dropping to CONDITIONAL GO? What minimum evidence deterioration would trigger a flip?
- **Scenario Analysis** — How does the determination perform under pessimistic assumptions? Does it hold?

**Presentation:** "Your determination is GO. We can test whether it remains GO under challenging scenarios, or identify the minimum evidence deterioration required to drop it to CONDITIONAL GO."

**Selection logic:** Boundary analysis is more revealing for GO determinations (identifies safety margin); scenario analysis validates resilience.

#### CONDITIONAL GO Determination (Readiness 55–74 + Conditions)

**Appropriate methodologies:**
- **Scenario Analysis** — Can the stated conditions realistically be met? What assumptions must hold for this determination to be valid?
- **Boundary/Flip-Point Analysis** — How far are we from GO (upward flip)? How close to CONDITIONAL HOLD (downward flip)?
- **Monte Carlo Simulation** — What is the probability distribution across all four determination levels given assumption uncertainty?

**Presentation:** "Your determination is CONDITIONAL GO with stated conditions. We can test whether those conditions are achievable, identify how far you are from full GO, or run a probability analysis under assumption uncertainty."

**Selection logic:** CONDITIONAL GO is the most sensitive determination type and benefits from all three methodologies. Scenario analysis validates condition achievability; boundary analysis shows flip distance; Monte Carlo quantifies probabilistic outcome.

#### CONDITIONAL HOLD Determination (Readiness 35–54 + Conditions)

**Appropriate methodologies:**
- **Scenario Analysis** — What remediation paths exist? What would need to improve to reach CONDITIONAL GO?
- **Boundary/Flip-Point Analysis** — What is the minimum evidence improvement to flip upward to CONDITIONAL GO?

**Presentation:** "Your determination is CONDITIONAL HOLD. We can map remediation paths under optimistic improvement scenarios, or calculate the minimum evidence changes needed to flip to CONDITIONAL GO."

**Selection logic:** CONDITIONAL HOLD assessments focus on improvement; boundary analysis quantifies the effort required; scenario analysis identifies which assumptions/areas matter most.

#### NO-GO Determination (Readiness Below 35)

**Appropriate methodologies:**
- **Scenario Analysis** — What would need to change for reconsideration? Which assumptions are most critical?
- **Boundary/Flip-Point Analysis** — How far are we from CONDITIONAL HOLD (upward flip)? What is the closest flip point?

**Presentation:** "Your determination is NO-GO. We can identify which critical assumptions would need to change for reconsideration, or calculate the evidence improvements required to reach CONDITIONAL HOLD."

**Selection logic:** NO-GO determinations are final unless fundamental evidence shifts. Scenario analysis identifies reconsideration triggers; boundary analysis quantifies the effort barrier.

### Methodology Presentation Format

The sensitivity-agent presents options using this structure:

```
METHODOLOGY OPTIONS FOR [DETERMINATION TYPE] DETERMINATION

Option 1: [Methodology Name]
  What it tests: [Clear description of what this methodology validates]
  Output: [What the assessor receives]
  Best for: [When this option is most valuable]
  Time estimate: [Execution time]

Option 2: [Methodology Name]
  [Same structure]

Option 3: [Methodology Name (if applicable)]
  [Same structure]

Please select the methodology you'd like to execute (enter 1, 2, or 3).
```

After assessor selection, the agent confirms:
"You've selected [Methodology Name]. I will now:
1. [Step 1 of execution]
2. [Step 2 of execution]
3. [Step 3 of execution]

Should I proceed?"

Only after confirmation does the agent execute the methodology.

---

## 3. Methodology 1: Scenario Analysis

### Definition and Purpose

Scenario analysis tests how the determination changes under different assumption sets. Three scenarios are evaluated:
- **Bull Case** (optimistic): favorable assumptions, best-case conditions
- **Base Case** (moderate): current assessment assumptions (locked from /assess phase)
- **Bear Case** (pessimistic): challenging assumptions, worst-case plausible conditions

Each scenario is re-scored using the original assessment rubric, producing a determination range. Robustness is assessed by the spread of outcomes across scenarios.

### Scenario Definition Process

Scenario assumptions are derived from:
1. **Domain 7 Key Assumptions** — extracted during /assess phase
2. **Gap Register Critical Gaps** — highest-severity gaps identified in assessment
3. **Research Conflicts** — areas where evidence is contradictory or uncertain

**Bull Case Construction:**
- Identify optimistic assumption variants for each critical assumption
- Example: "Market growth rate = 35% annually" (vs. Base 20%)
- Example: "Competitor response time = 24+ months" (vs. Base 12 months)
- Maintain internal consistency (all bull assumptions work together coherently)
- Document the narrative: "Assumes industry tailwind, delayed competitive response, faster adoption"

**Bear Case Construction:**
- Identify pessimistic assumption variants for each critical assumption
- Example: "Market growth rate = 8% annually" (vs. Base 20%)
- Example: "Competitor response time = 3 months" (vs. Base 12 months)
- Maintain internal consistency (all bear assumptions work together coherently)
- Document the narrative: "Assumes market headwinds, fast competitive response, slower adoption"

**Base Case:**
- Lock the assumptions from the completed /assess phase
- These are the assumptions that produced the initial determination
- Do not modify base case assumptions

### Score Re-Calculation Under Each Scenario

For each scenario (Bull, Base, Bear):

1. **Apply adjusted assumptions** to all seven assessment domains
2. **Re-score each domain** using the original assessment rubric (0–100 per domain)
3. **Calculate composite readiness score**:
   - Readiness = (sum of 7 domain scores) / 7
   - Rounded to nearest integer
4. **Map composite readiness to determination**:
   - 75–100: GO
   - 55–74: CONDITIONAL GO
   - 35–54: CONDITIONAL HOLD
   - Below 35: NO-GO
5. **Evaluate fit-to-purpose** under each scenario (adequate / inadequate)
6. **Combine readiness + fit-to-purpose** to produce determination

**Important:** Do not adjust the rubric itself. Use the identical scoring rubric across all three scenarios; only the input assumptions change.

### Robustness Classification from Scenario Spread

After scoring all three scenarios:

**Robust** — Determination remains identical across Bull, Base, and Bear cases
- Example: Base = GO, Bull = GO, Bear = GO → Robust GO
- Example: Base = CONDITIONAL GO, Bull = GO, Bear = CONDITIONAL GO → Robust CONDITIONAL GO (spread ≤1 level)

**Moderately Robust** — Determination holds in Base + one extreme; changes in the other extreme, with maximum 1-level spread
- Example: Base = CONDITIONAL GO, Bull = GO, Bear = CONDITIONAL HOLD → Moderately Robust (spread = 2 levels, but base holds)
- Example: Base = CONDITIONAL HOLD, Bull = CONDITIONAL GO, Bear = CONDITIONAL HOLD → Moderately Robust (spread = 1 level)

**Fragile** — Determination changes under moderate stress, or spread exceeds 1 level
- Example: Base = CONDITIONAL GO, Bull = GO, Bear = NO-GO → Fragile (spread = 3 levels)
- Example: Base = GO, Bull = GO, Bear = CONDITIONAL GO → Fragile if the concern is lack of downside protection (assessor's judgment)
- Example: Base = CONDITIONAL HOLD, Bull = NO-GO, Bear = CONDITIONAL HOLD → Fragile (base is worst-case in own range)

### Scenario Analysis Output Format

Generate output table:

| Scenario | Key Assumption Adjustments | Composite Score | Fit-to-Purpose | Determination |
|----------|---------------------------|-----------------|-----------------|---------------|
| Bull | Market growth 35%, no competition for 24mo, early adoption | 82 | Adequate | GO |
| Base | Market growth 20%, competition 12mo, standard adoption | 68 | Adequate | CONDITIONAL GO |
| Bear | Market growth 8%, competition 3mo, slow adoption | 42 | Adequate | CONDITIONAL HOLD |

**Determination Range:** NO-GO to GO (spread = 3 levels)
**Robustness Classification:** Fragile

**Analysis Notes:**
- Key sensitivities: Market growth rate, competitive response time
- Base case determination ([original determination]) is sensitive to [variable] and [variable]
- Under optimistic conditions, determination rises to [determination]; under pessimistic, drops to [determination]

---

## 4. Methodology 2: Boundary / Flip-Point Analysis

### Definition and Purpose

Boundary analysis identifies the minimum changes required to flip the determination up or down by one level. It answers questions like:
- "How much better would the evidence need to be to move from CONDITIONAL GO to GO?"
- "How much worse could the evidence get before dropping from CONDITIONAL GO to CONDITIONAL HOLD?"

This methodology identifies which modules/domains have the smallest gap to flip thresholds and quantifies the evidence improvement needed.

### Flip Analysis Process

#### Step 1: Identify Candidate Modules for Flip Analysis

From the /assess phase, extract the score for each of the seven domains:
- Domain 1 [name]: [score]
- Domain 2 [name]: [score]
- Domain 3 [name]: [score]
- ... Domain 7 [name]: [score]

**Composite readiness = average of all 7 domain scores**

Calculate distance to flip thresholds:
- Current composite: [current score]
- Distance to next higher determination: [points needed to raise]
- Distance to next lower determination: [points needed to lower]

Identify which single domain, if improved/deteriorated, would contribute most to a flip.

#### Step 2: Upward Flip Analysis (Move to More Favorable Determination)

**Example: CONDITIONAL GO (55–74) → GO (75–100)**

**Process:**
1. Current composite readiness: 68 (within CONDITIONAL GO range)
2. Target: 75 (minimum GO readiness)
3. Improvement needed: 7 points across the composite
4. Strategy: Identify which domain(s) are closest to improvement ceiling and have highest impact

**Calculation:**
- If Domain 3 (Product-Market Fit) currently scores 65, and the assessment identified specific gaps (e.g., "Limited TAM validation"), calculate the evidence needed to raise it to 72.
- Evidence requirements: "Conduct customer reference calls with X enterprises; document TAM expansion findings; present revised market model."
- Estimate: Is this evidence "easy" (1–2 supporting studies), "moderate" (formal customer validation program), or "intensive" (comprehensive market research engagement)?

**Output for upward flip:**

| Domain | Current Score | Target Score | Gap | Evidence Requirements | Feasibility |
|--------|---|---|---|---|---|
| Domain 3: Product-Market Fit | 65 | 72 | +7 | Validate TAM expansion; customer reference calls | Moderate (4–8 weeks) |
| Domain 5: Operations Readiness | 62 | 68 | +6 | Finalize hiring plan; vendor contracts | Moderate (2–4 weeks) |
| **Total composite lift needed:** | 68 | 75 | +7 | [Aggregated requirements] | **Moderate** |

**Interpretation:** To flip from CONDITIONAL GO to GO, the team would need to improve evidence in 2–3 domains by completing targeted validation work—achievable in 4–8 weeks.

#### Step 3: Downward Flip Analysis (Move to Less Favorable Determination)

**Example: CONDITIONAL GO (55–74) → CONDITIONAL HOLD (35–54)**

**Process:**
1. Current composite readiness: 68
2. Target (downward): 54 (maximum CONDITIONAL HOLD readiness)
3. Deterioration tolerance: 14 points
4. Question: Which single domain deterioration would trigger the flip?

**Calculation:**
- If Domain 2 (Business Model Viability) currently scores 58 and represents the team's assumed strength, calculate how much it could decline before the composite drops below 55.
- Deterioration scenario: Market size contract by 30%; unit economics deteriorate by 15%.
- Risk: How plausible is this? (e.g., "Plausible if customer acquisition costs rise" vs. "Highly unlikely given market structure")

**Output for downward flip:**

| Domain | Current Score | Flip Threshold | Tolerance | Deterioration Trigger | Risk Level |
|--------|---|---|---|---|---|
| Domain 2: Business Model | 58 | 48 | -10 | 30% market contraction; 15% CAC increase | Moderate (market dynamics) |
| Domain 5: Operations | 62 | 52 | -10 | 50% hiring delays; vendor failures | Low (operational risk) |
| **Composite floor:** | 68 | 54 | -14 | [Trigger scenarios] | **Moderate** |

**Interpretation:** CONDITIONAL GO determination could drop to CONDITIONAL HOLD if market size contracts materially or operational execution falters. Current safety margin is 14 points.

#### Step 4: Distance-to-Flip Metric

Express the ease or difficulty of flipping:

**Upward flip distance:**
- **Near** (easy to flip): ≤5 composite points needed; fewer than 2 domains; evidence requirements are light (existing studies, customer references)
- **Moderate**: 5–10 composite points; 2–3 domains; evidence requirements are medium (formal validation programs, market research)
- **Far** (robust): ≥10 composite points; 4+ domains; major evidence shifts required (comprehensive overhaul of business model, market repositioning)

**Downward flip distance:**
- **Near** (fragile): ≥10 composite points tolerance; deterioration triggers are plausible; current safety margin is low
- **Moderate**: 10–15 composite point tolerance; deterioration triggers are moderate risk; reasonable safety margin
- **Far** (robust): ≥15 composite points tolerance; deterioration triggers are unlikely; strong safety margin

### Asymmetry Interpretation

If upward and downward distances differ significantly:

**Asymmetry example:**
- Upward flip: 7 points (moderate effort)
- Downward flip: 14 points (robust margin)

**Interpretation:** "The determination is asymmetric—easier to improve than to deteriorate. This suggests the current evidence is solid; incremental validation could move to GO, but the determination is protected against moderate challenges."

**Alternative asymmetry:**
- Upward flip: 15 points (far/robust)
- Downward flip: 8 points (fragile)

**Interpretation:** "The determination is fragile downward. Even moderate adverse evidence (market headwinds, operational setbacks) could drop the determination. Upward movement requires major evidence shifts."

### Boundary Analysis Output Format

**Output section 1: Upward Flip Analysis**
```
UPWARD FLIP: [Current Determination] → [Next Favorable Determination]

Composite score improvement required: X points
Domains targeted for improvement: [List with specific gaps]
Evidence requirements:
  - [Requirement 1]
  - [Requirement 2]

Estimated effort: [Light / Moderate / Intensive]
Timeline: [Weeks / Months]

Probability of achieving flip: [High / Moderate / Low]
```

**Output section 2: Downward Flip Analysis**
```
DOWNWARD FLIP: [Current Determination] → [Next Unfavorable Determination]

Deterioration tolerance: X points
Domains most at risk: [List with deterioration scenarios]
Early warning indicators:
  - [Indicator 1]
  - [Indicator 2]

Current safety margin: [Strong / Adequate / Marginal]
```

**Output section 3: Distance-to-Flip Metric**
```
FLIP DISTANCE ASSESSMENT

Upward: [Near / Moderate / Far]
  Justification: [Composite points, number of domains, evidence burden]

Downward: [Near / Moderate / Far]
  Justification: [Deterioration tolerance, plausibility of triggers]

Asymmetry: [Determination is asymmetric upward / downward / balanced]
  Implication: [What this means for robustness]
```

---

## 5. Methodology 3: Monte Carlo Simulation (Simplified)

### Definition and Purpose

Monte Carlo analysis (executed analytically rather than computationally) quantifies the probability distribution of determinations across the range of assumption uncertainty. Instead of relying on a single "base case," it combines top assumptions probabilistically to estimate:
- Probability of GO
- Probability of CONDITIONAL GO
- Probability of CONDITIONAL HOLD
- Probability of NO-GO

This methodology is particularly valuable for CONDITIONAL GO determinations, where assumption sensitivity is highest.

### Key Assumption Identification

Identify the **top 5–8 key assumptions** from:
1. **Domain 7: Assumptions & Dependencies** — extracted during /assess phase (highest-sensitivity assumptions)
2. **Gap Register** — gaps flagged as "high-severity" or "high-uncertainty"
3. **Research Conflicts** — areas where evidence contradicts or is inconclusive

**Selection criteria:**
- Highest impact on composite readiness score (if assumption changes by 20%, how much does readiness shift?)
- Highest residual uncertainty (how confident is the assessment in this assumption's validity?)
- Cross-domain relevance (does this assumption affect multiple domains?)

**Example top 5 assumptions for a SaaS startup:**
1. **TAM growth rate** — 20% annually (high impact on market sizing, affects fit-to-purpose)
2. **Customer acquisition cost (CAC) payback period** — 18 months (high impact on business model, affects GO/CONDITIONAL threshold)
3. **Competitive response time** — 12 months to meaningful entry (high impact on market opportunity, affects GO/CONDITIONAL)
4. **Product-market fit validation** — 40% of target segment shows strong fit signals (high impact on product readiness, affects GO/CONDITIONAL)
5. **Founding team execution capability** — moderate risk; no prior unicorn exits (affects operations readiness)
6. **Regulatory/compliance barriers** — low risk; standard SaaS data practices sufficient (affects fit-to-purpose)
7. **Sales channel assumption** — direct sales model with 3-person team Year 1 (affects revenue model, affects readiness)

### Assumption Range Specification

For each key assumption, define three values and their probability weights:

| Assumption | Low (Pessimistic) | Mid (Base) | High (Optimistic) | Low Prob | Mid Prob | High Prob |
|---|---|---|---|---|---|---|
| TAM growth | 8% annually | 20% annually | 35% annually | 25% | 50% | 25% |
| CAC payback | 32 months | 18 months | 12 months | 25% | 50% | 25% |
| Competitor response | 3 months | 12 months | 24 months | 25% | 50% | 25% |
| PMF validation | 20% of segment | 40% of segment | 60% of segment | 25% | 50% | 25% |
| Team execution | High risk | Moderate risk | Low risk | 30% | 50% | 20% |
| Regulatory | High barriers | Standard compliance | Minimal barriers | 15% | 50% | 35% |
| Sales model | Partnership-dependent | Direct sales | Channel + direct | 20% | 50% | 30% |

**Probability weight derivation:**
- Base assumption probability = 50% (confidence in current assessment)
- Low and High probabilities = 25% each (equal tails) unless evidence suggests asymmetry
- Example: If regulatory landscape is favorable, adjust to Low=10%, Mid=40%, High=50%

### Iteration Methodology (Analytical Execution)

Rather than computational simulation, execute analytically by defining representative scenarios:

**Step 1: Define 8 representative scenarios** covering the assumption space:

| Scenario | TAM | CAC | Competitor | PMF | Team | Regulatory | Sales | Probability |
|---|---|---|---|---|---|---|---|---|
| 1. All Low | L | L | L | L | L | L | L | 0.25^7 ≈ 0.02% |
| 2. Mostly Low | L | L | L | L | L | L | M | 0.25^6 × 0.5 ≈ 0.03% |
| 3. Mixed-Low | L | L | M | M | M | M | M | 0.25^2 × 0.5^5 ≈ 0.5% |
| 4. Base Case | M | M | M | M | M | M | M | 0.5^7 ≈ 0.8% |
| 5. Mixed-High | H | H | M | M | M | M | M | 0.25^2 × 0.5^5 ≈ 0.5% |
| 6. Mostly High | H | H | H | H | H | H | M | 0.25^6 × 0.5 ≈ 0.03% |
| 7. All High | H | H | H | H | H | H | H | 0.25^7 ≈ 0.02% |
| 8. Bull Case | H | H | H | H | M | H | H | 0.25^5 × 0.5^2 ≈ 0.1% |

**Step 2: Calculate composite readiness** for each scenario
- Apply assumptions to all seven domains
- Re-score each domain
- Calculate composite readiness
- Map to determination

**Step 3: Weight outcomes by scenario probability**
- For each determination (GO, CONDITIONAL GO, CONDITIONAL HOLD, NO-GO), sum the probabilities of scenarios producing that outcome
- Example: If scenarios 4, 5, 8 produce GO, then P(GO) = 0.8% + 0.5% + 0.1% = 1.4%

**Step 4: Normalize probabilities**
- Probabilities should sum to 100% across all four determinations
- If using simplified weighting (50/25/25 for Mid/Low/High), adjust to ensure realistic distribution

### Probability Distribution Output Format

Generate output table:

| Determination | Probability | Interpretation |
|---|---|---|
| GO | 42% | Less likely than not |
| CONDITIONAL GO | 45% | Most probable outcome |
| CONDITIONAL HOLD | 11% | Downside risk |
| NO-GO | 2% | Unlikely but plausible under adverse conditions |

**Additional outputs:**

**Mode (Most Probable Determination):** CONDITIONAL GO (45%)

**90th Percentile Outcome (Downside Case):** CONDITIONAL HOLD
- Meaning: There is a 10% probability that the actual outcome falls at or below CONDITIONAL HOLD (combining CONDITIONAL HOLD + NO-GO = 13%)

**Expected Value Determination:** Weighted average of determination levels
- Example: GO=4, CONDITIONAL GO=3, CONDITIONAL HOLD=2, NO-GO=1
- Expected value = (4 × 0.42) + (3 × 0.45) + (2 × 0.11) + (1 × 0.02) = 3.27 → CONDITIONAL GO

### Robustness Classification from Monte Carlo

**Robust:** P(current determination) ≥ 75%
- Current determination dominates the probability distribution
- Other outcomes are tail risks
- Example: P(GO) = 78%, meaning GO is likely even under moderate assumption variance

**Moderately Robust:** P(current determination) 50–74%
- Current determination is probable but not dominant
- One alternative determination has non-trivial probability
- Example: P(CONDITIONAL GO) = 65%, P(GO) = 25%, P(CONDITIONAL HOLD) = 10%

**Fragile:** P(current determination) < 50%
- Current determination is less likely than at least one alternative
- Assumption uncertainty heavily affects outcome
- Example: P(CONDITIONAL GO) = 48%, P(GO) = 35%, P(CONDITIONAL HOLD) = 15%, P(NO-GO) = 2%

### Output Format Specification

```
MONTE CARLO PROBABILITY DISTRIBUTION

Key Assumptions (n=7):
  1. TAM growth rate (Low: 8%, Mid: 20%, High: 35%)
  2. CAC payback period (Low: 32mo, Mid: 18mo, High: 12mo)
  3. [Additional assumptions...]

Probability Weights: Low=25%, Mid=50%, High=25% (derived from assessment confidence)

Determination Probability Distribution:
  GO: 42%
  CONDITIONAL GO: 45%
  CONDITIONAL HOLD: 11%
  NO-GO: 2%
  Total: 100%

Mode (Most Probable): CONDITIONAL GO
90th Percentile Outcome: CONDITIONAL HOLD (downside case)
Expected Value Determination: CONDITIONAL GO

Robustness Classification: Moderately Robust
  Interpretation: Current determination (CONDITIONAL GO) has 45% probability, with meaningful upside (42% GO) and downside (13% CONDITIONAL HOLD or worse).

Key Insights:
  - Highest sensitivity: [Assumption name]; outcome is P(GO)=35% if High, P(CONDITIONAL HOLD)=25% if Low
  - Most stable assumption: [Assumption name]; outcome changes <5% across range
  - Tail risk (>10% probability): NO-GO only occurs in 2% of cases (Low TAM + High CAC payback + Competitor speed)
```

### Limitations and Disclosure

Document in the sensitivity report:

"This is a **structured analytical approach** to probability estimation, not statistical simulation software. The analysis:
- Combines assumptions probabilistically using weighted scenarios
- Does not account for statistical correlation between assumptions (assumes independence)
- Relies on expert probability weighting (Low=25%, Mid=50%, High=25%) rather than historical data
- Should be interpreted as 'order of magnitude' probability ranges, not precise percentages
- Confidence interval: ±10 percentage points on any single determination probability

For higher confidence in probability distributions, consider formal Monte Carlo simulation software or Bayesian analysis with historical data."

---

## 6. Robustness Classification

### Definition

Robustness is a summary judgment of how sensitive the current determination is to changes in assumptions, evidence, or operating conditions. All three methodologies (scenario analysis, boundary analysis, Monte Carlo) feed into this single classification.

### Classification Criteria

**Robust** — The determination is stable and unlikely to change under plausible stress

Indicators across methodologies:
- Scenario analysis: Same determination across all three scenarios (Bull, Base, Bear)
- Boundary analysis: Flip distance is "Far" (≥10 composite points or 4+ domains)
- Monte Carlo: P(current determination) ≥ 75%

**Moderately Robust** — The determination is probable but sensitive to assumptions; likely survives moderate challenge

Indicators across methodologies:
- Scenario analysis: Same determination in Base + one extreme; ≤1-level spread or Base holds
- Boundary analysis: Flip distance is "Moderate" (5–10 composite points or 2–3 domains)
- Monte Carlo: P(current determination) 50–74%

**Fragile** — The determination is sensitive to assumptions and likely to change under plausible challenge

Indicators across methodologies:
- Scenario analysis: Determination changes under Bear case or spread exceeds 1 level; Base case doesn't represent minimum
- Boundary analysis: Flip distance is "Near" (<5 composite points or fewer than 2 domains)
- Monte Carlo: P(current determination) < 50%

### Making the Classification

When multiple methodologies are executed:

1. **Aggregate indicators across all methodologies** applied
2. **Default to the most conservative assessment**: If one methodology says Fragile, give weight to that finding
3. **Resolve conflicts** by examining determination-specific context:
   - GO determination with Robust boundary-flip distance but Moderately Robust scenario spread → likely Robust (GO is hard to flip upward, and downward flip is moderate concern)
   - CONDITIONAL GO with Moderate boundary-flip distance and <50% Monte Carlo probability → likely Fragile (too many paths to other outcomes)
4. **Document the reasoning** in the HTML/PDF report

---

## 7. Path B Availability Rule

### The Rule

**Path B (deal terms negotiation in /recommend phase) is ONLY available when:**

1. **Determination is GO or CONDITIONAL GO**, AND
2. **Sensitivity robustness is "robust" or "moderately-robust"**

### Implications by Robustness

| Determination | Robust | Moderately Robust | Fragile |
|---|---|---|---|
| GO | ✓ Path B available | ✓ Path B available | ✗ Path A only |
| CONDITIONAL GO | ✓ Path B available | ✓ Path B available | ✗ Path A only |
| CONDITIONAL HOLD | ✗ Path A only | ✗ Path A only | ✗ Path A only |
| NO-GO | ✗ Path A only | ✗ Path A only | ✗ Path A only |

### Path A vs. Path B in /recommend Phase

**Path A — Assessment Recommendation:**
- Delivers determination (GO / CONDITIONAL GO / CONDITIONAL HOLD / NO-GO)
- Documents conditions or remediation steps if applicable
- No deal terms negotiation
- Available for all determinations and robustness levels

**Path B — Deal Terms Negotiation:**
- Available ONLY for GO or CONDITIONAL GO with Robust or Moderately Robust sensitivity
- Focuses on term negotiation: valuation, governance, investor rights, founder protection
- Assumes commitment to move forward
- Requires determination confidence (not fragile)

### Documenting in Sensitivity Output

In the `recommendation_implications` field of sensitivity-analysis.json:

```json
"recommendation_implications": {
  "path_b_available": true,
  "reasoning": "Determination is GO and sensitivity is Moderately Robust (scenario spread ≤1 level, boundary flip distance is Moderate). Path B (deal terms) is available for negotiation.",
  "conditions_if_available": [
    "Term negotiation can proceed assuming current market conditions and competitive timeline hold",
    "If market growth drops below 12% or competitor enters in <6 months, determination may shift to CONDITIONAL GO; revisit terms"
  ],
  "caveats_if_unavailable": []
}
```

If Path B is unavailable due to Fragile robustness:

```json
"recommendation_implications": {
  "path_b_available": false,
  "reasoning": "Determination is CONDITIONAL GO but sensitivity is Fragile (scenario spread >2 levels; boundary flip distance is Near). Path B (deal terms) is not available until robustness improves.",
  "conditions_if_available": [],
  "caveats_if_unavailable": [
    "Robustness must improve before deal terms negotiation. This requires stronger evidence in [Domain X] and [Domain Y].",
    "Consider a second sensitivity analysis after submitting additional evidence to validate robustness improvement."
  ]
}
```

---

## 8. Output Delivery

### File Outputs

The sensitivity-agent delivers three files:

1. **sensitivity-analysis.json** (machine-readable)
2. **sensitivity-report.html** (interactive, shareable)
3. **sensitivity-report.pdf** (archivable)

### sensitivity-analysis.json Schema

```json
{
  "assessment_id": "string (uuid from /assess phase)",
  "sensitivity_phase_execution": {
    "timestamp": "ISO 8601 datetime",
    "executed_by": "sensitivity-agent",
    "determination_locked": "string (GO / CONDITIONAL GO / CONDITIONAL HOLD / NO-GO)"
  },
  "methodology_options_presented": [
    {
      "option_number": 1,
      "methodology_name": "string",
      "description": "string (what it tests)",
      "output_summary": "string",
      "time_estimate": "string"
    }
  ],
  "methodology_applied": "scenario-analysis | boundary-flip-point | monte-carlo | combined",
  "analysis_results": {
    "if_scenario_analysis": {
      "scenarios": [
        {
          "name": "Bull / Base / Bear",
          "key_assumptions": ["string"],
          "composite_readiness_score": 0,
          "fit_to_purpose": "adequate | inadequate",
          "determination": "GO | CONDITIONAL GO | CONDITIONAL HOLD | NO-GO"
        }
      ],
      "determination_range": "string (e.g., 'NO-GO to GO')",
      "robustness_from_scenario_spread": "robust | moderately-robust | fragile"
    },
    "if_boundary_analysis": {
      "current_composite_score": 0,
      "upward_flip": {
        "target_determination": "string",
        "composite_points_needed": 0,
        "domains_targeted": ["string"],
        "evidence_requirements": ["string"],
        "estimated_effort": "light | moderate | intensive",
        "flip_distance": "near | moderate | far"
      },
      "downward_flip": {
        "target_determination": "string",
        "composite_points_tolerance": 0,
        "domains_at_risk": ["string"],
        "early_warning_indicators": ["string"],
        "flip_distance": "near | moderate | far"
      },
      "asymmetry_interpretation": "string"
    },
    "if_monte_carlo": {
      "key_assumptions_identified": ["string"],
      "probability_weights": "object (Low/Mid/High for each assumption)",
      "determination_probability_distribution": {
        "GO": 0,
        "CONDITIONAL GO": 0,
        "CONDITIONAL HOLD": 0,
        "NO_GO": 0
      },
      "mode_determination": "string",
      "percentile_90_outcome": "string",
      "expected_value_determination": "string",
      "robustness_from_monte_carlo": "robust | moderately-robust | fragile"
    }
  },
  "robustness_assessment": "robust | moderately-robust | fragile",
  "robustness_reasoning": "string (summary of evidence across methodologies)",
  "key_sensitivities": [
    {
      "variable": "string (e.g., 'TAM growth rate')",
      "impact_on_determination": "string (how much does outcome change if this shifts?)",
      "current_assumption": "string",
      "sensitivity_range": "string (low to high values)"
    }
  ],
  "recommendation_implications": {
    "path_b_available": true,
    "reasoning": "string",
    "conditions_if_available": ["string"],
    "caveats_if_unavailable": ["string"]
  },
  "next_phase_prompt": "string (guidance for /recommend phase)"
}
```

### HTML Sensitivity Report Template

The HTML report includes:
- Executive summary (determination + robustness + key findings)
- Methodology selection narrative (which methodology was chosen and why)
- Detailed results (tabular, with charts if applicable)
- Key sensitivities highlighted
- Path B availability statement
- Footer with timestamp, disclaimer, and next steps

### PDF Sensitivity Report

Export the HTML report to PDF for archival. Include:
- Cover page with assessment ID, date, determination, robustness
- Table of contents
- Full content from HTML
- Appendix: sensitivity-analysis.json (pretty-printed)

### Download Instructions

Provide the user with:
- Direct links to all three files (JSON, HTML, PDF)
- Instructions to download and store securely
- Note on JSON usage: "This file will be automatically loaded into the /recommend phase. You may also reference it for your own records."

### Next-Phase Prompt

Provide clear guidance for the /recommend phase:

```
SENSITIVITY ANALYSIS COMPLETE

Determination: [GO / CONDITIONAL GO / CONDITIONAL HOLD / NO-GO]
Robustness: [Robust / Moderately Robust / Fragile]
Path B Available: [Yes / No]

Key Findings:
- [Finding 1]
- [Finding 2]
- [Finding 3]

Next Step: Run /recommend to generate the final recommendation.

If Path B is available, you will be asked to negotiate deal terms.
If Path B is not available, you will receive a determination-based recommendation with conditions/remediation steps.
```

---

## 9. References Index

Detailed reference materials are available in the following files:

- **references/scenario-analysis.md** — Full procedures, assumption extraction, scoring rubric application, robustness classification, example walkthroughs
- **references/boundary-analysis.md** — Flip-point identification, upward/downward analysis procedures, asymmetry interpretation, output formats, example walkthrough
- **references/monte-carlo-approach.md** — Assumption identification, probability weighting, analytical iteration, distribution output, robustness classification, limitations disclosure

Consult these references during each methodology execution to ensure consistency and rigor.

---

**End of SKILL.md**
