# Boundary / Flip-Point Analysis Reference

## Full Boundary Analysis Execution Procedure

This reference provides the complete procedure for executing boundary/flip-point analysis as a sensitivity methodology.

---

## 1. Definition and Purpose

### What Is Boundary Analysis?

Boundary analysis (also called "flip-point analysis") identifies the minimum changes required to move a determination from one level to another. It answers:
- "How much better would evidence need to be to flip from CONDITIONAL GO to GO?"
- "How much worse could evidence become before dropping from CONDITIONAL GO to CONDITIONAL HOLD?"
- "What is the closest flip point (easiest to achieve)?"

### Why It Matters

Boundary analysis quantifies the effort and evidence required to change a determination. It distinguishes between:
- **Determinations far from flip points** (robust; would require major evidence shifts)
- **Determinations near flip points** (fragile; could flip with modest evidence changes)
- **Asymmetric determinations** (easier to improve than deteriorate, or vice versa)

This informs both sensitivity robustness assessment and practical next steps for the startup.

---

## 2. Candidate Module Identification

### Step 1: Extract Domain Scores from /Assess Phase

Retrieve the complete domain scoring from the assessment:

```
DOMAIN SCORES (LOCKED FROM /ASSESS PHASE)

Domain 1: Fit-to-Purpose: 75
Domain 2: Market Opportunity: 68
Domain 3: Product-Market Fit: 62
Domain 4: Business Model Viability: 66
Domain 5: Operations Readiness: 70
Domain 6: Competitive Position: 64
Domain 7: Key Assumptions: [Embedded in domain scores above]

Composite Readiness = (75 + 68 + 62 + 66 + 70 + 64) / 6 = 405 / 6 = 67.5 ≈ 68
```

### Step 2: Calculate Distance to Determination Thresholds

Determine the target determination and current composite score:

```
CURRENT DETERMINATION: CONDITIONAL GO (readiness 55-74)
CURRENT COMPOSITE READINESS: 68

Distance to higher threshold (GO threshold = 75):
  75 - 68 = 7 points needed to flip UPWARD

Distance to lower threshold (CONDITIONAL HOLD threshold = 54):
  68 - 54 = 14 points tolerance to flip DOWNWARD
```

### Step 3: Identify Candidate Domains for Flip Analysis

For upward flip, identify domains with:
1. **Gaps identified in assessment** (gaps are improvement opportunities)
2. **Scores close to improvement ceiling** (room to grow within domain)
3. **High impact on composite** (moving a domain score moves composite proportionally)

**Example upward flip candidates (toward GO):**

| Domain | Current Score | Ceiling | Gap to Ceiling | Assessment Gaps | Impact on Composite |
|--------|---|---|---|---|---|
| Product-Market Fit (3) | 62 | 75 | 13 | Limited TAM validation; unclear segment targeting | +2.2 per point |
| Operations Readiness (5) | 70 | 80 | 10 | Undefined hiring plan; vendor relationships weak | +2.2 per point |
| Business Model (4) | 66 | 78 | 12 | Unit economics unclear; CAC payback uncertain | +2.2 per point |
| Market Opportunity (2) | 68 | 82 | 14 | TAM validation incomplete; competitive timeline uncertain | +2.2 per point |

**Selection logic:** Product-Market Fit (Domain 3) has largest identified gaps and clear improvement pathway. Operations Readiness (Domain 5) is closest to floor of gaps.

For downward flip, identify domains with:
1. **Strongest current scores** (most to lose)
2. **Risk scenarios identified** (where could this deteriorate?)
3. **High impact on composite** (deterioration in high-value domain triggers flip)

**Example downward flip candidates (toward CONDITIONAL HOLD):**

| Domain | Current Score | Risk Floor | Deterioration Tolerance | Risk Scenarios | Impact |
|--------|---|---|---|---|---|
| Market Opportunity (2) | 68 | 48 | -20 | Market growth slowdown; competitor entry | -2.2 per point |
| Operations Readiness (5) | 70 | 52 | -18 | Key hire delays; execution slips | -2.2 per point |
| Business Model (4) | 66 | 48 | -18 | Unit economics worsen; CAC increases 30%+ | -2.2 per point |

