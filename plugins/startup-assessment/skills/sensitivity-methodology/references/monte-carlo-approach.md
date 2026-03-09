# Monte Carlo Approach Reference (Analytical)

## Full Monte Carlo Execution Procedure

This reference provides the complete procedure for executing Monte Carlo analysis (analytical rather than computational) as a sensitivity methodology.

---

## 1. Conceptual Basis

### What Is Monte Carlo Analysis in This Context?

Monte Carlo analysis quantifies the probability distribution of outcomes (determinations) by combining key assumptions across their ranges and weighting the combinations probabilistically. Instead of relying on a single "base case," it reflects the inherent uncertainty in assumptions and computes the likelihood of each possible determination.

### Analytical vs. Computational Approach

**Computational Monte Carlo (Statistical Software):**
- Runs 10,000+ simulations with randomly sampled assumption values
- Requires software and historical data for probability distributions
- Produces precise confidence intervals and probability distributions
- Requires technical expertise and execution time

**Analytical Monte Carlo (This Skill):**
- Identifies 5–8 key assumptions and defines Low/Mid/High ranges
- Creates 8 representative scenarios covering the assumption space
- Weights scenarios probabilistically and calculates composite outcomes
- Produces order-of-magnitude probability distribution
- Can be executed by assessment experts without software

### Why Analytical Monte Carlo?

Analytical Monte Carlo is appropriate for startup assessment because:
1. **Sample size constraint** — Limited historical data available; statistical methods unreliable
2. **Expert judgment** — Assessment findings are based on expert interpretation of evidence, not large datasets
3. **Scenario-based reasoning** — Sensitivity naturally decomposes into assumption scenarios
4. **Execution speed** — Analytical method can be completed in hours vs. days for software-based approach
5. **Transparency** — All assumptions and calculations are visible and auditable

---

## 2. Key Assumption Identification

### Identifying Candidates

Start by listing all assumptions recorded in Domain 7 and flagged gaps from assessment:

**Domain 7 Assumptions:**
- TAM growth rate: 20% annually
- Competitive response time: 12 months
- Product-market fit validation: 40% of segment
- Enterprise sales cycle: 6 months
- Founding team execution: On-plan
- Regulatory approval timeline: 18 months
- Sales channel strategy: Direct sales with 3 FTE Year 1
- Customer churn rate: 3% monthly
- [Additional assumptions...]

**Flagged Gaps (High-Severity, High-Uncertainty):**
- Gap: "Limited TAM validation with enterprise customers" → Underlying assumption: Enterprise adoption velocity = SMB adoption velocity
- Gap: "Undefined go-to-market strategy" → Underlying assumption: Direct sales is viable channel
- Gap: "Regulatory approval unclear" → Underlying assumption: Approval achievable within 18 months

### Selection Criteria

Select **5–8 assumptions** that meet ALL of these criteria:

1. **High impact on composite readiness score**
   - Changing the assumption by ±20% causes ≥3 point shift in composite score
   - Example: If TAM grows at 35% instead of 20%, does composite move ≥3 points? YES → Include

2. **High residual uncertainty**
   - Assessment confidence in the assumption is <75% (marked as gap or research conflict)
   - Example: Do we have strong evidence for 12-month competitive response time? NO (marked as gap) → Include

3. **Cross-domain relevance**
   - The assumption affects ≥2 domains (not siloed to single domain)
   - Example: Does TAM growth affect just Market Opportunity, or also Business Model and Fit-to-Purpose? Both → Include

4. **Actionable for probability weighting**
   - The assumption has clear variants (Low/Mid/High) and expert can assign probabilities
   - Example: Can we estimate probability of 8% growth vs. 20% vs. 35%? YES → Include

### Documented Assumption List

Create a structured candidate list:

