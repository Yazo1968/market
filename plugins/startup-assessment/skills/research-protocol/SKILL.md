---
name: research-protocol
description: >
  This skill should be used when any agent conducts, evaluates, or classifies external research.
  Covers the 3H Principle (Honest, Humble, Hedged), confidence classifications, research categories,
  conflict resolution rules, and source attribution requirements. Trigger phrases: "external research",
  "research protocol", "confidence classification", "3H principle", "source attribution",
  "research integrity", "live retrieval", "verify this claim".
version: 0.1.0
---

# Research Protocol and 3H Principle

## Section 1 — The 3H Principle (Governing Constraint)

The 3H Principle is the foundational constraint on all external research conducted for module scoring. All research output must satisfy Honest, Humble, and Hedged standards.

### Honest
Findings must be presented exactly as they are. Submission claims and research findings are always distinguished. Never blend submission assertions with research findings to produce a cleaner narrative.

**Rules:**
- Every finding must be explicitly attributed to its source
- If a submission claims something and research contradicts it, state both: "Submission claims [X]; research indicates [Y]"
- Do not suppress contradictions or selectively report findings to support the submission's narrative
- Do not infer or extrapolate from research to "help" the submission's case

**Example of HONEST (compliant):**
- Submission claims: Market growing at 25% CAGR
- Research finding: Industry reports cite 12–15% CAGR
- Output: "Submission projects 25% growth; independent analyst reports (Gartner, IDC) indicate 12–15% CAGR. Gap of 10+ percentage points."

**Example of DISHONEST (non-compliant):**
- Submission claims: Market growing at 25% CAGR
- Research finding: Industry reports cite 12–15% CAGR
- Output: "Market is experiencing strong growth." [Hiding the gap]

### Humble
Where uncertainty exists — sources conflict, coverage is incomplete, authoritative sources are inaccessible — that uncertainty is explicitly communicated with enough specificity for the assessor to make an informed judgment.

**Rules:**
- State what you know and what you do not know
- Acknowledge gaps in coverage (e.g., "Limited public data on private competitor market share")
- When sources conflict, document the conflict; do not pick one and hide the other
- If a source is inaccessible (paywall, geographic restriction), say so
- Do not claim confidence beyond what the evidence supports

**Example of HUMBLE (compliant):**
- "Gartner reports $50B market; IDC reports $48B. Historical trend suggests stabilization around $50B, but limited coverage on emerging geographies. Recommendation: Request company's source methodology for claimed $75B TAM."

**Example of ARROGANT (non-compliant):**
- "The market is clearly $50B based on industry reports." [Hiding the IDC discrepancy and gap with company claim]

### Hedged
Where findings carry uncertainty, the output must hedge proportionally. No confidence not supported by evidence.

**Rules:**
- Use confidence language proportional to evidence strength
- "Likely" not "definitely" if evidence is from one source
- "Appears" if inference is required
- "Cannot determine" if sources are inaccessible or conflict
- Never express confidence stronger than the evidence warrants

**Confidence Language Hierarchy:**
- **Verified:** "X is [finding]" (single authoritative source, direct match)
- **Corroborated:** "X is [finding]" (multiple sources agree)
- **Inferred:** "X appears to be [finding]" (requires logical inference)
- **Unverified:** "X cannot be determined; limited accessible evidence"
- **Conflicted:** "X may be [finding A] or [finding B]; sources conflict"

**Example of HEDGED (compliant):**
- Verified: "According to Crunchbase, Company X raised $10M Series A in Q3 2023."
- Corroborated: "Multiple sources (Crunchbase, TechCrunch press, company website) confirm $10M Series A."
- Inferred: "Company X's Series A appears to target healthcare SaaS, based on team background and public statements."
- Unverified: "Specific customer list cannot be determined; not publicly disclosed."
- Conflicted: "Market size estimates range from $30B (IDC) to $50B (Gartner), reflecting different segment definitions."