---

## 3. Upward Flip Analysis Procedure

### Objective

Determine the minimum evidence improvements required to flip from current determination to next higher determination (e.g., CONDITIONAL GO → GO).

### Step 1: Identify Target Determination and Required Composite Score

```
UPWARD FLIP: CONDITIONAL GO → GO

Current state:
  Composite readiness: 68 (within CONDITIONAL GO range 55-74)
  Fit-to-purpose: Adequate

Target state:
  Composite readiness: 75 (minimum GO threshold)
  Fit-to-purpose: Adequate (maintained)

Improvement required: 75 - 68 = 7 composite points
```

### Step 2: Calculate Per-Domain Improvement Needed

Composite readiness is the average of 6 domains (Domain 7 is embedded):

Improvement needed = 7 points composite
Average per domain = 7 / 6 ≈ 1.17 points per domain

**Strategy:** Identify which subset of domains can most easily achieve 7-point total improvement.

### Step 3: Identify Easiest Improvement Path

Create a table of domains with improvement potential:

| Domain | Current | Target for +7 Composite | Points Needed | Gap Assessment | Evidence Path | Effort Level |
|--------|---------|---|---|---|---|---|
| Product-Market Fit | 62 | 65 | +3 | Limited TAM validation with enterprise | Add 2-3 enterprise customer references; document PMF signals | Moderate (4 weeks) |
| Operations Readiness | 70 | 72 | +2 | Undefined hiring plan; key roles open | Finalize org chart; secure 2-3 key hires | Moderate (6 weeks) |
| Business Model | 66 | 68 | +2 | CAC payback period uncertain | Model 3 customer cohorts; show payback ≤18 months | Moderate (3 weeks) |
| **Subtotal** | | | **+7** | | | **Moderate (4-6 weeks)** |

**Interpretation:** To flip from CONDITIONAL GO to GO, the startup needs to improve evidence in 3 domains by combined +7 points. The most efficient path targets Product-Market Fit (enterprise validation), Operations Readiness (hiring plan), and Business Model (CAC payback modeling).

### Step 4: Detailed Evidence Requirements

For the upward flip path identified above, specify what evidence is needed:

**Domain 3: Product-Market Fit (Target: 62 → 65)**
- Current gap: "Limited TAM validation with enterprise customers"
- Evidence required:
  - Conduct reference calls with 3-5 enterprise customers who are active beta users
  - Document their use cases, satisfaction scores (NPS/CSAT), and purchasing intent
  - Show that enterprise PMF validation is ≥50% (vs. current 40%)
- Success criteria: Beta cohort shows strong enterprise signals; can articulate enterprise value prop clearly
- Timeline: 4 weeks (customer outreach, reference calls, documentation)

**Domain 5: Operations Readiness (Target: 70 → 72)**
- Current gap: "Undefined hiring plan; key VP Engineering not yet in place"
- Evidence required:
  - Finalize organizational structure for next 18 months
  - Document key hire priorities (rank by criticality)
  - Show progress on recruiting for priority roles (offer made, candidate in advanced discussions)
- Success criteria: Hiring plan is explicit; 1+ key hire shows strong signal of close
- Timeline: 6 weeks (recruiting pipeline build-out)

**Domain 4: Business Model Viability (Target: 66 → 68)**
- Current gap: "CAC payback period uncertain; unit economics not modeled"
- Evidence required:
  - Analyze actual customer acquisition costs for first customer cohort
  - Model customer lifetime value and CAC payback for multiple scenarios
  - Show that payback period is ≤18 months under base case
- Success criteria: Unit economics are clear; payback timeline is supportable
- Timeline: 3 weeks (customer cohort analysis, financial modeling)

### Step 5: Feasibility Assessment

Rate the feasibility of achieving the upward flip:

**Effort Level: MODERATE**
- Requires 3 concurrent work streams (customer validation, hiring, financial modeling)
- Evidence is accessible (uses existing customer relationships and internal data)
- Timeline is realistic (4-6 weeks vs. 8-12 weeks for intensive effort)

