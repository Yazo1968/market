# Confidence Classifications — Worked Examples and Edge Cases

## Overview

Confidence classification is assigned at the moment a research finding is retrieved. The classification determines whether the finding is eligible to contribute to Quality (Dimension B) scoring on the Readiness Track. This document provides worked examples for each classification level with real-world edge cases.

---

## Classification 1: VERIFIED

**Definition:** Retrieved from an accessible, authoritative source; content directly confirms or refutes a specific claim.

**Scoring Eligibility:** ELIGIBLE → Contributes to Quality (Dimension B) scoring

**Confidence Requirements:**
- Source is recognized as authoritative for this data type
- Data is directly retrievable without interpretation
- Source is current (within 2 years for market data, current for regulatory/factual data)
- Content matches the claim being verified

### Verified Examples

#### Example 1A — Regulatory Requirement (Verified)

**Scenario:**
- Claim to verify: "Companies providing mortgage lending services in California require California Residential Mortgage Lending Act (CRMLA) license"
- Search: California Department of Financial Protection and Innovation website
- Result: Official guidance states "Persons engaged in the business of taking residential mortgage loan applications must obtain a license under the CRMLA"

**Classification: VERIFIED**
- Source: Official regulatory authority (California DFPI)
- Content: Direct statement of requirement
- Current: Regulatory requirement is stable and current
- Scoring: Eligible — contributes to Quality

**Attribution:**
```
Source: California Department of Financial Protection and Innovation
URL: https://dfpi.ca.gov/licensing/residential-mortgage-lending/
Retrieved: 2026-03-08
Confidence Classification: Verified
Rationale: Direct quote from regulatory authority on licensing requirement; source is the official government body responsible for this regulation.
```

#### Example 1B — Company Funding (Verified)

**Scenario:**
- Claim to verify: "Company X raised $12M Series A in Q2 2024"
- Search: Crunchbase (structured connector)
- Result: Crunchbase database entry: "Series A: $12M, announced June 2024"

**Classification: VERIFIED**
- Source: Authoritative funding database (Crunchbase)
- Content: Direct data point from primary source
- Current: Retrieved in current session
- Scoring: Eligible — contributes to Quality

**Attribution:**
```
Source: Crunchbase, Inc.
URL: https://www.crunchbase.com/organization/[company-id]
Retrieved: 2026-03-08
Confidence Classification: Verified
Rationale: Crunchbase is the primary source for company funding data; entry directly states funding amount and date.
```

#### Example 1C — Competitor Pricing (Verified)

**Scenario:**
- Claim to verify: "Main competitor charges $500/month for standard tier"
- Search: Competitor website, pricing page
- Result: Public pricing page lists "Standard Plan: $500/month"

**Classification: VERIFIED**
- Source: Official pricing source (company website)
- Content: Direct pricing information
- Current: Retrieved in current session
- Scoring: Eligible — contributes to Quality

**Attribution:**
```
Source: Competitor website, public pricing page
URL: https://competitor.com/pricing
Retrieved: 2026-03-08
Confidence Classification: Verified
Rationale: Pricing is directly published on company's official website; no interpretation required.
```

#### Example 1D — Market Size (Verified)

**Scenario:**
- Claim to verify: "Global SaaS market is $232B in 2024"
- Search: Gartner research on SaaS market
- Result: Gartner report states "Global SaaS market reached $232B in 2024"

**Classification: VERIFIED**
- Source: Authoritative analyst (Gartner)
- Content: Direct market size statement
- Current: 2024 data (current as of 2026)
- Scoring: Eligible — contributes to Quality

**Attribution:**
```
Source: Gartner, Inc. "SaaS Market Share & Forecast 2024"
URL: https://www.gartner.com/en/...
Retrieved: 2026-03-08
Confidence Classification: Verified
Rationale: Gartner is a major authoritative analyst firm; this is a direct market size statement from their published research.
```

---

## Classification 2: CORROBORATED

**Definition:** Multiple independent sources confirm the same finding. Requires convergence of evidence from distinct sources.

**Scoring Eligibility:** ELIGIBLE → Higher evidentiary weight than Verified