```
KEY ASSUMPTION CANDIDATES FOR MONTE CARLO

Assumption: TAM Growth Rate (Current: 20% annually)
  Impact on score: ≥3 points if ±20% variance ✓
  Uncertainty: 60% confidence ✓ (external market risk)
  Cross-domain: Market Opportunity, Business Model, Fit-to-Purpose ✓
  Actionable: Yes (8%, 20%, 35% variants clear) ✓
  Status: INCLUDE

Assumption: Competitive Response Time (Current: 12 months)
  Impact on score: ≥3 points ✓ (affects market opportunity + positioning)
  Uncertainty: 55% confidence ✓ (competitor behavior unpredictable)
  Cross-domain: Market Opportunity, Competitive Position ✓
  Actionable: Yes (3mo, 12mo, 24mo variants clear) ✓
  Status: INCLUDE

Assumption: Product-Market Fit Validation (Current: 40% segment)
  Impact on score: ≥3 points ✓ (core fit assessment)
  Uncertainty: 65% confidence ✓ (gap flagged; validation incomplete)
  Cross-domain: Product-Market Fit, Market Opportunity ✓
  Actionable: Yes (20%, 40%, 60% variants clear) ✓
  Status: INCLUDE

Assumption: Sales Cycle Length (Current: 6 months average)
  Impact on score: ≥2 points ✓ (affects business model, but secondary)
  Uncertainty: 70% confidence (~70% confident in 6-month estimate)
  Cross-domain: Business Model primarily (single domain)
  Actionable: Yes (4mo, 6mo, 9mo variants clear)
  Status: BORDERLINE — INCLUDE if filling 8-assumption quota

Assumption: Regulatory Approval Timeline (Current: 18 months)
  Impact on score: <2 points (affects fit-to-purpose minimally if approval achievable)
  Uncertainty: 50% confidence (highly uncertain)
  Cross-domain: Fit-to-Purpose only (single domain)
  Actionable: Yes (variants clear: 12mo, 18mo, 24mo)
  Status: EXCLUDE (single-domain impact too small)

Assumption: Founding Team Execution Capability (Current: On-plan)
  Impact on score: ≥3 points ✓ (affects operations, business model, competitive execution)
  Uncertainty: 65% confidence ✓ (team execution is uncertain)
  Cross-domain: Operations, Business Model, Competitive Position ✓
  Actionable: Yes (-20%, on-plan, +20% variants clear) ✓
  Status: INCLUDE

Assumption: Enterprise vs. SMB Adoption Velocity (Current: Parity)
  Impact on score: ≥3 points ✓ (affects product-market fit, business model)
  Uncertainty: 60% confidence ✓ (gap flagged: limited enterprise validation)
  Cross-domain: Product-Market Fit, Business Model ✓
  Actionable: Yes (SMB-only, parity, enterprise-faster variants clear) ✓
  Status: INCLUDE

SELECTED ASSUMPTIONS FOR MONTE CARLO (n=6):
  1. TAM Growth Rate
  2. Competitive Response Time
  3. Product-Market Fit Validation
  4. Enterprise Adoption Velocity
  5. Founding Team Execution
  6. Sales Cycle Length
```

---

## 3. Assumption Range Specification

For each selected assumption, define three values (Low/Mid/High) and assign probability weights.

### Step 1: Define Low, Mid, High Values

For each assumption, extract from assessment findings:

| Assumption | Low Variant (Pessimistic) | Mid Variant (Base) | High Variant (Optimistic) |
|---|---|---|---|
| **TAM Growth Rate** | 8% annually | 20% annually | 35% annually |
| **Competitor Response** | 3 months | 12 months | 24 months |
| **Product-Market Fit** | 20% of segment | 40% of segment | 60% of segment |
| **Enterprise Adoption** | 0.5x SMB velocity | Parity with SMB | 1.5x SMB velocity |
| **Team Execution** | -20% vs. plan | On-plan | +20% vs. plan |
| **Sales Cycle** | 9 months | 6 months | 4 months |

### Step 2: Assign Probability Weights

**Default approach:** Equal-tail distribution (Low=25%, Mid=50%, High=25%)
- Reflects moderate confidence in base case (50%)
- Acknowledges equal uncertainty on both sides (25% each tail)

**Adjusted approach:** Asymmetric distribution (if evidence suggests asymmetry)
- Example: If market analyst reports suggest upside bias, adjust to Low=20%, Mid=40%, High=40%
- Example: If regulatory barrier is unlikely but severe if occurs, adjust to Low=10%, Mid=80%, High=10%

```
PROBABILITY WEIGHTS FOR KEY ASSUMPTIONS

Assumption 1: TAM Growth Rate
  Low (8% annually): 25% probability
    Reasoning: Market macro headwinds plausible; recession signals present
  Mid (20% annually): 50% probability
    Reasoning: Base case from analyst reports; most likely scenario
  High (35% annually): 25% probability
    Reasoning: Upside from accelerating adoption; plausible but requires industry tailwinds
  Distribution: 25% / 50% / 25% (equal tails; symmetric)

Assumption 2: Competitive Response Time
  Low (3 months): 25% probability
    Reasoning: Fast-moving incumbents; well-funded; motivated by threat
  Mid (12 months): 50% probability
    Reasoning: Base case from competitive analysis; realistic given incumbent priorities
  High (24 months): 25% probability
    Reasoning: Incumbent distraction or delayed response; plausible but requires luck
  Distribution: 25% / 50% / 25% (symmetric)

Assumption 3: Product-Market Fit Validation
  Low (20% of segment): 25% probability
    Reasoning: Gap flagged; actual validation may lag expectations
  Mid (40% of segment): 50% probability
    Reasoning: Base case from beta feedback; moderate validation signals
  High (60% of segment): 25% probability
    Reasoning: Strong customer uptake; upside from favorable reception
  Distribution: 25% / 50% / 25% (symmetric)

[Continue for remaining assumptions...]

AGGREGATE PROBABILITY WEIGHTS:
  - All assumptions use 25% / 50% / 25% distribution (symmetric tails)
  - Reflects moderate confidence in base case with equal upside/downside risk
  - No evidence of systematic bias in any single assumption direction
```