**Probability of Success: MODERATE-HIGH (60-70%)**
- Customer reference calls are low-risk; have existing beta relationships
- Hiring for VP Engineering is in market; recruiting should accelerate (moderate risk)
- Financial modeling is internal; can be completed (low risk)
- Aggregated probability: If 2 of 3 work streams succeed fully, flip is achieved

**Conditional Dependencies:**
- Hiring success depends on candidate market availability and founding team interview performance
- Customer validation success depends on beta customer satisfaction (already using product)
- Financial modeling success is nearly certain (internal control)

### Step 6: Upward Flip Output Format

```
UPWARD FLIP ANALYSIS: CONDITIONAL GO → GO

Current composite readiness: 68
Target composite readiness: 75
Improvement required: 7 points

Recommended improvement path:
  Domain 3 (Product-Market Fit): 62 → 65 (+3 points)
    - Validate enterprise PMF through customer reference calls
    - Evidence needed: 3-5 enterprise customer references with PMF signals
    - Effort: Moderate | Timeline: 4 weeks | Risk: Low

  Domain 5 (Operations Readiness): 70 → 72 (+2 points)
    - Complete hiring plan; advance key hires (VP Engineering)
    - Evidence needed: Explicit org chart; offer letter in-hand or advanced discussions
    - Effort: Moderate | Timeline: 6 weeks | Risk: Moderate

  Domain 4 (Business Model): 66 → 68 (+2 points)
    - Model unit economics; demonstrate CAC payback ≤18 months
    - Evidence needed: Customer cohort financial analysis; CAC payback scenarios
    - Effort: Moderate | Timeline: 3 weeks | Risk: Low

Total effort level: MODERATE (4-6 weeks; 3 concurrent work streams)
Probability of success: 60-70% (high confidence in 2/3 domains; moderate in hiring)

Benefits of achieving flip:
  - Moves from CONDITIONAL GO to GO (full investment confidence)
  - Unlocks Path B deal terms negotiation in /recommend phase
  - Demonstrates execution capability to investors
```

---

## 4. Downward Flip Analysis Procedure

### Objective

Determine how much evidence could deteriorate before the determination flips down to the next lower level (e.g., CONDITIONAL GO → CONDITIONAL HOLD).

### Step 1: Identify Target Determination and Deterioration Tolerance

```
DOWNWARD FLIP: CONDITIONAL GO → CONDITIONAL HOLD

Current state:
  Composite readiness: 68 (within CONDITIONAL GO range 55-74)
  Fit-to-purpose: Adequate

Target state (downward):
  Composite readiness: 54 (maximum CONDITIONAL HOLD threshold)
  Fit-to-purpose: Adequate or Inadequate

Deterioration tolerance: 68 - 54 = 14 composite points
```

### Step 2: Identify Domains Most at Risk

For downward flip analysis, focus on domains that:
1. **Have current vulnerabilities** (identified gaps or moderate scores)
2. **Could plausibly deteriorate** (external risk scenarios or execution risks)
3. **Have highest impact on composite** (movement in these domains triggers threshold breach)

**Example downward flip candidates:**

| Domain | Current | Deterioration Risk | Plausibility | Impact | Drop Tolerance |
|--------|---------|---|---|---|---|
| Market Opportunity (2) | 68 | Market growth stalls; competitor enters | HIGH (external risk) | 2.2 per point | Can drop 14 points before floor |
| Operations Readiness (5) | 70 | Key hire delays; execution slips | MODERATE (internal risk) | 2.2 per point | Can drop 14 points before floor |
| Business Model (4) | 66 | Unit economics worsen; CAC increases | MODERATE (market dependent) | 2.2 per point | Can drop 14 points before floor |

### Step 3: Identify Deterioration Scenarios

For each at-risk domain, define a plausible deterioration scenario:

**Domain 2: Market Opportunity (Current 68)**

Deterioration scenario:
- Market growth rate drops from 20% to 8% annually
- Competitor enters within 6 months (vs. expected 12 months)
- TAM narrows due to regulatory restriction in one key vertical

**Impact on Domain 2 score:**
- Current score (68): Reflects $2.5B TAM, 12-month competitive window
- Deteriorated score: $1.8B TAM (28% contraction), 6-month window, narrowed vertical focus
- New Domain 2 score: 52 (drop of 16 points)

