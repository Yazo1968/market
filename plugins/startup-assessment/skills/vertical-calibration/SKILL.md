---
name: vertical-calibration
description: >
  This skill should be used when framework-builder needs to adjust domain emphasis and module
  criticality based on the identified industry vertical and commercial model. Trigger phrases:
  "vertical calibration", "adjust for vertical", "fintech framework", "medtech requirements",
  "SaaS calibration", "B2B adjustments", "commercial model calibration", "vertical adjustments".
version: 0.1.0
---

# Vertical and Commercial Model Calibration Reference

## Introduction

Apply vertical and commercial model calibrations in combination with stage calibration. These adjustments modify the base assessment framework after stage calibration is applied. A single framework may trigger multiple vertical and commercial model adjustments—when they do, elevations stack and conflicts are resolved in favor of the higher criticality classification.

## Section 1: Vertical Adjustments

For each vertical, this section specifies: what changes, which modules are elevated to hard requirement, key evidence requirements, and the reasoning behind elevated emphasis.

### Fintech

**Adjustments:**
- Regulatory and Compliance Profile (D2) elevated to hard requirement at all stages
- Financial Risk Assessment (D8) elevated to primary domain
- Data Protection and Privacy (D10) elevated to primary domain

**Why:** Financial services regulation is a non-negotiable entry barrier. Data security is existential risk. Regulatory misalignment is a permanent blocker.

**Module elevations:**
- License/Regulatory Status (D2): Minimum threshold ≥0.7 at all stages
- KYC/AML Compliance Roadmap (D2): Minimum threshold ≥0.6
- PCI-DSS and Data Security (D10): Minimum threshold ≥0.6
- Financial Risk Modeling (D8): Minimum threshold ≥0.5

**What must be present:**
- Explicit statement of regulatory strategy (e.g., "pursuing EU e-money license")
- Timeline and cost estimate for regulatory approval
- Identification of primary regulatory body for target jurisdiction
- Evidence of legal counsel engagement on regulatory pathway

**Red flags to escalate:**
- Regulatory status is unclear or aspirational only ("will be regulated")
- Compliance cost not budgeted or underestimated (e.g., <$100K for EU banking license)
- No legal counsel identified for regulatory matters
- Product moves money without established regulatory precedent

**Vertical-specific domains to activate:**
- Anti-Money Laundering (AML) Strategy (custom module, D8): Required at Seed+
- Customer Verification (KYC) Process (D4): Evidence of implementation required at Series A+
- Fraud and Abuse Monitoring (D8): Operational evidence required at Traction stage

### Medtech / Healthtech

**Adjustments:**
- Regulatory and Compliance Profile (D2) elevated to hard requirement at all stages
- Clinical Validation Evidence (add as module within D5/Traction) elevated to hard requirement at Seed+
- IP Ownership and Patent Portfolio (D10) elevated to primary domain at all stages
- Medical Device Safety (D8) elevated to primary domain at Seed+

**Why:** FDA/CE/MDR/TGA regulatory pathway determines market access and viability. Clinical evidence determines scientific credibility. IP is the primary defensible asset in medtech.

**Module elevations:**
- Regulatory Pathway Identification (D2): Minimum threshold ≥0.7 at all stages
- Clinical Evidence and Validation Plan (D5): Minimum threshold ≥0.6 at Seed+
- Patent Strategy and IP Portfolio (D10): Minimum threshold ≥0.6 at Seed+
- Design Controls and Safety Analysis (D8): Minimum threshold ≥0.5 at Series A+

**What must be present:**
- Explicit identification of regulatory classification (Class I/II/III device, medication, diagnostic, etc.)
- Clinical trial strategy and timeline (even if pre-clinical, must have plan)
- Third-party clinical data or evidence from prototype testing
- Patent search results and freedom-to-operate analysis at Series A+
- Evidence of clinical advisors or medical advisors on team

**Red flags to escalate:**
- Regulatory classification is unclear or disputed
- No clinical evidence whatsoever and no clinical trial plan
- Patent landscape search not conducted
- Key clinical advisor conflicts of interest not disclosed
- Design controls documentation incomplete

