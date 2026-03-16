---
name: recommendations-framework
description: >
  This skill should be used by the recommendations-agent when generating investment
  recommendations after sensitivity analysis is complete. Covers Path A (improvement roadmap)
  and Path B (deal terms) construction, path availability logic, calibration to context,
  and professional standards for each assessor type.
  Trigger phrases: "generate recommendations", "improvement roadmap", "deal terms",
  "investment structure", "Path A", "Path B", "recommendations phase".
version: 0.1.0
---

# Recommendations Framework

## 1. Overview

The recommendations phase is the final phase of the startup assessment workflow. After sensitivity analysis confirms the robustness of the assessment determination, the recommendations-agent generates forward-looking, actionable recommendations in one or both of two distinct paths.

### Two-Path Structure

**Path A: Submitter Improvement Roadmap** (Always available)
- Structured, prioritized roadmap of gaps the submitter should address
- Actionable remediation steps, evidence requirements, timeline
- Impact statements showing how gap closure improves the assessment outcome
- Audience: the startup submitter, their advisors, internal stakeholders
- Purpose: clear guidance on what to fix and in what order

**Path B: Deal Terms and Investment Structure Alternatives** (Conditional availability)
- 2–4 realistic investment structure alternatives for professional assessor use
- Calibrated to assessor type, funding stage, vertical, commercial model, geography, ask amount
- Based on current market standards and industry norms
- Audience: the professional investor (VC, PE, credit officer, corporate development)
- Purpose: implementable, sector-appropriate investment structures for professional negotiation
- Disclaimer: not legal advice; subject to qualified legal and financial review

### When Each Path Is Available

Path A is always generated when recommendations are requested, regardless of determination or robustness score.

Path B is available ONLY when BOTH conditions are met:
1. Determination is GO or CONDITIONAL GO (not PASS or HOLD)
2. Sensitivity robustness is rated "robust" or "moderately-robust" (not "limited-robustness")

If Path B is unavailable, the recommendation output must clearly state the reason:
- If determination is PASS or HOLD: "Path B is not available because the determination is [PASS/HOLD]. Investment structures are only presented for determinations of GO or CONDITIONAL GO."
- If robustness is limited: "Path B is not available because sensitivity analysis indicates limited robustness. The assessment outcome may be significantly sensitive to key assumptions; investment structures are presented only when assessment robustness is moderate or higher."

When both conditions are met, both paths are delivered together in a single recommendations package. Path A is delivered first (submitter perspective), followed by Path B (investor perspective).

---

## 2. Path Availability Logic

### Path A Availability: Always

Path A is always generated. There is no scenario where the submitter does not receive an improvement roadmap.

### Path B Availability: Conditional on Determination AND Robustness

```
Path B available IF:
  (determination = "GO" OR determination = "CONDITIONAL GO")
  AND
  (robustness = "robust" OR robustness = "moderately-robust")

Path B unavailable IF:
  determination = "PASS" OR determination = "HOLD"
  OR
  robustness = "limited-robustness"
```

When Path B is unavailable, provide the reason in a clear statement immediately following the Path A recommendations, before the closing remarks.

When both paths are available, present them sequentially: Path A output in full, then Path B output in full. Use clear visual/structural separation in the deliverables.

---

## 3. Path A: Submitter Improvement Roadmap

### Purpose

Path A provides the startup submitter with a structured, professional roadmap of the highest-impact gaps to address. The roadmap is prioritized by impact (hard blockers first), then severity, then ease of remediation. It is constructive and specific—not punitive—and frames gaps as opportunities to strengthen the business case.

### Input: Gap Register

The gap register is drawn from two sources:
1. Pre-assessment gap register (high/medium/low severity gaps identified during initial screening)
2. Assessment gaps (gaps identified during detailed domain scoring)

Both registers are merged, deduplicated, and scored for impact on the overall determination.

### Prioritization Criteria

Gaps are prioritized in the following order:

1. **Hard Blocker Gaps** (must be addressed before re-assessment is meaningful)
   - Examples: regulatory non-compliance, missing founder team, failed unit economics at current scale
   - Timeline: 30 days or urgent (as applicable)

