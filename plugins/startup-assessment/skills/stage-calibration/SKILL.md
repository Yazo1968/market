---
name: stage-calibration
description: >
  This skill should be used when framework-builder needs to calibrate domain emphasis and module
  criticality based on the identified funding stage. Trigger phrases: "stage calibration",
  "adjust for stage", "pre-seed framework", "seed framework", "Series A weights", "stage weights",
  "funding stage emphasis", "stage-appropriate scoring".
version: 0.1.0
---

# Stage Calibration Reference

## Introduction

This is a reasoning reference for dynamic framework calibration. Apply it in combination with vertical and commercial model context. The plugin applies this logic—it does not execute a fixed configuration table. Stage calibration modifies the base assessment framework by elevating or deactivating domains and modules based on the company's funding stage.

## Section 1: Stage Calibration Logic

### Pre-Seed

**Emphasis:** Team quality, problem validity, and early thesis credibility dominate. Financial history is largely absent. Legal formalization is minimal.

**Primary domains:**
- Market and Opportunity (D1)
- Solution and Product (D2)
- Management (D6)

**Secondary domains:**
- Business Model (D3)
- Traction (D5—early signals only)

**Typically inactive or minimal:**
- Financial Performance (D7—historical)
- Capital Structure (D9)
- Legal and Governance (D10—unless red flags present)

**Framework behavior:** Domain 6 (Management) carries highest weight. Financial models are directional only. Traction evidence is early signals—conversations, pilot intent, waitlists, user testing—not revenue. Absence of advisors or domain expertise is a critical gap at this stage.

**Key calibration:** Do NOT penalize absence of revenue, formal financials, or polished unit economics at pre-seed. Penalize absence of problem insight, team credibility, and market understanding. A pre-seed submission with no revenue is expected; a pre-seed submission with no evidence of customer conversations or market validation is a failure.

### Seed

**Emphasis:** Commercial thesis is tested. Early traction signals and initial business model evidence begin to matter. Team remains primary but must show execution capability.

**Primary domains:**
- Market and Opportunity (D1)
- Management (D6)
- Solution and Product (D2)
- Traction (D5)

**Secondary domains:**
- Business Model (D3)
- Go-to-Market (D4)

**Typically inactive or minimal:**
- Financial Performance (D7—historical)
- Capital Structure detail (D9)

**Framework behavior:** Some revenue or traction signals expected. Unit economics may be incomplete but directional data should exist. Team execution evidence (first hires, product shipped, early customers) now matters more than thesis alone.

**Key calibration:** Absence of any revenue at Seed is a moderate gap but not disqualifying if strong traction signals exist (pilot customers, LOIs, waitlist engagement). However, complete absence of both revenue AND customer engagement is a critical gap at this stage.

### Series A

**Emphasis:** Product-market fit evidence, unit economics, and go-to-market scalability become primary. Financial model quality matters significantly.

**Primary domains:**
- Traction (D5)
- Business Model (D3)
- Go-to-Market (D4)
- Financial Projections (D7)
- Management (D6)

**Secondary domains:**
- Market and Opportunity (D1)
- Risk (D8)

**Typically inactive:**
- Legal and Governance (D10) at full depth only if red flags present

**Framework behavior:** PMF evidence is non-negotiable. Unit economics should be visible even if not fully optimized. Revenue history required—absence of any revenue at Series A is a significant gap requiring explicit justification. Financial model must be driver-based (CAC, LTV, churn, expansion metrics).

**Key calibration:** At Series A, traction is expected to be material (consistent revenue, meaningful customer count or engagement metrics, product actively used). A company claiming Series A stage with less than $10K MRR (for SaaS) or equivalent demonstrated traction is mispositioned and should be reassessed as Seed.

### Series B and Growth

**Emphasis:** Scalability, financial performance, and operational rigor dominate. Full financial scrutiny.

**Primary domains:**
- Financial Performance (D7)
- Business Model (D3)
- Traction (D5)
- Go-to-Market (D4)
- Risk (D8)

**Secondary domains:**
- Management (D6)
- Market and Opportunity (D1)

**Inactive:** None—all domains fully active.

**Framework behavior:** All 10 domains active. Financial history, audited accounts, and detailed projections required. Unit economics and cohort analysis required. Risk profile detailed with documented mitigation. Operational infrastructure and reporting maturity become observable.

**Key calibration:** All 10 domains active. Financial history, audited accounts, and detailed projections required. Unit economics and cohort analysis required. Risk profile detailed and with mitigation strategies. A Series B company should have audited financials or comprehensive management accounts available.

### Debt/Credit Instruments (Any Stage)

**Add:**
- Debt Service Analysis (D7) is a hard blocker
- Risk Profile (D8) elevated to hard blocker
- Capital Structure detail (D9) is required

**Shift:**
- Cash generation and repayment capacity prioritized over growth potential
- Revenue history weighted more heavily than projections

**Unique modules:**
- Collateral assessment
- Covenant design
- Liquidity stress testing
- Add as custom modules to D9 and D8

**Framework behavior:** For debt instruments at any stage, the assessment shifts from growth potential to repayment capacity. A pre-seed company raising a convertible note is evaluated on its ability to generate cash and maintain runway, not on growth projections.

## Section 2: Weight Adjustment Guidelines

**Weight elevation rules:**
- When elevating a domain from secondary to primary: increase weight by 30–50% relative to other active domains
- When elevating a module to hard-blocker status: assign minimum completeness threshold of 0.7 (cannot score below)
- When deactivating a domain: redistribute weight to remaining active domains proportionally

**Distribution formula:**
- Total weights across active domains must always equal 1.0
- For proportional redistribution: new_weight = (old_weight / sum_of_remaining_weights) × target_sum

**Documentation requirement:** Every adjustment must be logged in the framework construction log with:
- Stage identified
- Domains activated/deactivated
- Weight adjustments applied
- Justification reference (e.g., "Series A: D5 elevated per stage logic")

## Section 3: Stage Identification from Submission

**Explicit signals:**
- Statement in the submission ("Raising $2M seed round")
- Funding raised to date and current ask amount
- Current burn rate and runway if disclosed

**Traction signals:**
- Revenue present/absent
- Customer count and engagement metrics
- Product development stage
- Team size and headcount history

**Financial ask size guidance:**
- Pre-seed: $50K–$500K
- Seed: $500K–$3M
- Series A: $3M–$15M
- Series B+: $15M+

**Team composition indicators:**
- Founder background (first-time founder suggests earlier stage)
- First institutional hire vs. established team
- Presence of experienced VP-level functional leads

**If stage is ambiguous:**
1. Present both likely stages in Confirmation Point 1
2. Ask assessor to confirm based on company self-assessment or funding stage stated in investor update
3. If assessor cannot confirm, use conservative approach (assess for earlier stage)

## Reference

Complete weight tables, adjustment matrices, and examples: `references/stage-weights.md`