### Step 3: Probability Weight Derivation Logic

**How to assign probabilities:**

1. **Start with base case probability = 50%**
   - This reflects the assessment's conclusion (base case is most likely)

2. **Assign tail probabilities based on evidence uncertainty:**
   - **Equal tails (25% / 50% / 25%)**: When uncertainty is symmetric (equal evidence for upside and downside)
   - **Asymmetric tails (High=35%, Mid=40%, Low=25%)**: When evidence favors one direction (e.g., market analyst consensus is optimistic)
   - **Extreme asymmetry (High=60%, Mid=30%, Low=10%)**: When evidence strongly favors one direction (e.g., regulatory approval is highly likely)

3. **Example: Competitive Response Time**
   - Base case = 12 months (from competitive analysis)
   - Evidence for shorter response (3 months):
     - Competitor press releases mention this market
     - Well-funded competitor with aggressive product roadmap
     - Incumbent R&D budgets are large
     - → Probability of 3-month response: 25% (plausible)
   - Evidence for longer response (24 months):
     - Incumbent is currently focused on platform consolidation
     - Switching costs in incumbent installed base are high
     - Our product is differentiated (delays response understanding)
     - → Probability of 24-month response: 25% (plausible)
   - Evidence for base case (12 months):
     - Industry benchmarks suggest 12–18 months
     - Competitive analysis assumes focused response
     - Most likely given available evidence
     - → Probability of 12-month response: 50%
   - **Distribution: 25% / 50% / 25%**

---

## 4. Iteration Methodology (Analytical)

### Overview

Rather than running 10,000 computational simulations, use analytical approach:

1. **Define 8 representative scenarios** covering the assumption space corners and center
2. **Calculate composite readiness** for each scenario
3. **Map to determination** for each scenario
4. **Weight outcomes** by scenario probability
5. **Aggregate** to get probability distribution across all 4 determinations

### Step 1: Define 8 Representative Scenarios

Create a scenario matrix covering the assumption space:

| Scenario | TAM | Competitor | PMF | Execution | Sales Cycle | Frequency |
|----------|---|---|---|---|---|---|
| 1 | Low | Low | Low | Low | Low | L^5 = 0.10% |
| 2 | Low | Low | Mid | Mid | Mid | L^2 × M^3 = 0.31% |
| 3 | Low | Mid | Mid | Mid | Mid | L × M^4 = 0.63% |
| 4 | Mid | Mid | Mid | Mid | Mid | M^5 = 3.13% |
| 5 | High | Mid | Mid | Mid | Mid | H × M^4 = 0.63% |
| 6 | High | High | Mid | Mid | Mid | H^2 × M^3 = 0.31% |
| 7 | High | High | High | High | High | H^5 = 0.10% |
| 8 | High | High | High | High | Mid | H^4 × M = 0.39% |

**Why 8 scenarios?**
- Corner scenarios (1, 4, 7) represent extremes
- Mixed scenarios (2, 3, 5, 6, 8) represent realistic combinations
- Captures main effects and interactions
- Tractable for manual calculation

**Scenario weighting:**
- Combine assumption probabilities multiplicatively
- Example: Scenario 1 (all Low) = 0.25^5 ≈ 0.001 = 0.1%
- Example: Scenario 4 (all Mid) = 0.50^5 ≈ 0.031 = 3.1%

### Step 2: Calculate Composite Readiness for Each Scenario

For each of the 8 scenarios:

1. **Apply scenario assumption values** to all 6-7 domains
2. **Re-score each domain** using assessment rubric
3. **Calculate composite readiness** = (sum of domain scores) / number of domains
4. **Determine fit-to-purpose** (adequate / inadequate)
5. **Map to determination** using readiness + fit table

**Example Scenario 4 (All Mid = Base Case):**

```
SCENARIO 4: ALL MID (BASE CASE)

Assumption values:
  TAM growth: 20% annually
  Competitor response: 12 months
  PMF validation: 40% of segment
  Enterprise adoption: Parity with SMB
  Team execution: On-plan
  Sales cycle: 6 months

Domain scoring:
  1. Fit-to-Purpose: 75 (capital deployment timeline adequate)
  2. Market Opportunity: 68 (TAM $2.5B, 12-month competitive window)
  3. Product-Market Fit: 62 (40% validation, moderate signals)
  4. Business Model: 66 (6-month sales cycle, unit economics modeled)
  5. Operations: 70 (on-plan execution, key hires pending)
  6. Competitive Position: 64 (standard competitive position)

Composite readiness: (75 + 68 + 62 + 66 + 70 + 64) / 6 = 405 / 6 = 67.5 ≈ 68

Fit-to-purpose: Adequate

Determination (scenario 4): CONDITIONAL GO (readiness 68, adequate fit)
```

**Example Scenario 7 (All High = Bull Case):**