**Domain 5: Operations Readiness (Current 70)**

Deterioration scenario:
- VP Engineering hire falls through; restart recruiting (3-month delay)
- Key founding team member leaves (market opportunity elsewhere)
- Execution velocity slips 20% due to market uncertainty

**Impact on Domain 5 score:**
- Current score (70): Assumes on-plan execution, key hires progressing
- Deteriorated score: Team attrition, hiring delays, execution slowdown
- New Domain 5 score: 58 (drop of 12 points)

**Domain 4: Business Model (Current 66)**

Deterioration scenario:
- CAC increases 40% due to market saturation in channel
- Customer churn increases to 8% monthly (vs. expected 3%)
- Payback period extends to 24 months (vs. modeled 18 months)

**Impact on Domain 4 score:**
- Current score (66): Reflects healthy unit economics, 18-month payback
- Deteriorated score: Challenged unit economics, extended payback, churn concerns
- New Domain 4 score: 52 (drop of 14 points)

### Step 4: Calculate Deterioration Tolerance per Domain

**Question: How much can each domain drop before composite readiness falls below 54?**

Current composite: 68
Target composite (downward): 54
Total tolerance: 14 points across 6 domains

If single domain deteriorates:

| Domain | Current | Drop Tolerance | Drop Floor | Scenario Trigger |
|--------|---------|---|---|---|
| Market Opportunity (2) | 68 | 14 points | 54 | Market TAM contracts 30%; competitor 6-month entry |
| Operations (5) | 70 | 12 points | 58 | Key hire delays; 20% execution slip |
| Business Model (4) | 66 | 16 points | 50 | CAC increases 40%; churn doubles |

**Interpretation:** 
- Market Opportunity is most sensitive (can only drop 14 points before flip)
- Business Model has highest tolerance (can drop 16 points)
- Operations has moderate tolerance (can drop 12 points)

### Step 5: Multi-Domain Deterioration Scenarios

In reality, deterioration often affects multiple domains simultaneously:

**Scenario: Market Slowdown**
- Market Opportunity drops 16 points (68 → 52)
- Business Model drops 8 points (66 → 58) [due to elongated sales cycle]
- Operations drops 2 points (70 → 68) [execution fine]
- **Total composite impact: -26 points → New composite = 42 (CONDITIONAL HOLD)**

**Scenario: Execution Risk**
- Operations drops 12 points (70 → 58) [hiring/attrition]
- Market Opportunity drops 8 points (68 → 60) [market uncertainty slows adoption]
- Business Model drops 4 points (66 → 62) [longer sales cycles]
- **Total composite impact: -24 points → New composite = 44 (CONDITIONAL HOLD)**

**Scenario: Moderate Deterioration Across Domains**
- Market Opportunity drops 6 points (68 → 62)
- Operations drops 4 points (70 → 66)
- Business Model drops 4 points (66 → 62)
- **Total composite impact: -14 points → New composite = 54 (CONDITIONAL HOLD floor)**

### Step 6: Early Warning Indicators

For each at-risk domain, specify early warning indicators that signal deterioration is beginning:

**Market Opportunity Warning Indicators:**
- Quarterly market growth rate (YoY) drops below 15% (vs. expected 20%)
- Competitor announces product launch or funding (indicates 6-month entry likely)
- Industry analyst reports downgrade growth forecasts by >10% CAGR
- **Monitoring frequency:** Quarterly analyst tracking; monthly competitive intelligence

**Operations Readiness Warning Indicators:**
- Key hire interviews extend beyond 4 weeks (indicates slower recruiting)
- Founding team member signals job market interest or dissatisfaction
- Monthly execution velocity vs. plan drops >15%
- Hiring offer acceptance rate falls below 60% (indicates market competition for talent)
- **Monitoring frequency:** Weekly exec team check-in; monthly hiring metrics review

**Business Model Warning Indicators:**
- Actual CAC (from first 10-20 customers) exceeds model by >20%
- Customer churn rate rises above 5% monthly
- Sales cycle (from first inquiry to contract) extends beyond 7 months
- Channel partner termination or contract renegotiation
- **Monitoring frequency:** Monthly cohort analysis; weekly sales pipeline review