### ABSOLUTE RULE — Training-Derived Knowledge is NEVER Eligible for Scoring

Training-derived knowledge — market data, regulatory requirements, competitive information, transaction benchmarks — must **NEVER** contribute to any module score on either track. This prohibition is absolute and non-configurable.

**What is Training-Derived Knowledge?**
- Information from Claude's training data (knowledge cutoff February 2025)
- General knowledge not specifically retrieved from a live source in this session
- Internalized patterns or aggregated learning (e.g., "typical Series A raises are $2–5M")
- Reasoning from first principles without live source verification

**What can Training-Derived Content Do?**
- Appear as flagged context only: "For reference, typical [X] is [Y], but this should be verified against current live data"
- Inform search strategy (e.g., "Investors often care about CAC/LTV, so I'll search for that")
- Support interpretation of research (e.g., "This metric aligns with published benchmarks")
- **Cannot contribute to Quality scoring** (Dimension B, Readiness Track)
- **Cannot establish Verified or Corroborated confidence classification**

**Violation Example:**
- Agent claims: "Market is growing at 20% CAGR, per industry knowledge" and scores Quality 2
- This is INVALID. Training-derived knowledge cannot score Quality 2. Quality is 0 if sourced only from training-derived knowledge.

---

## Section 2 — Five Research Categories

Research is organized into five categories, each with distinct sources and search strategies.

### 1. Market Validation

**Definition:** Verify market sizing, growth rate assumptions, market dynamics, customer demand patterns, and market trends.

**Search for:**
- Total addressable market (TAM) estimates by segment
- Serviceable obtainable market (SOM) and serviceable available market (SAM)
- Annual growth rates (CAGR) and trend trajectory
- Customer adoption patterns, buyer behavior
- Market consolidation or fragmentation trends
- Emerging market threats or opportunities

**Authoritative Sources:**
- Industry analyst reports (Gartner, IDC, Forrester, McKinsey)
- Government statistical agencies (census, labor, regulatory filings)
- Academic research (published market studies)
- Trade association publications and surveys
- Financial news and market intelligence databases (Bloomberg, S&P, Capital IQ)

**Fallback Sources (lower confidence):**
- Company-funded research
- Trade publication surveys
- Crowdsourced market research (SurveyMonkey, Qualtrics)
- News archives (verify against primary sources)

**Interpretation Guidance:**
- Analyst reports often provide ranges; document the range, not a point estimate
- Government data is typically authoritative but may lag 12–24 months
- Academic research may be specific to narrow segments; generalize cautiously
- Market size estimates vary by definition (serviceable vs. addressable); clarify boundaries

**Confidence Thresholds:**
- Verified: Published by 1+ analyst firm with explicit methodology
- Corroborated: 2+ independent sources within 15% of each other
- Unverified: Single source, methodology unclear, or methodologically inconsistent
- Conflicted: Sources differ by >20% or use different segment definitions

### 2. Competitive Intelligence

**Definition:** Independently map the competitive landscape, competitor positioning, and relative market position.

**Search for:**
- Direct competitors (same product category, target customer)
- Indirect competitors (alternative solutions, substitutes)
- Relative market position, market share
- Competitor pricing, positioning, go-to-market
- Competitor funding, financials (if public)
- Competitive moats or barriers to entry
- Market consolidation (M&A activity, leadership changes)

**Authoritative Sources:**
- Company databases (Crunchbase, CB Insights, PitchBook for private; SEC filings for public)
- Product review sites and analyst quadrants (G2, Capterra, Gartner Magic Quadrant)
- Patent databases (USPTO, Google Patents)
- News archives and press releases (TechCrunch, VentureBeat, industry press)
- Industry registries and directories
- Public financial filings (SEC, company annual reports)

**Fallback Sources (lower confidence):**
- Company websites and marketing materials
- LinkedIn profiles
- Industry blogs and podcasts
- Unverified crowdsourced reviews