```
SCENARIO 7: ALL HIGH (BULL CASE)

Assumption values:
  TAM growth: 35% annually
  Competitor response: 24 months
  PMF validation: 60% of segment
  Enterprise adoption: 1.5x SMB velocity
  Team execution: +20% vs. plan
  Sales cycle: 4 months

Domain scoring:
  1. Fit-to-Purpose: 78 (accelerated deployment timeline; strong returns)
  2. Market Opportunity: 82 (TAM $4.5B+, 24-month competitive window)
  3. Product-Market Fit: 74 (60% validation, strong signals across segments)
  4. Business Model: 76 (4-month sales cycle, excellent unit economics)
  5. Operations: 79 (execution ahead of plan; key hires accelerated)
  6. Competitive Position: 77 (extended market lead; strong positioning)

Composite readiness: (78 + 82 + 74 + 76 + 79 + 77) / 6 = 466 / 6 = 77.7 ≈ 78

Fit-to-purpose: Adequate

Determination (scenario 7): GO (readiness 78, adequate fit)
```

**Continue for all 8 scenarios...**

### Step 3: Aggregate Scenario Results

Create summary table:

| Scenario | Probability | TAM | Competitor | PMF | Execution | Sales Cycle | Composite | Fit | Determination |
|---|---|---|---|---|---|---|---|---|---|
| 1 (All Low) | 0.1% | L | L | L | L | L | 54 | Inadequate | CONDITIONAL HOLD |
| 2 (Mixed Low) | 0.3% | L | L | M | M | M | 58 | Adequate | CONDITIONAL GO |
| 3 (Mixed Low) | 0.6% | L | M | M | M | M | 60 | Adequate | CONDITIONAL GO |
| 4 (Base) | 3.1% | M | M | M | M | M | 68 | Adequate | CONDITIONAL GO |
| 5 (Mixed High) | 0.6% | H | M | M | M | M | 73 | Adequate | CONDITIONAL GO |
| 6 (Mixed High) | 0.3% | H | H | M | M | M | 76 | Adequate | CONDITIONAL GO |
| 7 (All High) | 0.1% | H | H | H | H | H | 78 | Adequate | GO |
| 8 (Bull Mixed) | 0.4% | H | H | H | H | M | 77 | Adequate | GO |

### Step 4: Calculate Probability Distribution

Sum probabilities by determination:

```
DETERMINATION PROBABILITY AGGREGATION

Scenario contributions by determination:

NO-GO (readiness <35):
  [No scenarios produce NO-GO]
  P(NO-GO) = 0%

CONDITIONAL HOLD (readiness 35-54):
  Scenario 1 (All Low): 0.1%
  P(CONDITIONAL HOLD) = 0.1%

CONDITIONAL GO (readiness 55-74):
  Scenario 2: 0.3%
  Scenario 3: 0.6%
  Scenario 4: 3.1%
  Scenario 5: 0.6%
  Scenario 6: 0.3%
  P(CONDITIONAL GO) = 4.9%

GO (readiness 75+):
  Scenario 7: 0.1%
  Scenario 8: 0.4%
  P(GO) = 0.5%

TOTAL: 0% + 0.1% + 4.9% + 0.5% = 5.5%
```

**Issue:** Probabilities don't sum to 100%. This occurs because we selected discrete scenarios rather than exhaustive enumeration.

**Correction:** Normalize probabilities:

```
Normalized probabilities:
  P(NO-GO) = 0% / 5.5% = 0%
  P(CONDITIONAL HOLD) = 0.1% / 5.5% ≈ 2%
  P(CONDITIONAL GO) = 4.9% / 5.5% ≈ 89%
  P(GO) = 0.5% / 5.5% ≈ 9%
  TOTAL = 100%
```

**Alternative approach (Simpler):** Estimate directly without micro-probabilities

Instead of computing exact scenario probabilities, estimate directly:

```
DIRECT PROBABILITY ESTIMATION

Question: What is the probability that actual determination = GO?
Analysis across scenarios: Only high-assumption scenarios (7, 8) produce GO
Probability that 4+ assumptions align on High side: Roughly 5-10% (rare but possible)
Estimate: P(GO) ≈ 10%

Question: What is the probability that actual determination = CONDITIONAL GO?
Analysis across scenarios: Most scenarios (2-6) produce CONDITIONAL GO
Probability that 2-4 assumptions are Mid/High: Roughly 80-85% (most likely)
Estimate: P(CONDITIONAL GO) ≈ 85%

Question: What is the probability that actual determination = CONDITIONAL HOLD?
Analysis across scenarios: Only pessimistic scenario (1) produces CONDITIONAL HOLD
Probability that 4+ assumptions align on Low side: Roughly 5% (tail risk)
Estimate: P(CONDITIONAL HOLD) ≈ 5%

Question: What is the probability that actual determination = NO-GO?
Analysis across scenarios: No scenarios produce NO-GO
Estimate: P(NO-GO) ≈ 0%

Total: 10% + 85% + 5% + 0% = 100%
```