**Vertical-specific domains:**
- Clinical Endpoint Definition (D1 within Market): Reimbursement pathway tied to clinical outcomes
- Investigator and Hospital Relationships (D4): Enrollment and adoption depends on clinical relationships
- Real-World Evidence Plan (D5): Post-market monitoring and real-world data strategy

### Proptech

**Adjustments:**
- Cost Structure and Capital Intensity (D3) elevated to primary domain
- Balance Sheet and Asset Accounting (D7) elevated to hard requirement
- Regulatory and Compliance Profile (D10) activated and elevated based on geography
- Property and Real Estate Specific Risk (D8) elevated to primary

**Why:** Real estate regulation varies significantly by geography and property type. Capital structure is critical for asset-heavy models. Balance sheet integrity is directly tied to property valuations.

**Module elevations:**
- Capital Expenditure and Land/Asset Acquisition (D3): Minimum threshold ≥0.7
- Property Valuation Methodology (D7): Minimum threshold ≥0.6
- Jurisdictional Zoning and Regulatory Approval (D10): Minimum threshold ≥0.6 (varies by target property type/geography)
- Property Market Cyclicality (D8): Minimum threshold ≥0.5

**What must be present:**
- Breakdown of capital structure (cash vs. debt vs. equity capital required)
- Property/asset valuation methodology and third-party appraisal (if applicable)
- Zoning compliance and planning permission status for target properties
- Real estate attorney engagement for target market
- Historical property performance data or comparable property analysis

**Red flags to escalate:**
- Asset valuations not supported by independent appraisal or market comparables
- Zoning or planning permission missing or uncertain
- Capital requirements not clearly separated by property vs. operations vs. technology
- No understanding of local property market dynamics
- Regulatory pathway differs significantly from stated assumptions

**Vertical-specific domains:**
- Tenant/Occupancy Quality (D5): For rental/leasing models, tenant credit quality and diversification
- Construction and Development Timeline (D4): For development/construction, detailed project timeline and contingency
- Property Management Operational Capability (D6): In-house vs. outsourced property management and team capability

### Cleantech / Deeptech

**Adjustments:**
- Technology Architecture and Technical Moat (D2) elevated to hard requirement at all stages
- Defensibility Assessment and IP (D2) elevated to hard requirement at all stages
- Capital Intensity and Balance Sheet (D7 and D9) elevated to hard requirement at all stages
- Development Timeline and Regulatory Risk (D8) elevated to primary domain

**Why:** Deep tech has long development timelines and high capital requirements. Technical defensibility is the primary moat. Regulatory uncertainty is significant risk. Capital structure determines viability.

**Module elevations:**
- Technology Readiness Level (TRL) and Development Stage (D2): Minimum threshold ≥0.5
- Patent Portfolio and Freedom-to-Operate (D2): Minimum threshold ≥0.7 at Seed+
- Capital Requirements and Burn Model (D7/D9): Minimum threshold ≥0.7
- Development Risk and Contingency (D8): Minimum threshold ≥0.6
- Regulatory and Environmental Compliance Risk (D8): Minimum threshold ≥0.6

**What must be present:**
- Technology readiness level (TRL 1-9) explicitly stated with development plan
- Patent search and freedom-to-operate analysis (peer review or patent attorney assessment)
- Detailed development timeline to commercial viability with technical milestones
- Contingency plan and risk identification for critical technical bottlenecks
- Third-party technical validation or proof of concept if available
- Capital plan extending to commercial production or deployment

**Red flags to escalate:**
- Technology readiness level below TRL 3 at Seed stage
- Patent landscape not assessed or freedom-to-operate assumed without analysis
- Development timeline underestimated or lacking contingency buffer (e.g., >50% probability of delay)
- No third-party technical validation at Seed+
- Capital requirement uncertainty exceeds ±25% (e.g., "somewhere between $2M and $20M")

**Vertical-specific domains:**
- Materials Science and Supply Chain (D4): For hardware/physical tech, material sourcing and supply chain for novel materials
- Test and Validation Facilities (D2): Access to third-party testing or validation infrastructure
- Manufacturing Scalability Pathway (D4): From prototype to pilot to commercial scale; manufacturing partner strategy

