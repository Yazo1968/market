# The 3H Principle — Detailed Explanation with Examples

## Overview

The 3H Principle (Honest, Humble, Hedged) is the foundational constraint on all research conducted for the assessment framework. It governs how findings are presented, how uncertainty is communicated, and how confidence is expressed. Violations of the 3H Principle result in unreliable or misleading assessments.

---

## The Three Dimensions of 3H

### Dimension 1: HONEST

**Definition:** Findings must be presented exactly as they are, without distortion, suppression, or selective reporting. Submission claims and research findings are always distinguished and never blended.

**Core Rules:**
1. Every finding must be explicitly attributed to its source
2. When submission claims conflict with research findings, both must be stated
3. Never suppress contradictions to produce a "cleaner" narrative
4. Never infer or extrapolate from research to support the submission's story
5. Do not cherry-pick supporting findings while hiding contradictions

#### Example 1: HONEST — Direct Conflict

**Scenario:**
- Submission claims: "Market is growing 25% CAGR"
- Research finds: Gartner (2024) cites 15% CAGR; IDC (2024) cites 14% CAGR

**Honest Output:**
```
Market Growth Rate
- Submission claims: 25% CAGR
- Research findings: Gartner cites 15% CAGR; IDC cites 14% CAGR
- Gap: Submission's projection is 11 percentage points above published analyst consensus
- Implication: Submission's growth assumptions are significantly more aggressive than sector baseline
```

**DISHONEST Output (VIOLATION):**
```
Market Growth Rate
- The company projects 25% growth in a dynamic market segment
- [Hiding the analyst findings entirely]
```

**Why HONEST is better:** The assessor can see the gap and evaluate whether the company's more aggressive growth is justified (e.g., by superior product, market share capture, or market expansion). Hiding the gap prevents informed assessment.

#### Example 2: HONEST — Acknowledging Incompleteness

**Scenario:**
- Submission presents customer list of 12 companies
- Research finds public announcement of 8 of the 12 customers; 4 cannot be verified

**Honest Output:**
```
Customer Base
- Submission identifies 12 reference customers
- Public verification: 8 of 12 customers can be independently confirmed via press releases, case studies, or analyst reports
- Unverified: 4 customers are claimed but not independently verified
- Interpretation: Strong evidence of real customer traction; 67% verification rate is good but not complete
```

**DISHONEST Output (VIOLATION):**
```
Customer Base
- Company has 12 reference customers [Treating all as equally verified without noting the verification gaps]
```

**Why HONEST is better:** The assessor understands which claims are independently verified and which rest on the company's assertion. This allows calibrated confidence in the customer validation evidence.

#### Example 3: HONEST — Separating Data Types

**Scenario:**
- Company claims: "TAM is $500M based on internal market research"
- Research finds: Analyst reports cite $300–400M for the same market segment

**Honest Output:**
```
Total Addressable Market (TAM)
- Company's internal estimate: $500M
- Analyst estimates: $300M (source A), $400M (source B)
- Source of discrepancy: Company's estimate appears to include adjacent segments not included in analyst definitions
- Assessment: Company's TAM is 25–67% higher than analyst consensus; recommend clarifying segment boundaries
```

**DISHONEST Output (VIOLATION):**
```
TAM
- The market opportunity is substantial, with estimates in the $300–500M range
[Presenting the company's estimate alongside analyst estimates as if they're equal data points, obscuring that they use different definitions]
```

**Why HONEST is better:** Distinguishing the company's claim from independent research allows the assessor to understand the basis for the discrepancy and evaluate credibility of the company's more expansive TAM.

---

### Dimension 2: HUMBLE

**Definition:** Where uncertainty exists—sources conflict, coverage is incomplete, authoritative sources are inaccessible—that uncertainty is explicitly communicated with enough specificity for the assessor to make an informed judgment.

**Core Rules:**
1. Acknowledge what you know and what you do not know
2. Explicitly state coverage gaps (e.g., "Limited public data on private competitor revenue")
3. When sources conflict, document the conflict; never pick one and hide the other
4. If a source is inaccessible (paywall, geographic restriction), say so clearly
5. Do not claim confidence beyond what the evidence supports
6. Distinguish between certainty (verified fact) and reasonable inference

#### Example 1: HUMBLE — Acknowledging Gaps

**Scenario:**
- Research goal: Verify competitive market share
- Available data: Market share for three public competitors; private competitors' data unavailable
- Research result: Unable to determine complete competitive landscape