This direct approach produces reasonable estimates with less computational burden.

---

## 5. Probability Distribution Output

### Output Format

```
MONTE CARLO PROBABILITY DISTRIBUTION

Key Assumptions Analyzed (n=6):
  1. TAM Growth Rate (Low: 8%, Mid: 20%, High: 35%)
  2. Competitive Response Time (Low: 3mo, Mid: 12mo, High: 24mo)
  3. Product-Market Fit Validation (Low: 20%, Mid: 40%, High: 60%)
  4. Enterprise Adoption Velocity (Low: 0.5x, Mid: 1x, High: 1.5x SMB)
  5. Founding Team Execution (Low: -20%, Mid: 0%, High: +20%)
  6. Sales Cycle Length (Low: 9mo, Mid: 6mo, High: 4mo)

Probability Weights Applied:
  All assumptions: Low=25%, Mid=50%, High=25% (symmetric equal tails)
  Rationale: Moderate confidence in base case; symmetric uncertainty

Representative Scenarios Evaluated (n=8):
  [Scenario 1 through 8 with assumption combinations and probabilities]
  [Domain scoring and determinations for each scenario]

---

DETERMINATION PROBABILITY DISTRIBUTION

| Determination | Probability | Count | Interpretation |
|---|---|---|---|
| GO | 10% | Rare | Requires 4+ assumptions align on High side |
| CONDITIONAL GO | 85% | Most Likely | Base case + moderate variations |
| CONDITIONAL HOLD | 5% | Tail Risk | Requires 4+ assumptions align on Low side |
| NO-GO | 0% | Negligible | No plausible scenario produces this outcome |
| TOTAL | 100% | | |

---

MODE (Most Probable Determination): CONDITIONAL GO (85% probability)

90th PERCENTILE OUTCOME (Downside Case): CONDITIONAL HOLD
  - Interpretation: There is a 10% probability that actual outcome is at or worse than CONDITIONAL HOLD
  - Combines P(CONDITIONAL HOLD) + P(NO-GO) = 5% + 0% = 5% (not 10%)
  - More precisely: 90th percentile outcome is the determination where cumulative probability ≥ 90%
  - Cumulative: NO-GO (0%) → CONDITIONAL HOLD (5%) → CONDITIONAL GO (90%) → GO (100%)
  - 90th percentile = CONDITIONAL GO (just barely exceeds 90%)
  - Implication: Downside protection is limited; majority of outcomes cluster at CONDITIONAL GO

EXPECTED VALUE DETERMINATION:
  - Assign values: NO-GO=1, CONDITIONAL HOLD=2, CONDITIONAL GO=3, GO=4
  - Expected value = (1 × 0%) + (2 × 5%) + (3 × 85%) + (4 × 10%) = 0 + 0.1 + 2.55 + 0.4 = 3.05
  - Expected value ≈ 3.05 → Round to CONDITIONAL GO
  - Interpretation: On average, expected determination is CONDITIONAL GO with upside to GO

---

ROBUSTNESS CLASSIFICATION

Current determination (from /assess phase): CONDITIONAL GO

Robustness assessment:
  P(current determination) = P(CONDITIONAL GO) = 85%
  Classification: Robust (≥75%)

Interpretation:
  The CONDITIONAL GO determination is robust. Even accounting for assumption 
  uncertainty, CONDITIONAL GO is the most likely outcome in 85% of cases. 
  Probability of GO upside is non-trivial (10%); downside risk exists (5%) 
  but is modest. Overall, the determination is well-supported by the evidence 
  and assumption base.

---

KEY SENSITIVITIES

Variable with highest impact on determination outcome:

1. TAM GROWTH RATE (Highest sensitivity)
   Impact: If High (35%), P(GO) increases to 15-20%; if Low (8%), P(CONDITIONAL HOLD) increases to 10-15%
   Current assumption: 20% annually
   Range tested: 8% to 35%
   Implication: Market macro conditions are the primary driver of outcome variance

2. COMPETITIVE RESPONSE TIME (High sensitivity)
   Impact: If High (24mo), extends market lead scenario; if Low (3mo), compresses timeline
   Current assumption: 12 months
   Range tested: 3 months to 24 months
   Implication: Competitive activity is critical uncertainty

3. PRODUCT-MARKET FIT VALIDATION (Moderate sensitivity)
   Impact: If High (60%), supports GO determination; if Low (20%), increases CONDITIONAL HOLD risk
   Current assumption: 40%
   Range tested: 20% to 60%
   Implication: Customer validation progress is key monitoring variable

4. FOUNDING TEAM EXECUTION (Moderate sensitivity)
   Impact: Execution variance moves composite ±5 points but rarely flips determination alone
   Current assumption: On-plan
   Range tested: -20% to +20%
   Implication: Execution matters but is secondary to market and product factors

---

TAIL RISK ANALYSIS

Scenarios with <2% probability but material impact:

Tail Risk 1: All Low (Scenario 1)
  Probability: 0.1% (rare; requires all 5 assumptions pessimistic)
  Outcome: CONDITIONAL HOLD (composite 54)
  Trigger: TAM growth <8%, competitor <3 months, PMF <20%, execution -20%, sales cycle >9mo
  Mitigation: Unlikely given individual assumption probabilities; monitor for compound risk

Tail Risk 2: Market + Execution Deterioration (2-3 assumption alignment on Low)
  Probability: ~2-3% (more plausible; requires 2-3 pessimistic assumptions)
  Outcome: CONDITIONAL HOLD
  Trigger: Market slowdown + execution slips + PMF validation lags
  Mitigation: Monitor early warning indicators (market growth, hiring velocity, customer feedback)

Most Likely Upside: Enterprise Adoption + Execution Acceleration (Scenario 8)
  Probability: 0.4% (low but achievable)
  Outcome: GO (composite 77)
  Trigger: Enterprise customers adopt faster than expected + team execution exceeds plan
  Acceleration path: Focus on enterprise reference customers; accelerate key hiring
```

