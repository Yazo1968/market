---
name: html-dashboard
description: >
  This skill should be used when any agent needs to generate the HTML report,
  PDF report, or structured data exports for any phase of the assessment workflow.
  Trigger phrases: "generate report", "produce output", "create HTML", "build dashboard",
  "format report", "export JSON", "deliver outputs", "write report".
version: 0.1.0
---

# HTML Dashboard & Report Generation Skill

## Overview

The html-dashboard skill provides agents with comprehensive patterns and templates for generating professional reports in the startup assessment workflow. This skill covers four distinct output types that are produced at the conclusion of each assessment phase:

1. **HTML Interactive Report** — Multi-tab executive dashboard and detailed analysis
2. **PDF Archivable Report** — Adaptive format based on assessor type (investment, credit, or strategic)
3. **Scored Module Register** — JSON export containing all readiness and fit-to-purpose scores
4. **Research Provenance Register** — JSON export containing source citations and confidence levels

The skill is designed for professional assessors (venture capital, private equity, credit analysts, corporate strategists, family offices, sovereign wealth funds) who need to evaluate startup business cases and deliver actionable determinations. All reports are self-contained (inline CSS/JS with optional CDN links) and require no external dependencies beyond trusted content delivery networks.

### Key Principles

- **Self-Contained HTML**: Single-file reports with all styling and interactivity embedded
- **Responsive Design**: Mobile-friendly layouts that work across all screen sizes
- **Accessibility**: Semantic HTML, color-blind friendly palettes, alt text for all visuals
- **Professional Appearance**: Enterprise-grade typography, spacing, and color schemes
- **Deterministic Output**: Reproducible formatting with consistent naming conventions
- **Data Integrity**: JSON exports preserve raw scores and provenance for audit trails

---

## Output Manifest

All outputs follow a consistent naming convention: `[CompanyName]_[Phase]_[YYYY-MM-DD].[ext]`

### Example: Company "TechVenture Inc." assessed on 2026-03-08

| Output | Filename | Format | Purpose |
|--------|----------|--------|---------|
| HTML Report | `TechVenture-Inc_pre-assessment_2026-03-08.html` | HTML5 (self-contained) | Interactive dashboard, domain analysis, gap register, research log |
| PDF Report | `TechVenture-Inc_pre-assessment_2026-03-08.pdf` | PDF (format varies) | Archivable document, professional presentation, standardized sections |
| Scored Register | `TechVenture-Inc_pre-assessment_2026-03-08_scores.json` | JSON | Machine-readable scores, weights, domain details |
| Provenance Register | `TechVenture-Inc_pre-assessment_2026-03-08_provenance.json` | JSON | Source citations, confidence levels, methodology notes |

### Phase-Specific Outputs

The assessment workflow consists of four phases, each generating a full output set:

1. **Pre-Assessment** — Framework setup, domain activation, initial framework configuration
2. **Assessment** — Full domain evaluation, module scoring, final determination
3. **Sensitivity Analysis** — Robustness testing, scenario analysis, flip-point identification
4. **Recommendations** — Path identification, improvement roadmaps, deal term suggestions

---

## HTML Report Architecture

### Multi-Tab Structure

Each HTML report contains a tab-based navigation system that allows assessors to explore different aspects of the evaluation. The tab bar is sticky (remains visible while scrolling) and supports keyboard navigation.

### Self-Contained Design

All HTML reports are generated as single `.html` files that can be:
- Opened directly in any modern browser (Chrome, Firefox, Safari, Edge)
- Emailed without attachment complexity
- Archived with confidence in long-term readability
- Printed to PDF for permanent records

External dependencies are limited to:
- Google Fonts CDN (Inter typeface)
- Chart.js CDN (for interactive charts)
- No backend services required

All CSS is inline (within `<style>` tags) and all JavaScript is inline (within `<script>` tags).

### Responsive Design Principles

- **Desktop (1200px+)**: Full multi-column layouts, side-by-side charts
- **Tablet (768px–1200px)**: Single-column primary content, stacked sidebar panels
- **Mobile (<768px)**: Full-width single-column, collapsible sections, optimized typography

### Color Coding for Determinations

Determination outcomes are consistently color-coded throughout all reports:

| Outcome | Color | Hex | Usage |
|---------|-------|-----|-------|
| GO | Green | `#22c55e` | Proceed with confidence; no material concerns |
| CONDITIONAL GO | Blue | `#3b82f6` | Proceed with identified conditions; gaps addressable pre-close |
| CONDITIONAL HOLD | Amber | `#f59e0b` | Hold pending material issue resolution; significant gaps |
| NO-GO | Red | `#ef4444` | Do not proceed; fundamental concerns preclude investment |

These colors are used in:
- Determination badge (large, prominent)
- Domain score indicators
- Gap severity badges
- Status indicators throughout the report

---

## Executive Dashboard Tab (Landing Page)

The Executive Dashboard is the first tab in every HTML report and serves as the landing page. It provides a complete visual summary of the assessment in a single scrollable page.

### Dashboard Sections (top-to-bottom)

#### 1. Determination Badge (Hero Section)

```
┌─────────────────────────────┐
│ CONDITIONAL GO              │ (Large, colored badge)
│ Assessment Date: 2026-03-08 │ (Subtext with date)
│ Company: TechVenture Inc.   │ (Company name)
└─────────────────────────────┘
```

- Large circular or rounded-rectangle badge (100+ pixels)
- Determination text centered with icon
- Colored by outcome (green/blue/amber/red)
- Company name and assessment date displayed below

#### 2. Key Metrics Panel

Four key indicator cards in a 2×2 grid (responsive to 1×4 on mobile):

1. **Overall Readiness Score** — Percentage (0–100%), large number with percentage sign
2. **Fit-to-Purpose Score** — Percentage (0–100%), large number with percentage sign
3. **Active Domains** — Count (e.g., "9 of 10"), with brief explanation
4. **Critical Gaps** — Count (e.g., "3 Critical"), with severity indicator

Each card includes:
- Icon (assessor-relevant, e.g., clipboard, target, alert, chart)
- Label (bold)
- Value (large, colored by severity if applicable)
- Brief context or trend indicator (e.g., "↑ +5% from baseline")

#### 3. Domain Score Heatmap

A 2×5 grid displaying all 10 domains at a glance:

```
┌────┬────┬────┬────┬────┐
│ M  │ T  │ F  │ C  │ L  │ (Domain abbreviations)
├────┼────┼────┼────┼────┤
│ 78 │ 62 │ 85 │ 45 │ 91 │ (Readiness score %)
│ 72 │ 58 │ 79 │ 42 │ 88 │ (Fit-to-Purpose score %)
├────┼────┼────┼────┼────┤
│ CC │ IP │ OR │ RH │ BD │
├────┼────┼────┼────┼────┤
│ 88 │ 71 │ 64 │ 92 │ 77 │
│ 85 │ 68 │ 61 │ 89 │ 74 │
└────┴────┴────┴────┴────┘
```

Each cell:
- Background color interpolated from red (0) → amber (50) → green (100)
- Two numbers: top = Readiness Score %, bottom = Fit-to-Purpose Score %
- Domain abbreviation as label (2–3 characters)
- Clickable to navigate to domain detail tab

**Domain Abbreviations:**
- M: Market & TAM
- T: Technology
- F: Financials
- C: Competitive Positioning
- L: Leadership & Team
- CC: Customer & Channels
- IP: Intellectual Property
- OR: Operations & Resources
- RH: Regulatory & Health/Safety
- BD: Business Development & Partnerships

#### 4. Top 3 Strengths (Bullet List)

```
Strengths identified across the assessment:
• Domain name with brief context (e.g., "Leadership: Experienced founding team with 20+ years combined experience in industry")
• Domain name with brief context
• Domain name with brief context
```

- One bullet per strength
- Include domain name in bold
- 1–2 sentence explanation per bullet
- Ordered by priority/impact (not by domain)

#### 5. Top 3 Risks (Bullet List)

```
Key risks and gaps identified:
• Domain name with brief context (e.g., "Competitive Positioning: Limited differentiation vs. three established competitors in addressable market")
• Domain name with brief context
• Domain name with brief context
```

- One bullet per risk
- Include domain name in bold
- 1–2 sentence explanation per bullet
- Ordered by severity/impact (not by domain)

#### 6. Phase Navigation Prompts