**Humble Output:**
```
Competitive Market Position
- Public competitors: Company A (35% share), Company B (28% share), Company C (15% share)
- Private competitors: Market includes 15+ private companies; public market share data is unavailable
- Interpretation: Company enters a market with established public players; exact competitive positioning against private competitors cannot be independently determined
- Recommendation: Request company to provide evidence of competitive positioning (e.g., customer selection criteria, pricing strategy relative to competitors, win/loss analysis)
```

**ARROGANT Output (VIOLATION):**
```
Competitive Market Position
- The market is dominated by Company A (35%), Company B (28%), Company C (15%)
[Implying these three account for the full market, ignoring the 15+ private competitors and making false claim of market completeness]
```

**Why HUMBLE is better:** The assessor understands the limits of what was verified. They can independently decide whether the gap in private competitor data is material to their assessment, rather than being misled into thinking the market is fully mapped.

#### Example 2: HUMBLE — Acknowledging Source Conflict

**Scenario:**
- Research goal: Verify company's valuation benchmarks
- Finding 1: Gartner reports median Series A valuation for software companies is $30M
- Finding 2: Company data from VC firms suggests typical Series A valuation is $25M
- Finding 3: This company is requesting $50M Series A

**Humble Output:**
```
Series A Valuation Benchmarks
- Gartner (2024): Median Series A valuation is $30M for software companies
- VC market data: Typical Series A range is $20–30M depending on sector and traction
- This company's request: $50M Series A (67% above median benchmark)
- Interpretation: Company's valuation request is notably higher than typical Series A. This may reflect exceptionally strong traction, premium market dynamics, or calibration issue.
- Recommendation: Request company to justify valuation relative to customer traction, growth metrics, and comparable funded companies in the sector.
```

**ARROGANT Output (VIOLATION):**
```
Series A Valuation
- Typical Series A valuations in software are $25–30M
[Implying the company's $50M request is simply unreasonable without acknowledging that exceptionally strong companies do command higher valuations, and without inviting the company to justify their case]
```

**Why HUMBLE is better:** The assessor understands the benchmark and the deviation, but is invited to calibrate their judgment based on the company's specific case rather than being told what to conclude.

#### Example 3: HUMBLE — Acknowledging Inaccessible Sources

**Scenario:**
- Research goal: Verify private competitor funding
- Finding: Multiple sources reference funding round, but the most detailed source is behind a paywall (CB Insights)

**Humble Output:**
```
Competitive Funding
- Public sources: TechCrunch reports Competitor X raised $25M Series B in Q3 2023
- Detailed source: CB Insights maintains private company funding database; specific terms and lead investors are behind paywall (subscription required)
- Accessible information: Amount ($25M) and rough timing (Q3 2023) are confirmed from public announcement; detailed investor and term information is not accessible
- Recommendation: If detailed competitive term benchmarking is critical, recommend company provide access to CB Insights report or request company to provide comparable transaction analysis from research services
```

**ARROGANT Output (VIOLATION):**
```
Competitive Funding
- Competitor X raised $25M Series B
[Treating available public data as complete competitive benchmarking without acknowledging the detailed term information that exists but is inaccessible]
```

**Why HUMBLE is better:** The assessor understands what is publicly known vs. what exists but is inaccessible. If detailed term benchmarking matters to their assessment, they can request the company provide that information.

---

### Dimension 3: HEDGED

**Definition:** Where findings carry uncertainty, output must hedge proportionally to that uncertainty. Never express confidence stronger than the evidence warrants.

**Core Rules:**
1. Use confidence language proportional to evidence strength
2. "Likely" and "appears" for single-source findings; "is" for corroborated findings
3. Never use definitive language ("definitely," "clearly") for single-sourced or inferred findings
4. Distinguish between what is directly verified and what requires logical inference
5. Hedge inference ("appears to suggest") more strongly than direct findings ("confirms")

#### Hedging Language Hierarchy

| Evidence Strength | Language | Example |
|---|---|---|
| **Verified (authoritative single source, direct match)** | "X is [finding]" | "TAM is $250B per Gartner research" |
| **Corroborated (multiple sources agree)** | "X is [finding]; confirmed by N sources" | "TAM is $250B; confirmed by Gartner and IDC" |
| **Inferred (requires logical reasoning)** | "X appears to [finding]" or "X likely [finding]" | "Company appears to target enterprise SaaS based on team background and product positioning" |
| **Unverified (source identified but inaccessible)** | "X cannot be determined; [source] is inaccessible" | "Specific CAC cannot be determined; company financial details are not publicly available" |
| **Conflicted (sources disagree)** | "X may be [finding A] or [finding B]; sources differ" | "Market growth may be 15% (IDC) or 20% (Gartner); different segment definitions" |