2. **High-Severity Gaps** (directly impact determination; closure would improve outcome)
   - Examples: weak customer validation, unproven market sizing, weak management team depth
   - Timeline: 30–90 days

3. **Medium-Severity Gaps** (improve relative standing within determination category)
   - Examples: need for additional market research, capital efficiency metrics, governance structure
   - Timeline: 90–180 days

4. **Low-Severity Gaps** (nice-to-have improvements; address at next major milestone)
   - Examples: enhanced reporting, additional advisor expertise, expanded use-case validation
   - Timeline: 180+ days

### Roadmap Format: Per-Gap Structure

For each priority gap in the roadmap, provide the following fields:

#### Gap ID & Description
- Unique identifier (e.g., "GAP-A1", "GAP-B2")
- Domain (one of the 10 assessment domains: market, customer, product, unit-economics, fundraising, team, operations, traction, risk, fit)
- Severity level (Hard Blocker / High / Medium / Low)
- Specific gap description (not generic; rooted in the assessment findings)
  - Example: "Market sizing based on TAM assumption of $2.5B not validated by independent research; relies on single industry report"
  - Not: "Market size needs validation"

#### Remediation Action
- Specific, concrete action the submitter must take
- Actionable by the submitter (not dependent on external approvals or unknowns)
- Measurable end state
  - Example: "Commission an independent market sizing study from a Tier 1 research firm (e.g., Gartner, IDC, Arthur D. Little) covering the addressable market for [specific vertical/geography]. Budget: $15K–$25K. Deliverable: detailed TAM/SAM breakdown with customer segment analysis."
  - Not: "Improve market research"

#### Evidence Required
- What documentation, data, or milestone proves that the gap has been closed
- Specific formats and standards where applicable
- Examples:
  - For Market Sizing gap: "Independent market research report with TAM/SAM/SOM breakdown; must cite primary sources; must be dated within 6 months"
  - For Unit Economics gap: "6 months of audited transaction-level data showing CAC, LTV, payback period, gross margin; from accounting system or third-party audit"
  - For Team Depth gap: "CVs and reference check summaries for 2 new executives; domain expertise in [specific area]; minimum 10 years relevant experience each"

#### Impact on Determination
- Statement of how closure of this gap affects the assessment outcome and determination
- Use structured language: "Closing this gap would increase Domain X score from Y to approximately Z, improving overall readiness score by approximately N points. This would [maintain / improve / strengthen] the current determination from [current] to [projected]."
- Always include disclaimer: "Impact statement assumes re-assessment under same conditions; actual outcome subject to re-assessment and may differ based on new evidence or changing context."
- Avoid false precision: use "approximately", not exact figures

#### Estimated Timeline
- Realistic timeframe for the submitter to close the gap
- Format: "4–6 weeks", "3–4 months", "6–8 months"
- Based on typical industry timelines for similar remediation efforts
- Factors: complexity of evidence, third-party dependencies, data collection/audit cycles

### Roadmap Structure and Grouping

- Focus on the top 10–15 most impactful gaps (not exhaustive)
- Group related gaps when remediation actions overlap or when closure of one gap partially addresses another
  - Example: Market validation and customer reference collection might be grouped under a single "Customer Validation Phase" roadmap step
- Present in priority order (hard blockers first, then high-severity, then medium)
- Use clear numbering and visual hierarchy

### Tone and Professional Standards

- Constructive and solutions-focused, not punitive or critical
- Acknowledge what the submitter has demonstrated well (e.g., "Strong founding team and clear vision; the following roadmap addresses remaining validation gaps")
- Frame gaps as opportunities to strengthen the investment case ("Closing these gaps will significantly enhance the investment opportunity and de-risk the assessment")
- Avoid language that implies judgment of the founder or team
- Professional, clear writing; no jargon; explain technical terms where used
- Avoid absolute statements ("you will succeed if you do X"); use conditional language ("addressing this gap would strengthen your case")

---

## 4. Path B: Deal Terms and Investment Structure Alternatives