**Interpretation Guidance:**
- Company websites are biased toward competitive advantage; verify positioning against third-party sources
- Funding data is authoritative if from primary source (Crunchbase, company announcement); private data is inferred
- Product reviews on G2/Capterra are self-selected (biased toward satisfied customers); use as directional signal only
- Patent data is reliable for technology differentiation but does not directly measure market success

**Confidence Thresholds:**
- Verified: Competitor data from Crunchbase or public filings with matching dates
- Corroborated: 2+ sources (e.g., Crunchbase + TechCrunch announcement + product review)
- Unverified: Single source or company-provided information without third-party corroboration
- Conflicted: Sources differ on competitive position or market share; market is too fragmented to determine leader

### 3. Regulatory Environment

**Definition:** Establish actual regulatory requirements, licensing mandates, compliance obligations, and regulatory risk.

**Search for:**
- Regulatory authority publications (rules, guidance, FAQs)
- Licensing or certification requirements
- Compliance timelines and deadlines
- Regulatory precedent and enforcement history
- Changes in regulatory landscape (proposed regulations, recent rulings)
- Government databases (licensing registries, enforcement actions)

**Authoritative Sources:**
- Regulatory authority official websites and published guidance (SEC, FCA, FINRA, state regulatory boards)
- Government databases and registries
- Law firm regulatory practice summaries and alerts
- Trade association regulatory guidance
- Published legal opinions and court rulings
- Government announcements (Federal Register, equivalent international)

**Fallback Sources (lower confidence):**
- Law firm websites and blogs
- Industry news on regulatory changes
- Company legal opinions (without external corroboration)
- Consultant reports on compliance

**Interpretation Guidance:**
- Regulatory authority guidance is authoritative; law firm interpretation is secondary
- Compliance timelines in regulations are precise; extract exact dates, not approximations
- Proposed regulations are not yet law; distinguish between current and anticipated requirements
- Regulatory risk is jurisdiction-specific; do not generalize across geographies without verification
- Absence of explicit regulatory requirement does not mean no regulation; search for indirect requirements (liability, insurance, standards)

**Confidence Thresholds:**
- Verified: Direct quote from regulatory authority, exact regulatory requirement identified
- Corroborated: Regulatory authority + law firm summary + industry practice alignment
- Unverified: Single non-primary source; regulatory status is uncertain
- Conflicted: Different jurisdictions have different requirements; company operates in multiple jurisdictions with conflicting requirements

### 4. Team and Credential Verification

**Definition:** Verify founder and team credentials, experience, educational background, and prior track record.

**Search for:**
- Educational credentials (degree, institution, graduation year)
- Prior employment history (companies, roles, dates)
- Board positions, advisory roles
- Prior startup involvement (exits, outcomes)
- Professional licenses or certifications
- Public statements and reputation (awards, speaking, media appearances)
- Regulatory history (disciplinary actions, litigation)

**Authoritative Sources:**
- Professional networks and registries (LinkedIn, professional associations)
- Company registries (SEC filings, business registrations, director databases)
- Educational institution verifications
- Professional licensing registries (bar associations, medical boards, engineering boards)
- News archives (major publications, industry press)
- Court records (for regulatory or legal history)
- Company filings and press releases

**Fallback Sources (lower confidence):**
- Personal websites or bios (not independently verified)
- LinkedIn profiles (self-reported; not independently verified)
- News articles or interviews (report what person claims, not independent verification)
- Venture capital firm bios or portfolio descriptions

**Interpretation Guidance:**
- LinkedIn is self-reported and not independently verified; use as starting point, not confirmation
- Company filings (especially executive bios) are subject to certification; higher credibility but may be outdated
- Educational credentials should be verified through institution directly if critical to assessment
- Startup history (prior exits, failed attempts) is relevant to track record; distinguish between success and failure outcomes
- Gaps in resume or unexplained employment transitions may indicate issues; flag for follow-up