A small section at the bottom of the dashboard:

```
Next Steps:
[View Detailed Findings] [Download PDF] [Export Data] [Back to Assessment]
```

- Buttons styled consistently with determination color
- Links to other tabs or download functions
- Text like "Assessment complete. Review detailed findings by domain or export data."

---

## Pre-Assessment HTML Tab Structure

The HTML report for the Pre-Assessment phase includes the following 8 tabs:

### Tab 1: Executive Dashboard (Landing)
- See "Executive Dashboard Tab" section above
- Determination badge, key metrics, domain heatmap, top strengths/risks, navigation

### Tab 2: Assessment Framework
- **Domain Activation Table**: Rows for each of 10 domains, columns for "Active? (Y/N)", "Module Count", "Criticality Level"
- **Framework Metadata**: Assessment phase, date created, framework version, assessor name(s)
- **Module Criticality Legend**: Explanation of "Critical", "Important", "Contextual" levels
- **Weighting Summary**: How domains are weighted in overall readiness calculation (e.g., "Market (15%), Technology (12%), Financials (18%), ...")
- **Notes Section**: Any framework adjustments or custom configurations applied

### Tab 3: Readiness Scores
- **Domain-by-Domain Breakdown**: One collapsible section per domain
  - Domain name (header, colored by overall domain score)
  - Readiness Score: X/100 (%)
  - Fit-to-Purpose Score: X/100 (%)
  - Module-Level Detail (collapsible):
    - Table with rows: Module Name | Readiness | Fit-to-Purpose | Status (Complete/Incomplete)
    - Color-coded by score
  - Key findings summary (2–3 bullet points per domain)

### Tab 4: Fit-to-Purpose Analysis
- **Fit Assessment by Domain**: Parallel structure to Readiness Scores tab
- **Fit-to-Purpose Criteria**: Explanation of what "fit" means in this context
- **Assessor Type**: Shows the selected assessor profile (e.g., "Venture Capital — Seed/Series A Focus")
- **Fit Commentary**: Domain-specific narrative on how well the startup fits this assessor's focus areas
- **Misalignment Notes**: Any domains where the startup is weak relative to assessor expectations

### Tab 5: Gap Register
- **Gap Summary**: "X gaps identified across Y domains"
- **Filterable Gap Table**:
  - Columns: Domain | Gap Description | Severity (Critical/High/Medium/Low) | Gap Type | Status
  - Rows sorted by severity (Critical first)
  - Color-coded severity badges
  - Clickable rows to expand into full gap details (description, impact, suggested remediation)
- **Gap Distribution Chart**: Bar chart showing count by severity level
- **Export**: Button to download gap register as JSON or CSV

### Tab 6: Research Provenance
- **Source Log**: Chronological or alphabetical list of all sources cited
  - Each source entry: Source ID | Source Type (Interview/Document/Public/Inference) | Confidence Level (High/Medium/Low) | Date Accessed | Citation Text
- **Confidence Distribution**: Visual showing percentage of findings backed by High/Medium/Low confidence sources
- **Research Methodology**: Brief explanation of how sources were weighted and validated
- **Incomplete Research Notes**: Any areas where additional research is needed

### Tab 7: QA/QC Log
- **QA/QC Entry Table**: Columns: Check ID | Category (Scoring/Data Quality/Logic) | Status (Passed/Failed/Waived) | Finding | Resolution | Assessed By | Date
- **Summary**: Count of passed/failed/waived checks
- **Critical Findings**: Any QA issues that materially impact the assessment

### Tab 8: Appendix
- **Session Audit Trail**: Chronological log of all actions taken during the assessment
  - Timestamp | Action | Actor | Details
- **Framework Construction Log**: How the framework was built, any adjustments made
- **Assessor Corrections**: Any manual overrides or corrections applied to automated scoring
- **Data Provenance**: Where input data came from, any transformations applied
- **Version History**: Any previous versions of this assessment (if applicable)

---

## Assessment HTML Tab Structure

The HTML report for the full Assessment phase includes these 6 tabs:

### Tab 1: Executive Dashboard (Updated)
- Identical structure to Pre-Assessment
- Updated determination badge with final determination (GO/CONDITIONAL GO/CONDITIONAL HOLD/NO-GO)
- Updated metrics reflecting full assessment scores
- Updated domain heatmap with final scores across all 10 domains