### Purpose

Path B presents 2–4 realistic investment structure alternatives tailored to the specific assessor type, funding stage, vertical, commercial model, geographic market, and ask amount. Structures are based on current market standards and are implementable, not hypothetical or aspirational. Path B is designed for professional investor use in structuring the investment term sheet.

### Required Disclosure Statement

Path B output MUST include the following disclosure at the top, verbatim:

```
PROFESSIONAL INVESTOR DISCLAIMER FOR INVESTMENT STRUCTURES

The investment structure alternatives below are presented for professional investor use and
do not constitute legal advice, financial advice, or a definitive valuation. All structures
should be reviewed and modified as necessary by qualified legal counsel and financial advisors
before implementation. The structures reflect current market standards as of 2025 but are not
guaranteed to be appropriate for any specific transaction. Each investor should conduct their
own due diligence and risk assessment before proceeding with any investment.
```

### Inputs to Path B Calibration

Path B structure recommendations are calibrated to the following contextual factors:

1. **Assessor Type** (VC, Angel, PE, Credit/Debt, Corporate/Strategic, Family Office/SWF)
2. **Funding Stage** (Pre-seed, Seed, Series A, Series B, Series C+, Growth, Venture Debt)
3. **Vertical/Industry** (SaaS, FinTech, HealthTech, Climate, Manufacturing, etc.)
4. **Commercial Model** (B2B SaaS, B2C, B2B, Marketplace, Hardware, etc.)
5. **Geographic Market** (GCC/MENA, North America, Europe, Southeast Asia, other)
6. **Ask Amount** (funding size: seed-stage ask vs. Series A ask)
7. **Instrument Type** (equity, debt, convertible, revenue-based, hybrid)
8. **Conditions from Assessment** (any material conditions or red flags from the determination)

### Structure Alternative Format

For each of the 2–4 structure alternatives, provide:

#### Structure Name
- A descriptive, professional name
- Examples:
  - "Priced Equity Round with Milestone Tranche"
  - "Convertible Note with Valuation Cap and Discount"
  - "Venture Debt with Warrant Coverage"
  - "Strategic Preferred Equity with Commercial Exclusivity"
  - "Revenue-Based Financing with Equity Option"

#### Key Terms
- Instrument type (Common/Preferred Equity, SAFE, Convertible, Debt, etc.)
- Valuation or pricing approach (expressed as range, not point estimate)
  - Example: "Valuation: $X–$Y million pre-money, based on [comparable company, market multiple] analysis"
  - Do NOT prescribe a specific valuation; present frameworks and ranges
- Amount and pro-rata rights
  - Example: "Investment amount: $[X–Y]M; pro-rata rights in future rounds"
- Instrument-specific terms (interest rate for debt, cap/discount for convertible, etc.)
- Liquidation preference or conversion trigger (if applicable)
- Board representation or governance rights

#### Conditions or Milestones
- Any conditions precedent to funding (e.g., closing a customer reference contract, hiring a CFO)
- Any milestone-based tranching (e.g., first tranche at close, second tranche upon achieving specific revenue or customer targets)
- Timeline and measurement criteria for milestones
- Be realistic: conditions should be achievable by the submitter within 12 months

#### Investor Protections
- Anti-dilution provisions (weighted average, full ratchet, none)
- Board seat or board observation rights
- Information rights (quarterly financials, annual audit, etc.)
- Liquidation preferences or participation rights
- Drag-along or anti-dilution clauses (as applicable)
- Redemption or exit provisions (if applicable)
- Typical protective provisions for this stage/structure type

#### Industry Standard Basis
- Citation of the market basis for this structure
- Examples:
  - "Standard for Series A SaaS funding in North America (based on NVCA model term sheet documents, 2024–2025)"
  - "Typical venture debt facility structure for growth-stage companies (based on Silicon Valley Bank and other lenders' standard terms)"
  - "Market standard convertible note for seed-stage startups in GCC (based on regional angel networks and Tier 1 accelerators)"
- Note geographic applicability if this structure is region-specific