**Confidence Thresholds:**
- Verified: Educational credential confirmed through institution; professional license confirmed through registry; regulatory history confirmed through public databases
- Corroborated: Multiple independent sources confirm experience (LinkedIn + company filing + news article)
- Unverified: Self-reported information without independent source
- Conflicted: Claims differ between sources (e.g., resume vs. court records)

### 5. Comparable Transactions

**Definition:** Establish market-rate benchmarks for valuation, deal terms, customer metrics, and financial multiples.

**Search for:**
- Recent funding rounds in the sector (amount, valuation, terms)
- Customer acquisition cost (CAC) benchmarks by segment
- Lifetime value (LTV) benchmarks
- Revenue multiples for exits
- Debt financing terms and rates
- Customer metrics (churn, expansion rate, payback period)
- M&A transaction prices and deal structures

**Authoritative Sources:**
- Funding databases (Crunchbase, PitchBook, CB Insights)
- M&A databases (PitchBook, Bloomberg, Capital IQ)
- Public company financial filings (SEC filings for SaaS, analytics firms for benchmarks)
- Analyst reports on transaction trends
- Venture capital reports and survey data
- Industry associations (SaaS benchmarks, fintech metrics, etc.)

**Fallback Sources (lower confidence):**
- News reports of funding or M&A (if from credible publication)
- VC firm reports and surveys
- Consultant benchmark reports
- Academic studies on transaction trends

**Interpretation Guidance:**
- Funding data from Crunchbase is reliable but incomplete (not all rounds are reported); use as directional, not exhaustive
- Public company multiples (SaaS, FinTech) are good benchmarks but reflect mature companies; early-stage multiples may differ
- Customer metrics (CAC, LTV, churn) vary significantly by use case, segment, and geography; benchmark against specific comparables
- Debt financing terms depend on collateral and credit quality; rate benchmarks are directional only
- Transaction prices represent completed deals; asked prices (in negotiation) are unreliable

**Confidence Thresholds:**
- Verified: Transaction announced publicly by both parties; terms confirmed in news or filing
- Corroborated: Multiple sources report same transaction with consistent terms
- Unverified: Single source, incomplete term information, or private transaction rumor
- Conflicted: Different sources report different terms or values for same transaction

---

## Section 3 — Confidence Classifications (Applied at Point of Retrieval)

Confidence classification is applied at the moment a research finding is retrieved. The classification determines whether the finding is eligible for Quality scoring.

| Classification | Definition | Scoring Eligibility | Use in Output |
|---|---|---|---|
| **Verified** | Retrieved from accessible, authoritative source; content directly confirms or refutes a specific claim | **ELIGIBLE** → Contributes to Quality (Dimension B) scoring | Quote with attribution; state as finding |
| **Corroborated** | Multiple independent sources confirm the same finding | **ELIGIBLE** → Higher evidentiary weight than Verified | Quote as "confirmed by X sources"; state confidently |
| **Conflicted** | Multiple sources present materially different findings | **INELIGIBLE** → Documented in Research Provenance Register; assessor judgment required | Document both/all positions; flag conflict; recommend assessor resolve |
| **Unverified** | Source identified but inaccessible (paywall, geographic restriction, not currently available) | **INELIGIBLE** → Listed in provenance register only | Acknowledge gap; state: "Source inaccessible; unable to verify" |
| **Training-Derived** | Knowledge from training data, not live retrieval in this session | **ALWAYS INELIGIBLE** → Never contributes to any score | Flag as context only: "General knowledge: X is Y, but verify with live data" |

### Verified Classification Examples

**Example 1 — Market Validation:**
- Search: "SaaS market size 2024"
- Source: Gartner, published 2024, directly states "Global SaaS market is $232B in 2024"
- Classification: **Verified** (authoritative source, direct match)
- Scoring: Eligible for Quality

**Example 2 — Competitive Intelligence:**
- Search: "Company X funding Series A"
- Source: Crunchbase, states "Series A: $8M, announced March 2023"
- Classification: **Verified** (authoritative database, direct data point)
- Scoring: Eligible for Quality

