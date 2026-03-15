# CP5 Artifact: Reconciled Findings Review

## Data Sources

- `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
- `$WORKSPACE/assessment/assessment/data/domain-findings-*.json` (all domain files)
- `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`

## Artifact Structure

### Header — Final Determination Bar

```
[Company Name]                                          [FINAL DETERMINATION BADGE]
Assessment · Confirmation Point 5

Pre-Assessment: [BADGE] ──▶ Assessment: [BADGE]     [Overall Score: NN%]
```

- Side-by-side comparison of pre-assessment vs assessment determination
- Arrow between them showing upgrade/downgrade/no-change (with color: green arrow up, red arrow down, grey arrow right)
- If determination changed: brief explanation text below

### Tabs

**Tab 1: Cross-Domain Conflicts**

Render each item from `integrated-findings-register.json.reconciled_findings[]` as a conflict card:

**Conflict Card Layout:**
```
┌────────────────────────────────────────────────────────────────────┐
│ CONF-001                                    [evidence-weight] badge│
│                                                                    │
│ Domains: [Domain 2 badge] [Domain 7 badge]                        │
│                                                                    │
│ Domain A position:                                                 │
│ "Product shows strong technical differentiation and IP..."         │
│                                                                    │
│ Domain B position:                                                 │
│ "Financial projections don't reflect the R&D investment needed..." │
│                                                                    │
│ ── Reconciled Position ──────────────────────────────────────────  │
│ "Technical strength is real but revenue timeline must account..."  │
│                                                                    │
│ [Override Note: ________________________] (textarea, expandable)   │
└────────────────────────────────────────────────────────────────────┘
```

- Reconciliation method badge: `evidence-weight` (blue), `assessor-judgment` (amber), `unresolved-with-flag` (red)
- Override note textarea: collapsed by default, expand on click

**Tab 2: Compounding Risks**

Render `compounding_risks[]` as risk cards ordered by severity:

**Risk Card Layout:**
```
┌────────────────────────────────────────────────────────────────────┐
│ RISK-001                                      [critical] severity  │
│                                                                    │
│ Domains: [Domain 6 badge] [Domain 7 badge] [Domain 8 badge]       │
│                                                                    │
│ Execution risk compounds with founder concentration and cash       │
│ burn acceleration. If the sole technical founder leaves...         │
│                                                                    │
│ Compounding effect:                                                │
│ "Combined probability of adverse outcome estimated at..."          │
│                                                                    │
│ [Flag] checkbox                                                    │
└────────────────────────────────────────────────────────────────────┘
```

- Red-tinted background for critical, orange for significant, amber for moderate
- Flag checkbox per risk

**Tab 3: Reinforcing Strengths**

Render `reinforcing_strengths[]` as strength cards:

**Strength Card Layout:**
```
┌────────────────────────────────────────────────────────────────────┐
│ STR-001                                                            │
│                                                                    │
│ Domains: [Domain 1 badge] [Domain 4 badge] [Domain 5 badge]       │
│                                                                    │
│ Strong product-market fit signals reinforced by growing traction   │
│ and effective go-to-market execution...                            │
│                                                                    │
│ Reinforcement effect:                                              │
│ "Cross-domain validation increases confidence in..."               │
└────────────────────────────────────────────────────────────────────┘
```

- Green-tinted background (`bg-green-500/5 border-green-500/20`)

**Tab 4: Domain-by-Domain Summary**

Compact table with one row per domain:

| Domain | Readiness | Fit | Mode | Key Finding | Key Risk | QA/QC |
|--------|-----------|-----|------|-------------|----------|-------|
| Name | ScoreBar | ScoreBar | Badge | Truncated text | Truncated text | Badge |

- Mode: assessment mode badge (gap-focused/verification/deep-independent)
- QA/QC: badge (passed = green, passed-with-flag = amber)
- Click a domain row to expand and see full module findings from `domain-findings-{id}.json`

**Expanded Domain Detail:**
- Module findings table:

| Module | Classification | Finding Summary | Confidence | Risks | Strengths |
|--------|---------------|-----------------|------------|-------|-----------|

- Classification badge: confirmed (green), partially-confirmed (amber), contradicted (red), gap-remains (red), gap-resolved (green)
- Risks and strengths as bullet lists

**Tab 5: Final Determination**

- Full determination card (same as CP3 Tab 4 but with assessment-phase data):
  - Large determination badge
  - Full rationale paragraph
  - Score breakdown (readiness, fit, overall)
  - Conditions (if conditional)
  - Comparison with pre-assessment determination

**Assessor General Notes** (bottom section, outside tabs):
- Large textarea: "Final notes, overrides, or observations for the audit trail..."
- Placeholder text: "These notes will be recorded in the session audit trail and included in the final report appendix."

## Editable Elements

**Scores are NOT editable.** Available interactions:

| Element | Control | Effect |
|---------|---------|--------|
| Override note per conflict | Textarea in conflict card | Recorded in delta |
| Flag per compounding risk | Checkbox | Recorded in delta |
| General assessor notes | Textarea at bottom | Recorded in delta |

## Changes Delta Format

```json
[
  {
    "field": "conflict_CONF-001.override_note",
    "original": "",
    "to": "I disagree with the reconciled position. The technical differentiation is not sufficient to...",
    "context": "reconciliation-override"
  },
  {
    "field": "risk_RISK-002.flagged",
    "original": false,
    "to": true,
    "context": "risk-flag"
  },
  {
    "field": "general_notes",
    "original": "",
    "to": "Overall assessment is sound but I want to note that the regulatory landscape...",
    "context": "assessor-note"
  }
]
```