#### Suitability Rationale
- Explanation of why this structure is appropriate for THIS specific context
- Consider: stage, vertical, commercial model, assessor type, risk profile
- Examples:
  - "This structure is suitable because the company is pre-revenue and early-stage, and a convertible defers valuation questions until clearer product-market fit is demonstrated. The discount reflects early-stage risk, and the valuation cap protects early investors."
  - "This structure suits a credit assessor evaluating venture debt because it provides interest income and warrant coverage, aligning the lender's upside potential with equity holders while providing senior security."
  - "This structure is appropriate for a PE assessor targeting growth equity because the milestone tranching aligns founder and investor incentives and provides flexibility to adjust investment size based on demonstrated traction."

### Market Standards and Current Terms

All structures MUST reflect current market standards as of 2025. Key references:

- **NVCA Model Term Sheet**: standard for US VC rounds (priced equity, Series A and beyond)
- **SAFE (Seed Stage)**: common for seed funding in North America
- **Convertible Note Standards**: typical interest 5–7%, maturity 24–36 months, cap in $2–5M range for seed
- **Venture Debt**: typical structure 3–5 year facility, 8–12% interest, 10–20% warrant coverage, standard covenants (cash/quarterly revenue minimum, debt/revenue cap)
- **Revenue-Based Financing**: typical structure 3–7 year term, 1–2.5% monthly repayment (6–30% annual amount financed), no equity dilution, monthly revenue cap trigger
- **PE Growth Equity**: typical equity check $10M+, 20–40% target ownership, 3–5 year hold, EBITDA multiple valuation approach
- **PE Majority Buyout**: typical structure 100% equity ownership or majority control, seller rollover equity, earnout contingent on EBITDA/revenue milestones

Do NOT prescribe point valuations. Express valuation as comparable-based ranges or multiple-based frameworks (e.g., "3–5x trailing revenue for SaaS in this segment").

### Structures Must Be Realistic and Implementable

- Avoid hypothetical or aspirational structures
- All terms must be achievable in the current market without requiring exceptional circumstances
- Milestones must be measurable and achievable by a typical submitter in this stage/vertical
- Do not present structures that require extraordinary founder concessions or that are not market-standard

### Geographic Calibration for Path B

Structures should be tailored to the geographic market where the investment is likely to occur.

#### GCC/MENA
- Note regulatory considerations (SAMA, ADGM, DFSA) where relevant to the instrument type
- Common structures: SAFEs (increasingly adopted), convertible notes, priced equity rounds
- Typical valuation multiples: SaaS 4–7x ARR (lower than North America), fintech 2–4x revenue, traditional sectors 1–2x EBITDA
- Governance and board composition considerations: family office / SWF patience, longer horizons
- Currency: USD common; note FX considerations for regional founders raising in USD
- Cross-border: flag if founder/company jurisdiction creates tax or regulatory complications

#### North America (US/Canada)
- NVCA model documents and standard VC practices
- Typical VC terms: Series A $2–10M, Series B $10–40M, Series C+ $30M+
- Convertible notes: common for seed, 5–7% interest, 20–24 month maturity, cap $1–3M
- SAFEs: increasingly common alternative to convertibles for early-stage
- Board seats: early-stage (seed) 1 board seat for lead; Series A typically 1–2 board seats; Series B+ larger boards with investor representation
- Protective provisions: standard package per NVCA (redemption, liquidation, etc.)

#### Europe (UK, Germany, France, other)
- BVCA and Invest Europe standards
- SAFE equivalents less common; priced rounds and convertibles more typical
- Typical VC terms: seed €500K–2M, Series A €2–8M, Series B €10–30M
- Governance: German/Dutch structures may require supervisory boards or specific governance provisions
- Regulatory: note UK FCA or ESMA considerations if applicable

#### Southeast Asia
- Regional norms: convertibles and SAFEs increasingly common
- Valuation multiples: SaaS 3–5x ARR, e-commerce 1–2x revenue (market-dependent)
- Currency: USD common; may need to address THB, SGD, or PHP hedging
- Regulatory: flag if cross-border investment creates Singapore MAS, Thai SEC, or Indonesian OJK considerations
- Board composition: may reflect founder control preference and local governance norms

