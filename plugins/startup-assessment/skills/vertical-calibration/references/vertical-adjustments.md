# Vertical Adjustment Matrices and Examples

## Fintech Vertical: Complete Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Regulatory Status (D2) | Secondary | Primary | Hard | Hard | Elevated | ≥0.7 |
| License Strategy (D2) | Secondary | Primary | Hard | Hard | Elevated | ≥0.6 |
| KYC/AML Roadmap (D2) | Minimal | Primary | Hard | Hard | Elevated | ≥0.6 |
| Financial Risk Modeling (D8) | Minimal | Primary | Primary | Hard | Elevated | ≥0.5 |
| Data Security (D10) | Minimal | Primary | Primary | Hard | Elevated | ≥0.6 |
| Market Size (D1) | Primary | Primary | Secondary | Secondary | Unchanged | 0.5 |
| Unit Economics (D3) | Minimal | Primary | Hard | Hard | Unchanged | 0.7 |

**Weight adjustments by stage:**

**Pre-Seed Fintech:**
- D2: 0.20 → 0.30 (regulatory enters; product/solution weight reduced)
- D8: 0.02 → 0.05 (financial risk assessment)
- D10: 0.01 → 0.08 (data protection critical)
- Total reallocation: D2 +10%, D8 +3%, D10 +7%, offset by reducing D1 and other domains

**Seed Fintech:**
- D2: 0.15 → 0.22 (regulatory and compliance primary)
- D8: 0.02 → 0.08 (financial risk elevated to primary)
- D10: 0.00 → 0.10 (data security elevated to primary)
- Offset reductions: D1 −4%, D3 −4%, D6 −5% (management weighted less as compliance matters more)

**Series A Fintech:**
- D2: 0.08 → 0.15 (regulatory hard blocker)
- D8: 0.02 → 0.10 (financial risk primary)
- D10: 0.00 → 0.08 (data protection hard blocker)
- Offset: D1 −5%, D4 −3%, D6 −3%

### Hard Blockers Introduced

**At Pre-Seed:**
- None; regulatory assessed but not hard-blocker at idea stage

**At Seed:**
- Regulatory Status (D2) ≥0.6: License path must be identified
- KYC/AML Compliance Roadmap (D2) ≥0.5: Process design begun or planned

**At Series A+:**
- License/Regulatory Status (D2) ≥0.7: Explicit license in progress or secured
- Data Security (D10) ≥0.6: PCI-DSS compliance plan or equivalent
- Financial Risk Model (D8) ≥0.6: Risk assessment documented

### Example: Fintech B2B Pre-Seed Assessment

**Company:** Payment processing API startup (YC S23 company raising seed)

**Base framework (pre-seed):** D1, D2, D6 primary; D3, D5 secondary

**Fintech vertical adjustment applied:**
- D2 elevated: Regulatory and Compliance enters primary domain
- D8 elevated: Financial Risk Assessment becomes observable

**Adjusted framework:**
- D1: 0.20 (market/opportunity; payments market clear)
- D2: 0.28 (solution + regulatory + data security; two of three are regulatory)
- D3: 0.06 (business model secondary)
- D5: 0.08 (traction; early customers expected)
- D6: 0.24 (team; financial services expertise critical)
- D8: 0.08 (financial risk; payment processing means reconciliation and fraud risk)
- D10: 0.06 (data protection; payment data is sensitive)
- Others: minimal or deactivated

**Assessment findings:**
- D2 Regulatory Status: Status = "Applied for MSB license in 3 states; pending response"; Completeness = 0.5 (application in progress); Quality = 0.6 (reasonable roadmap but aggressive timeline)
- D8 Financial Risk: Status = "Payment reconciliation process documented; fraud detection TBD"; Completeness = 0.4; Quality = 0.4 (incomplete)
- D10 Data Security: Status = "PCI-DSS assessment underway; third-party assessor engaged"; Completeness = 0.5; Quality = 0.6 (proper third-party process)

**QA/QC note:** Financial risk (D8) is flagged as below threshold for fintech at this stage (0.4 < 0.5 minimum). Request fraud detection strategy document.

---

