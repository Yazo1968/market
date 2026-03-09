# Scenario Analysis Reference

## Full Scenario Analysis Execution Procedure

This reference provides the complete procedure for executing scenario analysis as a sensitivity methodology.

---

## 1. Extraction: Key Assumptions from Assessment Findings

### Data Sources

**Domain 7: Assumptions & Dependencies** (from /assess phase)
- Extract the explicit assumptions recorded during assessment
- These are assumptions about market conditions, competitor behavior, customer adoption, regulatory environment, etc.
- Example assumptions:
  - "TAM grows at 20% annually through 2028"
  - "Competitive entry occurs within 12 months of Series A close"
  - "Founding team has 15+ years combined enterprise software experience"
  - "Regulatory approval required but expected within 18 months"

**Gap Register: Critical Gaps** (from assessment findings)
- Identify gaps marked as "high-severity" or "high-uncertainty"
- For each gap, extract the assumption underlying the gap assessment
- Example: Gap = "Limited TAM validation with enterprise customers" → Underlying assumption = "Enterprise segment adoption will match SMB adoption curve"
- Example: Gap = "Undefined go-to-market strategy" → Underlying assumption = "Direct sales will be viable channel in Year 1"

**Research Conflicts & Uncertain Areas**
- Identify areas where assessment evidence was contradictory or scarce
- Extract the assumption that would bridge the conflict
- Example: One customer reference said "6-month sales cycle" while industry benchmarks said "3-month"; underlying assumption = "This startup's sales cycle = TBD, currently using 4-month midpoint"

### Assumption Selection Criteria

Select assumptions for scenario construction that meet ALL of these criteria:

1. **High impact on composite readiness score**: Changing the assumption ±20% causes ≥3 point shift in composite score
2. **High residual uncertainty**: Assessment confidence in the assumption is <75% (flagged as gap or research conflict)
3. **Cross-domain relevance**: The assumption affects ≥2 domains (not siloed to single domain)
4. **Actionable for scenarios**: The assumption has clear optimistic and pessimistic variants

**Example: TAM growth rate**
- Impact: High (affects market opportunity domain, fit-to-purpose, business model viability)
- Uncertainty: High (depends on market macro trends outside startup control)
- Cross-domain: Yes (affects Domains 2, 3, 4)
- Actionable: Yes (variants: 8%, 20%, 35%)
- **Selection: INCLUDE**

**Example: Founder's previous exit experience**
- Impact: Moderate (affects operations/team capability)
- Uncertainty: None (factually determined, public record)
- Cross-domain: No (only operations)
- Actionable: No (binary fact, not a range)
- **Selection: EXCLUDE**

### Documented Assumption List

Create a structured list:

```
EXTRACTED KEY ASSUMPTIONS FOR SCENARIO CONSTRUCTION

1. TAM GROWTH RATE
   Source: Domain 7 assumptions, market research conflicts
   Current assumption: 20% annually through 2028
   Certainty: 65% (moderate; depends on macro trends)
   Domains affected: Market Opportunity (Domain 2), Product-Market Fit (Domain 3), Business Model (Domain 4)
   Impact estimate: ±20% on assumption = ±4 point shift in composite score
   Actionable range: 8% (pessimistic) — 20% (base) — 35% (optimistic)

2. COMPETITIVE RESPONSE TIME
   Source: Domain 7 assumptions, industry benchmarking
   Current assumption: 12 months to meaningful competitive entry
   Certainty: 55% (low; depends on competitor strategic priorities)
   Domains affected: Market Opportunity (Domain 2), Fit-to-Purpose (Domain 1)
   Impact estimate: ±20% on assumption = ±3 point shift in composite score
   Actionable range: 3 months (pessimistic) — 12 months (base) — 24 months (optimistic)

3. [Additional assumptions...]
```

---

## 2. Scenario Definition: Bull, Base, Bear Construction

### Base Case Scenario

**Definition:** The base case is locked from the /assess phase. Do not modify or reinterpret base case assumptions.

**Procedure:**
1. Extract the exact assumptions used during /assess phase scoring
2. Record in scenario definition: "These are the assumptions that produced the initial [Determination] determination"
3. Do not second-guess or improve base case assumptions
4. Lock base case as reference point for Bull and Bear variants