### Tab 2: Domain Findings (Deep Findings)
- One collapsible section per domain (10 total)
- Domain name (header with color by final score)
- **Overall Scores**: Readiness % | Fit-to-Purpose % | Determination (GO/CONDITIONAL GO/HOLD/NO-GO)
- **Module Findings**: Expandable list of all modules within domain with detailed findings
  - Module name | Score | Narrative findings (1–3 paragraphs of analysis)
  - Key evidence supporting score
  - Sources cited (with confidence levels)
- **Domain Summary**: 2–3 key takeaways for this domain
- **Domain Risks**: Any material risks or gaps within this domain
- **Domain Strengths**: Any particular strengths identified

### Tab 3: Cross-Domain Analysis
- **Compounding Risks**: Narrative discussion of how weaknesses in one domain compound risks in others
  - Example: "Technology risk (gap in core IP) is amplified by Competitive Positioning risk (three competitors have stronger IP portfolios)"
- **Reinforcing Strengths**: How strengths in one domain reinforce confidence in others
  - Example: "Strong leadership team (Leadership domain) provides confidence that Technology gaps can be addressed"
- **Interdependencies**: Visual or narrative map of how domains interact
- **Portfolio Fit**: For multi-domain assessments, how the startup fits across all relevant dimensions

### Tab 4: Final Determination (Reconciled)
- **Determination Badge**: Large, prominent, final determination
- **Determination Logic**: Narrative explaining the determination rationale
  - What drove the determination
  - Trade-offs considered
  - Conditions (if CONDITIONAL GO/HOLD)
  - Paths to remediation (if applicable)
- **Sensitivity**: Brief note on robustness (e.g., "Determination stable ±10% variation in scoring")
- **Next Steps**: Recommended actions based on determination

### Tab 5: QA/QC Log
- Complete QA/QC checklist from assessment phase
- Any material findings or deviations from standard procedure

### Tab 6: Appendix
- Full audit trail from assessment phase
- All assessor corrections and overrides
- Data transformations
- Version history

---

## Sensitivity HTML Tab Structure

The HTML report for the Sensitivity Analysis phase includes these 4 tabs:

### Tab 1: Sensitivity Summary
- **Methodology**: Which sensitivity analysis techniques were applied (e.g., Scenario Analysis, Boundary Analysis, Monte Carlo Simulation)
- **Robustness Classification**: Determination classified as "Highly Robust", "Robust", "Moderately Robust", or "Sensitive"
- **Key Drivers**: Which variables/domains have the most impact on determination
- **Executive Summary**: 1–2 paragraph summary of sensitivity findings

### Tab 2: Analysis Results
- **Scenario Analysis Results** (if conducted):
  - Table: Scenario Name | Readiness Score | Fit Score | Determination | Key Changes
  - Scenarios might include "Optimistic", "Base Case", "Conservative", "Downside"
- **Boundary Analysis Results** (if conducted):
  - Critical thresholds identified
  - What parameter values would flip determination
  - Table: Variable | Base Value | Lower Bound | Upper Bound | Impact
- **Monte Carlo Results** (if conducted):
  - Distribution of outcomes
  - Histogram/chart of 1000+ simulated assessments
  - Confidence intervals for each score

### Tab 3: Flip-Point Analysis
- **Determination Flip Points**: What would need to change for determination to flip (e.g., "If Technology score drops 12%, determination shifts to CONDITIONAL HOLD")
- **Score Sensitivities**: Sensitivity matrix showing impact of ±5%, ±10%, ±15% changes in each domain
- **Most Sensitive Domains**: Ranked list of domains with highest impact on final determination
- **Trade-off Analysis**: Which domain improvements would offset which domain weaknesses

### Tab 4: Appendix
- Methodology details
- Assumptions
- Data used for sensitivity analysis
- Any caveats or limitations

---

## Recommendations HTML Tab Structure

The HTML report for the Recommendations phase includes these 4 tabs:

### Tab 1: Recommendations Summary
- **Available Paths**: List of recommendation paths available based on determination
  - If GO: "Proceed with standard due diligence"
  - If CONDITIONAL GO: "Path A: Proceed with conditions | Path B: Improvement roadmap before close"
  - If CONDITIONAL HOLD: "Path A: Gap remediation roadmap | Path B: Deal term adjustments"
  - If NO-GO: "Path A: Strategic improvements | Path B: Alternative structures" (if applicable)
- **Recommendation Overview**: High-level summary of what's recommended and why

### Tab 2: Path A — Improvement Roadmap (if applicable)
- **Roadmap Title**: e.g., "6-Month Technology Roadmap" or "18-Month Competitive Positioning Improvement"
- **Phase-by-Phase Breakdown**:
  - Phase 1 (Months 0–3): Specific actions to address gaps
    - Action item | Owner | Success Criteria | Resource Requirements
  - Phase 2 (Months 3–6): Continued progress
  - Phase 3 (Months 6+): Final milestones
- **Success Metrics**: How to measure progress
- **Risk Mitigation**: Actions to reduce risk during remediation period
- **Checkpoints**: Recommended review points (e.g., "Reassess Technology domain at Month 3")

### Tab 3: Path B — Deal Terms (if applicable)
- **Deal Structure Recommendations**: Suggested term sheet adjustments or protective provisions
  - Term | Rationale | Impact on Risk | Implementation Notes
- **Examples might include**:
  - Earn-out structures to protect against execution risk
  - Board seats or observer rights for governance
  - Escrows or clawback provisions
  - Staged funding tied to milestones
  - IP holdback clauses
  - Revenue-based protections
- **Alternative Structures**: If standard equity is not recommended, alternative structures (revenue share, debt, hybrid) with pros/cons

### Tab 4: Appendix
- Recommendation methodology
- Benchmark data (if applicable)
- Industry standards referenced
- Detailed roadmap templates (if provided)

---

## PDF Formatting Standards

### Three Report Format Types

PDF reports are generated in one of three formats based on assessor type:

#### 1. Investment Memorandum Format (for VC / PE / Angel Investors)

**Sections:**
1. Cover Page (Company name, date, assessor/fund name, confidentiality notice)
2. Executive Summary (1 page: determination, investment highlights, key metrics, recommendation)
3. Investment Thesis (1–2 pages: why this investment, market opportunity, team, differentiation)
4. Market Analysis (1–2 pages: TAM, market trends, competitive landscape)
5. Technology & Product (1–2 pages: technology risk assessment, product-market fit, IP status)
6. Financial Analysis (2–3 pages: unit economics, cash flow projections, funding needs, financial risk)
7. Team & Management (1 page: leadership assessment, skill gaps, bench strength)
8. Commercial Strategy (1–2 pages: GTM, customer acquisition, partnerships)
9. Risk Assessment (1–2 pages: key risks by domain, severity, mitigation strategies)
10. Valuation Considerations (1 page: comparable company analysis, suggested valuation range)
11. Investment Recommendation (1 page: determination, conditions if applicable, next steps)
12. Appendices (domain scores, gap register excerpt, key assumptions, glossary)

**Tone:** Professional, forward-looking, focused on upside potential and risk management

#### 2. Credit Memorandum Format (for Debt / Credit Analysis)

**Sections:**
1. Cover Page (Borrower name, date, lender/analyst name, credit rating if assigned)
2. Executive Summary (1 page: credit decision, key credit strengths/weaknesses, facility requested, recommendation)
3. Borrower Overview (1 page: business description, industry position, management)
4. Financial Analysis (3–4 pages: historical financials, leverage ratios, debt service coverage, cash flow analysis)
5. Debt Service Capacity (1–2 pages: ability to repay, stress scenarios, covenant compliance)
6. Collateral Analysis (1 page: collateral offered, valuation, haircut assumptions)
7. Industry & Market Risk (1 page: industry cyclicality, competitive risks, market trends)
8. Management & Operational Risk (1 page: team assessment, operational controls, key person risk)
9. Legal & Covenant Structure (1 page: proposed loan structure, covenants, documentation)
10. Risk Assessment (1–2 pages: credit risks by domain, probability of default, recovery assumptions)
11. Credit Decision (1 page: determination, proposed terms, conditions, monitoring plan)
12. Appendices (financial schedules, ratio analysis, loan structure summary, glossary)

