---
name: domain-taxonomy
description: >
  This skill should be used when any agent needs to understand the 10-domain analytical framework,
  identify which domains and modules apply to a given submission, determine module criticality,
  or construct/validate a dynamic assessment framework. Trigger phrases: "build the framework",
  "which domains apply", "what modules are relevant", "activate domains", "module criticality",
  "domain taxonomy", "analytical framework construction".
version: 0.1.0
---

# Domain and Module Taxonomy

The full analytical universe from which the assessment framework is constructed. This is not a checklist — it is the complete set of possible analytical units. The framework is built dynamically by selecting, weighting, and organizing from this universe based on the context profile and assessor criteria.

## Overview: 10 Domains

| Domain | ID | Focus |
|--------|----|-------|
| Market and Opportunity | 1 | Market validity, size, dynamics, competition |
| Solution and Product | 2 | Product maturity, IP, defensibility, regulatory |
| Business Model and Commercial Architecture | 3 | Revenue model, unit economics, margins |
| Go-to-Market and Commercial Execution | 4 | Sales, channels, acquisition, expansion |
| Traction and Commercial Validation | 5 | Revenue history, customer metrics, milestones |
| Management and Organizational Capability | 6 | Team, leadership, execution track record |
| Financial Performance and Projections | 7 | Historical financials, projections, scenarios |
| Risk Profile | 8 | All risk types across market, execution, finance, people |
| Capital Structure and Transaction Terms | 9 | Cap table, instrument, use of proceeds, protections |
| Legal, Compliance, and Corporate Governance | 10 | Corporate structure, contracts, IP ownership, governance |

## Module Summary (quick-reference for framework construction)

**Domain 1 — Market and Opportunity (8 modules):** Problem Definition · Market Sizing · Market Dynamics · Timing Thesis · Competitive Landscape · Competitive Positioning · Customer Segmentation · Demand Validation.

**Domain 2 — Solution and Product (8 modules):** Solution Description · Value Proposition · Development Stage · Technology Architecture · Intellectual Property · Product Roadmap · Defensibility Assessment · Regulatory and Compliance Profile.

**Domain 3 — Business Model (8 modules):** Revenue Model · Pricing Strategy · Cost Structure · Unit Economics · Operating Leverage · Revenue Quality · Customer Economics · Monetization Sequencing.

**Domain 4 — Go-to-Market (8 modules):** Sales Strategy · Channel Strategy · Marketing Strategy · Customer Acquisition Economics · Retention and Expansion Mechanisms · Partnership Strategy · Market Entry Sequencing · Pipeline and Backlog.

**Domain 5 — Traction (7 modules):** Revenue History · Customer Metrics · Product Engagement · Commercial Milestones · Pilot and PoC Results · Independent Validation · Failure and Adaptation Record.

**Domain 6 — Management (8 modules):** Founder and Leadership Profile · Functional Coverage · Team Depth · Advisory and Board Composition · Organizational Structure · Talent Strategy · Cultural and Execution Evidence · Identified Gaps.

**Domain 7 — Financial Performance (10 modules):** Historical Financials · Revenue Projections · Cost and Margin Projections · Cash Flow Projections · Balance Sheet Projections · Key Assumptions · Scenario Analysis · Break-Even Analysis · Debt Service Analysis · Return Analysis.

**Domain 8 — Risk Profile (9 modules):** Market Risk · Execution Risk · Technology Risk · Financial Risk · Regulatory and Legal Risk · People Risk · Concentration Risk · Macroeconomic and Systemic Risk · Mitigation Assessment.

**Domain 9 — Capital Structure and Transaction Terms (8 modules):** Current Capital Structure · Funding Instrument · Use of Proceeds · Valuation Basis · Investor/Lender Protections · Governance Rights · Exit Mechanisms · Dilution and Waterfall Analysis.

**Domain 10 — Legal, Compliance, and Governance (8 modules):** Corporate Structure · Ownership and Cap Table · Material Contracts · Intellectual Property Ownership · Litigation and Contingent Liabilities · Regulatory Compliance Status · Governance Structure · Data Protection and Privacy.

## Framework Construction Process

**Step 1 — Domain Activation:** Apply stage calibration (`stage-calibration` skill) and vertical calibration (`vertical-calibration` skill). Document inactivation rationale for any domain excluded.

**Step 2 — Module Activation:** For each active domain, determine module criticality: `mandatory` (always scored), `important` (scored unless clearly inapplicable), `optional` (scored when evidence exists). Apply vertical and commercial model adjustments.

**Step 3 — Criticality Classification:** Classify each active domain as `hard-blocker`, `critical`, `standard`, or `contextual`. This drives go/no-go gate logic and domain floor thresholds. Hard-blocker status is determined dynamically.

**Step 4 — Weight Assignment:** Assign domain weights summing to 1.0 across active domains. Assign module weights within each domain summing to 1.0. Both scoring tracks use the same weights.

**Step 5 — Framework Confirmation:** Present full framework at Confirmation Point 2. Document all adjustments in the framework construction log.

## Hard Blocker Determination

A module is a hard blocker when: (a) its absence renders the submission analytically incoherent for the identified transaction type, or (b) professional standards for the identified assessor type require it. Examples by context:

- **Founder and Leadership Profile** — hard blocker for all equity assessors at all stages
- **Regulatory and Compliance Profile** — hard blocker for verticals with regulatory exposure (Fintech, Medtech, Healthtech, regulated sectors)
- **Debt Service Analysis** — hard blocker for all credit/debt assessors
- **Use of Proceeds** — hard blocker for all transaction types
- **IP Ownership** — hard blocker for technology companies with proprietary IP claims
- **Unit Economics** — hard blocker for Series A+ equity assessors
- **Market Sizing** — hard blocker for all equity assessors (any stage)

Hard blocker status must be documented in the framework construction log with the standard or rationale.

## References

Full module definitions with analytical content, assessment indicators, and common failure patterns are in the domain-specific reference files. Load these when performing module-level analysis or scoring:

- `references/domain-1-market.md` — Domain 1: Market and Opportunity
- `references/domain-2-product.md` — Domain 2: Solution and Product
- `references/domain-3-business-model.md` — Domain 3: Business Model
- `references/domain-4-gtm.md` — Domain 4: Go-to-Market
- `references/domain-5-traction.md` — Domain 5: Traction
- `references/domain-6-management.md` — Domain 6: Management
- `references/domain-7-financials.md` — Domain 7: Financial Performance
- `references/domain-8-risk.md` — Domain 8: Risk Profile
- `references/domain-9-capital.md` — Domain 9: Capital Structure
- `references/domain-10-legal.md` — Domain 10: Legal and Governance