#### Cross-Border Transactions
- Flag regulatory/tax complications (e.g., US investor into GCC company, GCC investor into SEA company)
- Note currency risk and hedging considerations
- Governance jurisdiction (company domicile for stock option plan, Delaware/BVI shell, etc.)
- Compliance and regulatory approval timelines

### Assessor Type Calibration for Path B

Structures are tailored to the professional investor type conducting the assessment.

#### VC / Angel Investor
- Focus: equity structures (priced rounds, SAFEs, convertibles)
- Key terms: pro-rata rights, board seat, standard protective provisions
- Protective provisions: information rights, liquidation preferences, anti-dilution
- Board composition: investor director or observer (depending on stage)
- Suitable structures:
  - Priced equity round (Series A and beyond)
  - SAFE or convertible (seed-stage)
  - Milestone-based priced rounds (early-stage with defined de-risking milestones)
- Governance: founder maintains operational control; investor veto rights on major decisions (fundraising, exit, related-party transactions)

#### Private Equity (Growth, Buyout)
- Focus: equity structures with control/majority characteristics; EBITDA multiple valuation
- Key terms: acquisition price, equity rollover, earnout, working capital adjustments
- Protective provisions: board control, minority put/call, drag-along, non-compete
- Suitable structures:
  - Majority or significant minority equity with control board seat(s)
  - Earnout contingent on EBITDA/revenue growth (3–5 year hold)
  - Management rollover equity (founder/key mgmt 5–25% retain for upside)
  - Seller financing or preferred equity (if founder has tax considerations)
- Valuation approach: EBITDA multiples (e.g., 5–8x EBITDA for stable businesses, lower for high-growth)
- Timeline: 3–5 year hold, potential for continuation fund extension

#### Credit/Debt Assessor
- Focus: debt structures with security, covenants, and warrants
- Key terms: senior debt, interest rate, repayment schedule, covenants, security/collateral
- Suitable structures:
  - Venture debt facility (3–5 year term, 8–12% interest, 10–20% warrant coverage)
  - Revenue-based financing (monthly repayment % of revenue, no equity, 3–7 year term)
  - Credit facility (secured against assets/receivables, covenants on debt/EBITDA or cash burn)
- Protective provisions: personal guarantee (if early-stage), cash flow/revenue covenants, prepayment penalties (if applicable)
- Security: first lien on company assets, second lien on preferred equity (if applicable)
- Warrants: typically 10–20% of facility size (or 10–20% of funded amount), strike price at par

#### Corporate/Strategic Investor
- Focus: equity structures with commercial terms (exclusivity, ROFR, etc.)
- Key terms: preferred equity stake, commercial exclusivity, ROFR in future rounds
- Suitable structures:
  - Strategic preferred equity (2–10% stake) with preferred commercial terms
  - Revenue-sharing or profit-sharing arrangement (if applicable)
  - Preferred supplier arrangement with equity upside
  - Joint venture or embedded minority stake
- Protective provisions: board seat (if stake >5%), information rights, ROFR in future funding
- Commercial terms: exclusivity (product vertical, customer segment, geography), pricing favorable to corporate, first-refusal on customer contracts or technology licensing

#### Family Office / Sovereign Wealth Fund (SWF)
- Focus: flexible, longer-horizon equity structures with governance flexibility
- Key terms: equity stake (variable), patient capital, extended hold horizon
- Suitable structures:
  - Preferred equity (variable terms, negotiable liquidation preference)
  - Common equity with governance comfort (board seat, information rights)
  - Co-investment with VC syndicates (flexible terms)
  - Long-duration preferred equity (no redemption timeline)
- Protective provisions: board observation, information rights, limited anti-dilution
- Governance: founder retains operational flexibility; investor focuses on strategic oversight

### Stage Calibration for Path B

Structures should reflect the appropriate stage and typical round characteristics.