### SaaS

**Adjustments:**
- Unit Economics and Revenue Quality (D3) elevated to primary domain at all stages
- Retention and Churn Dynamics (D5) elevated to hard requirement at Seed+
- Customer Acquisition Economics (D4) elevated to primary domain at Seed+
- Expansion and Upsell Mechanisms (D4) elevated at Series A+

**Why:** SaaS businesses are defined by recurring revenue and unit economics. Cohort retention determines long-term value. CAC payback period determines sustainability.

**Module elevations:**
- Monthly Recurring Revenue (MRR) and MRR Growth (D5): Minimum threshold ≥0.6 at Seed+
- Monthly Churn Rate (D5): Minimum threshold ≥0.6 at Seed+
- Customer Acquisition Cost (D4): Minimum threshold ≥0.6 at Series A+
- LTV:CAC Ratio (D3): Minimum threshold ≥0.6 at Series A+
- Net Revenue Retention / Expansion Rate (D4): Minimum threshold ≥0.5 at Series A+

**What must be present:**
- Monthly churn rate tracked by cohort (even if cohorts are small)
- CAC calculated and payback period established (even if directional)
- Evidence of MRR trends (month-over-month growth rate)
- Pricing model and customer segment breakdown
- Expansion upsell opportunity identified and quantified

**Red flags to escalate:**
- Monthly churn rate above 10% at Seed or above 5% at Series A
- CAC payback period > 24 months at Series A (> 12 months is deteriorating)
- No monthly breakdown of revenue (all metrics annual only)
- LTV:CAC ratio below 3:1 at Series A
- Expansion revenue is zero or not tracked

**Vertical-specific domains:**
- Logo Retention vs. Dollar Retention (D5): Distinguish between customer count retention and revenue retention
- Free-to-Paid Conversion (D5): For freemium models, conversion rate and funnel
- Self-Serve vs. Sales-Led Motion (D4): Understand unit economics differ significantly; both must be tracked separately if both exist

### Hardware / Physical Technology

**Adjustments:**
- Cost Structure and Manufacturing Economics (D3) elevated to hard requirement
- Supply Chain and Production Risk (D4) elevated to primary domain
- Capital Structure and Balance Sheet (D9) elevated to hard requirement
- Go-to-Market Channel Complexity (D4) elevated

**Why:** Physical products have manufacturing and supply chain risk. Capital intensity is high. Channel-to-market complexity is significant.

**Module elevations:**
- Bill of Materials (BOM) and Unit Cost (D3): Minimum threshold ≥0.6
- Manufacturing Partner and Capacity (D4): Minimum threshold ≥0.6 at Series A+
- Supply Chain Risk and Contingency (D4): Minimum threshold ≥0.5
- Capital Requirements for Tooling and Inventory (D9): Minimum threshold ≥0.7
- Distribution and Channel Strategy (D4): Minimum threshold ≥0.5

**What must be present:**
- Detailed BOM with unit cost breakdown
- Manufacturing partner identified (or internal manufacturing plan with equipment capital)
- Tooling cost and timeline for production-ready design
- Supply chain for critical components identified and vetted
- Inventory financing plan (capital required for initial production run)
- Distribution channel(s) identified with partner agreements or timeline

**Red flags to escalate:**
- BOM incomplete or unit costs are estimates with high variance
- Manufacturing partner not identified or not committed
- Tooling cost underestimated (common: ±50-100% for first-time hardware companies)
- Critical components sourced from single supplier with no contingency
- No inventory financing plan; unclear how working capital will be funded
- Distribution channel unclear; selling strategy not defined

**Vertical-specific domains:**
- Regulatory Certifications and Compliance (D2 via D10): FCC, CE, RoHS, safety certifications
- Warranty and Returns Strategy (D3): Post-sale support cost and product reliability assumptions
- Reverse Logistics and Repair (D4): Return and repair fulfillment channel and cost

### Marketplace