**Base Case Documentation:**
```
BASE CASE SCENARIO

Locked from: /assess phase, Domain 7 Assumptions record
Determination from base case: [GO / CONDITIONAL GO / CONDITIONAL HOLD / NO-GO]

Key assumptions:
  - TAM growth rate: 20% annually
  - Competitive response time: 12 months
  - Product-market fit: 40% of target segment shows strong signals
  - [Additional assumptions...]

Composite readiness score (base case): [Score]
Fit-to-purpose (base case): Adequate / Inadequate
Determination (base case): [Determination]

Status: LOCKED - Do not modify for scenario analysis
```

### Bull Case Scenario Construction

**Definition:** Optimistic but plausible scenario where favorable assumptions hold true.

**Guiding principle:** Bull case should reflect genuine upside opportunity that is within the realm of plausibility given current evidence. Not fantasy, but a realistic best-case.

**Construction process:**

**Step 1: Identify optimistic assumption variants**

For each key assumption, define the High variant:

| Assumption | Base | Bull Case | Narrative Justification |
|---|---|---|---|
| TAM growth | 20% annually | 35% annually | Market trends support accelerating adoption; recent analyst reports project enterprise spending growth at 30%+ CAGR in this category |
| Competitive response | 12 months | 24 months | Incumbents are distracted by legacy platform migration; new entrant window extends beyond initial expectation |
| Product-market fit | 40% of segment | 60% of segment | Beta feedback is stronger than baseline, 6-month NPS projection supports 55%+ fit signals |
| Sales cycle | 6 months average | 4 months average | Initial customer cohort is more sophisticated, shorter procurement timelines |
| [More assumptions...] | Base | Optimistic | [Narrative support] |

**Step 2: Construct coherent narrative**