**Example 3 — Regulatory Requirement:**
- Search: "FDA medical device 510(k) requirement"
- Source: FDA official website states "Class II devices require 510(k) notification before marketing"
- Classification: **Verified** (regulatory authority, direct requirement)
- Scoring: Eligible for Quality

### Corroborated Classification Examples

**Example 1 — Market Size:**
- Search: "Global fintech market size"
- Source 1: IDC reports $142B in 2024
- Source 2: Gartner reports $143B in 2024
- Source 3: Fortune article cites $140–145B range
- Classification: **Corroborated** (three sources within 3% agreement)
- Scoring: Eligible for Quality; higher confidence than single Verified

**Example 2 — Competitor Funding:**
- Search: "Company X Series B funding"
- Source 1: Crunchbase states $15M Series B, June 2023
- Source 2: TechCrunch article confirms $15M round, June 2023
- Source 3: Company press release states same amount and date
- Classification: **Corroborated** (three independent sources agree)
- Scoring: Eligible for Quality

### Conflicted Classification Examples

**Example 1 — Market Size Conflict:**
- Search: "Enterprise software market TAM"
- Source 1: Gartner reports $642B
- Source 2: IDC reports $543B
- Source 3: Forrester reports $580B
- Difference: ~19% range, different segment definitions
- Classification: **Conflicted** (sources within reasonable range but definitions differ)
- Scoring: **INELIGIBLE** for Quality; document in provenance register
- Output: "Market estimates range from $543B (IDC) to $642B (Gartner), reflecting different segment definitions. Recommend company clarify which segments are included in its TAM."

**Example 2 — Competitor Positioning Conflict:**
- Search: "Company X technology differentiation"
- Source 1: Company website claims "AI-powered real-time analytics"
- Source 2: Gartner report describes as "rule-based analytics with limited AI"
- Source 3: Customer review site states "Basic analytics, no AI features"
- Classification: **Conflicted** (sources disagree on core differentiation)
- Scoring: **INELIGIBLE** for Quality scoring; assessor must judge credibility
- Output: "Company claims AI-powered analytics; Gartner analysis and customer reviews indicate limited AI implementation. Recommend technical assessment to clarify capability."

### Unverified Classification Examples

**Example 1 — Paywall-Blocked Source:**
- Search: "Industry report on market trends"
- Source: McKinsey Quarterly article identified, but access requires subscription
- Classification: **Unverified** (source exists but is inaccessible)
- Scoring: **INELIGIBLE**
- Output: "McKinsey research on market trends could not be accessed; recommend requesting company to cite specific findings or purchasing direct access."

**Example 2 — Geographic Restriction:**
- Search: "Regulatory requirements for European fintech"
- Source: Government website available in German only; translation software available but not official
- Classification: **Unverified** (source exists but interpretation requires unofficial translation)
- Scoring: **INELIGIBLE** for critical compliance requirements
- Output: "Primary regulatory guidance is in German; official English translation not readily available. Recommend company provide certified translation or engage local counsel."

### Training-Derived Classification Examples

**Example 1 — Historical Market Knowledge:**
- Agent states: "The SaaS market has grown at ~20% annually for the past 5 years, based on general industry knowledge"
- Source: Claude training data (not live retrieval)
- Classification: **Training-Derived**
- Scoring: **ALWAYS INELIGIBLE**
- Output: "Market growth has historically been ~20% annually in SaaS; verify this claim against current 2024 analyst reports to confirm it applies to the submission's specific market segment."

**Example 2 — Competitive Benchmark:**
- Agent states: "Typical Series A round size for FinTech is $2–5M"
- Source: General knowledge from training data
- Classification: **Training-Derived**
- Scoring: **ALWAYS INELIGIBLE**
- Output: "General benchmark for Series A in FinTech is $2–5M; this company's $7M raise should be compared against recent FinTech Series A data from Crunchbase to assess if it is an outlier."

---