**Adjustments:**
- Customer Segmentation for Supply and Demand (D1) elevated to hard requirement with dual-side analysis
- Network Effects and Defensibility (D2) elevated to primary domain at all stages
- Customer Acquisition Economics (Dual-side) (D4) elevated to hard requirement at Seed+
- Liquidity and Transaction Quality (D5) elevated to hard requirement at Series A+

**Why:** Marketplace dynamics require simultaneous analysis of both supply and demand sides. Network effects are the defining moat. Dual-sided CAC must be analyzed separately.

**Module elevations:**
- Supply-Side Market Definition (D1): Minimum threshold ≥0.6
- Demand-Side Market Definition (D1): Minimum threshold ≥0.6
- Network Effects and Defensibility (D2): Minimum threshold ≥0.7 at Seed+
- Supply-Side Acquisition Cost (D4): Minimum threshold ≥0.6 at Series A+
- Demand-Side Acquisition Cost (D4): Minimum threshold ≥0.6 at Series A+
- Marketplace Liquidity and Transaction Quality (D5): Minimum threshold ≥0.6 at Series A+

**What must be present:**
- Separate market definition and TAM for supply side and demand side
- Thesis on network effects and why the model is defensible (explain the moat)
- Evidence of supply and demand balance (not just one side growing)
- Separate CAC figures for supply-side and demand-side acquisition
- Transaction quality metrics (completion rate, fraud rate, return rate)
- Evidence of repeat transaction behavior (not one-time transactions)

**Red flags to escalate:**
- Supply or demand side not clearly defined as separate segments
- Network effects thesis is vague or absent ("our network grows faster over time" without mechanism)
- Supply or demand side is growing while the other side is stagnant
- Single CAC figure without breakdown by supply/demand
- Transaction completion rate below 80% (high friction/trust issues)
- No evidence of repeat transactions; primarily first-time transactions

**Vertical-specific domains:**
- Payment and Settlement (D3): Transaction fee structure, payment terms, settlement timing
- Dispute Resolution and Trust (D10): Fraud detection, seller/buyer dispute process, trust mechanisms
- Supply-Demand Rebalancing Strategy (D4): Playbook for rebalancing if one side grows faster

### AI / Machine Learning

**Adjustments:**
- Data Strategy and Data Access (add as module within D2) elevated to hard requirement at all stages
- Technology Architecture and Model Quality (D2) elevated to hard requirement
- Defensibility Assessment and Model IP (D2) elevated to hard requirement at Seed+
- Regulatory and Bias Risk (D8 and D10) elevated based on application domain

**Why:** AI value is driven by data quality and availability. Model IP and training data ownership is increasingly litigated. Regulatory uncertainty (bias, transparency, data privacy) is significant.

**Module elevations:**
- Data Sourcing Strategy (D2): Minimum threshold ≥0.6
- Data Ownership and Licensing (D2): Minimum threshold ≥0.7 at Seed+
- Model Performance and Validation (D2): Minimum threshold ≥0.6
- Model Training Data Attribution (D2): Minimum threshold ≥0.6 at Series A+
- Algorithmic Bias and Fairness (D8): Minimum threshold ≥0.5
- Data Privacy and Compliance (D10): Minimum threshold ≥0.6

**What must be present:**
- Clear statement of data sourcing strategy (proprietary, licensed, user-generated, synthetic)
- Evidence of data ownership or licensing rights (not implied or assumed)
- Model performance metrics on hold-out test set (accuracy, precision, recall, F1, AUC-ROC as appropriate)
- Model validation on real-world data (not just training data)
- Bias testing results or methodology (for models used in consequential decisions)
- Data privacy compliance plan aligned with GDPR, CCPA, or relevant regulation

**Red flags to escalate:**
- Data sourcing strategy relies on web scraping without clear legal basis or licensing
- Model trained on public datasets without investigation of licensing terms
- Model performance reported only on training data (no hold-out test set)
- No bias testing or fairness assessment conducted
- Data privacy compliance is assumed or not clearly addressed
- Model training data provenance unknown or not documented
- Dependency on a single data provider without contingency

**Vertical-specific domains:**
- Model Explainability and Interpretability (D2): For regulated domains, ability to explain model decisions
- Model Drift and Retraining (D4): Operational capability to monitor and retrain models as data distribution changes
- Adversarial Robustness (D2): For security-sensitive applications, testing against adversarial inputs