### Step 7: Downward Flip Output Format

```
DOWNWARD FLIP ANALYSIS: CONDITIONAL GO → CONDITIONAL HOLD

Current composite readiness: 68
Target composite readiness: 54 (CONDITIONAL HOLD floor)
Deterioration tolerance: 14 points

Domains most at risk:

1. Market Opportunity (Domain 2)
   Current: 68 | Drop tolerance: -14 points | Floor: 54
   Deterioration trigger: Market TAM contracts 30%; competitor entry within 6 months
   Plausibility: HIGH (external market risk)
   Early warning indicators:
     - YoY market growth rate <15% (vs. projected 20%)
     - Competitor announces product launch
     - Analyst downgrades market forecast
   Monitoring: Quarterly analyst tracking; monthly competitive intelligence

2. Operations Readiness (Domain 5)
   Current: 70 | Drop tolerance: -12 points | Floor: 58
   Deterioration trigger: Key hire (VP Eng) fails through; team attrition ≥1 founder-level
   Plausibility: MODERATE (internal execution risk)
   Early warning indicators:
     - VP Eng recruiting extends >4 weeks
     - Founding team member job market activity
     - Monthly velocity vs. plan drops >15%
   Monitoring: Weekly exec check-in; monthly hiring metrics

3. Business Model (Domain 4)
   Current: 66 | Drop tolerance: -16 points | Floor: 50
   Deterioration trigger: CAC increases 40%+; payback period extends to 24+ months
   Plausibility: MODERATE (market/execution dependent)
   Early warning indicators:
     - Actual CAC (first cohort) exceeds model >20%
     - Monthly churn rate rises above 5%
     - Sales cycle elongates to 7+ months
   Monitoring: Monthly cohort analysis; weekly sales pipeline

Most vulnerable pathway: Market slowdown affecting multiple domains
  If: Market TAM contracts + competitor enters + CAC rises, then:
  → Composite drops 20-26 points → Determination flips to CONDITIONAL HOLD

Safety margin: MODERATE
  Current 68 → Floor 54 gives 14-point buffer
  Multi-domain deterioration scenarios (market + operations or market + business model) can consume 14-24 points
  Conclusion: Moderate deterioration across 2-3 domains triggers flip; single-domain deterioration alone unlikely to flip (except market opportunity, which has slim tolerance)
```

---

## 5. Distance-to-Flip Metric

### Definition

Distance-to-flip is a summary metric expressing how "easy" or "hard" it is to achieve an upward or downward flip. It combines three factors:
1. **Composite points required** (for upward) or **tolerance** (for downward)
2. **Number of domains affected**
3. **Evidence burden** (light = existing data; moderate = validation needed; intensive = major research required)

### Upward Flip Distance Categories

**NEAR (Easy to flip upward)**
- Composite points needed: ≤5 points
- Domains affected: 1-2 domains
- Evidence burden: Light (existing customer/market data; internal analysis)
- Timeline: ≤4 weeks
- Interpretation: Small improvements in 1-2 areas achieves flip; low-hanging fruit

**MODERATE (Moderate effort to flip upward)**
- Composite points needed: 5-10 points
- Domains affected: 2-3 domains
- Evidence burden: Moderate (customer validation; market research; hiring)
- Timeline: 4-8 weeks
- Interpretation: Meaningful but achievable improvements across multiple domains

**FAR (Robust against upward flip; hard to improve)**
- Composite points needed: 10+ points
- Domains affected: 4+ domains
- Evidence burden: Intensive (comprehensive market validation; major hiring; business model overhaul)
- Timeline: 8+ weeks or ongoing
- Interpretation: Would require significant business changes; current determination is robust against improvement skeptics

### Downward Flip Distance Categories

**NEAR (Fragile; easy to flip downward)**
- Deterioration tolerance: <10 points
- Risk scenarios: Plausible, multiple triggers
- Safety margin: Low (small deterioration achieves flip)
- Interpretation: Determination is fragile; even moderate adverse conditions trigger downward flip

**MODERATE (Adequate safety margin)**
- Deterioration tolerance: 10-15 points
- Risk scenarios: Plausible but require coordinated failure (multiple domains)
- Safety margin: Reasonable (can tolerate some deterioration)
- Interpretation: Determination is stable under single-domain challenges; vulnerable to multi-domain stress

