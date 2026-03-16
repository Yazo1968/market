# Plan: Interactive CP Review Artifacts for startup-assessment Plugin

## Goal

Replace the current CP review flow (save .md file → user opens externally → edits → re-uploads) with **inline interactive React artifacts** rendered directly in the Cowork conversation. Each artifact is dynamically generated from the actual pipeline data at that stage.

---

## Architecture

### Data Flow

```
Pipeline Stage Output (JSON)
  → Claude generates React artifact (embedded data)
  → User interacts (sliders, toggles, dropdowns, notes)
  → Collapsed footer shows: "N changes made" · [Copy to Clipboard]
  → User clicks Copy, pastes delta JSON into chat
  → AskUserQuestion: "Confirm" or "Continue editing"
  → Claude validates delta, applies to workspace JSON, proceeds
```

### Technology Stack (available in Cowork artifact sandbox)

- **React 18** with hooks (useState, useCallback, useMemo)
- **Tailwind CSS** for styling
- **Shadcn UI** components (Accordion, Badge, Button, Card, Slider, Switch, Select, Tabs, Tooltip, Table)
- **Recharts** for charts (RadarChart, BarChart, PieChart)
- **Lucide React** for icons

### Shared Design System

All CP artifacts share a consistent visual language:

**Color palette:**
- GO: `#10B981` (emerald-500)
- CONDITIONAL GO: `#F59E0B` (amber-500)
- CONDITIONAL HOLD: `#F97316` (orange-500)
- NO-GO: `#EF4444` (red-500)
- Confidence High: `#3B82F6` (blue-500)
- Confidence Low: `#94A3B8` (slate-400)
- Background: `#0F172A` (slate-900) — dark professional theme
- Surface: `#1E293B` (slate-800)
- Text: `#F8FAFC` (slate-50)

**Layout pattern:**
- Header: Company name, phase badge, CP number
- Main content: Tab-based or section-based review panels
- Footer (sticky): Changes counter (collapsed) + Copy to Clipboard button
- All interactive elements have subtle hover states and transitions

**Changes tracking:**
- Every artifact maintains a `changes` state object
- On any user modification, the delta is recorded: `{ field, from, to }`
- Footer shows count: "3 changes made"
- Collapsed by default — expandable accordion shows full delta list
- "Copy to Clipboard" serializes to compact JSON and copies without requiring expand

---

## CP-by-CP Artifact Specifications

### Context Review: Context & Assessor Profile Review

**Data sources:** `context-profile.json` + `assessor-profile.json`

**Layout — Two-panel tabbed view:**

**Tab 1: Company Context**
| Section | UI Component | Editable? | Control Type |
|---------|-------------|-----------|--------------|
| Company name | Text display | Yes | Inline text edit |
| Funding stage | Badge | Yes | Dropdown (enum values from schema) |
| Vertical / Sub-vertical | Badge pair | Yes | Dropdown + text input |
| Commercial model | Badge | Yes | Dropdown |
| Revenue architecture | Card with primary + secondary list | Yes | Dropdown (primary) + tag input (secondary) + toggle (recurring) |
| Geography | Card with primary + secondary | Yes | Text input + tag list |
| Ask | Card (amount, currency, instrument, use of proceeds) | Yes | Text + dropdown + textarea |
| Regulatory exposure | Toggle + framework tags | Yes | Switch + tag input |
| Traction status | Badge | Yes | Dropdown |
| Team structure | Mini-table (founders, size, tech cofounder) | Yes | Number inputs + toggle |

**Tab 2: Assessor Profile**
| Section | UI Component | Editable? | Control Type |
|---------|-------------|-----------|--------------|
| Assessor type | Large badge | Yes | Dropdown |
| Transaction type | Text | Yes | Text input |
| Primary priorities | Ranked list with weight modifiers | Yes | Drag-reorder + slider (0.5–2.0) |
| Non-negotiables | Tag list with severity | Yes | Add/remove tags |
| Firm-specific standards | Table (standard, applies_to, threshold) | Yes | Editable table rows |

**Tab 3: Confidence Flags**
| Section | UI Component | Editable? |
|---------|-------------|-----------|
| Extracted from submission | Green check list | No (display) |
| Inferred with uncertainty | Amber flag list | Yes — user can confirm or correct each |
| Missing from submission | Red gap list | No (display, informational) |

**Visual highlights:**
- Uncertainty flags shown as amber alert cards at top
- Inconsistencies flagged with red border + tooltip explanation
- Extraction basis shown as small badge on each field ("extracted" / "inferred" / "uncertain")

---

### Framework Review: Assessment Framework Review

**Data source:** `framework.json`

**Layout — Domain-centric dashboard:**

**Header section:**
- Overall stats bar: Active domains count, Total modules count, Readiness weight vs Fit weight split (mini bar chart)

**Main section — Domain cards (one per domain):**

Each domain is a collapsible card:

| Element | UI Component | Editable? | Control Type | Constraint |
|---------|-------------|-----------|--------------|------------|
| Domain name + ID | Header text | No | — | — |
| Active/Inactive | Toggle switch | No (mandatory stay active) | Display only for mandatory; switch for optional | Cannot deactivate mandatory domains |
| Domain weight | Slider (0–40%) | Yes | Range slider with live % display | Sum must = 100% (auto-redistribute) |
| Criticality | Badge | Yes (escalate only) | Dropdown: contextual → standard → critical → hard-blocker | Can only go UP, never down |
| Module list | Nested table | Partially | — | — |
| ↳ Module active | Checkbox | Yes (optional only) | Checkbox | Cannot deactivate mandatory modules |
| ↳ Module criticality | Badge | Yes (escalate only) | Dropdown: optional → important → mandatory | Can only go UP |
| ↳ Module weights | Mini slider | Yes | Range slider | Must sum to 1.0 within domain |

**Right sidebar:**
- Hard Blockers panel: locked list, non-editable, red border
- Framework construction log: collapsible, shows calibration notes
- Weight distribution radar chart (Recharts RadarChart) — updates live as weights change

**Validation rules (enforced in artifact):**
- Domain weights must sum to 100% — if user adjusts one, others auto-redistribute proportionally
- Module weights must sum to 1.0 within each domain
- Mandatory modules cannot be deactivated
- Criticality can only be escalated, never reduced
- Hard blockers are locked (displayed but not editable)

---

### Scores Review: Scored Findings Review

**Data sources:** `readiness-register.json` + `fit-to-purpose-register.json` + `gap-register.json` + `dependency-map.json` + `go-nogo-determination.json`

**Layout — Executive dashboard:**

**Header section:**
- Determination badge (large, color-coded: GO/CONDITIONAL GO/CONDITIONAL HOLD/NO-GO)
- Overall Readiness % (circular progress gauge)
- Overall Fit-to-Purpose % (circular progress gauge)
- Gate status indicators (3 gates: hard blocker ✓/✗, domain floor ✓/✗, fit threshold ✓/✗)

**Tab 1: Domain Scores**
- Radar chart: all domains plotted on readiness and fit axes (dual-series radar)
- Below radar: domain score table

| Column | Content |
|--------|---------|
| Domain | Name + ID |
| Readiness | Score bar (0-100) + percentage |
| Fit-to-Purpose | Score bar (0-100) + percentage |
| Key Strengths | Top 2 bullet points (truncated with tooltip) |
| Key Gaps | Top 2 bullet points with severity badge |

**Tab 2: Gap Register**
- Sortable, filterable table:

| Column | Content | Filter/Sort |
|--------|---------|-------------|
| Gap ID | GAP-001 etc | — |
| Domain | Name | Filter dropdown |
| Module | Name | — |
| Type | Badge (absent/fragmentary/unverified/misaligned/conflicted) | Filter dropdown |
| Severity | Color badge (critical/significant/moderate/minor) | Sort + filter |
| Track | readiness / fit / both | Filter |
| Description | Truncated + expand | — |
| Remediation | Truncated + expand | — |

**Tab 3: Dependency Map**
- Visual flow diagram showing domain sequencing (Wave 1 → Wave 2 → Wave 3)
- Rendered as a horizontal flow with colored nodes per domain
- Cross-domain dependencies shown as connecting lines