---

## 6. Robustness Classification from Monte Carlo

### Classification Criteria

**Robust** — P(current determination) ≥ 75%

Interpretation: Current determination is dominant outcome even under assumption uncertainty. Alternative outcomes are tail risks. Strong confidence in determination.

Example: P(CONDITIONAL GO) = 85% → **Robust CONDITIONAL GO**

**Moderately Robust** — P(current determination) 50–74%

Interpretation: Current determination is probable but not dominant. Alternative outcomes have meaningful probability. Reasonable confidence in determination but with notable sensitivity to assumptions.

Example: P(GO) = 65%, P(CONDITIONAL GO) = 25%, P(CONDITIONAL HOLD) = 10% → **Moderately Robust GO**

**Fragile** — P(current determination) < 50%

Interpretation: Current determination is less likely than at least one alternative. Assumption uncertainty creates substantial outcome variance. Low confidence in determination; highly sensitive to assumptions.

Example: P(CONDITIONAL GO) = 48%, P(GO) = 35%, P(CONDITIONAL HOLD) = 15%, P(NO-GO) = 2% → **Fragile CONDITIONAL GO**

### Making the Classification

1. **Identify current determination** (from /assess phase)
2. **Locate probability** in Monte Carlo distribution
3. **Classify based on probability threshold**

**Example classifications:**

```
Current determination: GO
Monte Carlo P(GO) = 42%
Classification: FRAGILE (P < 50%)
→ Determination GO is less certain than upside/downside alternatives

Current determination: CONDITIONAL GO
Monte Carlo P(CONDITIONAL GO) = 85%
Classification: ROBUST (P ≥ 75%)
→ Determination CONDITIONAL GO is dominant outcome

Current determination: CONDITIONAL HOLD
Monte Carlo P(CONDITIONAL HOLD) = 62%
Classification: MODERATELY ROBUST (50% ≤ P < 75%)
→ Determination CONDITIONAL HOLD is probable but has notable alternatives
```

---

## 7. Limitations and Disclosure

### Important Caveats

Document these limitations in the sensitivity report:

```
MONTE CARLO ANALYSIS: LIMITATIONS AND DISCLOSURE

This analysis employs a STRUCTURED ANALYTICAL APPROACH to probability estimation,
NOT statistical simulation software. Users should understand these limitations:

1. INDEPENDENCE ASSUMPTION
   - Analysis assumes assumptions are independent
   - Reality: Assumptions may be correlated (e.g., if TAM grows fast, competitor response may be faster)
   - Impact: Probability distribution may underestimate tail risks if positive correlation exists
   - Mitigation: Key correlated assumptions (market growth + competitive response) are treated as coupled in scenario design

2. PROBABILITY WEIGHTING BASIS
   - Probabilities (Low=25%, Mid=50%, High=25%) are expert estimates, not historical data
   - No large sample of similar startups available for statistical validation
   - Weighting reflects assessor's confidence in base case, not empirical distribution
   - Impact: Actual probability distribution may differ from analytical estimate by ±10 percentage points

3. SCENARIO COVERAGE
   - 8 representative scenarios do not exhaustively cover assumption space
   - Some rare combinations (e.g., TAM Low + Competitor High) are not explicitly calculated
   - Impact: Probability distribution may have small discretization error
   - Mitigation: Normalization and direct estimation adjust for missing scenarios

4. ASSUMPTION RANGE SPECIFICATION
   - Low and High values represent plausible extremes, not true 5th/95th percentiles
   - Actual range may be wider (tail risk) or narrower (tail underestimated)
   - Impact: Probability distribution may not capture true tail probabilities accurately

5. DOMAIN RE-SCORING APPROXIMATION
   - Scenario-based domain re-scoring is approximate (uses rubric judgment, not formulaic calculation)
   - Small estimation errors in domain scores compound into composite score variance
   - Impact: Probability distribution may have ±2 point composite score uncertainty

CONFIDENCE INTERVAL:
   - Reported probabilities should be interpreted as order-of-magnitude estimates
   - Confidence interval: Reported P ± 10 percentage points
   - Example: Reported P(GO) = 10% should be interpreted as 0-20% range

APPROPRIATE USE:
   - Suitable for: Relative ranking of outcomes, sensitivity analysis, robustness assessment
   - Not suitable for: Precise probability predictions, option pricing, formal Bayesian analysis
   - Recommended: Triangulate Monte Carlo results with scenario analysis and boundary analysis

FOR HIGHER CONFIDENCE:
   - Use formal Monte Carlo simulation software (10,000+ iterations) if precise probabilities required
   - Collect historical data on similar startup populations for probability weighting validation
   - Employ Bayesian inference with historical priors if available
   - Conduct expert consensus elicitation (multiple assessors) to validate probability weights
```