**FAR (Robust against downward flip; strong safety margin)**
- Deterioration tolerance: 15+ points
- Risk scenarios: Require major deterioration; unlikely under plausible conditions
- Safety margin: Strong (substantial buffer before flip)
- Interpretation: Determination is robust against adverse scenarios

### Asymmetry Interpretation

Compare upward flip distance to downward flip distance to understand the "shape" of the determination:

**Asymmetric Upward** (easy to improve, hard to deteriorate)
- Example: Upward flip = NEAR (5 points), Downward flip = FAR (16 points)
- Interpretation: Determination is conservative and stable. Investor should be confident in downside protection but should recognize upside is achievable. Company can move to GO with modest additional evidence. Good risk/reward profile.

**Asymmetric Downward** (hard to improve, easy to deteriorate)
- Example: Upward flip = FAR (12 points), Downward flip = NEAR (8 points)
- Interpretation: Determination is aggressive and fragile. Investor should be cautious; modest adverse news could drop determination. Unlikely to improve to next level without major changes. High-risk profile.

**Balanced** (similar effort in both directions)
- Example: Upward flip = MODERATE (7 points), Downward flip = MODERATE (12 points)
- Interpretation: Determination is middle-of-the-road. Outcomes could move either direction depending on execution and market conditions. Requires active monitoring.

### Distance-to-Flip Output Format

```
DISTANCE-TO-FLIP METRIC

UPWARD FLIP: CONDITIONAL GO → GO
  Composite points needed: 7
  Domains affected: 3 (Product-Market Fit, Operations, Business Model)
  Evidence burden: Moderate (customer validation + hiring + financial modeling)
  Timeline: 4-6 weeks
  Probability of success: 60-70%
  
  Distance classification: MODERATE
  
  Interpretation: Achievable with focused effort on 3 domains. Customer 
  validation is low-risk; hiring is moderate-risk; financial modeling is 
  low-risk. Timeline aligns with Series A decision-making cadence.

DOWNWARD FLIP: CONDITIONAL GO → CONDITIONAL HOLD
  Deterioration tolerance: 14 points
  Domains at risk: Market Opportunity (high), Operations (moderate), Business Model (moderate)
  Risk scenarios: Market slowdown + competitor entry (plausible); execution delays + market uncertainty (plausible)
  Safety margin: Moderate (14-point buffer; multi-domain deterioration triggers flip)
  
  Distance classification: MODERATE
  
  Interpretation: Determination has adequate safety margin against single-
  domain deterioration. Vulnerable to coordinated multi-domain stress (market 
  + operations/business model). Market Opportunity is most sensitive (14-point 
  tolerance means 20% growth assumption is tight threshold).

ASYMMETRY ANALYSIS
  Upward vs. Downward: Balanced (7-point improvement vs. 14-point tolerance)
  Asymmetry direction: Slightly downside-fragile (easier to deteriorate than improve)
  
  Implication: Determination is neither conservative nor aggressive. Investor 
  should monitor market trends and competitive activity closely. Upside 
  (GO) is achievable but requires execution; downside (CONDITIONAL HOLD) is 
  a real risk if market conditions adverse. Overall robustness: MODERATE.
```

---

## 6. Full Boundary Analysis Example: Series A SaaS Startup

### Starting Point (from /assess phase)

```
DOMAIN SCORES
  Domain 1 (Fit-to-Purpose): 75
  Domain 2 (Market Opportunity): 68
  Domain 3 (Product-Market Fit): 62
  Domain 4 (Business Model): 66
  Domain 5 (Operations): 70
  Domain 6 (Competitive Position): 64

Composite readiness: 68
Current determination: CONDITIONAL GO
Fit-to-purpose: Adequate
```

### Upward Flip Analysis

**Objective:** CONDITIONAL GO → GO (75 composite needed; +7 points)

**Upward flip candidates:**