#### Pre-Seed / Seed Stage ($500K–$2M)
- Typical instruments: SAFEs, convertible notes, small equity rounds ($250K–$500K per investor)
- Valuation: typically not established (SAFE/convertible defers valuation)
- Governance: minimal; no board seats; possibly 1 advisor seat
- Typical terms: SAFE with cap and discount (cap $1–3M, discount 10–20%); convertible with 5–7% interest, 24 month maturity
- Protective provisions: information rights (quarterly updates), liquidation preference (non-participating, 1x)
- Timeline: 30–90 day close

#### Series A ($2–10M)
- Typical instruments: Priced equity (Series A Preferred)
- Valuation: $5–30M pre-money (range highly variable by vertical and geography)
- Governance: 1–2 investor board seats, possibly 1 founder seat; standard NVCA protective provisions
- Typical terms: Series A Preferred with 1x non-participating liquidation preference, pro-rata rights, board seat, standard anti-dilution (weighted average)
- Protective provisions: information rights (monthly financials, annual audit), registration rights, approval rights (major fundraising, exits, related-party transactions)
- Timeline: 60–120 day close

#### Series B ($10–40M)
- Typical instruments: Priced equity (Series B Preferred)
- Valuation: $20–100M+ pre-money
- Governance: 2–3 investor board seats, founder CEO seat; standard protective provisions plus participation rights
- Typical terms: Series B Preferred with 1x participation (multiple liquidation preferences), pro-rata rights, board seats (2+), anti-dilution protection
- Protective provisions: enhanced information rights, registration rights, drag-along on exit >$X, approval rights
- Timeline: 90–150 day close

#### Series C+ ($30M+)
- Typical instruments: Priced equity (Series C Preferred), possibly secondary equity components
- Valuation: $100M+ pre-money (unicorn-stage)
- Governance: Professional board with investor director(s), independent directors, audit/compensation committees (if mature)
- Typical terms: Series C Preferred with 1x participation, enhanced pro-rata, board seats (2–3 investors), full anti-dilution
- Protective provisions: comprehensive including drag-along, registration rights, board composition provisions
- Timeline: 120–180 day close

#### Growth Equity ($10M–100M+)
- Typical instruments: Growth Preferred Equity, secondary equity (founder/employee share purchases)
- Valuation: EBITDA multiple or comparable transaction multiple approach
- Governance: Lead investor board seat, founder often retains CEO role, professional board with independent directors
- Typical terms: Growth Preferred with 1x–1.5x participation, 5–7 year exit target, earnout contingent on EBITDA growth
- Protective provisions: standard growth equity package, governance provisions for interim CEO replacement scenario
- Timeline: 90–150 day close

#### Venture Debt ($500K–$5M)
- Typical instruments: Term loan facility, equipment financing, revenue-based financing
- Valuation approach: based on monthly burn rate (venture debt), monthly revenue (revenue-based)
- Governance: monthly reporting, covenant compliance monitoring
- Typical terms: 3–5 year amortization, 8–12% interest, 10–20% warrant coverage, monthly revenue/cash covenants, prepayment options
- Protective provisions: security on assets, personal guarantee (if early-stage), acceleration on default
- Timeline: 30–45 day close

#### Revenue-Based Financing ($250K–$5M)
- Typical instruments: Revenue-based financing agreement
- Valuation approach: based on monthly revenue, repayment cap (2–2.5x amount financed)
- Governance: monthly revenue reporting, capped repayment upon reaching 2x–2.5x cap
- Typical terms: 1–2% monthly repayment (effective 6–30% annual), 3–7 year term, no equity dilution, monthly revenue cap trigger, potential pause on repayment if revenue declines
- Protective provisions: company must notify lender of material revenue decline, fund usage restrictions (no related-party transfers), potential acceleration on breach
- Timeline: 15–30 day close

### Output Delivery for Path B

Path B recommendations are delivered in three formats:

1. **recommendations.json** (machine-readable)
   - Path B details in structured JSON format
   - Include path_selected, path_b_deal_terms array, industry_standard_basis fields

2. **HTML Recommendations Report**
   - Full Path B content with formatted tables, styling, narrative explanation
   - Professional, ready for investor circulation