#### Example 1: HEDGING INFERENCE

**Scenario:**
- Research: Found company team bios and LinkedIn profiles showing 3/5 team members have prior SaaS experience
- Research: Company is positioning in enterprise SaaS market
- Logical inference: Team has relevant experience for this market

**Hedged Output (COMPLIANT):**
```
Team Market Fit
- Evidence: 3 of 5 core team members have prior SaaS company experience (5+ years each)
- Company positioning: Enterprise SaaS (confirmed from website, job postings)
- Inference: Team appears well-suited for the target market; prior SaaS experience is relevant to product and customer dynamics
- Confidence: Medium (inferred from background, not from prior success in identical market segment)
```

**OVER-HEDGED Output (also compliant but less useful):**
```
Team Market Fit
- Evidence: Some team members may have SaaS experience
[Hedging so much that the positive signal is lost]
```

**UNDER-HEDGED Output (VIOLATION):**
```
Team Market Fit
- The team clearly has extensive SaaS expertise
[Using "clearly" without acknowledging that 2/5 members lack SaaS background, and that prior SaaS work is different from prior success in this company's specific market segment]
```

**Why correct hedging is better:** "Appears" signals that this is an inference supported by evidence, not a verified fact. The assessor can weigh this inference appropriately alongside other evidence about team capability.

#### Example 2: HEDGING CORROBORATED vs. SINGLE-SOURCE

**Scenario A — Single Source:**
- Research: Gartner reports cloud computing market will grow 18% CAGR through 2026
- Finding: This is a direct statement from one authoritative source

**Hedged Output (COMPLIANT):**
```
Market Growth — Cloud Computing
- Gartner projects 18% CAGR through 2026
- Confidence: Medium-High (authoritative source; published methodology; represents analyst consensus for this segment)
```

**Scenario B — Corroborated:**
- Research: Gartner reports cloud computing market will grow 18% CAGR through 2026
- Research: IDC independently reports 17% CAGR for the same segment through 2026
- Finding: Two major analyst firms converge on ~17–18% growth

**Hedged Output (COMPLIANT):**
```
Market Growth — Cloud Computing
- Gartner projects 18% CAGR through 2026; IDC projects 17% CAGR
- Confidence: High (two independent authoritative sources converge on similar projection; convergence reduces outlier risk)
```

**Why the distinction matters:** Single-source findings, even from authoritative sources, carry the risk that one analyst got it wrong. Corroboration from multiple sources significantly increases confidence. Hedging language should reflect this difference.

#### Example 3: HEDGING DIRECT VERIFICATION

**Scenario:**
- Research: Retrieve SEC filing for public company
- Finding: Filing states company revenue was $100M in FY2023

**Hedged Output (COMPLIANT):**
```
Company Revenue — [Public Company]
- FY2023 revenue: $100M (per SEC 10-K filing, confirmed in earnings release)
- Confidence: Very High (directly verified from audited financial statements)
```

**Non-hedged (acceptable for verified facts):**
```
Company Revenue — [Public Company]
- FY2023 revenue is $100M per SEC 10-K filing
[No hedge needed; this is a directly verified fact from official documents]
```

**Over-hedged (VIOLATION):**
```
Company Revenue — [Public Company]
- FY2023 revenue appears to be approximately $100M (based on some sources)
[Over-hedging a directly verified fact reduces credibility and suggests uncertainty where none exists]
```

**Why appropriate hedging for verified facts is important:** Verified facts do not require hedging language ("appears," "likely"). Using hedging language for verified facts undermines confidence in findings that are actually solid, while under-hedging inference makes speculation appear certain.

---

## Common Violations and Corrections

### Violation 1: BLENDING SUBMISSION CLAIM WITH RESEARCH FINDING

**Violation:**
```
Market Opportunity
- The company estimates the market will reach $500M by 2026, with annual growth of 20%, representing a substantial opportunity.
```

**Problem:** The output doesn't distinguish between the company's projection (submission claim) and the supporting evidence for that projection. If the company's $500M estimate is actually higher than analyst estimates, the reader can't tell.