**Confidence Requirements:**
- 2+ independent sources report the same finding
- Sources are from different organizations (not one source reporting another's findings)
- Data points are within acceptable variance (±10% for market size, ±20% for forecasts)
- Sources are retrieved within the same session

### Corroborated Examples

#### Example 2A — Market Size Corroboration

**Scenario:**
- Finding to corroborate: Global enterprise software market size is approximately $600B
- Source 1: Gartner research states $602B in 2024
- Source 2: IDC research states $598B in 2024
- Source 3: Company cites Forrester estimate of $595B

**Classification: CORROBORATED**
- Agreement: Three sources within $7B range (1.2% variance) on market size
- Independence: Gartner, IDC, and Forrester are independent analyst firms
- Magnitude: Convergence on ~$600B is very strong agreement
- Scoring: Eligible — contributes to Quality with high confidence

**Attribution:**
```
Sources:
1. Gartner, Inc. (2024): $602B
2. IDC (2024): $598B
3. Forrester Research (2024): $595B

Retrieved: 2026-03-08
Confidence Classification: Corroborated
Rationale: Three independent analyst firms converge on enterprise software market size of ~$600B; 1.2% variance indicates high reliability of this estimate.
```

#### Example 2B — Competitive Funding Corroboration

**Scenario:**
- Finding to corroborate: "Competitor raised $15M Series B in June 2023"
- Source 1: Crunchbase entry: Series B $15M, June 2023
- Source 2: TechCrunch article: "$15M Series B announced June 2023"
- Source 3: Company press release: "Series B funding of $15M"

**Classification: CORROBORATED**
- Agreement: All three sources agree on amount and date
- Independence: Crunchbase (database), TechCrunch (news), Company (press release) are distinct sources
- Consistency: Perfect agreement on material facts
- Scoring: Eligible — contributes to Quality with very high confidence

**Attribution:**
```
Sources:
1. Crunchbase (June 2023 entry)
2. TechCrunch news article (June 2023)
3. Company press release (June 2023)

Retrieved: 2026-03-08
Confidence Classification: Corroborated
Rationale: Three independent sources (database, news, company) confirm $15M Series B funding; perfect alignment on amount and date.
```

#### Example 2C — Customer Reference Corroboration

**Scenario:**
- Finding to corroborate: "Company X is a customer of the startup"
- Source 1: Startup's customer list on website
- Source 2: Company X's LinkedIn post mentioning partnership
- Source 3: Case study on startup's website with Company X as named customer

**Classification: CORROBORATED** (with caveat)
- Agreement: Multiple sources confirm customer relationship
- Independence: Startup website, Company X's LinkedIn (external to startup), Case study (more detailed)
- Caveat: All sources are influenced by the company being assessed; not fully independent
- Revised Classification: **CORROBORATED (but with company-influenced sources)**
- Scoring: Eligible — contributes to Quality, but with acknowledgment that sources favor the company

**Attribution:**
```
Sources:
1. Startup website, customer page
2. Company X LinkedIn post
3. Startup case study (with Company X identified)

Retrieved: 2026-03-08
Confidence Classification: Corroborated
Rationale: Multiple sources confirm Company X as customer; however, sources are influenced by company being assessed (website and case study are company-published). Company X's LinkedIn mention provides independent confirmation.
```

#### Example 2D — Regulatory Requirement Corroboration

**Scenario:**
- Finding to corroborate: "FDA 510(k) pre-market notification is required for Class II medical devices"
- Source 1: FDA official website, Device Classification guidance
- Source 2: FDA regulations (21 CFR 807.87)
- Source 3: Law firm summary of medical device regulations

**Classification: CORROBORATED**
- Agreement: All sources confirm 510(k) requirement for Class II
- Authoritative: FDA sources are primary; law firm confirms
- Consistency: Regulatory requirement is consistent across all sources
- Scoring: Eligible — contributes to Quality with very high confidence (regulatory requirements are stable)

**Attribution:**
```
Sources:
1. FDA Device Classification, Regulatory Requirements
2. 21 CFR 807.87 (Federal Regulations)
3. Law firm regulatory summary

Retrieved: 2026-03-08
Confidence Classification: Corroborated
Rationale: FDA regulations and official guidance consistently require 510(k) for Class II devices; law firm summary aligns with official regulatory text.
```

---

## Classification 3: CONFLICTED

**Definition:** Multiple sources present materially different findings on the same topic. Sources conflict in a way that prevents determination of the "true" value.

**Scoring Eligibility:** INELIGIBLE → Documented in Research Provenance Register; assessor judgment required

**Conflict Thresholds:**
- Market size: >15% difference between sources
- Growth rates: >5 percentage points difference
- Valuations: >25% difference
- Factual claims (funding, customer count): Any unexplained discrepancy

### Conflicted Examples

#### Example 3A — Market Size Conflict

**Scenario:**
- Finding: Global AI software market size in 2024
- Source 1: Gartner reports $200B
- Source 2: IDC reports $145B
- Source 3: McKinsey estimates $250B
- Discrepancy: Sources differ from $145B to $250B (72% range)

**Classification: CONFLICTED**
- Magnitude of conflict: $105B range is 42% of lowest estimate
- Possible explanations: Different segment definitions (which AI applications count?), different geographic coverage, different methodologies
- Cannot determine single "correct" value
- Scoring: INELIGIBLE — Cannot contribute to Quality scoring

**Output:**
```
Global AI Software Market Size (2024)
- Gartner: $200B
- IDC: $145B
- McKinsey: $250B
- Conflict: Estimates range from $145B–$250B (72% variance)
- Likely explanation: Different segment definitions (e.g., whether enterprise AI, consumer AI, AI infrastructure are included)
- Assessment: Cannot determine definitive market size from available sources
- Recommendation: Request company to clarify which segments it serves and which analyst definition aligns with its TAM; request source documentation for company's own TAM estimate
```

**Why Conflicted (not cherry-picked):** Instead of selecting Gartner's $200B as the "answer," we flag that multiple authoritative sources disagree, and the assessor must decide how to interpret this (e.g., are they in the $145B segment or the broader $250B definition?).

#### Example 3B — Competitive Funding Conflict

**Scenario:**
- Finding: Competitor raised Series B funding
- Source 1: Crunchbase states $20M Series B
- Source 2: TechCrunch article states $15M Series B
- Source 3: Competitor press release is vague ("Significant Series B funding")
- Discrepancy: $20M vs. $15M (25% difference)

**Classification: CONFLICTED**
- Magnitude: $5M difference is 25%, above typical data variance threshold
- Possible explanations: One source misreported, undisclosed secondary tranche, different reporting timing
- Cannot determine which amount is correct
- Scoring: INELIGIBLE

**Output:**
```
Competitor Series B Funding
- Crunchbase: $20M Series B
- TechCrunch: $15M Series B
- Company press release: "Significant Series B" (non-specific)
- Conflict: Sources differ by $5M (25%)
- Possible explanations: One source may be inaccurate; possibly multiple tranches announced at different times
- Assessment: Cannot definitively determine Series B amount from available sources
- Recommendation: If competitive valuation benchmarking is important, request company to provide competitor analysis from research service (CB Insights, Pitchbook) with clarified funding details
```

#### Example 3C — Customer Count Conflict

**Scenario:**
- Finding: Company's active customer count
- Source 1: Company Q1 2026 earnings call: "250 active customers"
- Source 2: Gartner customer survey: "Product has approximately 180 active users"
- Source 3: Company Q2 2026 press release: "250+ customers"
- Discrepancy: 250 vs. 180 (28% difference)

**Classification: CONFLICTED**
- Magnitude: 70 customer difference is material (28% of lower estimate)
- Possible explanations: Gartner survey lags earnings call timing, definition of "active" differs (paying vs. logged-in), multiple locations counted differently
- Cannot determine which count is accurate
- Scoring: INELIGIBLE for Quality scoring; creates customer validation concern

**Output:**
```
Active Customer Count
- Company reporting (Q1-Q2 2026): 250+ customers
- Gartner customer survey: ~180 active users
- Conflict: 28% discrepancy (250 vs. 180)
- Possible explanations: Survey timing lag, different definitions of "active," multiple customer locations
- Assessment: Cannot determine definitive customer count from available sources
- Implication: Customer validation strength is unclear; estimate ranges from 180–250 depending on source credibility assessment
- Recommendation: Request company to define "active customer" methodology and provide supporting data; request Gartner to clarify survey timing and sampling methodology
```

#### Example 3D — Regulatory Requirement Conflict

**Scenario:**
- Finding: Whether company's product requires FDA approval
- Source 1: Company legal assessment: "Product is a wellness app; no FDA approval required"
- Source 2: FDA guidance on lab-developed tests: Product may meet definition of LDT and require FDA oversight
- Source 3: Law firm analysis: "Regulatory status depends on specific product claims and performance"
- Discrepancy: Company says no; FDA guidance suggests possible requirement; lawyers say it depends

**Classification: CONFLICTED**
- Magnitude of conflict: Differs from "no requirement" to "possible requirement"
- Critical for regulatory assessment: This is a hard-blocker module
- Cannot determine status without direct regulatory inquiry
- Scoring: INELIGIBLE; hard-blocker gate may be triggered

**Output:**
```
Regulatory Status — FDA Approval Requirement
- Company position: Product is wellness app; no FDA approval required
- FDA guidance: Product may meet definition of laboratory developed test (LDT); regulatory oversight may apply
- Legal analysis: Regulatory status depends on specific product claims and performance characteristics
- Conflict: Company claims no requirement; FDA guidance suggests possible requirement; legal status is ambiguous
- CRITICAL: Regulatory status is unresolvable from available sources
- Assessment: Cannot independently verify regulatory status
- Recommendation: **Request company to provide written regulatory assessment from qualified regulatory counsel confirming FDA classification and any approval requirements**
- Impact: Regulatory compliance module cannot be scored; hard-blocker gate triggered until verified
```

---

## Classification 4: UNVERIFIED

**Definition:** Source identified but inaccessible (paywall, geographic restriction, not currently available). The information exists but cannot be retrieved in this session.

**Scoring Eligibility:** INELIGIBLE → Listed in provenance register only

**Circumstances:**
- Paywall-protected research (subscription required)
- Geographic restrictions (available only in specific country)
- Out-of-print or archived sources
- Database entries not currently available
- Source exists but is offline/unavailable

### Unverified Examples

#### Example 4A — Paywall-Blocked Analyst Report

**Scenario:**
- Finding: Industry analyst report on market size cited in company pitch
- Company cites: "Per McKinsey, the enterprise automation market is $120B (2024)"
- Search: Locate McKinsey report on enterprise automation
- Result: Article identified but full report requires subscription; cannot access detailed methodology or specific findings

**Classification: UNVERIFIED**
- Source exists: McKinsey research is published and credible
- Content inaccessible: Full report behind paywall; only abstract is available
- Cannot verify: Cannot see methodology or confirm the specific $120B figure
- Scoring: INELIGIBLE

**Output:**
```
Enterprise Automation Market Size
- Company cites: $120B per McKinsey (2024)
- Research result: McKinsey article identified but full report is behind paywall; abstract available but detailed methodology and figures are inaccessible
- Verification status: Cannot independently verify the $120B figure or McKinsey's methodology
- Recommendation: Company should provide copy of McKinsey report or supply alternative analyst sources with accessible methodology (Gartner, IDC, Forrester)
```

**What to do:**
- Flag the gap in provenance register
- Request company to provide the source or alternative verification
- Do not use the McKinsey figure in Quality scoring

#### Example 4B — Geographic Restriction

**Scenario:**
- Finding: Regulatory requirements in India for fintech companies
- Search: India's Reserve Bank of India (RBI) payment system operator regulations
- Result: RBI website is accessible; some materials in Hindi; key regulatory guidance documents are only available in Hindi, not English

**Classification: UNVERIFIED** (for non-Hindi-reading assessor)
- Source exists: Official RBI regulatory guidance
- Content partially inaccessible: Non-English materials
- Translation required: Official English translation not readily available
- Cannot verify: Cannot confidently interpret Hindi regulatory text without official translation
- Scoring: INELIGIBLE (for critical compliance requirements)

**Output:**
```
India Fintech Regulatory Requirements
- Company operates in India; requires verification of regulatory requirements
- Source: Reserve Bank of India (RBI) official regulatory guidance available
- Access limitation: Key regulatory documents are in Hindi; no official English translation is readily available
- Verification status: Cannot independently verify requirements from English sources; would require official translation or local legal counsel
- Recommendation: Request company to provide certified English translation of applicable RBI regulations OR engage India-based legal counsel to confirm regulatory status
```

**What to do:**
- Acknowledge that the information exists but is inaccessible in the required language
- Request company to provide translation or legal analysis
- Do not attempt machine translation for regulatory requirements

#### Example 4C — Database Record Not Found

**Scenario:**
- Finding: Competitor funding amount
- Company names competitor: "TechCorp Industries (founded 2021)"
- Search: Crunchbase search for "TechCorp Industries"
- Result: No entry found in Crunchbase; company may be too early-stage, private with no disclosed funding, or registered under different name

**Classification: UNVERIFIED**
- Source (database): Crunchbase is the primary funding source but has no record
- Existence unclear: Company may be private without disclosed funding, or may not be registered in Crunchbase
- Cannot verify: No funding information is accessible
- Scoring: INELIGIBLE

**Output:**
```
Competitor Funding — TechCorp Industries
- Company identified competitor: TechCorp Industries (founded 2021)
- Research result: No Crunchbase record found; company may be unfunded, private without disclosed funding, or registered under different name
- Verification status: Competitor funding cannot be independently verified
- Recommendation: Request company to provide evidence of competitor positioning (e.g., customer list, pricing, market share) if available; or request company to provide competitor analysis from research service
```

**What to do:**
- Flag as data not available in primary source
- Request company to provide information if material to assessment
- Do not assume company doesn't have funding; just note that it's not publicly disclosed

#### Example 4D — Subscription Research Service

**Scenario:**
- Finding: Detailed competitive intelligence on private company
- Source identified: CB Insights has detailed research on private competitors; accessible only with CB Insights subscription
- Search: Attempt to retrieve; subscription required
- Result: Source exists but inaccessible without subscription

**Classification: UNVERIFIED**
- Source credible: CB Insights is a primary source for private company data
- Access required: Subscription or company-provided access needed
- Cannot retrieve: Cannot access in current session without subscription
- Scoring: INELIGIBLE

**Output:**
```
Detailed Competitive Landscape
- Company competitor analysis suggests multiple private competitors
- Research result: CB Insights maintains detailed private company research; specific competitive data requires subscription
- Verification status: Competitive intelligence cannot be independently verified without subscription access
- Recommendation: If detailed competitive benchmarking is material, recommend either:
  a) Company subscribes to CB Insights and provides relevant research
  b) Company provides its own competitive analysis with supporting evidence (customer feedback, win/loss analysis, pricing comparison)
```

---

## Classification 5: TRAINING-DERIVED

**Definition:** Knowledge from training data, not from live retrieval in this session. This is NOT a valid research source for module scoring.

**Scoring Eligibility:** ALWAYS INELIGIBLE → Never contributes to any score; flagged as context only

**Examples of Training-Derived Knowledge:**
- "Typical Series A funding is $2–5M" (general knowledge)
- "SaaS churn is typically 5% per month" (pattern knowledge)
- "Medical device regulations require FDA approval" (background knowledge)
- "Venture investors focus on market size and team" (conceptual knowledge)
- Any knowledge not retrieved from a live source in this session

### Training-Derived Examples

#### Example 5A — Using Training Knowledge as Baseline

**Violation — Training-Derived Used for Scoring:**
```
Series A Valuation Assessment
- Typical Series A valuations for SaaS companies range from $15–30M post-money
- This company requests $40M post-money
- Assessment: Company's valuation is above typical range (Quality 1)
```

**Problem:** The "typical $15–30M" range is from training data, not a live analyst report. It cannot contribute to Quality scoring.

**Correction:**
```
Series A Valuation Assessment
- Company requests: $40M post-money valuation
- General benchmark: Typical SaaS Series A post-money valuations are $15–30M (training-derived baseline; should be verified)
- Live research findings:
  - Gartner (2024): Median SaaS Series A is $25M post-money
  - Crunchbase data (2023–2024): Series A SaaS companies range $15–35M post-money depending on traction
- Assessment: Company's $40M request is 10–60% above published benchmarks depending on segment
- Recommendation: Request company to justify valuation relative to traction metrics and comparable Series A companies in the sector (Quality: UNVERIFIED without company justification)
```

#### Example 5B — Training Knowledge for Context, Not Scoring

**Compliant Use of Training-Derived Knowledge:**
```
Market Dynamics — SaaS Consolidation

Training context: SaaS markets often consolidate around a few major players; average market leader captures 30–40% share.

Live research findings:
- [Gartner data on market concentration]
- [IDC competitive landscape]

Assessment: [Based on live research]
```

**Why this is compliant:** Training knowledge is labeled as "context" and is not used for scoring. Live research drives the assessment.

#### Example 5C — Hypothesis Generation (Acceptable Use)

**Acceptable Use:**
```
To assess competitive positioning, I will search for:
- Market share data (competitors' revenue as % of addressable market)
- Customer retention and expansion metrics
- Pricing and go-to-market positioning

[Background knowledge about what investors care about informs search strategy, but scoring will be based on retrieved data, not training knowledge]
```

**Why this is compliant:** Training knowledge informs the search strategy but does not contribute to scoring; only live research does.

#### Example 5D — Flagging Training vs. Live Knowledge

**Compliant Output Distinguishing Sources:**
```
Financial Metrics Benchmarks

General knowledge (training-derived): Typical SaaS CAC payback is 12–18 months; LTV/CAC ratio target is 3+; gross margin is 70–80%

Live research findings:
- OpenView SaaS benchmarks (2024): Median CAC payback 14 months; median LTV/CAC 3.2x; median gross margin 73%
- Insight Partners SaaS benchmark: Similar findings

Company metrics:
- CAC payback: 20 months (above typical)
- LTV/CAC: 2.1x (below target)
- Gross margin: 65% (below typical)

Assessment: [Based on live research comparison to company metrics]
```

**Why compliant:** Training-derived knowledge is labeled as context; live research provides the actual benchmark; company metrics are compared to live (not training-derived) benchmarks.

---

## Edge Cases and Conflict Resolution

### Edge Case 1: Source Claims vs. Independent Research

**Scenario:**
- Company claims: "Our product has been adopted by 50+ Fortune 500 companies"
- Research: Identifies 15 Fortune 500 companies publicly mentioned in case studies or press releases
- Remaining 35 companies: Claimed but not independently verifiable

**Classification:**
- Verified findings: 15 companies independently confirmed
- Unverified claims: 35 companies claimed but not verified

**Output (Honest):**
```
Enterprise Adoption
- Company claim: 50+ Fortune 500 company adoption
- Independent verification: 15 Fortune 500 companies confirmed through public case studies and press releases
- Unverified: 34 Fortune 500 companies are claimed but cannot be independently verified (likely due to confidentiality)
- Assessment: Strong evidence of Fortune 500 adoption (15 confirmed); claim of 50+ is not fully verifiable but is plausible given typical customer confidentiality
- Scoring: Verified portion (15 customers) contributes to Quality; unverified portion should be treated as company assertion
```

### Edge Case 2: Outdated Data (Outside 2-Year Window)

**Scenario:**
- Company claims: Product regulation was finalized in 2023
- Research finds: 2020 regulatory guidance (most recent available)
- Gap: Regulations may have changed in the intervening 3 years

**Classification: UNVERIFIED** (due to recency threshold)
- Source: Exists and was authoritative at time of publication
- Recency: Outside 2-year window for regulatory requirements; likely superseded
- Current status: Unknown

**Output:**
```
Regulatory Status
- Company claims: Product regulation finalized in 2023
- Research finding: Most recent regulatory guidance located is from 2020
- Gap: Regulations may have been updated since 2020; current status is unclear
- Verification status: Cannot verify current regulatory status from available sources
- Recommendation: Request company to provide most recent regulatory guidance (2023 or later) confirming current requirements
```

### Edge Case 3: Conflicted but High-Confidence Sources

**Scenario:**
- Finding: Market growth rate
- Source 1: Gartner (2024) — 18% CAGR
- Source 2: IDC (2024) — 22% CAGR
- Difference: 4 percentage points (unusual discrepancy for major analysts)

**Classification: CONFLICTED** (but with a note on quality of sources)
- Magnitude: 4 percentage point difference is material but not huge
- Sources: Both Gartner and IDC are top-tier analysts
- Likely explanation: Different segment definitions or methodologies
- Scoring: INELIGIBLE for scoring, but with high confidence that true value is 18–22%

**Output:**
```
Market Growth Rate
- Gartner (2024): 18% CAGR
- IDC (2024): 22% CAGR
- Discrepancy: 4 percentage points (likely due to segment definition differences)
- Confidence level: High (both sources are top-tier analysts; true value likely falls within 18–22% range)
- Scoring: Conflicted classification (ineligible for Quality scoring); however, high confidence that estimate is in the 18–22% range
- Recommendation: Request company to clarify segment definition and compare against both analyst estimates
```

---

## Summary Classification Decision Matrix

| Evidence Quality | Classification | Scoring | Language | Example |
|---|---|---|---|---|
| Authoritative single source, direct match | Verified | Eligible | "X is Y" | "FDA requires 510(k) for Class II devices" |
| 2+ sources align within 10% | Corroborated | Eligible (high confidence) | "X is Y; confirmed by N sources" | "Market is $600B per Gartner, IDC, Forrester" |
| Sources differ 15%+ or unresolvable | Conflicted | Ineligible | "X may be Y or Z; sources differ" | "Market size ranges $145–250B; definitions differ" |
| Source identified but inaccessible | Unverified | Ineligible | "X cannot be determined; source inaccessible" | "McKinsey report behind paywall; cannot verify" |
| Knowledge from training data, no live retrieval | Training-Derived | Always Ineligible | Flag as context: "General knowledge: X is Y; verify with live data" | "Typical Series A is $2–5M; verify with Crunchbase" |