### EdTech

**Adjustments:**
- Engagement and Retention Metrics (D5) elevated to hard requirement at Seed+
- Regulatory and Data Privacy Compliance (D10) elevated based on geography and student age group
- B2B vs. B2C vs. B2B2C Channel Complexity (D4) elevated to hard requirement
- Learning Outcome Evidence (D5) elevated to hard requirement at Series A+

**Why:** EdTech value is defined by learning outcomes and user engagement. Student data privacy regulations (FERPA, COPPA, GDPR) vary by geography. Channel-to-market complexity determines unit economics.

**Module elevations:**
- User Engagement and Session Metrics (D5): Minimum threshold ≥0.6 at Seed+
- Learning Outcome Measurement (D5): Minimum threshold ≥0.6 at Series A+
- Student Data Privacy Compliance (D10): Minimum threshold ≥0.6 (varies by geography)
- Go-to-Market Channel (D4): Minimum threshold ≥0.6 (must address if B2B, B2C, or B2B2C)
- Teacher/Educator Adoption (D5): Minimum threshold ≥0.5 (for teacher-dependent models)

**What must be present:**
- Engagement metrics tracked (session frequency, time-on-platform, completion rate)
- Learning outcome measurement methodology (assessment-based, credential-based, or proxy metric)
- Evidence of student learning gain (pre/post-test, cohort analysis, or third-party validation)
- Identification of student data privacy regulation in target market(s)
- Privacy policy and data handling practices aligned with relevant regulation
- For B2B2C: clear definition of roles (institution, teacher, parent, student) and decision-maker

**Red flags to escalate:**
- Engagement metrics not tracked or only aggregated (cannot assess cohort behavior)
- No learning outcome measurement; only engagement metrics reported
- Student data privacy compliance not considered or assumed
- Channel strategy unclear (B2B, B2C, or B2B2C not defined)
- Teacher adoption rate or educator sentiment not measured
- Age of students not specified; potential COPPA compliance issues not addressed

**Vertical-specific domains:**
- Accreditation and Credential Recognition (D1): If offering credentials, recognition by employers or institutions
- Institutional Integration and APIs (D4): For B2B2C, integration with school/university systems
- Accessibility and Inclusive Design (D2): Meeting WCAG and accessibility standards

### AgriTech

**Adjustments:**
- Technology Architecture and Innovation (D2) elevated based on hardware vs. software vs. hybrid
- Go-to-Market and Farmer/Agronomist Channels (D4) elevated to hard requirement
- Regulatory and Compliance for Pesticides/Chemicals/Food Safety (D10) elevated based on product type
- Climate, Seasonality, and Geographic Risk (D8) elevated to primary domain

**Why:** Agricultural adoption depends on trusted channels. Regulatory barriers vary significantly by product type. Seasonality and geographic variability create operational complexity.

**Module elevations:**
- Farmer/Agronomist Relationship and Distribution (D4): Minimum threshold ≥0.6
- Technology Readiness for Agricultural Context (D2): Minimum threshold ≥0.5
- Climate, Weather, and Seasonality Impact (D8): Minimum threshold ≥0.5
- Regulatory Compliance (Pesticides/Chemicals/Food Safety) (D10): Minimum threshold ≥0.6 (if applicable to product)
- Agricultural Economics and Farmer ROI (D3): Minimum threshold ≥0.6

**What must be present:**
- Go-to-market channel identified (direct to farmers, through agronomists/advisors, through equipment dealers, through cooperatives)
- Evidence of farmer engagement or advisory board input
- Technology tested in real farm conditions (not just lab/proof of concept)
- Farmer economics analyzed (cost savings or yield improvement quantified; ROI calculated)
- Identification of relevant regulations (if offering seed treatments, pesticides, or food safety products)
- Understanding of seasonal variation and geographic differences in applicability

**Red flags to escalate:**
- Go-to-market channel not identified or unclear
- No evidence of farmer input or feedback
- Technology not tested in field conditions
- Farmer ROI not calculated or ROI claims not supported
- Regulatory applicability not assessed (for seed, chemical, or food safety products)
- Geo-specificity of technology not addressed (works in Iowa corn belt; applicability elsewhere unclear)