---

## 8. Full Monte Carlo Example: Series A SaaS Startup

### Setup

Base case determination: CONDITIONAL GO (composite 68)

Key assumptions selected:
1. TAM Growth Rate
2. Competitive Response Time
3. Product-Market Fit Validation
4. Enterprise Adoption Velocity
5. Founding Team Execution
6. Sales Cycle Length

Probability weights: 25% / 50% / 25% (symmetric) for all assumptions

---

### Eight Representative Scenarios

**Scenario 1: All Low (0.1% frequency)**
- TAM 8%, Competitor 3mo, PMF 20%, Execution -20%, Sales 9mo
- Composite: 54 | Determination: CONDITIONAL HOLD

**Scenario 2: Mixed Low 1 (0.3% frequency)**
- TAM 8%, Competitor 3mo, PMF Mid, Execution Mid, Sales Mid
- Composite: 58 | Determination: CONDITIONAL GO

**Scenario 3: Mixed Low 2 (0.6% frequency)**
- TAM 8%, Competitor Mid, PMF Mid, Execution Mid, Sales Mid
- Composite: 60 | Determination: CONDITIONAL GO

**Scenario 4: Base Case (3.1% frequency)**
- TAM 20%, Competitor 12mo, PMF 40%, Execution plan, Sales 6mo
- Composite: 68 | Determination: CONDITIONAL GO

**Scenario 5: Mixed High 1 (0.6% frequency)**
- TAM 35%, Competitor 12mo, PMF Mid, Execution Mid, Sales Mid
- Composite: 73 | Determination: CONDITIONAL GO

**Scenario 6: Mixed High 2 (0.3% frequency)**
- TAM 35%, Competitor 24mo, PMF Mid, Execution Mid, Sales Mid
- Composite: 76 | Determination: CONDITIONAL GO

**Scenario 7: All High (0.1% frequency)**
- TAM 35%, Competitor 24mo, PMF 60%, Execution +20%, Sales 4mo
- Composite: 78 | Determination: GO

**Scenario 8: Bull Mixed (0.4% frequency)**
- TAM 35%, Competitor 24mo, PMF 60%, Execution +20%, Sales 6mo
- Composite: 77 | Determination: GO

### Probability Distribution

Aggregating scenarios:

```
PROBABILITY DISTRIBUTION

| Determination | Scenarios | Probability | Interpretation |
|---|---|---|---|
| GO | 7, 8 | 0.1% + 0.4% = 0.5% | Rare; requires high-assumption alignment |
| CONDITIONAL GO | 2, 3, 4, 5, 6 | 0.3% + 0.6% + 3.1% + 0.6% + 0.3% = 4.9% | Most likely; covers all moderate scenarios |
| CONDITIONAL HOLD | 1 | 0.1% | Tail risk; all-low assumption scenario |
| NO-GO | — | 0% | No plausible scenarios |

Total raw: 5.5%
Normalized: 
  P(GO) = 0.5% / 5.5% ≈ 9%
  P(CONDITIONAL GO) = 4.9% / 5.5% ≈ 89%
  P(CONDITIONAL HOLD) = 0.1% / 5.5% ≈ 2%
  P(NO-GO) = 0% / 5.5% = 0%
```

OR using direct estimation:

```
DIRECT PROBABILITY ESTIMATION

P(GO): 10% (all-high or mostly-high scenarios; plausible but rare; requires market + team + product alignment)

P(CONDITIONAL GO): 85% (base case + variations; most likely; covers >80% of assumption space)

P(CONDITIONAL HOLD): 5% (all-low or mostly-low scenarios; plausible tail risk; market/product deterioration)

P(NO-GO): 0% (no plausible scenario deteriorates to this level)

Total: 100%
```

### Robustness Classification

Current determination: CONDITIONAL GO
P(CONDITIONAL GO) = 85%
Threshold for robustness: ≥75%

**Classification: ROBUST**