**Correction:**
```
Market Opportunity
- Company projection: $500M TAM by 2026, 20% annual growth
- Research findings: Analyst reports (Gartner, IDC) cite current market size of $300M with 15% CAGR
- Gap: Company projects market 67% larger and growing 33% faster than analyst consensus
- Assessment: Company's projection is materially more aggressive than published forecasts; recommend company explain growth assumptions
```

---

### Violation 2: HIDING CONFLICTING DATA

**Violation:**
```
Customer Validation
- The company has demonstrated strong customer adoption with reference customers including [lists 3 companies], indicating strong market demand.
```

**Problem:** The submission lists 5 reference customers, but research only verified 3 of them. By listing only the verified customers without noting the discrepancy, the output hides the verification gap.

**Correction:**
```
Customer Validation
- Submission lists 5 reference customers
- Public verification: 3 of 5 customers can be independently confirmed through press releases or case studies
- Unverified: 2 customers are claimed but cannot be independently verified
- Assessment: Strong evidence of real customer adoption; however, 40% of claimed reference customers lack public verification
- Recommendation: Request company to provide evidence (customer contact, case study, or mutual NDA release) for the 2 unverified customers
```

---

### Violation 3: OVER-CONFIDENT INFERENCE

**Violation:**
```
Competitive Positioning
- Company's technology clearly differentiates the product from competitors based on the AI-powered analytics capabilities.
```

**Problem:** The output claims "clearly" differentiates, but research only found that the company claims AI capabilities; competitor products were not directly evaluated, so the differentiation claim is inference, not fact.

**Correction:**
```
Competitive Positioning
- Company claims: AI-powered analytics capabilities
- Competitive evidence: Competitor products reviewed via product websites and G2 reviews; most competitors cite "rule-based" or "rule-and-analytics" approaches
- Inference: Company appears to offer more AI-powered automation than competitors; however, no direct technical assessment of underlying AI sophistication was conducted
- Recommendation: Request technical white papers or product demos to validate the depth of AI differentiation; competitor technical assessment from third-party review
```

---

### Violation 4: TREATING TRAINING KNOWLEDGE AS RESEARCH

**Violation:**
```
Market Growth
- The SaaS market typically grows at 20% annually, and this company's projection of 15% growth appears conservative.
```

**Problem:** The output presents "typical 20% growth" as if it's research finding, when it's actually general knowledge from training data. It's not based on current live data, and it's compared against the company's projection without citing sources.

**Correction:**
```
Market Growth
- Company projection: 15% CAGR for its market segment
- General industry baseline: SaaS market has historically grown at ~18–22% annually; however, this should be verified against current segment-specific data
- Live research findings: [Gartner reports 16% growth for this specific segment; IDC reports 14%]
- Assessment: Company's 15% projection aligns with published analyst estimates for its specific segment
```

---

### Violation 5: ACKNOWLEDGING UNCERTAINTY TOO WEAKLY

**Violation:**
```
Regulatory Status
- The company does not appear to require FDA approval.
```

**Problem:** For a regulated product, regulatory status is critical. Saying "does not appear to" is dangerously weak hedging if the actual regulatory status is uncertain. This is a hard blocker module and needs to be explicitly verified.

**Correction:**
```
Regulatory Status — FDA Approval Requirement
- Company claim: "No FDA approval required"
- Research: FDA guidance reviewed for device classification
- Finding: Company's product classification is unclear from public sources; regulatory status cannot be independently verified
- CRITICAL: Regulatory status is unresolvable from public sources
- Recommendation: **Request company to provide written regulatory assessment from qualified counsel confirming product class and approval pathway**
- Until verified: Regulatory compliance cannot be scored; hard-blocker gate may be triggered
```

---

## Summary: 3H in Practice

| Principle | Golden Rule | Test Question |
|---|---|---|
| **HONEST** | Never blend claims with findings; always distinguish. | "Can the assessor tell which parts are the company's claims and which parts are independent research?" |
| **HUMBLE** | Acknowledge what you don't know; flag gaps explicitly. | "Does the output acknowledge limitations and gaps in available data?" |
| **HEDGED** | Use confidence language proportional to evidence strength. | "Is the language (is/appears/likely/cannot determine) calibrated to the evidence available?" |

All three principles must be satisfied simultaneously. Violation of any one principle undermines the integrity of the entire assessment.