| Domain | Current | Improvement Target | Gap | Evidence Path | Effort |
|--------|---------|---|---|---|---|
| Product-Market Fit (3) | 62 | 65 | +3 | Enterprise customer validation; 3-5 references | Moderate |
| Operations (5) | 70 | 72 | +2 | Complete hiring plan; advance VP Eng hire | Moderate |
| Business Model (4) | 66 | 68 | +2 | Model unit economics; prove CAC payback ≤18mo | Low |

**Total pathway:** +7 points via 3 domains | Effort = MODERATE | Timeline = 4-6 weeks

**Detailed evidence requirements:**

**Product-Market Fit (62 → 65):**
- Current gap: Limited TAM validation with enterprise customers
- Evidence needed:
  - Conduct 3-5 reference calls with enterprise beta customers
  - Document use cases; measure NPS/engagement
  - Show 50%+ of target enterprise segment has strong PMF signals
- Success criteria: Enterprise PMF validation improves from 35% to 50%
- Timeline: 4 weeks
- Risk level: Low (existing beta relationships)

**Operations (70 → 72):**
- Current gap: Hiring plan undefined; VP Engineering not in place
- Evidence needed:
  - Finalize 18-month org chart
  - Demonstrate VP Eng hire is imminent (offer pending or advanced stage)
  - Secure 1-2 additional key hires
- Success criteria: Hiring plan explicit; 1+ key hire shows strong signal (offer in hand)
- Timeline: 6 weeks
- Risk level: Moderate (market hiring conditions)

**Business Model (66 → 68):**
- Current gap: CAC and payback period undefined
- Evidence needed:
  - Analyze actual CAC from first customer cohort
  - Model customer lifetime value; compute payback period
  - Show payback ≤18 months under base case scenarios
- Success criteria: Unit economics are modeled; payback is ≤18 months
- Timeline: 3 weeks
- Risk level: Low (internal data)

**Distance-to-flip classification: MODERATE**
- 7 points needed; 3 domains; moderate evidence burden; 4-6 weeks
- Achievable with focused execution; 60-70% success probability

---

### Downward Flip Analysis

**Objective:** CONDITIONAL GO → CONDITIONAL HOLD (54 composite floor; -14 point tolerance)

**At-risk domains:**

| Domain | Current | Deterioration Scenario | Impact | Trigger Plausibility | Tolerance |
|--------|---------|---|---|---|---|
| Market Opportunity (2) | 68 | TAM contracts 30%; competitor 6-month entry | 68 → 52 (-16) | HIGH | 14 points |
| Operations (5) | 70 | Key hires fail; team attrition | 70 → 58 (-12) | MODERATE | 12 points |
| Business Model (4) | 66 | CAC increases 40%; payback 24+ months | 66 → 50 (-16) | MODERATE | 16 points |

**Single-domain deterioration:** Would require drop of ≥14 points in one domain to flip (only Market Opportunity easily achieves this)

**Multi-domain deterioration scenarios:**
- Market + Operations: 68 → 52 + 70 → 62 = -14 points → **Flips to CONDITIONAL HOLD**
- Market + Business Model: 68 → 52 + 66 → 60 = -12 points → **Does not flip** (still 56 composite)
- Operations + Business Model + Market (moderate): 68 → 62 + 70 → 66 + 66 → 62 = -14 points → **Flips to CONDITIONAL HOLD**

**Most vulnerable scenario:** Market slowdown + operations execution risk (two plausible, correlated risks)

**Early warning indicators:**
1. Market growth rate drops below 15% YoY
2. Competitor announces product launch
3. VP Eng recruiting extends beyond 4 weeks
4. Actual CAC exceeds model by >20%

**Safety margin assessment: MODERATE**
- Can tolerate 14-point deterioration before flip
- Single-domain deterioration alone (except market) insufficient
- Multi-domain deterioration (market + operations, or all three domains moderately) triggers flip
- Current safety margin is adequate but not strong

**Distance-to-flip classification: MODERATE**
- 14-point tolerance; likely requires 2+ domains affected
- Downward scenarios are plausible (market macro; execution risk)
- Safety margin is reasonable but not robust

---

### Asymmetry Analysis