**Tone:** Conservative, focused on downside protection, debt repayment ability, and risk mitigation

#### 3. Strategic Assessment Format (for Corporate / Family Office / Sovereign Wealth Investors)

**Sections:**
1. Cover Page (Company name, date, analyst/firm name, assessment date)
2. Executive Summary (1–2 pages: strategic fit assessment, determination, key opportunities, strategic risks)
3. Strategic Context (1 page: investor strategic objectives, sector focus, investment criteria)
4. Company Overview (1–2 pages: business model, current performance, strategic position)
5. Market & Opportunity Assessment (1–2 pages: market size, growth, competitive dynamics, strategic positioning)
6. Strategic Fit Analysis (1–2 pages: fit with investor's portfolio, synergies, integration opportunities)
7. Technology & Capabilities (1 page: technology assessment, capability gaps, technology integration opportunities)
8. Organizational & Talent (1 page: team assessment, cultural fit, retention considerations)
9. Financial Projections & Value Creation (2 pages: base case projections, value drivers, 5-year upside scenario)
10. Strategic Risks & Mitigation (1–2 pages: integration risks, execution risks, market risks, mitigation strategies)
11. Strategic Recommendation (1 page: determination, strategic rationale, suggested approach, next steps)
12. Appendices (detailed scoring, strategic roadmap outline, comparable transaction analysis, glossary)

**Tone:** Balanced, focused on strategic fit, synergies, and long-term value creation

### Common PDF Elements (All Formats)

- **Cover Page Design**: Professional letterhead, company name, assessment date, confidentiality footer
- **Headers/Footers**: Page numbers, date, company name, assessor/fund name, "CONFIDENTIAL - For Internal Use Only"
- **Typography**:
  - Heading 1 (Section titles): 18pt, bold, color accent (determination color)
  - Heading 2 (Subsections): 14pt, bold, dark gray
  - Body: 11pt, line spacing 1.5, dark gray/charcoal
  - Monospace: 9pt for tables and data
- **Tables**:
  - Gray header row (background #f3f4f6)
  - Alternating white/light-gray row backgrounds for readability
  - Borders: thin, light gray
- **Color Scheme**: White background, dark text, accent color for headers/highlights based on determination
- **Page Breaks**: Logical breaks before major sections, orphan/widow control
- **Appendix Formatting**: Smaller font for reference material, clear section labeling

---

## Data Export Specifications

### Scored Register JSON

The Scored Register contains all domain and module scores from both Readiness and Fit-to-Purpose tracks.

**Structure:**
```json
{
  "metadata": {
    "company_name": "TechVenture Inc.",
    "assessment_date": "2026-03-08",
    "assessment_phase": "assessment",
    "assessor_name": "Jane Analyst",
    "assessor_type": "venture-capital",
    "framework_version": "2.0"
  },
  "overall_scores": {
    "readiness_score": 76.5,
    "fit_to_purpose_score": 72.3,
    "determination": "CONDITIONAL_GO"
  },
  "domain_scores": [
    {
      "domain_id": "market",
      "domain_name": "Market & TAM",
      "readiness_score": 78.0,
      "fit_to_purpose_score": 74.0,
      "weight": 0.15,
      "status": "complete",
      "modules": [
        {
          "module_id": "tam_size",
          "module_name": "TAM Sizing",
          "readiness_score": 82.0,
          "fit_to_purpose_score": 80.0,
          "criticality": "critical",
          "status": "complete"
        }
      ]
    }
  ],
  "critical_gaps": [
    {
      "gap_id": "gap_001",
      "domain_id": "technology",
      "gap_description": "Core IP protection strategy underdeveloped",
      "severity": "critical",
      "gap_type": "risk",
      "status": "identified"
    }
  ]
}
```

**Delivery:** Offered as JSON download alongside HTML report

### Research Provenance JSON

The Research Provenance Register contains all sources cited and their confidence levels.

**Structure:**
```json
{
  "metadata": {
    "company_name": "TechVenture Inc.",
    "assessment_date": "2026-03-08",
    "total_sources": 42
  },
  "sources": [
    {
      "source_id": "src_001",
      "source_type": "founder_interview",
      "source_name": "Interview with CEO, TechVenture Inc.",
      "date_accessed": "2026-03-05",
      "confidence_level": "high",
      "topics": ["market_size", "team_experience"],
      "summary": "CEO confirmed TAM estimates and detailed founding team backgrounds"
    },
    {
      "source_id": "src_002",
      "source_type": "public_document",
      "source_name": "Crunchbase profile: TechVenture Inc.",
      "url": "https://crunchbase.com/...",
      "date_accessed": "2026-03-06",
      "confidence_level": "medium",
      "topics": ["funding_history", "team_composition"],
      "summary": "Reviewed funding rounds and team information from public sources"
    }
  ],
  "confidence_distribution": {
    "high": 28,
    "medium": 12,
    "low": 2
  }
}
```

**Delivery:** Offered as JSON download alongside HTML report

---

## Chart and Visualization Patterns

### Domain Score Radar Chart

Uses Chart.js library via CDN. Displays all 10 domains with two overlaid datasets (Readiness + Fit-to-Purpose).

**Integration:** See `references/chart-patterns.md` for full working snippet

### Gap Severity Distribution Bar Chart

Horizontal bar chart showing count of gaps by severity level (Critical, High, Medium, Low).

**Integration:** See `references/chart-patterns.md` for full working snippet

### Score Comparison Bar Chart

Side-by-side bar chart comparing Readiness vs Fit-to-Purpose scores for each domain.

**Integration:** See `references/chart-patterns.md` for full working snippet

### Domain Score Heatmap Grid

CSS Grid-based heatmap (no Chart.js required) displaying 10 domain cells with color interpolation from red → amber → green.

**Integration:** See `references/chart-patterns.md` for full working snippet

### Score Color Interpolation

Function to convert 0–100 score to RGB color (red → amber → green gradient).

```javascript
function scoreToColor(score) {
  if (score < 50) {
    // Red to Amber: 0 → 50
    const ratio = score / 50;
    const r = 239;
    const g = Math.round(158 + (94 - 158) * ratio);
    const b = 68;
    return `rgb(${r}, ${g}, ${b})`;
  } else {
    // Amber to Green: 50 → 100
    const ratio = (score - 50) / 50;
    const r = Math.round(245 - (245 - 34) * ratio);
    const g = Math.round(158 + (85 - 158) * ratio);
    const b = Math.round(15 + (39 - 15) * ratio);
    return `rgb(${r}, ${g}, ${b})`;
  }
}
```

---

## Styling Standards

### Typography

- **Primary Font**: Inter (via Google Fonts CDN)
  - Body: 16px, line-height 1.5, weight 400
  - Headings: weight 600–700
  - Monospace (data/code): SF Mono, Monaco, or system monospace at 13px
- **Color**: Dark gray (#1f2937) for body text, darker (#0f172a) for headings

### Color Palette

| Element | Color | Hex |
|---------|-------|-----|
| Primary Text | Dark Gray | #1f2937 |
| Secondary Text | Medium Gray | #6b7280 |
| Tertiary Text | Light Gray | #9ca3af |
| Background | White | #ffffff |
| Surface (Cards) | Light Gray | #f9fafb |
| Border | Border Gray | #e5e7eb |
| Accent (GO) | Green | #22c55e |
| Accent (CONDITIONAL GO) | Blue | #3b82f6 |
| Accent (CONDITIONAL HOLD) | Amber | #f59e0b |
| Accent (NO-GO) | Red | #ef4444 |

### Table Formatting Standards

- Header row: background #f3f4f6, bold text, padding 12px
- Data rows: alternating white / #f9fafb backgrounds
- Cell padding: 12px (horizontal), 10px (vertical)
- Borders: 1px solid #e5e7eb
- Font: 14px, monospace for numeric data
- Right-align numeric columns, left-align text

### Badge and Pill Component Standards

- **Determination Badge** (large):
  - 100+ pixels diameter/height
  - Centered text, 32px+ font
  - Icon + text side-by-side
  - Colored border + background

- **Status Badge** (small):
  - 40–60px height
  - Inline padding, 12px text
  - Colored background, white text
  - Rounded corners (20px border-radius)

- **Tag/Pill**:
  - Inline display
  - Small font (12px), gray background, dark text
  - Rounded corners (16px border-radius)
  - Padding 4px 8px

### Score Display Formats

- **Percentage**: "78%" (always with percent sign)
- **Fraction**: "78/100" (only if raw score requested)
- **Colored Bar**:
  - Full width bar, height 8–12px
  - Background #e5e7eb (light gray)
  - Foreground color by scoreToColor() function
  - Label overlay (percentage or score) in center, white text
- **Ring/Circle**:
  - SVG circle, stroke-based
  - Circumference represents 0–100
  - Colored stroke by scoreToColor()
  - Center text with percentage

---

## Inline HTML Template Pattern

Agents must generate HTML reports as complete, valid HTML5 documents with all CSS and JavaScript inline. No external file dependencies are permitted (CDN links for Chart.js and Google Fonts are acceptable).

### Template Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{COMPANY_NAME}} - {{PHASE_NAME}} Report</title>
  <!-- CDN Links -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>

  <!-- Inline CSS -->
  <style>
    /* All styling here - no external stylesheets */
  </style>
</head>
<body>
  <!-- Tab Navigation -->
  <nav class="tab-nav">
    <!-- Tabs here -->
  </nav>

  <!-- Tab Content Panels -->
  <div class="tab-content">
    <!-- Panels here -->
  </div>

  <!-- Inline JavaScript -->
  <script>
    // All interactivity here
  </script>
</body>
</html>
```

### Variable Substitution Pattern

Use double-curly-brace syntax for template variables:
- `{{COMPANY_NAME}}` — Company name
- `{{PHASE_NAME}}` — Phase (Pre-Assessment / Assessment / Sensitivity / Recommendations)
- `{{ASSESSMENT_DATE}}` — Date (YYYY-MM-DD format)
- `{{ASSESSOR_NAME}}` — Assessor or analyst name
- `{{DETERMINATION}}` — Final determination (GO / CONDITIONAL_GO / CONDITIONAL_HOLD / NO_GO)
- `{{READINESS_SCORE}}` — Overall readiness % (e.g., 76.5)
- `{{FIT_SCORE}}` — Overall fit-to-purpose % (e.g., 72.3)
- `{{DOMAIN_SCORES}}` — JSON-formatted domain scores (for chart data)
- `{{GAP_DATA}}` — JSON-formatted gap list (for table population)
- `{{STRENGTHS_LIST}}` — HTML bullet list of top 3 strengths
- `{{RISKS_LIST}}` — HTML bullet list of top 3 risks

### No External Dependencies

All CSS must be inline. All JavaScript must be inline. The only external resources allowed:
- Google Fonts CDN (for Inter typeface)
- Chart.js CDN (for charts)
- Trusted emoji or icon CDN (if icons are used)

The generated HTML file must be:
- Valid HTML5
- Openable in any modern browser without server-side rendering
- Printable to PDF without loss of information
- Fully functional when emailed or transferred (no broken links)

---

## References Index

Detailed implementation patterns and code snippets are available in supporting reference files:

- **`references/chart-patterns.md`** — Chart.js implementations (radar, bar, heatmap), color interpolation, responsive sizing
- **`references/component-library.md`** — Reusable HTML/CSS components (badges, cards, tables, tabs, alerts, etc.)
- **`templates/base.html`** — Complete working HTML template skeleton ready for variable substitution

For specific implementation guidance, consult the appropriate reference file based on your task.

---

## Quick Start for Agents

When tasked with generating a report:

1. **Determine the phase**: Pre-Assessment, Assessment, Sensitivity, or Recommendations
2. **Select the appropriate tab structure** from this skill file
3. **Use `templates/base.html`** as the starting point
4. **Populate tabs** using components from `references/component-library.md`
5. **Add charts** using patterns from `references/chart-patterns.md`
6. **Substitute template variables** with actual assessment data
7. **Validate HTML**: Open in browser to verify rendering and interactivity
8. **Generate PDF**: Use browser "Print to PDF" for archival format
9. **Export data**: Serialize Scored Register and Research Provenance as JSON
10. **Deliver all 4 outputs** (HTML, PDF, Scores JSON, Provenance JSON)

---

**Last Updated:** 2026-03-08
**Skill Version:** 0.1.0
**Status:** Ready for production use