**Vertical-specific domains:**
- Farmer Adoption Barriers and Decision Factors (D1): Time to payback, ease of use, required behavior change
- Integration with Existing Equipment and Workflows (D4): Compatibility with John Deere, CBOT, existing farm management systems
- Scaling and Seasonal Capacity (D4): Ability to support peak-season demand and farmer onboarding

---

## Section 2: Commercial Model Adjustments

Commercial model adjustments modify domain emphasis based on the go-to-market and revenue model structure. Apply after vertical adjustments.

### B2B (Business-to-Business)

**Adjustments:**
- Sales Strategy and Sales Cycle Complexity (D4) elevated to hard requirement
- Customer Concentration and Revenue Quality (D3) elevated to hard requirement at Seed+
- Customer References and Reference-Ability (D5) elevated at Series A+
- Enterprise Contract Terms and Lock-in (D10) elevated at Series A+

**Why:** Enterprise sales cycles are long and complex. Customer concentration creates revenue risk. Enterprise customers demand proof points (references) and contractual terms.

**Module elevations:**
- Sales Cycle Length and Complexity (D4): Minimum threshold ≥0.6
- Customer Acquisition Cost (Enterprise) (D4): Minimum threshold ≥0.6 at Series A+
- Average Contract Value (ACV) (D3): Minimum threshold ≥0.6
- Customer Concentration (Top 3-5) (D3): Minimum threshold ≥0.6 at Seed+ (no single customer >30% revenue)
- Customer References and Referenceable Accounts (D5): Minimum threshold ≥0.5 at Series A+
- Contract Terms and Lock-in (D10): Minimum threshold ≥0.5 at Series A+

**What must be present:**
- Detailed sales process with defined stages and conversion rates
- Sales cycle length quantified (e.g., "average 4-6 months from initial contact to contract")
- Customer acquisition cost calculated and tracked by customer segment
- ACV identified (minimum $50K at Series A; minimum $10K at Seed)
- Customer concentration breakdown (top customers as % of revenue)
- At least 2-3 referenceable customers at Series A
- Contract terms including length, auto-renewal, termination clauses

**Red flags to escalate:**
- Sales cycle longer than 12 months without clear explanation
- No defined sales process or conversion metrics
- Single customer representing >40% of revenue
- No referenceable customers at Series A
- Contract terms are non-standard or heavily favorable to customer (e.g., 30-day termination clause)
- CAC payback period > 24 months

**Commercial model-specific adjustments:**
- Multi-product or suite upsell (D4): If selling multiple products, separate CAC and revenue per product
- Partner channel dynamics (D4): If selling through resellers, margin structure and partner incentive alignment
- Logo growth vs. dollar growth (D5): Distinguish between new customer acquisition and expansion revenue

### B2C (Business-to-Consumer)

**Adjustments:**
- Marketing Strategy and Customer Acquisition Economics (D4) elevated to hard requirement at Seed+
- Churn and Retention Metrics (D5) elevated to hard requirement at Seed+
- Brand and Market Positioning (D1) elevated at Series A+
- Customer Lifetime Value (LTV) (D3) elevated to hard requirement

**Why:** Consumer acquisition is expensive and volatile. Unit economics are driven by CAC and LTV. Retention determines long-term value.

**Module elevations:**
- Customer Acquisition Cost (D4): Minimum threshold ≥0.6 at Seed+
- Marketing Channel Effectiveness (D4): Minimum threshold ≥0.5 at Seed+
- Monthly Churn Rate (D5): Minimum threshold ≥0.6 at Seed+
- Customer Lifetime Value (D3): Minimum threshold ≥0.6 at Series A+
- LTV:CAC Ratio (D3): Minimum threshold ≥0.5 at Series A+
- Brand Recognition and Positioning (D1): Minimum threshold ≥0.4 at Series A+

