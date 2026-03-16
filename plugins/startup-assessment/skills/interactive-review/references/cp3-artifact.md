# CP3 Artifact: Scored Findings Review

## Data Sources

- `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json`
- `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json`
- `$WORKSPACE/assessment/pre-assessment/data/gap-register.json`
- `$WORKSPACE/assessment/pre-assessment/data/dependency-map.json`
- `$WORKSPACE/assessment/pre-assessment/data/go-nogo-determination.json`

## Artifact Structure

### Header — Executive Summary Bar

```
[Company Name]                              [DETERMINATION BADGE — large, color-coded]
Pre-Assessment · Confirmation Point 3

[Readiness: NN%]  [Fit-to-Purpose: NN%]  [Gate 1: ✓/✗] [Gate 2: ✓/✗] [Gate 3: ✓/✗]
```

- Readiness and Fit-to-Purpose shown as circular progress gauges (Recharts PieChart donut style)
- Gate status: green check or red X for each of the 3 gates from go-nogo-determination
- If any gate failed: amber tooltip explaining what triggered

### Tabs

**Tab 1: Domain Scores**

**Dual-series Radar Chart** (top):
- Recharts RadarChart with two series: Readiness (blue) and Fit-to-Purpose (purple)
- All active domains as axes
- Hover shows exact values

**Domain Score Table** (below radar):

| Domain | Readiness | Fit-to-Purpose | Key Strengths | Key Gaps | Flag |
|--------|-----------|----------------|---------------|----------|------|
| Market & Opportunity | ScoreBar (72%) | ScoreBar (68%) | Bullet text | Bullet text | Checkbox |

- ScoreBar component for visual bars
- Key strengths/gaps: truncated with "show more" tooltip
- **Flag checkbox**: assessor can flag any domain for reconsideration (this is the only editable element for scores)

**Module Drill-Down** (expandable per domain):
- Click a domain row to expand and see module-level scores
- Module table:

| Module ID | Module Name | Completeness (0-3) | Quality (0-2) | Readiness | Stage Fit | Assessor Fit | Ask Coherence | Combined Fit | Flag |
|-----------|-------------|--------------------:|---------------:|----------:|----------:|-------------:|---------------:|-------------:|------|

- Scores shown as numeric values with color-coded backgrounds
- Flag checkbox per module

**Tab 2: Gap Register**

**Filter Bar** (top):
- Domain filter: dropdown (All / specific domain)
- Severity filter: multi-select (critical / significant / moderate / minor)
- Type filter: multi-select (absent-unresolvable / fragmentary / unverified / misaligned / conflicted / flagged)
- Track filter: dropdown (All / readiness / fit-to-purpose / both)

**Gap Table:**

| Gap ID | Domain | Module | Type | Severity | Track | Description | Remediation |
|--------|--------|--------|------|----------|-------|-------------|-------------|

- Type: color-coded badge
- Severity: SeverityBadge component
- Description + Remediation: truncated, click to expand full text in a slide-out panel

**Gap Summary Stats** (sidebar or top bar):
- Total gaps: N
- By severity: N critical, N significant, N moderate, N minor (colored chips)
- Domains with critical gaps: listed

**Tab 3: Dependency Map**

**Wave Flow Visualization:**

Render the sequencing plan as a horizontal flow:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    WAVE 1        │───▶│    WAVE 2        │───▶│    WAVE 3        │
│  (parallel)      │    │  (parallel)      │    │  (parallel)      │
│                  │    │                  │    │                  │
│  Domain 1        │    │  Domain 2        │    │  Domain 8        │
│  Domain 6        │    │  Domain 3        │    │                  │
│                  │    │  Domain 7        │    │                  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

- Each domain node is colored by its score band (green/amber/orange/red)
- Dependency arrows connect specific domains
- Hover on a domain shows its score summary

**Cross-Domain Dependencies Table:**

| Source Module | Target Module | Dependency Description |
|--------------|---------------|----------------------|

**Tab 4: Determination Detail**

- Full determination card:
  - Determination badge (large)
  - Rationale text (full paragraph)
  - Readiness track score: N%
  - Fit-to-Purpose track score: N%
  - Overall weighted score: N%
- Gate results detail:
  - Gate 1 (Hard Blockers): pass/fail + triggered blockers list (if any)
  - Gate 2 (Domain Floor): pass/fail + domains below floor (if any)
  - Gate 3 (Fit Threshold): pass/fail + domains below threshold (if any)
- Conditions (if CONDITIONAL GO or CONDITIONAL HOLD):
  - Condition table: ID, description, gap reference, responsible party, resolution timeline

**Assessor Notes** (textarea at bottom of this tab):
- Free-text area for assessor notes on the determination
- Placeholder: "Add any observations about the determination, flags, or additional context..."

## Editable Elements

**Scores are NOT editable.** The only interactive elements are:

| Element | Control | Effect |
|---------|---------|--------|
| Flag domain for reconsideration | Checkbox per domain row | Recorded in delta |
| Flag module for reconsideration | Checkbox per module row | Recorded in delta |
| Assessor note per domain | Expandable textarea (appears when domain row is expanded) | Recorded in delta |
| Assessor note on determination | Textarea at bottom of Tab 4 | Recorded in delta |

## Changes Delta Format

```json
[
  { "field": "flag_domain_3", "original": false, "to": true, "context": "domain-flag" },
  { "field": "flag_M3.2", "original": false, "to": true, "context": "module-flag" },
  { "field": "note_domain_1", "original": "", "to": "Market sizing methodology seems optimistic given...", "context": "assessor-note" },
  { "field": "note_determination", "original": "", "to": "Agree with conditional assessment but...", "context": "assessor-note" }
]
```