The CONDITIONAL GO determination is robust. Even accounting for substantial assumption uncertainty, CONDITIONAL GO is the most likely outcome (85% probability). Upside to GO (10%) and downside to CONDITIONAL HOLD (5%) both exist but are minority outcomes.

---

### Key Sensitivities

```
TOP 5 SENSITIVITIES FROM MONTE CARLO

1. TAM GROWTH RATE (Highest impact)
   - If High (35%): P(GO) increases to 15%+
   - If Low (8%): P(CONDITIONAL HOLD) increases to 10%+
   - Current assumption sensitivity: ±8-10 on composite score
   - Monitoring: Track industry analyst forecasts; quarterly market growth data

2. COMPETITIVE RESPONSE TIME (High impact)
   - If High (24mo): Extends market opportunity window; supports higher determination
   - If Low (3mo): Compresses timeline; increases execution pressure
   - Current assumption sensitivity: ±6-8 on composite score
   - Monitoring: Track competitor press releases, patent filings, hiring announcements

3. PRODUCT-MARKET FIT VALIDATION (Moderate-High impact)
   - If High (60%): Enterprise segment clearly validated; moves toward GO
   - If Low (20%): Product-market fit in question; moves toward CONDITIONAL HOLD
   - Current assumption sensitivity: ±5-6 on composite score
   - Monitoring: Customer reference feedback, NPS trends, customer acquisition velocity

4. FOUNDING TEAM EXECUTION (Moderate impact)
   - If High (+20%): Accelerated hiring, faster go-to-market, increased revenue
   - If Low (-20%): Execution slips, hiring delays, slower growth trajectory
   - Current assumption sensitivity: ±4-5 on composite score
   - Monitoring: Monthly execution metrics vs. plan; hiring pipeline velocity; key hire signals

5. ENTERPRISE ADOPTION VELOCITY (Moderate impact)
   - If High (1.5x SMB): Enterprise segment becomes primary driver; higher payback
   - If Low (0.5x SMB): SMB-only focus; lower LTV; smaller market
   - Current assumption sensitivity: ±3-4 on composite score
   - Monitoring: Enterprise vs. SMB customer acquisition mix; segment-specific NPS/retention
```

---

### Monte Carlo Output (Final Format)

```
MONTE CARLO PROBABILITY DISTRIBUTION ANALYSIS

Assessment Phase: CONDITIONAL GO determination (composite readiness 68)

Key Assumptions Analyzed (n=6):
  1. TAM Growth Rate: 8% / 20% / 35% annually
  2. Competitive Response: 3mo / 12mo / 24mo to meaningful entry
  3. Product-Market Fit: 20% / 40% / 60% of target segment
  4. Enterprise Adoption: 0.5x / 1x / 1.5x vs. SMB velocity
  5. Team Execution: -20% / on-plan / +20% vs. plan
  6. Sales Cycle: 9mo / 6mo / 4mo average

Probability Weights: 25% / 50% / 25% (symmetric; no evidence of directional bias)

Determination Probability Distribution:
  NO-GO: 0% (no plausible scenario)
  CONDITIONAL HOLD: 5% (all-low assumption scenario; tail risk)
  CONDITIONAL GO: 85% (base case + moderate variations; most likely)
  GO: 10% (all-high or bull scenarios; plausible upside)
  Total: 100%

Mode (Most Probable Determination): CONDITIONAL GO (85%)

90th Percentile Outcome (Downside Risk): CONDITIONAL GO-CONDITIONAL HOLD boundary
  Cumulative P(≤CONDITIONAL HOLD) = 5%; P(≤CONDITIONAL GO) = 90%
  Interpretation: 90% of outcomes cluster at CONDITIONAL GO or better; downside risk is modest

Expected Value Determination: CONDITIONAL GO (3.05 on 1-4 scale)

Robustness Classification: ROBUST
  P(current determination) = 85% ≥ 75% threshold
  Interpretation: CONDITIONAL GO is the dominant outcome; sensitive to extreme assumption 
  variance but resilient to moderate stress scenarios

Highest Sensitivity Assumptions:
  1. TAM growth rate (affects composite ±8-10 points)
  2. Competitive response time (affects composite ±6-8 points)
  3. Product-market fit validation (affects composite ±5-6 points)
  
Recommended Monitoring Variables:
  - Market growth rate (quarterly analyst tracking; alert if <15% CAGR)
  - Competitive activity (monthly intelligence; alert on product/funding announcements)
  - Product-market fit signals (monthly customer feedback; track NPS, cohort retention)
  - Enterprise customer acquisition (monthly mix tracking; early warning if <20% of new customers)

Limitations Disclosure:
  This analysis uses structured analytical estimation (not statistical simulation). 
  Reported probabilities are order-of-magnitude estimates (confidence: ±10%). 
  For higher precision, employ formal Monte Carlo software or Bayesian methods with 
  historical data. This analysis is suitable for sensitivity ranking and robustness 
  assessment but not for precise probability predictions.
```

---

**End of monte-carlo-approach.md**