**What must be present:**
- CAC tracked by marketing channel (organic, paid social, content, referral, etc.)
- Customer acquisition funnel (impression to conversion) with conversion rates by channel
- Cohort analysis showing retention by acquisition channel and cohort month
- Monthly churn rate or daily active user metrics tracked
- LTV estimated based on customer lifetime revenue and margin
- Brand differentiation or positioning explained

**Red flags to escalate:**
- CAC calculated at aggregate level only (no channel-level breakdown)
- CAC > 30% of LTV at Series A (meaning >3.3 month payback required)
- Monthly churn rate > 10% at Seed or > 5% at Series A
- No cohort retention analysis; only aggregate retention reported
- LTV estimation based on assumptions only; no historical customer lifetime data
- Primary customer acquisition channel is paid ads; no organic or owned channel

**Commercial model-specific adjustments:**
- Freemium conversion funnel (D4): If freemium model, conversion rate from free to paid must be tracked
- Referral mechanics and viral loop (D4): If referral-based growth, invitation and acceptance rates
- Subscription renewal rate (D5): For subscription, renewal rate distinct from daily churn
- Customer acquisition seasonality (D4): Identify seasonal patterns in CAC and conversion

### B2B2C (Business-to-Business-to-Consumer)

**Adjustments:**
- Channel Strategy and Partner Dependency (D4) elevated to hard requirement
- Revenue Split and Partner Economics (D3) elevated to hard requirement at Seed+
- Dual Customer Acquisition (D4) elevated to hard requirement (measure both sides separately)
- Partner Compliance and Data Governance (D10) elevated

**Why:** B2B2C creates dual-channel execution complexity. Partner dependency creates strategic risk. Revenue is split and aligned incentives are critical.

**Module elevations:**
- Partner/Platform Channel Strategy (D4): Minimum threshold ≥0.6
- Partner Acquisition and Onboarding (D4): Minimum threshold ≥0.5 at Seed+
- Revenue Sharing and Margin Alignment (D3): Minimum threshold ≥0.6 at Seed+
- End-Consumer Acquisition (D4): Minimum threshold ≥0.6 at Series A+ (separate from partner)
- Partner Concentration and Stickiness (D3): Minimum threshold ≥0.6 at Series A+
- Partner Compliance and Data Governance (D10): Minimum threshold ≥0.5

**What must be present:**
- Clear identification of the partner/platform (not generic "B2B partners")
- Revenue sharing model defined (% split, per-transaction, tiered, other)
- Partner acquisition strategy and identified partner pipeline
- End-consumer CAC through partners quantified separately from organic
- Evidence of multiple partner sources (not single partner dependency)
- Partner SLA and compliance requirements documented
- Data sharing agreements and data governance framework

**Red flags to escalate:**
- Partner/platform not identified or only one potential partner
- Revenue share not negotiated or terms are unfavorable (partner takes >70%)
- No end-consumer acquisition metrics tracked separately
- Single partner represents >60% of revenue (concentration risk)
- Partner SLAs not defined
- Unclear who owns the customer relationship

**Commercial model-specific adjustments:**
- Ecosystem lock-in and switching costs (D2): Strategic moat provided by platform lock-in
- Partner incentive alignment (D3): Partner commission structure and conflicts of interest
- White-label vs. co-branded (D1): Consumer brand awareness and positioning varies

### Platform

**Adjustments:**
- Network Effects and Defensibility (D2) elevated to hard requirement at all stages
- Monetization Sequencing and Timing (D3) elevated to hard requirement at Series A+
- Supply and Demand Acquisition Separate (D4) elevated (similar to marketplace)
- Ecosystem Health and Retention (D5) elevated to hard requirement at Series A+

**Why:** Platform value is non-linear and driven by network effects. Monetization timing is critical strategic decision. Ecosystem density (both sides) determines viability.

**Module elevations:**
- Network Effects Thesis (D2): Minimum threshold ≥0.7 at Seed+
- Defensibility and Switching Costs (D2): Minimum threshold ≥0.6 at Series A+
- Monetization Model and Timing (D3): Minimum threshold ≥0.6 at Series A+
- Creator/Supplier Acquisition and Stickiness (D5): Minimum threshold ≥0.6 at Series A+
- User/Consumer Acquisition and Engagement (D5): Minimum threshold ≥0.6 at Series A+
- Ecosystem Health Metrics (custom): Minimum threshold ≥0.5