3. **PDF Recommendations Report**
   - Final archivable deliverable
   - Includes full session audit trail appendix
   - Signed/dated by assessor and submission platform

---

## 5. Output Delivery

### Output Artifacts

The recommendations phase generates the following outputs:

1. **recommendations.json**
   - Machine-readable recommendations object
   - Fields:
     - `path_selected`: "path-a-only" | "path-b-only" | "both-paths"
     - `path_availability_rationale`: explanation of why each path is/isn't available
     - `path_a_improvement_roadmap`: array of gap objects
     - `path_b_deal_terms`: array of investment_structure_alternatives
     - `timestamp`: ISO 8601 datetime of generation
     - `assessor_context`: assessor type, stage, vertical, geography, ask (for path B calibration reference)

2. **HTML Recommendations Report**
   - Professional HTML5 document
   - Sections: Path A in full, Path B in full (if available), closing remarks
   - Styled for readability; suitable for printing or web viewing
   - Includes recommended next steps and contact information

3. **PDF Recommendations Report** (Final Deliverable)
   - PDF export of HTML report
   - Full session audit trail appendix
     - Submission date, submitter name, company, assessor name and type
     - Assessment determination, robustness rating
     - Summary of assessment findings
     - Sensitivity analysis summary
   - Timestamped footer with assessor signature block
   - This is the final archivable deliverable—it completes the workflow

### Phase Closure

The recommendations phase is the END of the assessment workflow. Upon delivery of the recommendations report (PDF), the session is concluded with final delivery instructions:

- Submitter should review Path A improvement roadmap within 1 week and begin prioritization
- If Path B is available, investor should engage legal and financial advisors before finalizing terms
- Re-assessment timeline: recommend re-assessment after 6–12 months or upon significant business milestones
- Support contacts: provide assessor contact for follow-up questions

---

## 6. Professional Standards Disclosure

### Path A Disclaimer

Path A recommendations are framed with the following disclaimer:

```
These recommendations represent areas where strengthening the business case would likely
improve the assessment outcome. However, gap closure does not guarantee improved determination;
actual outcome is subject to re-assessment and may differ based on new evidence, market changes,
or other factors. The submitter should view this roadmap as a professional assessment of
material opportunities to strengthen their investment case.
```

### Path B Disclaimer (Required at Top of Path B Output)

See Section 4 for the required professional investor disclaimer that must appear at the top of all Path B output.

### Tone Across Both Paths

- Constructive and solutions-focused
- Professional and respectful to founders and investors
- Clear about limitations and conditional statements
- Avoid language implying certainty or guarantees
- Acknowledge both strengths and gaps

---

## 7. References Index

This skill references the following detailed reference files:

1. **references/deal-terms-by-stage.md**: detailed deal terms, valuation multiples, investor protections, and market standards by funding stage
2. **references/investment-structures.md**: detailed explanation of each investment structure type (equity, SAFE, convertible, venture debt, etc.)
3. **references/improvement-roadmap-standards.md**: gap prioritization framework, evidence standards, remediation action writing standards, impact language templates

Consult these references when constructing Path A roadmap gaps and Path B structure alternatives.

---

## 7b. Residual Risk Assessment and Risk Appetite Linkage (ISO 31000 / COSO ERM)

### Residual Risk Assessment

For each gap in the Path A roadmap and each risk identified in the assessment, the recommendations-agent must assess **residual risk** — the risk that remains after proposed mitigation or remediation.

**Per-gap residual risk fields** (appended to each Path A gap entry):

```json
{
  "inherent_risk_score": 20,
  "proposed_treatment": "Commission independent market study; validate with 3 customer interviews",
  "residual_risk_score": 8,
  "residual_risk_classification": "medium",
  "residual_risk_note": "Market sizing risk reduced from extreme to medium if independent study confirms TAM within 30% of submission claim"
}
```

- **Inherent risk score**: the likelihood x impact score from the gap register (before any treatment)
- **Residual risk score**: estimated likelihood x impact after the proposed treatment is implemented
- **Residual risk classification**: low (1–4), medium (5–9), high (10–15), extreme (16–25)