```
UPWARD FLIP: 7 points needed across 3 domains (MODERATE effort)
DOWNWARD FLIP: 14 points tolerance; requires multi-domain deterioration (MODERATE risk)

Asymmetry: Slightly downside-fragile
  - Easier to deteriorate than improve (14 vs. 7 point thresholds)
  - Upward improvement is concentrated in 3 achievable domains
  - Downward risk is distributed (multiple plausible triggers)
  - Market conditions (external) are most sensitive factor

Implication: Determination is moderately robust. Investor should:
  1. Monitor market trends and competitive activity (highest downside risk)
  2. Track operations execution closely (hiring pipeline, team retention)
  3. Recognize upside (GO) is achievable with focused 4-6 week effort
  4. Be cautious of multi-domain adverse scenarios (rare but possible)
  
Overall sensitivity: MODERATELY ROBUST (asymmetrically downside-fragile)
```

---

### Final Boundary Analysis Output

```
BOUNDARY / FLIP-POINT ANALYSIS

UPWARD FLIP: CONDITIONAL GO → GO

Distance metric: MODERATE
  - 7 composite points needed
  - 3 domains: PMF validation, Operations, Business Model
  - Evidence burden: Moderate (customer refs, hiring, financial modeling)
  - Timeline: 4-6 weeks
  - Success probability: 60-70%

Key upward pathway:
  Domain 3 (PMF): 62 → 65 (+3) via enterprise customer validation [4 weeks, low risk]
  Domain 5 (Ops): 70 → 72 (+2) via hiring plan + VP Eng hire [6 weeks, moderate risk]
  Domain 4 (BM): 66 → 68 (+2) via unit economics modeling [3 weeks, low risk]

Interpretation: GO determination is achievable with focused evidence gathering. 
Not a trivial lift (requires 3 concurrent work streams), but realistic timeline 
and probability support pursuing this path during Series A process.

---

DOWNWARD FLIP: CONDITIONAL GO → CONDITIONAL HOLD

Distance metric: MODERATE
  - 14 point deterioration tolerance
  - Most at risk: Market Opportunity (14-point tolerance), Operations (12 points)
  - Likely trigger: Multi-domain stress (market slowdown + execution delay)
  - Safety margin: Moderate

Key downward risk scenarios:
  Scenario 1: Market slowdown + operations execution risk
    Market Opportunity: 68 → 52 (-16) [TAM contracts, competitor enters fast]
    Operations: 70 → 62 (-8) [hiring delays, team attrition signal]
    → Composite: 68 → 54 (CONDITIONAL HOLD) [FLIP TRIGGERED]
    
  Scenario 2: Balanced multi-domain deterioration
    Market: 68 → 62 (-6) [modest market slowdown]
    Operations: 70 → 66 (-4) [modest execution delays]
    Business Model: 66 → 62 (-4) [CAC increases slightly]
    → Composite: 68 → 54 (CONDITIONAL HOLD) [FLIP TRIGGERED]

Early warning indicators to monitor:
  - Market growth rate (threshold: 15% YoY; alert if <12%)
  - Competitive activity (track for entry signals)
  - VP Eng recruiting velocity (alert if >4 weeks)
  - Actual CAC vs. model (alert if >20% overage)
  - Team retention (founding team engagement signals)

Interpretation: Determination is vulnerable to coordinated adverse scenarios 
(market slowdown + execution challenges). Investor should maintain active 
monitoring and be prepared to reassess if early warning indicators appear. 
Single-factor deterioration alone is unlikely to trigger flip (except market 
opportunity, which has tight tolerance).

---

ASYMMETRY ASSESSMENT: BALANCED WITH DOWNSIDE FRAGILITY

Upward flip effort: MODERATE (7 points; 3 domains; 4-6 weeks)
Downward flip risk: MODERATE (14-point tolerance; multi-domain trigger)

Asymmetry direction: Slightly downside-fragile
  - Upward improvement is achievable but requires execution
  - Downward deterioration requires coordinated stress but is plausible
  - Market conditions (external risk) are most sensitive factor
  - Operations and execution (internal control) are secondary factors

Overall robustness classification: MODERATELY ROBUST

This determination can withstand single-domain stress but is vulnerable to 
multi-domain adverse conditions. Investor confidence should be tempered by 
external market risk and execution dependencies.
```

---

**End of boundary-analysis.md**