**What must be present:**
- Explicit network effects thesis (explain mechanism: 1-sided or 2-sided, direct or indirect)
- Defensibility thesis explaining why competitors cannot replicate (data moat, switching costs, standardization, other)
- Monetization strategy identified (when and how the platform will extract value)
- Creator and user cohort analysis showing growth and retention separately
- Platform engagement metrics (transaction volume, repeat usage, ecosystem contribution)
- Governance and moderation strategy

**Red flags to escalate:**
- Network effects thesis is vague or absent
- Monetization strategy is unclear or assumed ("we'll figure it out at scale")
- Monetization delay creates runaway/capital inefficiency (e.g., "free for 5 years until we have 100M users")
- Only one side of platform is growing; the other side is stagnant
- No ecosystem health metrics; only aggregate user numbers reported
- Creator/supplier concentration is high (few creators generating most content/value)
- No governance or moderation; spam or abuse is widespread

**Commercial model-specific adjustments:**
- Creator economics and incentive (D3): Revenue share to creators, creator profitability, creator satisfaction
- Ecosystem rent extraction risk (D8): Risk of being disintermediated or rent extracted by creators
- Multi-sided monetization (D3): Different revenue model for different sides (e.g., consumers pay, creators paid differently)

---

## Section 3: Applying Multiple Adjustments

### Stacking and Conflict Resolution

When a submission triggers both vertical and commercial model adjustments (or multiple adjustments within each):

**Stacking rule:** Elevations from different rules stack. If both vertical and commercial model rules elevate the same module to hard requirement, the elevation applies once (no double-counting).

**Conflict resolution:** When adjustments conflict (e.g., vertical says "minimize financial scrutiny at pre-seed" but commercial model says "detailed revenue analysis required"), resolve in favor of the higher criticality classification.

### Example: FinTech B2B SaaS at Seed Stage

**Vertical (Fintech) elevations:**
- D2: Regulatory and Compliance Profile (hard blocker)
- D8: Financial Risk Assessment (primary)
- D10: Data Protection and Privacy (primary)

**Commercial Model (B2B SaaS) elevations:**
- D3: Unit Economics and Revenue Quality (primary)
- D4: Sales Strategy and Sales Cycle (hard blocker)
- D5: Retention and Churn (hard blocker)

**Combined framework:**
- D2 Regulatory: Hard blocker (from vertical)
- D3 Unit Economics: Primary (from commercial model)
- D4 Sales Strategy: Hard blocker (from commercial model)
- D5 Retention and Churn: Hard blocker (from commercial model)
- D8 Financial Risk: Primary (from vertical)
- D10 Data Protection: Primary (from vertical)

**Resulting priority:** Regulatory compliance + Sales execution + Retention dynamics = FinTech B2B SaaS assessment

### Documentation Template

When applying multiple adjustments:

```
Vertical Calibration Log

Submission ID: [ID]
Identified Vertical(s): [list all]
Identified Commercial Model(s): [list all]

VERTICAL ADJUSTMENTS
[Vertical name]: [list module elevations]
[Vertical name]: [list module elevations]

COMMERCIAL MODEL ADJUSTMENTS
[Commercial model]: [list module elevations]
[Commercial model]: [list module elevations]

COMBINED FRAMEWORK ADJUSTMENTS
[Module ID]: [Original status] → [Adjusted status], triggered by [vertical/commercial]
[Module ID]: [Original status] → [Adjusted status], triggered by [vertical/commercial]

CONFLICTS IDENTIFIED AND RESOLVED
[Describe any conflicts and resolution applied]

HARD BLOCKERS CONFIRMED
[List all hard blocker modules from combined adjustments]

ASSESSOR CONFIRMATION REQUIRED
[Any new or unexpected combinations requiring verification]
```

---

## References

- `references/vertical-adjustments.md` — Detailed vertical adjustment matrices with worked examples
- `references/commercial-model-adjustments.md` — Commercial model adjustment matrices with worked examples