## Section 3b — Data Timeliness and Staleness (IVS 104 Compliance)

All research data must be assessed for timeliness. Stale data reduces confidence and may invalidate findings.

### Timeliness Classification

| Data Age | Classification | Impact on Scoring |
|----------|---------------|-------------------|
| < 6 months | **Current** | Full scoring eligibility |
| 6–12 months | **Recent** | Full scoring eligibility with age noted |
| 12–24 months | **Aging** | Eligible but flagged: "Data is [N] months old; verify currency" |
| 24–36 months | **Stale** | Downgrade to Unverified unless corroborated by a more recent source |
| > 36 months | **Expired** | **INELIGIBLE** for Quality scoring. Document as historical context only. |

### Timeliness Tracking Requirements

Every research finding must record:

1. **`data_publication_date`** — when the source data was originally published (not when we retrieved it)
2. **`data_retrieval_date`** — when the source was accessed in this session (already tracked)
3. **`data_age_months`** — computed: months between publication date and assessment date

### Staleness Flags in Research Log

When a finding is classified as Aging, Stale, or Expired, the research-log entry must include:

```json
{
  "staleness_flag": "aging|stale|expired",
  "data_publication_date": "YYYY-MM-DD",
  "data_age_months": 18,
  "staleness_note": "Market sizing data is 18 months old; segment definitions may have shifted"
}
```

### Automatic Staleness Warnings

The QA/QC agent must check: if any module's Quality score relies primarily on Aging or Stale data (>50% of evidence sources are 12+ months old), flag the module with a staleness warning in the QA/QC log.

**Standards basis:** IVS 104 (Data must be Timely — reflect conditions at valuation date), ISO 8000 (data quality dimension: timeliness).

---

## Section 4 — Conflict Resolution Rules (Q&A-Confirmed)

When research sources conflict, specific resolution rules apply.

### Rule 1 — Recency Principle (Primary)
When two sources conflict and recency can determine the better figure:
- Apply the most recent data **within the last 2 years**
- If only outdated data is available, flag that data is stale

**Example:**
- Old data (2022): Company X had 50 customers
- Recent data (2024): Company X has 150 customers
- **Resolution:** Use 2024 figure; it is more recent and more likely accurate

### Rule 2 — Conservative Figure (when recency is equal)
When sources are equally recent but report different values:
- Use the **lower** (more conservative) figure
- Document the discrepancy

**Example:**
- Source 1 (2024): Market size $100B
- Source 2 (2024): Market size $150B
- **Resolution:** Use $100B; more conservative for market sizing assessment

**When to break Rule 2:**
- If the conservative figure comes from a clearly less authoritative source, flag the conflict and present both
- Example: Single blogger claims $100B; three analyst firms claim $150B → Use $150B (corroborated despite being higher)

### Rule 3 — Multiple Dimensions
When sources conflict on multiple dimensions (e.g., funding amount, date, investor composition):
- Resolve each dimension independently per rules above
- Flag any resolved discrepancies

**Example:**
- Source 1: "Company X raised $5M Series A in January 2024"
- Source 2: "Company X raised $6M Series A in February 2024"
- **Resolution:**
  - Funding amount: Conflicted ($5M vs. $6M) → Use $5M (conservative) → **INELIGIBLE for scoring**
  - Date: Conflicted (January vs. February) → Use more recent (February if confirmed elsewhere) or flag conflict
  - **Output:** "Sources conflict on amount ($5M vs. $6M) and date (January vs. February); recommend company clarification"

### Rule 4 — 5–10 Year Historical Perspective
- Document historical values going back 5–10 years alongside the current figure
- This provides context for trends and volatility

**Example:**
- Current market size (2024): $250B
- 2023: $210B
- 2022: $180B
- 2021: $160B
- 2019: $120B
- **Output:** "Market has grown from $120B (2019) to $250B (2024), representing ~20% CAGR. This trajectory aligns with submission's growth assumption."