## Medtech Vertical: Complete Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Regulatory Pathway (D2) | Secondary | Hard | Hard | Hard | Elevated | ≥0.7 |
| Clinical Evidence (D5) | Minimal | Hard | Hard | Hard | Elevated | ≥0.6 |
| Patent Portfolio (D10) | Minimal | Primary | Hard | Hard | Elevated | ≥0.6 |
| Design Controls (D8) | Minimal | Secondary | Primary | Hard | Elevated | ≥0.5 |
| Problem Validation (D2) | Primary | Primary | Primary | Primary | Unchanged | 0.6 |
| Unit Economics (D3) | Minimal | Minimal | Secondary | Hard | Original | 0.7 |

**Weight adjustments by stage:**

**Pre-Seed Medtech:**
- D2: 0.20 → 0.25 (regulatory pathway identification)
- D10: 0.01 → 0.05 (IP assessment enters)
- Offset: D1 −0.02%, D3 −0.03%

**Seed Medtech:**
- D2: 0.15 → 0.25 (regulatory pathway hard blocker; design stage critical)
- D5: 0.15 → 0.20 (clinical evidence becomes primary evidence of viability)
- D10: 0.00 → 0.10 (patent strategy and IP freedom-to-operate)
- D8: 0.02 → 0.07 (design controls and safety assessment begins)
- Offset: D1 −0.08%, D3 −0.10%, D6 −0.09%

**Series A Medtech:**
- D2: 0.08 → 0.18 (regulatory pathway hard blocker; timeline and cost critical)
- D5: 0.20 → 0.22 (clinical evidence hard blocker; trial enrollment proof)
- D8: 0.02 → 0.12 (design controls hard blocker; safety documentation critical)
- D10: 0.00 → 0.12 (patent portfolio hard blocker; freedom-to-operate required)
- Offset: D1 −0.06%, D3 −0.04%, D4 −0.06%, D6 −0.08%

### Hard Blockers Introduced

**At Pre-Seed:**
- None; pathway being explored

**At Seed:**
- Regulatory Pathway (D2) ≥0.6: FDA classification or CE/MDR pathway identified
- Clinical Evidence Plan (D5) ≥0.5: Trial design or clinical validation plan documented
- Patent Strategy (D10) ≥0.5: Patent landscape search conducted or planned

**At Series A+:**
- Regulatory Pathway (D2) ≥0.7: License application in progress or granted
- Clinical Trial Status (D5) ≥0.6: Enrollment underway or completed; or pre-clinical validation data present
- Design Controls (D8) ≥0.6: Design history file or equivalent safety documentation
- Patent Portfolio (D10) ≥0.6: Freedom-to-operate analysis completed; patent strategy clear

### Example: Medtech Series A Assessment

**Company:** AI-powered radiology diagnosis tool (Class II medical device, 510(k) pathway)

**Base framework (Series A):** D3, D4, D5, D7 primary; D1, D2 secondary

**Medtech vertical adjustment applied:**
- D2 regulatory elevated to hard blocker
- D5 clinical evidence elevated to hard blocker
- D8 design controls elevated to primary
- D10 IP elevated to hard blocker

**Adjusted framework:**
- D1: 0.08 (market; medical imaging TAM clear)
- D2: 0.16 (clinical validation + regulatory; regulatory becomes ~50% of domain weight)
- D3: 0.14 (unit economics for healthcare selling)
- D4: 0.12 (GTM; hospital channel complexity)
- D5: 0.22 (traction now = clinical evidence + adoption + retention)
- D6: 0.12 (clinical team and hospital relationships)
- D7: 0.08 (financial projections)
- D8: 0.12 (design controls + safety + regulatory risk)
- D10: 0.10 (IP and patent portfolio)

**Assessment findings:**
- D2 Regulatory: Status = "510(k) application submitted; FDA response expected Q3 2024"; Completeness = 0.8; Quality = 0.8 (on track, well-documented)
- D5 Clinical Evidence: Status = "Retrospective validation study completed on 500 cases; 94% sensitivity, 88% specificity vs. radiologist consensus"; Completeness = 0.7; Quality = 0.7 (good validation, but prospective data preferred)
- D8 Design Controls: Status = "Design history file completed; FDA compliance review conducted"; Completeness = 0.8; Quality = 0.7
- D10 Patent Portfolio: Status = "3 utility patents granted; 2 pending; freedom-to-operate analysis shows clear space"; Completeness = 0.8; Quality = 0.8