Ensure all bull case assumptions work together logically. For example:
- "Accelerating TAM growth + delayed competitor response + strong product-market fit" ✓ Coherent
- "Accelerating TAM growth + delayed competitor response + weak product-market fit" ✗ Incoherent (why would TAM accelerate if product doesn't resonate?)

**Bull case narrative:**
```
BULL CASE SCENARIO

Narrative: Industry tailwinds accelerate; customer adoption is faster and broader than expected; competitive response is delayed by incumbent distraction.

Key assumption shifts:
  - TAM growth: 35% annually (vs. Base 20%)
  - Competitive response: 24 months (vs. Base 12)
  - Product-market fit: 60% of segment (vs. Base 40%)
  - Enterprise adoption velocity: 2x faster than SMB (vs. Base parity)
  - Founding team execution: Exceeds plan by 20% (vs. Base on-plan)

Supporting evidence for bull case:
  - Recent analyst reports project 30%+ CAGR in this market segment
  - Customer feedback indicates stronger-than-expected product positioning
  - Incumbent vendors' recent strategic announcements suggest delayed aggressive response

Coherence check:
  - Do all assumptions reinforce each other? YES
  - Is the narrative grounded in current evidence? YES
  - Could this plausibly occur? YES (probability: ~25% in this assessment view)
```

**Step 3: Document assumption values clearly**

Create a bull case assumption table that can be used for re-scoring.

### Bear Case Scenario Construction

**Definition:** Pessimistic but plausible scenario where challenging assumptions materialize.

**Guiding principle:** Bear case should reflect genuine downside risk that is within the realm of plausibility given current evidence and identified gaps. Not worst-case catastrophe, but a realistic adverse scenario.

**Construction process:**

**Step 1: Identify pessimistic assumption variants**

For each key assumption, define the Low variant. Often these are derived from gaps and concerns flagged during /assess:

| Assumption | Base | Bear Case | Narrative Justification |
|---|---|---|---|
| TAM growth | 20% annually | 8% annually | Market macro headwinds; enterprise spending freezes due to recession signals; adoption slower than expected |
| Competitive response | 12 months | 3 months | Incumbent recognizes threat early; launches aggressive competitive response immediately |
| Product-market fit | 40% of segment | 20% of segment | Beta feedback reveals integration challenges; adoption signals weaker among target enterprise segment |
| Sales cycle | 6 months average | 10 months average | Enterprise procurement elongates due to compliance requirements; complex RFP processes |
| [More assumptions...] | Base | Pessimistic | [Narrative support] |

**Step 2: Construct coherent narrative**

Ensure all bear case assumptions work together logically:
- "Slowing TAM growth + fast competitor response + weak product-market fit" ✓ Coherent
- "Slowing TAM growth + 3-month competitor response + founder execution exceeds plan" ✗ Incoherent (why would execution excel under hostile conditions?)

**Bear case narrative:**
```
BEAR CASE SCENARIO

Narrative: Market headwinds slow adoption; competitive response is faster and more aggressive than expected; product-market fit validation lags early expectations.

Key assumption shifts:
  - TAM growth: 8% annually (vs. Base 20%)
  - Competitive response: 3 months (vs. Base 12)
  - Product-market fit: 20% of segment (vs. Base 40%)
  - Enterprise adoption velocity: 0.5x vs. SMB (slower enterprise adoption)
  - Sales cycle elongation: 10 months average (vs. Base 6)

Supporting evidence for bear case:
  - Gap register flagged "limited TAM validation with enterprise customers"
  - Gap register flagged "undefined go-to-market strategy"
  - Recent market macro signals suggest enterprise spending caution
  - Competitor response time assumption is uncertain (±9 month range)

Coherence check:
  - Do all assumptions reinforce each other? YES
  - Is the narrative grounded in current evidence? YES
  - Could this plausibly occur? YES (probability: ~25% in this assessment view)
```

**Step 3: Document assumption values clearly**

Create a bear case assumption table that can be used for re-scoring.

---

## 3. Score Re-Calculation Procedure Under Each Scenario

### Setup: Assessment Rubric Reference

**Before re-scoring**, ensure you have the complete assessment rubric available:
- Domain scoring rubric (0–100 per domain with clear criteria at 0, 25, 50, 75, 100 levels)
- Fit-to-purpose evaluation criteria (what makes a business "adequate" fit vs. "inadequate")
- Determination mapping table (score ranges to determinations)

### Re-Scoring Process for Single Scenario

**For each scenario (Bull, Base, Bear):**

**Step 1: Apply scenario assumptions to all seven domains**

Create a domain evaluation matrix:

| Domain | Name | Base Case Score | Scenario Assumptions Applied | Adjusted Assessment |
|---|---|---|---|---|
| 1 | Fit-to-Purpose | 75 | [Scenario-specific fit assumptions] | [Reassess under scenario] |
| 2 | Market Opportunity | 68 | TAM growth 35%, competitor delay 24mo | [Reassess: Market TAM is larger, time window longer → potential score: 78] |
| 3 | Product-Market Fit | 62 | PMF validation 60% of segment | [Reassess: Stronger signals → potential score: 72] |
| 4 | Business Model Viability | 66 | Faster adoption, shorter sales cycle | [Reassess: Unit economics improve → potential score: 75] |
| 5 | Operations Readiness | 70 | Team execution +20% | [Reassess: Better execution trajectory → potential score: 75] |
| 6 | Competitive Position | 64 | Competitor delay 24mo | [Reassess: Extended market lead → potential score: 73] |
| 7 | Key Assumptions | [Evaluated within domain scores] | [Scenario assumptions by definition] | [Reflected in domain scores above] |

**Step 2: Re-score each domain under scenario**

For each domain, apply the assessment rubric using scenario assumptions:

**Example: Domain 2 (Market Opportunity) under Bull Case**

Rubric:
- 0–20: Market is non-existent or contracting; TAM < $100M; competition eliminates opportunity within 2 years
- 21–40: Market exists but fragmented; TAM $100–500M; significant competition within 3–5 years
- 41–60: Market is identifiable; TAM $500M–2B; competition expected within 12–18 months
- 61–80: Large, growing market; TAM $2–5B; competitive window 18–36 months; clear customer segments
- 81–100: Large, rapidly growing market; TAM $5B+; competitive window 36+ months; well-defined segments and channels

**Bull Case Scenario:**
- TAM growth: 35% annually (vs. Base 20%) → Affects TAM sizing upward
- Competitor response: 24 months (vs. Base 12) → Extends competitive window
- Market analyst coverage supports accelerating adoption

**Re-scoring:**
- Base TAM estimate (Domain 2): $2.5B → Bull case TAM: $2.5B × 1.75 (1.35^2 projection) ≈ $4.4B
- Competitive window: 24 months (extends from base 12) → Moves into "18–36 month" bracket
- Market growth is accelerating rather than stable
- **New Domain 2 score under bull: 78** (up from base 68)

**Example: Domain 3 (Product-Market Fit) under Bull Case**

Rubric:
- 0–20: No customer validation; product doesn't solve identified problem; high churn
- 21–40: Early signals from friendly customers; unclear problem-solution fit; significant churn likely
- 41–60: Moderate validation from target segment; core functionality resonates; addressable repeat customers identified
- 61–80: Strong validation from target segment; customers report measurable value; engagement metrics healthy; clear repeat customer base
- 81–100: Exceptional product-market fit across multiple segments; customers would recruit others; exceptional engagement; clear path to sustained growth

**Bull Case Scenario:**
- Product-market fit validation: 60% of target segment shows strong fit signals (vs. Base 40%)
- Beta feedback stronger than baseline
- Enterprise adoption velocity accelerating

**Re-scoring:**
- Base assessment (Domain 3): 62 (moderate to strong validation, but concentrated in SMB)
- Bull scenario: 60% of enterprise segment now showing signals (vs. base 40% SMB) → Moves to "strong validation across multiple segments"
- **New Domain 3 score under bull: 72** (up from base 62)

**Continue for all seven domains under bull case scenario**

### Step 3: Calculate Composite Readiness Score Under Scenario

```
COMPOSITE READINESS (BULL CASE SCENARIO)

Domain 1 (Fit-to-Purpose): 75
Domain 2 (Market Opportunity): 78
Domain 3 (Product-Market Fit): 72
Domain 4 (Business Model Viability): 75
Domain 5 (Operations Readiness): 75
Domain 6 (Competitive Position): 73
Domain 7 (Key Assumptions): [Embedded in domain scores] 

Composite Readiness = (75 + 78 + 72 + 75 + 75 + 73) / 6 = 438 / 6 = 73

Rounded Composite: 73
```

**Important:** Do not average Domain 7 as a separate score; Domain 7 is evaluated by whether the key assumptions are reasonable, not scored independently.

### Step 4: Evaluate Fit-to-Purpose Under Scenario

**Fit-to-Purpose Definition:**
- Adequate: Business model, product positioning, and growth plan align with startup fund requirements and investor return expectations
- Inadequate: Misalignment that would prevent effective deployment of investor capital

**Re-evaluation:**

**Base Case Fit-to-Purpose:** Adequate
- Reasoning: Series A valuation target of $X aligns with growth trajectory; capital deployment plan matches investor expectations

**Bull Case Fit-to-Purpose:** Adequate (likely stronger)
- Reasoning under bull scenario: Accelerated growth + stronger PMF means capital deployment is MORE efficient; returns accelerate
- **Fit-to-Purpose: Adequate** (maintained; possibly enhanced)

**Bear Case Fit-to-Purpose:** Adequate (possibly challenged)
- Reasoning under bear scenario: Slower adoption + longer sales cycles means capital deployment takes longer to yield returns
- Question: Does the investor thesis still work if TAM growth = 8% and product-market fit = 20%?
- If YES → **Fit-to-Purpose: Adequate**
- If NO (capital deployment becomes inefficient, returns horizon extends to unacceptable level) → **Fit-to-Purpose: Inadequate**

### Step 5: Combine Readiness + Fit-to-Purpose → Determination

**Determination Mapping Table:**

| Readiness Range | Fit Adequate | Fit Inadequate |
|---|---|---|
| 75–100 | GO | CONDITIONAL GO |
| 55–74 | CONDITIONAL GO | CONDITIONAL HOLD |
| 35–54 | CONDITIONAL HOLD | CONDITIONAL HOLD |
| Below 35 | NO-GO | NO-GO |

**Example:**
- Bull case composite readiness: 73
- Bull case fit-to-purpose: Adequate
- **Bull case determination: CONDITIONAL GO**

### Full Re-Scoring Example: Three Scenarios

| Scenario | Domain 1 | Domain 2 | Domain 3 | Domain 4 | Domain 5 | Domain 6 | Composite | Fit | Determination |
|---|---|---|---|---|---|---|---|---|---|
| Bull | 75 | 78 | 72 | 75 | 75 | 73 | 73 | Adequate | CONDITIONAL GO |
| Base | 75 | 68 | 62 | 66 | 70 | 64 | 68 | Adequate | CONDITIONAL GO |
| Bear | 68 | 52 | 48 | 55 | 62 | 52 | 56 | Adequate | CONDITIONAL GO |

---

## 4. Robustness Classification from Scenario Spread

### Spread Analysis

**Determination spread = maximum determination level - minimum determination level**

Calculate spread by assigning values:
- GO = 4
- CONDITIONAL GO = 3
- CONDITIONAL HOLD = 2
- NO-GO = 1

**Example from table above:**
- Bull: CONDITIONAL GO = 3
- Base: CONDITIONAL GO = 3
- Bear: CONDITIONAL GO = 3
- **Spread = 3 - 3 = 0 levels**

### Robustness Classification Criteria

**Robust** — Spread = 0 (all scenarios produce identical determination)

OR Spread = 1 level AND base case holds (doesn't deteriorate to minimum outcome)

Examples:
- Bull=GO(4), Base=GO(4), Bear=GO(4) → Spread 0 → Robust GO
- Bull=CONDITIONAL GO(3), Base=CONDITIONAL GO(3), Bear=CONDITIONAL HOLD(2) → Spread 1, Base holds → Robust CONDITIONAL GO
- Bull=GO(4), Base=CONDITIONAL GO(3), Bear=CONDITIONAL GO(3) → Spread 1, Base not at minimum → Robust CONDITIONAL GO

**Moderately Robust** — Spread = 2 levels AND base case holds (isn't worst-case in its range)

OR Spread = 1 level AND base case is at minimum (deteriorates in one direction)

Examples:
- Bull=GO(4), Base=CONDITIONAL GO(3), Bear=CONDITIONAL HOLD(2) → Spread 2, Base holds middle → Moderately Robust
- Bull=CONDITIONAL GO(3), Base=GO(4), Bear=CONDITIONAL GO(3) → Spread 1, but asymmetric (Bull worse than Base) → Assess as Moderately Robust (fragile upside)
- Bull=NO-GO(1), Base=CONDITIONAL HOLD(2), Bear=CONDITIONAL HOLD(2) → Spread 1, Base not minimum → Moderately Robust

**Fragile** — Spread ≥ 3 levels

OR Spread = 2 levels AND base case is at or near extreme (either best or worst outcome in spread)

OR Base case determination is not representative of scenario range (outlier determination)

Examples:
- Bull=GO(4), Base=CONDITIONAL GO(3), Bear=NO-GO(1) → Spread 3 → Fragile
- Bull=GO(4), Base=GO(4), Bear=CONDITIONAL HOLD(2) → Spread 2, Base at best → Fragile (lacks downside protection)
- Bull=CONDITIONAL HOLD(2), Base=GO(4), Bear=CONDITIONAL HOLD(2) → Spread 2, Base is outlier → Fragile
- Bull=CONDITIONAL GO(3), Base=CONDITIONAL HOLD(2), Bear=CONDITIONAL HOLD(2) → Spread 1, but base is worst → Fragile

### Robustness Reasoning Documentation

Document the logic:

```
ROBUSTNESS CLASSIFICATION: MODERATELY ROBUST

Scenario outcomes:
  Bull Case: CONDITIONAL GO (composite 73)
  Base Case: CONDITIONAL GO (composite 68)
  Bear Case: CONDITIONAL GO (composite 56)

Spread analysis: CONDITIONAL GO across all scenarios (spread = 0 levels)

Classification rationale:
  - Determination is identical across all three scenarios (Bull, Base, Bear)
  - Base case is stable; neither best nor worst outcome in scenario set
  - Composite readiness shows sensitivity to assumptions (73 to 56 = 17-point range)
  - Fit-to-purpose remains adequate across all scenarios
  
Result: Despite composite score sensitivity, determination is ROBUST across scenario range.
```

---

## 5. Scenario Analysis Output Format

### Summary Table

```
SCENARIO ANALYSIS RESULTS

| Scenario | Key Assumption Adjustments | Composite Score | Fit | Determination |
|----------|---------------------------|-----------------|-------|---|
| Bull | TAM growth 35%, competitor 24mo, PMF 60% | 73 | Adequate | CONDITIONAL GO |
| Base | TAM growth 20%, competitor 12mo, PMF 40% | 68 | Adequate | CONDITIONAL GO |
| Bear | TAM growth 8%, competitor 3mo, PMF 20% | 56 | Adequate | CONDITIONAL GO |

Determination Range: CONDITIONAL GO to CONDITIONAL GO (spread = 0 levels)
Robustness Classification: ROBUST
```

### Detailed Results Section

```
SCENARIO ANALYSIS: DETAILED FINDINGS

1. BULL CASE SCENARIO
   Narrative: Industry tailwinds accelerate; customer adoption faster than expected; competitive response delayed.
   
   Key assumption shifts from base:
   - TAM growth: 35% annually (was 20%)
   - Competitive response time: 24 months (was 12)
   - Product-market fit: 60% segment validation (was 40%)
   
   Domain scoring under bull case:
   | Domain | Base | Bull | Change | Rationale |
   |--------|------|------|--------|-----------|
   | Market Opportunity | 68 | 78 | +10 | Larger TAM, extended competitive window |
   | Product-Market Fit | 62 | 72 | +10 | Stronger PMF signals across segment |
   | Business Model | 66 | 75 | +9 | Better unit economics from faster adoption |
   | [Other domains...] | ... | ... | ... | ... |
   
   Composite readiness (bull): 73
   Fit-to-purpose (bull): Adequate
   Determination (bull): CONDITIONAL GO

2. BASE CASE SCENARIO
   [Locked from /assess phase - do not modify]
   
   Composite readiness (base): 68
   Fit-to-purpose (base): Adequate
   Determination (base): CONDITIONAL GO

3. BEAR CASE SCENARIO
   Narrative: Market headwinds slow adoption; competitive response aggressive; product-market fit validation lags.
   
   Key assumption shifts from base:
   - TAM growth: 8% annually (was 20%)
   - Competitive response time: 3 months (was 12)
   - Product-market fit: 20% segment validation (was 40%)
   
   Domain scoring under bear case:
   | Domain | Base | Bear | Change | Rationale |
   |--------|------|------|--------|-----------|
   | Market Opportunity | 68 | 52 | -16 | Smaller TAM growth, compressed competitive window |
   | Product-Market Fit | 62 | 48 | -14 | Weaker PMF signals; adoption slower |
   | Business Model | 66 | 55 | -11 | Deteriorated unit economics, longer payback |
   | [Other domains...] | ... | ... | ... | ... |
   
   Composite readiness (bear): 56
   Fit-to-purpose (bear): Adequate
   Determination (bear): CONDITIONAL GO
```

### Key Sensitivities Summary

```
KEY SENSITIVITIES IDENTIFIED

1. TAM GROWTH RATE
   - Range tested: 8% (bear) to 35% (bull)
   - Impact on determination: None (determination holds across range)
   - Impact on composite score: 68 → 56 = -12 points under bear; 68 → 73 = +5 points under bull
   - Interpretation: TAM growth is high-sensitivity variable, but doesn't cross determination threshold

2. COMPETITIVE RESPONSE TIME
   - Range tested: 3 months (bear) to 24 months (bull)
   - Impact on determination: None (determination holds across range)
   - Impact on composite score: Part of bull case +5 point gain; part of bear case -12 point loss
   - Interpretation: Competitive response time drives market opportunity scoring but not determination flip

3. PRODUCT-MARKET FIT VALIDATION
   - Range tested: 20% segment (bear) to 60% segment (bull)
   - Impact on determination: None (determination holds across range)
   - Impact on composite score: Part of bull case +5 gain; part of bear case -12 loss
   - Interpretation: PMF validation is critical sensitivity; if actual validation ≤20%, bear case scenario becomes reality
```

### Analysis Notes & Interpretation

```
SCENARIO ANALYSIS NARRATIVE

Determination Stability:
The CONDITIONAL GO determination is ROBUST across all three scenarios. Even under pessimistic 
assumptions (market growth 8%, competitor 3-month response, PMF 20%), the startup still reaches 
CONDITIONAL GO (composite 56, adequate fit).

Conservative Upside:
Under optimistic conditions (TAM growth 35%, competitor 24-month response, PMF 60%), the 
determination rises to CONDITIONAL GO but does NOT reach GO (composite 73). This suggests that 
while market tailwinds help, they do not overcome underlying readiness gaps in operations or 
business model execution that prevent full GO status.

Key Vulnerabilities:
The scenario analysis reveals two key sensitivities that don't flip determination but significantly 
affect composite score:
1. TAM growth (17-point swing): Market macro trends heavily influence upside
2. Product-market fit validation (14-point swing): If actual PMF signals lag optimistic assumptions, 
   composite score drops into CONDITIONAL HOLD range

Fit-to-Purpose Stability:
Fit-to-purpose remains adequate across all scenarios. Capital deployment efficiency may vary 
(bull case = highly efficient; bear case = slower returns), but investor thesis holds even under 
adverse conditions.

Recommendation:
Sensitivity analysis supports the CONDITIONAL GO determination with confidence. The startup can 
proceed with conditional terms, understanding that determination is stable but composite score is 
sensitive to market growth and product-market fit validation. Priority monitoring: market adoption 
velocity and competitive response timing.
```

---

## 6. Full Scenario Analysis Example: Series A SaaS Startup

### Scenario Setup

**Startup:** CloudAnalytics (Series A AI/analytics SaaS)

**Base Case Assessment (locked):**
- Composite readiness: 68
- Determination: CONDITIONAL GO
- Conditions: Validate product-market fit with enterprise customers; finalize go-to-market strategy

**Key Assumptions Identified:**
1. TAM growth rate: 20% annually
2. Competitive response time: 12 months
3. Product-market fit: 40% of target segment shows strong signals
4. Enterprise sales cycle: 6 months average
5. Founding team execution: On-plan (no acceleration or deceleration)

---

### Bull Case Construction

**Scenario Narrative:**
Industry AI/analytics adoption accelerating beyond analyst projections; CloudAnalytics' unique positioning gives extended competitive window; beta customer feedback stronger than anticipated.

**Assumption Adjustments:**

| Assumption | Base | Bull Case | Justification |
|---|---|---|---|
| TAM growth rate | 20% annually | 35% annually | Recent Gartner report projects 32%+ CAGR; analyst upgrades accelerating adoption forecasts |
| Competitive response | 12 months | 24 months | Incumbent Tableau/Looker focused on platform consolidation; window extends |
| PMF validation | 40% of segment | 60% of segment | Beta cohort showing 8.2 NPS (vs. expected 6.5); 70% adoption in target enterprise accounts |
| Enterprise sales cycle | 6 months | 4 months | Enterprise sponsors more sophisticated; lower procurement friction; RFP processes streamlined |
| Team execution | On-plan | +15% | Hiring pipeline ahead of plan; key VP engineering recruited successfully |

**Bull Case Domains:**

| Domain | Base | Bull | Rationale |
|---|---|---|---|
| 1. Fit-to-Purpose | 75 | 78 | Accelerated TAM growth means faster capital deployment; returns timeline compressed |
| 2. Market Opportunity | 68 | 82 | TAM expands to $4.5B+ (from base $2.5B); 24-month competitive window extends opportunity |
| 3. Product-Market Fit | 62 | 74 | 60% enterprise segment validation (vs. base 40% SMB) moves to strong multi-segment fit |
| 4. Business Model | 66 | 76 | Shorter sales cycles and faster adoption improve unit economics and payback period |
| 5. Operations Readiness | 70 | 79 | +15% team execution; hiring ahead of plan; key gap (VP Eng) closed |
| 6. Competitive Position | 64 | 79 | 24-month window gives runway for product differentiation and market share building |

**Bull Case Composite:** (78 + 82 + 74 + 76 + 79 + 79) / 6 = 468 / 6 = **78**

**Bull Case Determination:** GO (readiness 78, adequate fit)

---

### Bear Case Construction

**Scenario Narrative:**
Macroeconomic headwinds slow enterprise spending; competitive entrant (well-funded) responds faster than expected; product-market fit validation concentrates in SMB (lower LTV); enterprise adoption lags.

**Assumption Adjustments:**

| Assumption | Base | Bear Case | Justification |
|---|---|---|---|
| TAM growth rate | 20% annually | 7% annually | Enterprise spending slowdown signals; analyst downgrades amid recession concerns; adoption delays |
| Competitive response | 12 months | 4 months | Well-funded competitor (e.g., elastic.co) enters market aggressively; launches comparable product |
| PMF validation | 40% of segment | 22% of segment | Gap register flagged "limited enterprise validation"; beta feedback weaker than expected; churn signals appear |
| Enterprise sales cycle | 6 months | 9 months | Enterprise procurement caution; RFP processes elongate; compliance reviews delay deals |
| Team execution | On-plan | -10% | Key hire delays; market uncertainty affects hiring pipeline; execution timeline slips |

**Bear Case Domains:**

| Domain | Base | Bear | Rationale |
|---|---|---|---|
| 1. Fit-to-Purpose | 75 | 68 | Slower TAM growth means capital deployment less efficient; extended returns timeline challenges investor thesis |
| 2. Market Opportunity | 68 | 48 | TAM contracts to $1.8B; 4-month competitive window compresses opportunity materially |
| 3. Product-Market Fit | 62 | 44 | 22% segment validation (vs. base 40%) suggests product resonates with SMB only; enterprise fit unclear |
| 4. Business Model | 66 | 52 | Longer sales cycles and slower adoption worsen unit economics and extend CAC payback |
| 5. Operations Readiness | 70 | 60 | -10% execution impact; hiring pipeline delays; execution risks crystallize |
| 6. Competitive Position | 64 | 48 | 4-month window insufficient for differentiation; competitive positioning vulnerable |

**Bear Case Composite:** (68 + 48 + 44 + 52 + 60 + 48) / 6 = 320 / 6 = **53**

**Bear Case Fit-to-Purpose Reassessment:**
- Question: Can investor still deploy capital efficiently and expect returns if TAM = $1.8B and growth = 7%?
- Analysis: At 7% growth, TAM size becomes constraining factor. Series A deployment would need to target SMB segment (which has shown PMF), but SMB CAC payback is longer.
- Conclusion: **Fit-to-purpose = INADEQUATE under bear case** (capital deployment thesis breaks down)

**Bear Case Determination:** CONDITIONAL HOLD (readiness 53, inadequate fit)

---

### Full Scenario Results Table

| Scenario | Composite Score | Fit-to-Purpose | Determination |
|---|---|---|---|
| Bull | 78 | Adequate | GO |
| Base | 68 | Adequate | CONDITIONAL GO |
| Bear | 53 | Inadequate | CONDITIONAL HOLD |

**Determination Range:** CONDITIONAL HOLD (2) to GO (4) = **Spread 2 levels**

---

### Robustness Classification

**Spread = 2 levels (CONDITIONAL HOLD to GO)**
**Base case = CONDITIONAL GO (middle of range)**
**Base case = NOT at extreme (good; not outlier)**

**Classification: MODERATELY ROBUST**

**Reasoning:**
- Determination spread is 2 levels, which would normally suggest fragility
- However, base case CONDITIONAL GO sits squarely in the middle of the range (not best or worst)
- This positioning indicates the determination is stable under moderate conditions but sensitive to extremes
- Upside to GO is achievable (requires acceleration); downside to CONDITIONAL HOLD is plausible (requires slowdown)
- Overall: Determination is robust enough for Series A decision-making, but monitoring of key assumptions is critical

---

### Key Sensitivities Analysis

```
KEY SENSITIVITIES

1. TAM GROWTH RATE (Highest sensitivity)
   - Bull case: 35% → Composite +10, determination GO
   - Base case: 20% → Composite 68, determination CONDITIONAL GO
   - Bear case: 7% → Composite -15, determination CONDITIONAL HOLD
   - Implication: TAM growth is the primary driver of determination spread. Market macro environment is critical monitoring variable.

2. COMPETITIVE RESPONSE TIME (High sensitivity)
   - Bull case: 24 months → Extends competitive window, composite +11
   - Bear case: 4 months → Compresses opportunity, composite -16
   - Implication: Competitive response timeline significantly affects market opportunity and positioning. Early signals of competitor entry are critical early warning.

3. PRODUCT-MARKET FIT VALIDATION (High sensitivity)
   - Bull case: 60% segment → Composite +6 (multi-segment fit validated)
   - Bear case: 22% segment → Composite -9 (segmentation and positioning questioned)
   - Implication: Enterprise PMF validation is critical. If actual validation lags assumptions, determination deteriorates significantly.

4. ENTERPRISE SALES CYCLE LENGTH (Moderate sensitivity)
   - Bull case: 4 months → Faster capital deployment
   - Bear case: 9 months → Slower deployment, extended payback
   - Implication: Sales cycle impacts business model timing but not determination threshold. Monitoring sales pipeline velocity is important for execution tracking.

5. FOUNDING TEAM EXECUTION (Lower sensitivity)
   - Bull case: +15% acceleration → Composite +9
   - Bear case: -10% slowdown → Composite -10
   - Implication: Team execution is important but not primary determination driver. Determination assumes on-plan execution; both acceleration and deceleration affect probability of success.
```

---

### Scenario Analysis Conclusion

CloudAnalytics' CONDITIONAL GO determination is **moderately robust**. The company can proceed with Series A investment under conditional terms (validate enterprise PMF, finalize go-to-market strategy). However:

- **Upside opportunity**: If market tailwinds continue and enterprise PMF validates strongly, determination could flip to GO within 12 months
- **Downside risk**: If market growth stalls and competitive response accelerates, determination could deteriorate to CONDITIONAL HOLD; this risk is real given macro environment uncertainty
- **Critical monitoring**: TAM growth rate and competitive activity should be tracked closely; enterprise PMF validation (through beta cohort expansion) should be prioritized
- **Path B**: Deal terms negotiation is appropriate given CONDITIONAL GO + moderately robust sensitivity

---

**End of scenario-analysis.md**