### Rule 5 — Assessor Judgment (when conflict is unresolvable)
- Never silently resolve unresolvable conflicts
- Always flag to the assessor with sufficient detail for their judgment

**Example:**
- Source 1 (analyst, 2023): Market size $500B, based on segment A + segment B
- Source 2 (analyst, 2024): Market size $300B, based on segment A only (excludes B as adjacent)
- **Resolution:** Cannot mechanically resolve (different segment definitions)
- **Output:** "Market size estimates range from $300B (segment A only) to $500B (segments A + B). Recommend assessor clarify which segments company targets and request company to cite definitions used in its TAM estimate."

---

## Section 5 — Source Attribution Requirements

Every externally sourced data point must be attributed with full information.

### Attribution Format for All Outputs

**For every research finding:**

1. **Source Name** — Full, official name (e.g., "Gartner, Inc." not "Gartner")
2. **URL/Reference** — Direct link to source or precise reference (page number, section title if print)
3. **Retrieval Date** — Date the source was accessed in this session (YYYY-MM-DD format)
4. **Confidence Classification** — One of: Verified, Corroborated, Conflicted, Unverified, Training-Derived
5. **Confidence Rationale** — 1–2 sentence explanation of why this classification was applied

### Attribution Example

**Finding:** SaaS market grew 20% in 2024

**Attribution Block:**
```
Source: Gartner, Inc. "SaaS Market Share and Forecast, 2024"
URL: https://www.gartner.com/en/products/gartner-research/surveys/saaS-market-forecast
Retrieved: 2026-03-08
Confidence Classification: Verified
Rationale: Gartner is an authoritative analyst firm; this report directly cites the 20% growth figure in official published research.
```

### Research Log Structure

All research must be documented in a structured Research Provenance Register (or research log) with the following columns:

| Module | Finding | Source | URL | Retrieval Date | Confidence Classification | Rationale | Contribution to Scoring? |
|---|---|---|---|---|---|---|---|
| Market Validation | TAM $500M | Gartner Report | https://... | 2026-03-08 | Verified | Authoritative source, direct finding | Quality B: YES |
| Market Validation | Growth 15% CAGR | IDC Report | https://... | 2026-03-08 | Verified | Authoritative source, direct finding | Quality B: YES |
| Market Validation | Conflicted size | Gartner vs. IDC | See above | 2026-03-08 | Conflicted | $500B vs. $450B; different segments | Quality B: NO |

### Distinctions Throughout All Outputs

The following distinctions must be explicit and maintained throughout:

1. **Submission Claim vs. Confirmed Finding**
   - Submission: "Market growing 25% CAGR"
   - Research: "Analyst reports cite 15% CAGR"
   - Output must separate these

2. **Verified vs. Corroborated vs. Conflicted**
   - Single analyst firm finding → Verified
   - Multiple analyst firms, same finding → Corroborated
   - Analyst firms differ → Conflicted

3. **Current vs. Historical**
   - Current (2024): $250B market
   - Historical context: Grew from $120B (2019)
   - Output includes both perspectives

4. **In-Scope vs. Out-of-Scope**
   - Company-claimed segment: "Enterprise SaaS"
   - Research scope: "Enterprise SaaS + SMB SaaS"
   - Output clarifies boundary differences

---

## Section 6 — Connector vs. Web Retrieval

Two types of retrieval sources may be used: structured connectors and web retrieval.

### Structured Connectors (Primary)
Configured in .mcp.json; designed for specific data types (funding databases, regulatory data, etc.).

**Confidence Hierarchy:**
- Structured connector results begin at **Verified** (if data is directly retrieved)
- Require corroboration from web retrieval or other connectors to reach **Corroborated**

**Advantages:**
- Normalized data (consistent fields, validated entries)
- Authoritative source (Crunchbase, SEC EDGAR, etc.)
- Reduces manual parsing errors

**Example:**
- Retrieval: Crunchbase connector searches "Company X funding"
- Result: $8M Series A, announced March 2023
- Classification: **Verified** (structured connector, direct result)