### Risk Appetite Linkage

The assessor's risk tolerance (captured in the assessor profile) must be formally linked to determination thresholds and recommendation framing:

| Risk Tolerance | Effect on Determination | Recommendation Framing |
|---------------|------------------------|----------------------|
| **Conservative** (credit, debt, capital preservation) | Domain floors raised by +5 points; Fit modifier stricter | Emphasize downside protection; lead with risk mitigation; Path B structures prioritize security |
| **Moderate** (PE, family office, balanced) | Standard thresholds apply | Balanced risk/return framing; Path B structures balance protections with upside |
| **Aggressive** (VC, angel, growth-focused) | Domain floors lowered by -5 points; early-stage gaps weighted less | Emphasize upside potential; lead with opportunity; Path B structures prioritize flexibility and optionality |

**Implementation:** The `go_nogo_determinator.py` script accepts a `risk_appetite` parameter that adjusts the readiness score bands and domain floor thresholds per the table above. This is set during framework construction (Framework Review) based on the assessor profile and cannot be changed after Framework Review confirmation.

**Standards basis:** COSO ERM (risk appetite defined and linked to strategy), ISO 31000 (risk evaluation against risk criteria/appetite).

---

## 8. Key Principles

1. **Adaptive, not prescriptive**: All recommendations are tailored to context (assessor type, stage, vertical, geography). No hardcoded defaults.

2. **Evidence-based**: All recommendations are rooted in the assessment findings and gap register. Recommendations that are not supported by assessment evidence are not included.

3. **Professional standards**: All recommendations reflect current market standards (as of 2025) and are implementable by typical founders and investors.

4. **Constructive tone**: Recommendations frame gaps as opportunities and acknowledge strengths.

5. **Clear disclaimer**: All recommendations include appropriate disclaimers about their conditional nature and limitations.

6. **Audience-aware**: Path A speaks to the submitter; Path B speaks to the professional investor. Language, detail, and tone differ accordingly.

7. **Actionable and specific**: Every recommendation (roadmap gap, structure alternative) is specific, measurable, and actionable.

8. **No legal advice**: Path B explicitly disclaims legal advice; all structures should be reviewed by qualified legal counsel.

---

## 9. Prompt Template for Recommendations-Agent

When the recommendations-agent invokes this skill, provide the following context:

```
{
  "assessment_determination": "GO" | "CONDITIONAL GO" | "PASS" | "HOLD",
  "sensitivity_robustness": "robust" | "moderately-robust" | "limited-robustness",
  "gap_register": [
    {
      "gap_id": "GAP-A1",
      "domain": "market",
      "severity": "high",
      "description": "...",
      "evidence_of_closure": "...",
      "estimated_impact_points": 15
    },
    ...
  ],
  "assessor_context": {
    "assessor_type": "VC" | "PE" | "Credit" | "Strategic" | "Family Office",
    "funding_stage": "Seed" | "Series A" | "Series B" | ...,
    "vertical": "SaaS" | "FinTech" | "HealthTech" | ...,
    "commercial_model": "B2B SaaS" | "B2C" | ...,
    "geographic_market": "GCC/MENA" | "North America" | "Europe" | "Southeast Asia",
    "ask_amount_usd": 5000000,
    "instrument_type": "Equity" | "Debt" | "Convertible" | "SAFE"
  },
  "assessment_summary": "..."
}
```

The recommendations-agent processes this context and generates recommendations according to the paths and standards defined in this skill.

---

## 10. References

- NVCA Model Term Sheet: https://nvca.org/resources/nvca-model-documents/
- SAFE Primer: https://www.ycombinator.com/documents
- Venture Debt Best Practices: Silicon Valley Bank, Gold Hill Capital, Horizon Technology Finance
- Private Equity Term Sheet Standards: BVCA, EVCA (Invest Europe), NVCA
- Revenue-Based Financing Industry Standards: Clearco, Uncapped, Lighter Capital documentation
- Regional Standards: GCC VC Alliance, Southeast Asia Investment Forum, European Venture Capital Association