**Editable elements (limited at Scores Review):**
| Element | Control | Effect |
|---------|---------|--------|
| Flag for reconsideration | Checkbox per module score row | Records flag in delta (doesn't change score) |
| Assessor note per domain | Expandable text area | Carried forward in audit trail |
| Assessor note on determination | Textarea below determination badge | Carried forward |

**No score editing** — scores are locked at this point. User can only flag and annotate.

---

### Scope Review: Assessment Scope Review

**Data source:** `assessment-scope-plan.json` (generated by scope-determinator)

**Layout — Scope planning dashboard:**

**Header:**
- Total domains to assess, Estimated duration
- Wave summary: Wave 1 (N domains, parallel) → Wave 2 (N domains) → Wave 3 (N domains)

**Main section — Domain scope table:**

| Column | Content | Editable? | Control | Constraint |
|--------|---------|-----------|---------|------------|
| Domain | Name + ID | No | — | — |
| Pre-Assess Readiness | Score % | No | Display | — |
| Pre-Assess Fit | Score % | No | Display | — |
| Assigned Mode | Badge | Yes (escalate only) | Dropdown: Gap-Focused → Verification → Deep-Independent | Can only escalate |
| Wave | Number | No | Display (auto-calculated from dependencies) | — |
| Escalation Rationale | Text | Yes (if mode changed) | Text input (appears when mode is escalated) | Required if escalated |

**Visual elements:**
- Wave timeline visualization: horizontal swim lanes showing which domains run in parallel per wave
- Mode distribution pie chart: how many domains in each mode
- Color coding: Gap-Focused (blue), Verification (amber), Deep-Independent (red)

**Validation:**
- Modes can ONLY be escalated (gap-focused → verification → deep-independent)
- If user escalates a mode, a rationale text input appears (required)
- Wave assignments auto-update if dependencies change

---

### Findings Review: Reconciled Findings Review

**Data sources:** `integrated-findings-register.json` + `domain-findings-*.json` + `updated-go-nogo-determination.json`

**Layout — Final assessment dashboard:**

**Header section:**
- Final determination badge (large, color-coded)
- Pre-assessment vs Assessment determination comparison (side-by-side badges with arrow showing change/no-change)
- Overall assessment score

**Tab 1: Cross-Domain Conflicts**
- Conflict cards (one per conflict):

| Element | Content |
|---------|---------|
| Conflict ID | CONF-001 |
| Domains involved | Badge list |
| Domain A position | Quoted text |
| Domain B position | Quoted text |
| Reconciled position | Highlighted text |
| Method | Badge (evidence-weight / assessor-judgment / unresolved) |

**Tab 2: Compounding Risks (Top 5)**
- Risk cards ordered by severity:

| Element | Content |
|---------|---------|
| Risk ID | RISK-001 |
| Domains involved | Badge list |
| Description | Full text |
| Compounding effect | Highlighted text |
| Severity | Color badge |

**Tab 3: Reinforcing Strengths (Top 5)**
- Strength cards (green-tinted):

| Element | Content |
|---------|---------|
| Domains involved | Badge list |
| Description | Full text |
| Reinforcement effect | Highlighted text |

**Tab 4: Domain-by-Domain Summary**
- Compact domain table:

| Column | Content |
|--------|---------|
| Domain | Name |
| Readiness | Score bar |
| Fit | Score bar |
| Assessment Mode | Badge |
| Key Findings | Top bullet |
| Key Risk | Text |
| QA/QC Status | Badge (passed/passed-with-flag) |

**Editable elements (limited at Findings Review):**
| Element | Control | Effect |
|---------|---------|--------|
| Override note per conflict | Textarea | Recorded in audit trail |
| General assessor notes | Textarea at bottom | Recorded in audit trail |
| Flag items | Checkbox per risk/conflict | Records flag |

**Scores are locked.** User can only add notes, flags, and overrides to the audit trail.

---

### Sensitivity: Methodology Selection

**Data sources:** `updated-go-nogo-determination.json` + `integrated-findings-register.json`

**Layout — Methodology picker:**

**Header:**
- Current determination badge
- Overall score display

**Main — Methodology cards:**
- 2–3 large clickable cards (based on determination type)
- Each card shows:
  - Methodology name (bold)
  - Description (2-3 sentences)
  - What it tests
  - What you'll learn
  - Recommended badge (if applicable)
- Cards have radio-button selection behavior (click to select, visual highlight)

**No delta tracking needed** — this is a pure selection. The artifact outputs the selected methodology name.

---

## Implementation Approach

### What Changes

1. **New skill: `interactive-review/SKILL.md`**
   - Contains the shared design system specification (colors, components, layout patterns)
   - Contains React component templates and generation instructions for each CP
   - Referenced by output agents when generating CP artifacts

2. **Modified commands:**
   - `commands/pre-assess.md` — Context Review, Framework Review, Scores Review sections updated:
     - Remove "save review file" instructions
     - Replace with "generate interactive React artifact" instructions
     - Update AskUserQuestion flow: after artifact, ask "Paste your changes or confirm no changes"
     - Add delta parsing and validation logic
   - `commands/assess.md` — Scope Review, Findings Review sections updated (same pattern)
   - `commands/sensitivity.md` — Methodology selection updated to use card-based artifact

3. **Modified agents:**
   - Agents that produce CP outputs (`pre-assess-output-agent`, `assess-output-agent`) may need awareness of the new artifact format
   - QA/QC agent flow remains unchanged (operates on JSON data, not review format)

4. **Schemas — No changes needed**
   - The JSON schemas remain identical
   - The artifacts consume the same data; only the presentation layer changes
   - The delta JSON from user changes follows the existing `assessor_corrections` / `assessor_adjustments` patterns already in the schemas

### What Stays The Same

- All pipeline logic (agents, scoring, determination)
- All JSON schemas and data contracts
- All Python scripts
- Final HTML/PDF report generation (separate from CP review artifacts)
- The 5 CP checkpoint positions in the workflow
- The rules (can only escalate, can't remove mandatory, scores locked at Scores Review/Findings Review)

### Implementation Order

1. Create `skills/interactive-review/SKILL.md` with shared design system
2. Create `skills/interactive-review/references/` with CP-specific artifact generation instructions (one per CP)
3. Modify `commands/pre-assess.md` — update Context Review, Framework Review, Scores Review sections
4. Modify `commands/assess.md` — update Scope Review, Findings Review sections
5. Modify `commands/sensitivity.md` — update methodology selection
6. Test each CP artifact individually with sample data
