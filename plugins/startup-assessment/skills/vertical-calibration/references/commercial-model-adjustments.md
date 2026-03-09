# Commercial Model Adjustment Matrices and Examples

## B2B Commercial Model: Complete Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Sales Cycle (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Customer CAC (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| ACV (D3) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Customer Concentration (D3) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Customer References (D5) | Minimal | Secondary | Primary | Hard | Elevated | 0.5 |
| Contract Terms (D10) | Minimal | Minimal | Secondary | Primary | Elevated | 0.5 |

**Weight adjustments by stage:**

**Seed B2B:**
- D3: 0.08 → 0.14 (ACV and concentration enter primary)
- D4: 0.10 → 0.16 (sales cycle and CAC primary)
- D5: 0.15 → 0.16 (references become observable)
- Offset: D1 −0.05%, D2 −0.04%, D6 −0.03%

**Series A B2B:**
- D3: 0.18 → 0.20 (ACV and concentration hard blockers)
- D4: 0.17 → 0.20 (CAC and sales cycle hard blockers)
- D5: 0.20 → 0.18 (references hard blocker; retention secondary)
- D10: 0.00 → 0.04 (contract terms enter)
- Offset: D1 −0.04%, D2 −0.02%, D8 −0.02%

**Series B B2B:**
- All B2B modules at hard blocker (0.6 threshold minimum)
- D3: 0.16 → 0.18 (concentration risk assessed)
- D4: 0.16 → 0.18 (sales execution and expansion)
- D10: 0.00 → 0.04 (contract terms and lock-in)

### Hard Blockers Introduced

**At Seed:**
- Sales Cycle Length (D4) ≥0.5: Sales process documented; cycle length quantified
- Customer CAC (D4) ≥0.5: CAC tracked for first customers
- Average Contract Value (D3) ≥0.5: Pricing model established; deals have financial substance

**At Series A:**
- Sales Cycle (D4) ≥0.6: Sales process with defined stages and conversion rates
- Customer CAC (D4) ≥0.6: CAC calculated; payback period <24 months
- ACV (D3) ≥0.6: Minimum $50K ACV documented (if lower, reassess as SMB-focused)
- Customer Concentration (D3) ≥0.6: No customer >30% of revenue
- Customer References (D5) ≥0.5: Minimum 2-3 referenceable accounts

**At Series B:**
- All B2B modules above at hard blocker (0.6+ threshold)
- Contract Terms (D10) ≥0.5: Standard contracts documented; lock-in and renewal terms understood

### Example: Enterprise SaaS Series A Assessment

**Company:** Security and compliance platform (Series A, landing enterprise customers, $1.2M ARR)

**Base framework (Series A):** D3, D4, D5 primary; D1, D6 secondary

**B2B commercial model adjustment applied:**
- Sales cycle and CAC elevated to hard blocker
- ACV and concentration elevated to hard blocker
- References elevated to hard blocker
- Contract terms enter assessment

**Adjusted framework:**
- D1: 0.08 (market; security TAM large but competitive)
- D2: 0.06 (product; relatively less critical)
- D3: 0.20 (ACV ≥0.6, concentration ≥0.6 hard blockers)
- D4: 0.22 (sales cycle ≥0.6, CAC ≥0.6 hard blockers)
- D5: 0.18 (retention and references hard blockers)
- D6: 0.12 (team; enterprise sales expertise critical)
- D7: 0.08 (financial projections)
- D8: 0.04 (risk)
- D10: 0.02 (contract terms)

**Assessment findings:**
- D3 ACV: Average contract value = $85K (range $30K–$400K). Top 5 customers = $310K (26% of revenue). Completeness = 0.8; Quality = 0.8 (healthy concentration)
- D4 Sales Cycle: 4–6 months from initial contact to signature (typical for enterprise); 3 SDRs → 8 AEs; conversion rate 15% from qualified leads to deal. Completeness = 0.8; Quality = 0.8 (well-defined)
- D4 CAC: Blended CAC = $32K (includes sales + marketing + implementation support); CAC payback = 4.6 months. Completeness = 0.8; Quality = 0.8 (strong)
- D5 References: 4 enterprise customers willing to serve as references (out of 15 total enterprise customers); all with 10+ seat deployments. Completeness = 0.8; Quality = 0.8
- D10 Contract Terms: 2-year lock-in standard; auto-renewal with 90-day notice. Completeness = 0.6; Quality = 0.6