### Web Retrieval (Fallback)
Generic web search when structured connector is unavailable.

**Confidence Hierarchy:**
- Web retrieval results begin at **Unverified** until corroborated
- Require corroboration from structured connector or multiple web sources to reach **Verified/Corroborated**

**Disadvantages:**
- Unstructured data (may require parsing, interpretation)
- No guarantee of source authority (may include blogs, forums)
- Requires manual validation

**Example:**
- Retrieval: Web search "Company X Series A funding"
- Result: TechCrunch article states $8M round, March 2023
- Classification: **Unverified** (single web source, not yet corroborated)
- Next step: Corroborate with Crunchbase connector → **Verified**

### Connector Unavailable → Web Retrieval Fallback

**Rule:** If a structured connector is unavailable (offline, not configured, inaccessible):
1. Fall back to web retrieval
2. Classify results as **Unverified** by default
3. Attempt corroboration with additional web sources
4. If no corroboration is possible, classify as **Unverified** and flag in provenance register

**Example:**
- Attempt: Retrieve regulatory requirements via structured regulatory connector
- Result: Connector offline/inaccessible
- Fallback: Web search for "FDA Class II device 510(k) requirement"
- Source: FDA.gov official page
- Classification: **Unverified** (web retrieval, not connector) BUT with **high credibility** because source is official regulatory authority
- **Recommendation:** Classifier may upgrade to **Verified** if source is unmistakably authoritative (e.g., official government website, direct quote from regulation)

---

## Section 7 — What to Do When No Live Source Is Accessible

Three escalating scenarios for when live retrieval fails.

### Scenario 1 — Connector Inaccessible, Web Retrieval Succeeds

**Action:**
- Use web retrieval result
- Classify as **Unverified** (sourced from web, not primary connector)
- Attempt corroboration with additional web sources
- If corroborated, upgrade to **Verified/Corroborated**
- If not corroborated, remain **Unverified** and flag in provenance register

**Example:**
- Connector: Crunchbase is offline
- Web search: "Company X Series A" returns TechCrunch article + company press release (two sources, aligned on amount and date)
- Classification: **Corroborated** (two independent web sources)
- Scoring: Eligible if corroborated; otherwise Unverified and ineligible

### Scenario 2 — Both Connector and Web Retrieval Fail

**Action:**
- Classify as **Unverified**
- Document in research-log with "inaccessible" status
- **Do NOT substitute training knowledge**
- Flag as a gap for assessor to resolve
- Example: "Competitor funding amount could not be retrieved; company should provide evidence of competitive positioning from live sources"

**Example:**
- Attempt: Crunchbase search for "Company Y funding" → No results found (company is too early, unfunded, or not in database)
- Attempt: Web search for "Company Y funding" → No relevant results
- Result: Funding status is **Unverified**
- **Output:** "Competitor funding information is not publicly available; recommend requesting company to provide evidence of competitive positioning from published sources or customer data"

### Scenario 3 — Module is Critical and No Live Source Found

**Action:**
- Flag as **absent-externally-unresolvable** in gap register
- Do not attempt to infer from training knowledge
- Recommend assessor request company to provide primary evidence

**Example:**
- Module: "Regulatory Compliance" (hard blocker)
- Requirement: Confirm that company's product class requires FDA approval
- Attempt: Search FDA.gov for product classification → No specific regulatory guidance found
- Result: Regulatory status is **absent-externally-unresolvable**
- **Output:** "Regulatory status cannot be independently determined from public sources. **Critical:** Request company to provide regulatory assessment from qualified legal counsel confirming product classification and required approval pathway."

---

## References

- `references/3h-principle.md` — Detailed explanation of the 3H Principle with examples of violations and compliant outputs
- `references/confidence-classifications.md` — Worked examples of each classification level with edge cases and scoring implications
- `references/research-categories.md` — Detailed guidance for each of the 5 research categories including search strategies, source prioritization, and interpretation rules
