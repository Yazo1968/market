# Scope Review Artifact: Assessment Scope Review

## Data Source

- `$WORKSPACE/assessment/assessment/data/assessment-scope-plan.json`
- `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json` (for pre-assess scores display)
- `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json` (for pre-assess scores display)

## Artifact Structure

### Header

```
[Company Name]                              [Domains to Assess: N]
Assessment · Scope Review            [Estimated Duration: ~Xh]
```

**Wave Summary Bar:**
```
Wave 1 (N domains, parallel) ──▶ Wave 2 (N domains) ──▶ Wave 3 (N domains)
```

Rendered as a horizontal step indicator with colored nodes.

### Main Content

**Scope Table** (primary view):

| Column | Content | Editable? | Control | Constraint |
|--------|---------|-----------|---------|------------|
| Domain | Name + ID badge | No | Display | — |
| Pre-Assess Readiness | Score % with ScoreBar | No | Display | — |
| Pre-Assess Fit | Score % with ScoreBar | No | Display | — |
| Assigned Mode | Large badge | **Yes (escalate only)** | Dropdown | Gap-Focused → Verification → Deep-Independent |
| Wave | Number badge | No | Display (auto from dependencies) | — |
| Escalation Rationale | Text input | **Yes (required if escalated)** | Text input | Appears only when mode is escalated |

**Mode Badges:**
- Gap-Focused: blue badge (`bg-blue-500/20 text-blue-400`)
- Verification: amber badge (`bg-amber-500/20 text-amber-400`)
- Deep-Independent: red badge (`bg-red-500/20 text-red-400`)

**Mode Escalation Dropdown Logic:**
```jsx
const getModeOptions = (current) => {
  const modes = ['gap-focused', 'verification', 'deep-independent'];
  const idx = modes.indexOf(current);
  return modes.slice(idx); // current and above only
};
```

When the user escalates a mode:
1. The dropdown updates to the new mode
2. A text input field appears below the row: "Escalation rationale (required):"
3. The rationale is required — the change is not recorded until rationale is entered

### Sidebar (right, 30%)

**Wave Timeline Visualization:**

Vertical swim-lane diagram showing:

```
WAVE 1          WAVE 2          WAVE 3
┌──────────┐    ┌──────────┐    ┌──────────┐
│ Domain 1 │───▶│ Domain 2 │───▶│ Domain 8 │
│ Domain 6 │    │ Domain 3 │    │          │
│          │    │ Domain 7 │    │          │
└──────────┘    └──────────┘    └──────────┘
   parallel        parallel        parallel
```

Each domain node colored by its assigned mode (blue/amber/red).

**Mode Distribution Chart:**
- Recharts PieChart showing count of domains in each mode
- Updates live as user escalates modes

**Pre-Assessment Context Card** (collapsible):
- Company name, funding stage, vertical
- Pre-assessment determination badge
- Quick reference for the assessor

## Changes Delta Format

```json
[
  {
    "field": "domain_3.mode",
    "original": "gap-focused",
    "to": "verification",
    "context": "scope-plan",
    "rationale": "Financial projections showed significant inconsistencies that need independent verification"
  },
  {
    "field": "domain_7.mode",
    "original": "verification",
    "to": "deep-independent",
    "context": "scope-plan",
    "rationale": "Revenue claims in submission appear materially overstated based on market research"
  }
]
```

Note: The `rationale` field is included in the delta for mode escalations (required).