**Assessment confidence:** High. Regulatory and clinical evidence both strong. IP protected.

---

## SaaS Vertical: Complete Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Unit Economics (D3) | Minimal | Primary | Hard | Hard | Elevated | 0.6-0.8 |
| Monthly Churn (D5) | Minimal | Hard | Hard | Hard | Elevated | 0.6 |
| Customer CAC (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| MRR Growth (D5) | Minimal | Primary | Primary | Hard | Elevated | 0.6 |
| LTV:CAC Ratio (D3) | Minimal | Secondary | Hard | Hard | Elevated | 0.6 |
| Expansion Revenue (D4) | Minimal | Secondary | Primary | Primary | Elevated | 0.5 |

**Weight adjustments by stage:**

**Seed SaaS:**
- D3: 0.08 → 0.15 (unit economics enters primary)
- D4: 0.10 → 0.14 (CAC and retention emphasis)
- D5: 0.15 → 0.20 (traction = revenue + retention + growth)
- Offset: D1 −0.10%, D2 −0.08%, D6 −0.06%

**Series A SaaS:**
- D3: 0.18 → 0.22 (unit economics hard blocker)
- D4: 0.17 → 0.18 (CAC and expansion)
- D5: 0.20 → 0.22 (traction includes cohort retention)
- D7: 0.10 → 0.08 (financial projections become less critical if unit economics clear)
- Offset: D1 −0.04%, D2 −0.03%, D8 −0.01%

**Series B SaaS:**
- D3: 0.16 → 0.20 (unit economics hard blocker at 0.8 threshold)
- D4: 0.16 → 0.18 (CAC and expansion hard blocker)
- D5: 0.18 → 0.20 (cohort analysis hard blocker)
- Offset: D1 −0.03%, D2 −0.02%, D8 −0.01%

### Hard Blockers Introduced

**At Seed:**
- Monthly Churn Rate (D5) ≥0.6: Must track and report monthly cohort churn
- Customer CAC (D4) ≥0.6: CAC calculated by channel

**At Series A:**
- Unit Economics (D3) ≥0.7: LTV and CAC calculated; LTV:CAC ≥3:1
- Monthly Churn (D5) ≥0.6: <10% monthly for seed or <5% for mature cohorts
- CAC Payback (D4) ≥0.6: <12 months payback period

**At Series B:**
- Unit Economics (D3) ≥0.8: Detailed cohort LTV/CAC analysis; LTV:CAC ≥5:1
- Monthly Churn (D5) ≥0.7: <5% monthly for mature cohorts
- Expansion Revenue (D4) ≥0.6: Net revenue retention (NRR) >100% for healthy SaaS

### Example: SaaS Series B Assessment

**Company:** B2B SaaS HR platform (Series B, $40M ARR, raising Series B)

**Base framework (Series B):** D3, D4, D5, D7 primary; D6, D1 secondary

**SaaS vertical adjustment applied:**
- Unit Economics hard blocker (0.8 threshold)
- Monthly Churn hard blocker
- CAC and expansion elevation

**Adjusted framework:**
- D1: 0.06 (market; HR tech TAM known)
- D2: 0.04 (product maturity; less weight)
- D3: 0.20 (unit economics hard blocker)
- D4: 0.18 (CAC, expansion revenue)
- D5: 0.22 (churn, retention, NRR hard blockers)
- D6: 0.12 (team; less critical at Series B)
- D7: 0.12 (financial projections; less critical if unit economics clear)
- D8: 0.04 (risk)
- D9: 0.02 (capital structure)
- D10: 0.00 (legal; minimal)

**Assessment findings:**
- D3 Unit Economics: LTV = $8,400 (calculated from 3-year customer lifetime); CAC = $1,600; LTV:CAC = 5.25:1; Payback = 2.4 months. Completeness = 0.9; Quality = 0.9 (strong)
- D5 Monthly Churn: Overall = 2.3% monthly; Cohort analysis shows range 1.8% (12+ months) to 3.5% (0-3 months). Completeness = 0.9; Quality = 0.9 (excellent data)
- D4 Expansion: NRR = 118% (customers expand into additional products over time). Completeness = 0.8; Quality = 0.8 (strong)

**Assessment result:** All hard blockers met; unit economics are healthy. Series B investment candidate.

---

## Marketplace Vertical: Complete Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Supply Definition (D1) | Primary | Primary | Hard | Hard | Elevated | 0.6 |
| Demand Definition (D1) | Primary | Primary | Hard | Hard | Elevated | 0.6 |
| Network Effects (D2) | Secondary | Hard | Hard | Hard | Elevated | 0.7 |
| Supply CAC (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Demand CAC (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Liquidity (D5) | Minimal | Secondary | Hard | Hard | Elevated | 0.6 |

**Weight adjustments by stage:**

**Seed Marketplace:**
- D1: 0.18 → 0.22 (supply and demand must be separately defined)
- D2: 0.15 → 0.20 (network effects thesis becomes critical)
- D4: 0.10 → 0.18 (dual-sided CAC measurement)
- D5: 0.15 → 0.18 (liquidity and transaction quality)
- Offset: D3 −0.08%, D6 −0.06%, D7 −0.04%

**Series A Marketplace:**
- D1: 0.10 → 0.16 (supply and demand hard blockers)
- D2: 0.08 → 0.16 (network effects hard blocker)
- D4: 0.17 → 0.20 (dual-sided CAC hard blockers)
- D5: 0.20 → 0.24 (liquidity hard blocker; transaction completion rate)
- Offset: D3 −0.04%, D6 −0.04%, D7 −0.04%, D8 −0.02%

### Hard Blockers Introduced

**At Seed:**
- Network Effects Thesis (D2) ≥0.6: Explicit mechanism explained
- Supply and Demand Definition (D1) ≥0.5: Both sides clearly scoped

**At Series A:**
- Supply Segment (D1) ≥0.6: Hard blocker; supply-side growth rate and count documented
- Demand Segment (D1) ≥0.6: Hard blocker; demand-side growth rate and count documented
- Network Effects (D2) ≥0.7: Hard blocker; mechanism validated with growth data
- Supply CAC (D4) ≥0.6: Hard blocker; supply-side acquisition cost measured
- Demand CAC (D4) ≥0.6: Hard blocker; demand-side acquisition cost measured
- Marketplace Liquidity (D5) ≥0.6: Hard blocker; transaction completion rate >80%

### Example: Marketplace Seed Assessment

**Company:** Peer-to-peer rental marketplace for specialty equipment (Series Seed)

**Base framework (Seed):** D1, D5, D6 primary; D3, D4 secondary

**Marketplace vertical adjustment applied:**
- D1 supply and demand both hard blockers
- D2 network effects elevated to primary
- D4 dual-sided CAC elevated to primary
- D5 liquidity elevated to hard blocker

**Adjusted framework:**
- D1: 0.22 (supply definition ≥0.5; demand definition ≥0.5)
- D2: 0.18 (network effects thesis ≥0.6)
- D3: 0.08 (revenue model; secondary)
- D4: 0.18 (supply CAC ≥0.6; demand CAC ≥0.6)
- D5: 0.18 (liquidity metrics hard blocker)
- D6: 0.12 (team)
- D7: 0.02 (financial; directional only)
- D8: 0.02 (risk)
- D10: 0.00 (legal minimal at seed)

**Assessment findings:**
- D1 Supply: 127 active equipment owners (tools, generators, camera gear, etc.); gross supply growing 15% MoM. Completeness = 0.7; Quality = 0.6
- D1 Demand: 340 renters (individuals and small contractors); demand growing 12% MoM. Completeness = 0.7; Quality = 0.6
- D2 Network Effects: "Supply-side growth drives more demand by increasing selection; demand growth attracts more supply by promising utilization." Mechanism understood but not yet validated. Completeness = 0.6; Quality = 0.5 (thesis present; validation pending)
- D4 Supply CAC: $45 per supplier acquisition (via owner referral program and Craigslist outreach). Completeness = 0.6; Quality = 0.5
- D4 Demand CAC: $18 per renter (organic search + word-of-mouth). Completeness = 0.6; Quality = 0.5
- D5 Liquidity: 72% of rental requests result in completed transaction (28% friction). Completeness = 0.6; Quality = 0.5 (acceptable at seed but room for improvement)

**Assessment result:** Marketplace axes defined. Network effects thesis plausible but not yet proven. Dual-sided CAC measured. Proceed to Series A validation phase.