**Assessment result:** All B2B hard blockers met. Strong enterprise go-to-market. Series A investment ready.

---

## B2C Commercial Model: Complete Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Marketing CAC (D4) | Minimal | Hard | Hard | Hard | Elevated | 0.6 |
| Channel Effectiveness (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.5 |
| Churn Rate (D5) | Minimal | Hard | Hard | Hard | Elevated | 0.6 |
| LTV (D3) | Minimal | Secondary | Hard | Hard | Elevated | 0.6 |
| LTV:CAC Ratio (D3) | Minimal | Minimal | Hard | Hard | Elevated | 0.5 |
| Brand Positioning (D1) | Secondary | Secondary | Primary | Hard | Elevated | 0.4 |

**Weight adjustments by stage:**

**Seed B2C:**
- D1: 0.18 → 0.14 (market less critical; acquisition more critical)
- D3: 0.08 → 0.12 (LTV and unit economics enter)
- D4: 0.10 → 0.18 (CAC and channel effectiveness primary; hard blocker)
- D5: 0.15 → 0.20 (churn hard blocker; retention critical)
- Offset: D2 −0.03%, D6 −0.05%, D7 −0.02%

**Series A B2C:**
- D1: 0.10 → 0.12 (brand positioning becomes observable)
- D3: 0.18 → 0.20 (LTV:CAC hard blocker)
- D4: 0.17 → 0.20 (CAC and channel hard blockers)
- D5: 0.20 → 0.20 (churn hard blocker; stable)
- Offset: D2 −0.03%, D6 −0.03%, D7 −0.03%

### Hard Blockers Introduced

**At Seed:**
- CAC (D4) ≥0.6: CAC tracked by channel; minimum $5 CAC (depends on price point)
- Churn Rate (D5) ≥0.6: Monthly cohort churn calculated

**At Series A:**
- CAC (D4) ≥0.6: CAC by channel; payback period <6 months
- Churn Rate (D5) ≥0.6: Monthly churn <10% (depends on category; 5% better)
- LTV:CAC Ratio (D3) ≥0.5: Minimum 3:1 at Series A; 5:1 is healthy
- LTV (D3) ≥0.6: LTV estimated or calculated from historical data

### Example: D2C E-Commerce Series A Assessment

**Company:** Direct-to-consumer apparel brand (Series A, $8M revenue, raising Series A)

**Base framework (Series A):** D1, D3, D4, D5 primary; D6 secondary

**B2C commercial model adjustment applied:**
- CAC and channel effectiveness hard blockers
- Churn rate hard blocker
- LTV:CAC hard blocker
- Brand positioning primary

**Adjusted framework:**
- D1: 0.12 (brand positioning; market size secondary)
- D2: 0.05 (product; less critical)
- D3: 0.20 (LTV and LTV:CAC hard blockers)
- D4: 0.22 (CAC and channel hard blockers)
- D5: 0.20 (churn hard blocker)
- D6: 0.10 (team; founder brand important)
- D7: 0.08 (financial projections)
- D8: 0.02 (risk)
- D9: 0.01 (capital structure)

**Assessment findings:**
- D4 CAC: Paid social (Instagram, TikTok) = $22 CAC; organic/email = $2 (attributed); blended = $18. Completeness = 0.8; Quality = 0.8 (healthy mix)
- D4 Channel: 65% paid social, 25% email/organic, 10% affiliates/influencer. Completeness = 0.7; Quality = 0.6 (over-reliant on paid social)
- D5 Churn: Month 1 = 8.5%; Month 3 = 6.2%; Month 12 = 4.1%. Completeness = 0.8; Quality = 0.8 (healthy retention curve)
- D3 LTV: 18-month customer lifetime; average order value $65; repeat purchase rate 25% within 12 months; LTV = $195. Completeness = 0.7; Quality = 0.7 (based on actual cohorts)
- D3 LTV:CAC: LTV $195 / CAC $18 = 10.8:1. Completeness = 0.8; Quality = 0.8 (excellent)
- D1 Brand: Strong brand recognition in millennial female apparel segment; Instagram following 250K; social proof evident. Completeness = 0.7; Quality = 0.7

**Assessment result:** Excellent unit economics. Brand strong. Over-reliance on paid social flagged as risk; recommend channel diversification. Series A ready.

---

## Platform Commercial Model: Complete Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Network Effects (D2) | Secondary | Hard | Hard | Hard | Elevated | 0.6-0.7 |
| Defensibility (D2) | Secondary | Secondary | Primary | Hard | Elevated | 0.5-0.6 |
| Monetization Timing (D3) | Minimal | Secondary | Hard | Hard | Elevated | 0.6 |
| Creator Retention (D5) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| User Engagement (D5) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Ecosystem Health (Custom) | Minimal | Secondary | Primary | Hard | Elevated | 0.5 |

**Weight adjustments by stage:**

**Seed Platform:**
- D2: 0.15 → 0.22 (network effects and defensibility primary)
- D3: 0.08 → 0.10 (monetization timing secondary)
- D5: 0.15 → 0.22 (creator and user engagement primary)
- Add: Ecosystem Health (custom module): 0.04
- Offset: D1 −0.10%, D4 −0.06%, D6 −0.05%

**Series A Platform:**
- D2: 0.08 → 0.18 (network effects hard blocker; defensibility primary)
- D3: 0.18 → 0.20 (monetization timing hard blocker)
- D5: 0.20 → 0.24 (creator and user engagement hard blockers)
- Ecosystem Health: 0.04 → 0.08
- Offset: D1 −0.04%, D4 −0.06%, D6 −0.04%

### Hard Blockers Introduced

**At Seed:**
- Network Effects Thesis (D2) ≥0.6: Mechanism explained; at least one side growing
- Creator/Supplier Retention (D5) ≥0.5: Repeat content/contribution from creators

**At Series A:**
- Network Effects (D2) ≥0.7: Growth accelerating; 2+ sides of platform showing network growth
- Defensibility (D2) ≥0.6: Defensibility mechanism clear (data, switching costs, standardization, etc.)
- Monetization Model (D3) ≥0.6: Explicit monetization timeline and model identified
- Creator Retention (D5) ≥0.6: High repeat contribution rate; creator cohort analysis
- User Engagement (D5) ≥0.6: Repeat usage and session frequency tracked
- Ecosystem Health (Custom) ≥0.5: Platform density and quality of content/supply assessed

### Example: Creator Platform Series A Assessment

**Company:** Creator monetization platform (Seed-to-Series A transition; 50K creators, 2M users)

**Base framework (Series A):** D1, D3, D4, D5 primary; D6 secondary

**Platform commercial model adjustment applied:**
- Network effects elevated to hard blocker (0.7)
- Defensibility elevated to primary (0.6)
- Monetization timing hard blocker (0.6)
- Creator and user retention hard blockers (0.6)
- Ecosystem health elevated

**Adjusted framework:**
- D1: 0.08 (market; creator economy TAM growing)
- D2: 0.18 (network effects ≥0.7; defensibility ≥0.6)
- D3: 0.20 (monetization hard blocker; timing critical)
- D4: 0.12 (go-to-market; creator acquisition)
- D5: 0.26 (creator and user retention hard blockers; ecosystem health)
- D6: 0.10 (team; platform/network expertise critical)
- D7: 0.04 (financial; monetization timing more important)
- D8: 0.02 (risk)

**Assessment findings:**
- D2 Network Effects: 50K creators generating content; 2M users consuming; 120% YoY creator growth; 90% YoY user growth. Mechanism: supply growth attracts users; user growth attracts creators. Evidence present. Completeness = 0.8; Quality = 0.8 (strong)
- D2 Defensibility: "Creator base is sticky due to direct payment relationships and audience portability; competitive differentiation is monetization efficiency (90% payout vs. 70% for competitors)." Defensibility is thin (model easily replicated). Completeness = 0.5; Quality = 0.4 (weak)
- D3 Monetization: Currently: free for creators and users (no revenue). Plan: 10% transaction fee on creator payouts starting Month 18 (at 500K creator milestone). Completeness = 0.7; Quality = 0.5 (timeline aggressive; monetization timing unvalidated)
- D5 Creator Retention: 35% of creators post more than once per month; 65% inactive (post <1x per month). Month-over-month creator churn = 12%. Completeness = 0.6; Quality = 0.5 (engagement below desired threshold)
- D5 User Engagement: Average session = 18 minutes; 40% DAU/MAU ratio. Completeness = 0.7; Quality = 0.6

**Assessment result:** Network effects present but defensibility weak. Monetization timing ambitious and unvalidated. Creator engagement lower than ideal for Series A platform. Flag monetization strategy for deeper discussion; platform model needs stronger defensibility thesis. Conditional Series A candidate.

---

## B2B2C Commercial Model: Adjustment Matrix

### Module Criticality Changes

| Module (Domain) | Pre-Seed | Seed | Series A | Series B | Adjustment | Threshold |
|--------|----------|------|----------|----------|-----------|-----------|
| Channel Strategy (D4) | Minimal | Hard | Hard | Hard | Elevated | 0.6 |
| Partner Acquisition (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.5 |
| Revenue Split (D3) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Dual CAC (D4) | Minimal | Primary | Hard | Hard | Elevated | 0.6 |
| Partner Concentration (D3) | Minimal | Secondary | Hard | Hard | Elevated | 0.6 |
| Data Governance (D10) | Minimal | Minimal | Primary | Primary | Elevated | 0.5 |

**Weight adjustments by stage:**

**Seed B2B2C:**
- D3: 0.08 → 0.12 (revenue split and partner concentration)
- D4: 0.10 → 0.20 (channel, partner acquisition, dual CAC primary)
- D10: 0.01 → 0.02 (data governance emerges)
- Offset: D1 −0.04%, D5 −0.04%, D6 −0.03%

**Series A B2B2C:**
- D3: 0.18 → 0.22 (concentration and split hard blockers)
- D4: 0.17 → 0.22 (all B2B2C modules hard blockers)
- D10: 0.00 → 0.04 (data governance primary)
- Offset: D1 −0.05%, D2 −0.02%, D6 −0.03%

### Hard Blockers Introduced

**At Seed:**
- Channel Strategy (D4) ≥0.5: Partner/platform identified; partnership in discussion
- Revenue Split (D3) ≥0.5: Economic model defined (even if unfinalized)
- Dual CAC (D4) ≥0.5: Partner acquisition cost + end-consumer acquisition cost tracked separately

**At Series A:**
- Channel Strategy (D4) ≥0.6: Partner/platform partner agreement signed or LOI
- Partner Acquisition (D4) ≥0.6: Multiple partners in pipeline; not single-partner dependency
- Revenue Split (D3) ≥0.6: Revenue share terms negotiated; split documented
- Dual CAC (D4) ≥0.6: Separate metrics for partner CAC and end-consumer CAC
- Partner Concentration (D3) ≥0.6: No single partner >60% of revenue

### Example: Payroll Integration Platform Series A Assessment

**Company:** Payroll benefits distribution B2B2C platform (raises Series A via integration with major payroll partners)

**Base framework (Series A):** D3, D4, D5 primary; D1, D6 secondary

**B2B2C commercial model adjustment applied:**
- Channel strategy hard blocker
- Partner acquisition hard blocker
- Revenue split hard blocker
- Dual CAC hard blocker
- Partner concentration hard blocker
- Data governance elevated to primary

**Adjusted framework:**
- D1: 0.06 (market; benefits distribution market defined)
- D3: 0.22 (revenue split and concentration hard blockers)
- D4: 0.24 (channel, partner acquisition, dual CAC hard blockers)
- D5: 0.16 (end-consumer adoption)
- D6: 0.12 (team; partnership execution critical)
- D7: 0.08 (financial projections)
- D8: 0.04 (risk; partner dependency)
- D10: 0.08 (data governance; employee benefits data sensitive)

**Assessment findings:**
- D4 Channel: Integrated with ADP and Paylocity (2 largest payroll platforms, ~60% US SMB market). Completeness = 0.8; Quality = 0.8
- D4 Partner Acquisition: ADP partnership = 3-year contract, 60% revenue split (40% to platform). Paylocity = 2-year contract, 55% revenue split. Additional 3 partners in LOI. Completeness = 0.8; Quality = 0.7
- D3 Revenue Split: 40% to company, 60% to partner (ADP); structure allows co-branding. Completeness = 0.8; Quality = 0.6 (80/20 favorable to payroll partner is standard)
- D4 Dual CAC: Partner-driven end-user acquisition cost = $0 (driven by partner); company acquisition cost for additional users = $45 (marketing). Completeness = 0.7; Quality = 0.6
- D3 Partner Concentration: ADP = 65% of projected Year 1 revenue; Paylocity = 25%; other = 10%. Completeness = 0.7; Quality = 0.5 (concentration risk present)
- D10 Data Governance: HIPAA compliance plan documented; DPA with partners in negotiation. Completeness = 0.6; Quality = 0.5 (late-stage work)

**Assessment result:** Partner channel validated. Revenue model acceptable (though partner-favorable). Concentration risk above 0.6 threshold; mitigation critical. Data governance needs acceleration. Series A candidate with conditions on partner diversification timeline.

