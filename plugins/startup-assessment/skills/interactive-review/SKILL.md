---
name: interactive-review
description: >
  This skill should be used when generating interactive Confirmation Point (CP) review artifacts
  for the assessor. Provides the shared design system, component library, and generation patterns
  for all CP artifacts across the assessment workflow. Trigger phrases: "generate CP review",
  "confirmation point", "interactive review", "CP1", "CP2", "CP3", "CP4", "CP5",
  "build review artifact", "render review dashboard".
version: 0.1.0
---

# Interactive Review Artifact System

## Overview

Every Confirmation Point (CP1–CP5) and the Sensitivity methodology selection renders an **inline interactive React artifact** directly in the Cowork conversation. The artifact is dynamically generated from the actual pipeline data at that stage — no static templates. The assessor reviews and adjusts within the artifact, then submits changes back to the workflow.

## Data Flow

```
Pipeline JSON output
  → Claude generates self-contained React artifact with data embedded
  → Assessor interacts (sliders, toggles, dropdowns, inline edits, notes)
  → Collapsed footer: "N changes made" · [Copy to Clipboard]
  → Assessor clicks Copy → pastes compact delta JSON into chat
  → Claude validates, applies delta to workspace JSON, continues pipeline
```

## Technology Stack

All artifacts use only libraries available in the Cowork artifact sandbox:

- **React 18** — useState, useCallback, useMemo, useRef
- **Tailwind CSS** — utility classes for all styling
- **Shadcn UI** — Accordion, Badge, Button, Card, Slider, Switch, Select, Tabs, Table, Tooltip, Dialog
- **Recharts** — RadarChart, BarChart, PieChart, ResponsiveContainer
- **Lucide React** — icons (Check, X, AlertTriangle, ChevronDown, Copy, Lock, Flag, Edit3, Info, ArrowRight)

**No external API calls. No localStorage. All state in React hooks.**

---

## Shared Design System

### Color Palette

```
Determination colors:
  GO:               #10B981 (emerald-500)
  CONDITIONAL GO:   #F59E0B (amber-500)
  CONDITIONAL HOLD: #F97316 (orange-500)
  NO-GO:            #EF4444 (red-500)

Confidence:
  High:   #3B82F6 (blue-500)
  Medium: #F59E0B (amber-500)
  Low:    #94A3B8 (slate-400)

Severity:
  Critical:    #EF4444 (red-500)
  Significant: #F97316 (orange-500)
  Moderate:    #F59E0B (amber-500)
  Minor:       #94A3B8 (slate-400)

Assessment modes:
  Gap-Focused:      #3B82F6 (blue-500)
  Verification:     #F59E0B (amber-500)
  Deep-Independent: #EF4444 (red-500)

Surfaces (dark professional theme):
  Background: #0F172A (slate-900)
  Surface:    #1E293B (slate-800)
  Elevated:   #334155 (slate-700)
  Border:     #475569 (slate-600)
  Text:       #F8FAFC (slate-50)
  Muted text: #94A3B8 (slate-400)
  Accent:     #6366F1 (indigo-500)
```

### Typography

- Font family: `Inter, system-ui, -apple-system, sans-serif` (available via Google Fonts CDN)
- Headings: font-weight 600–700, tracking-tight
- Body: font-weight 400, text-sm (14px) for data-dense layouts
- Monospace: `JetBrains Mono, monospace` for scores, IDs, and JSON

### Layout Pattern

Every CP artifact follows this structure:

```jsx
<div className="min-h-screen bg-slate-900 text-slate-50 p-6">
  {/* HEADER */}
  <header className="mb-8">
    <div className="flex items-center justify-between">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">{companyName}</h1>
        <p className="text-slate-400 text-sm">{phaseLabel} · {cpLabel}</p>
      </div>
      <DeterminationBadge value={determination} />  {/* if applicable */}
    </div>
  </header>

  {/* MAIN CONTENT — tab-based or section-based, varies per CP */}
  <main className="space-y-6">
    {/* CP-specific content */}
  </main>

  {/* STICKY FOOTER — changes tracker */}
  <footer className="fixed bottom-0 left-0 right-0 bg-slate-800 border-t border-slate-700 px-6 py-3">
    <ChangesFooter changes={changes} />
  </footer>
</div>
```

### Changes Footer Component

Present in every CP artifact. Collapsed by default.

```jsx
function ChangesFooter({ changes }) {
  const [expanded, setExpanded] = useState(false);
  const count = changes.length;

  const copyToClipboard = () => {
    const delta = JSON.stringify(changes, null, 2);
    navigator.clipboard.writeText(delta);
  };

  return (
    <div>
      <div className="flex items-center justify-between">
        <button
          onClick={() => setExpanded(!expanded)}
          className="text-sm text-slate-400 hover:text-slate-200 flex items-center gap-2"
        >
          {count === 0 ? (
            <span className="text-slate-500">No changes</span>
          ) : (
            <>
              <span className="text-indigo-400 font-medium">{count} change{count !== 1 ? 's' : ''} made</span>
              <ChevronDown className={`w-4 h-4 transition ${expanded ? 'rotate-180' : ''}`} />
            </>
          )}
        </button>
        <button
          onClick={copyToClipboard}
          className="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-sm font-medium transition"
        >
          <Copy className="w-4 h-4" />
          Copy to Clipboard
        </button>
      </div>
      {expanded && count > 0 && (
        <pre className="mt-3 p-3 bg-slate-900 rounded-lg text-xs text-slate-300 max-h-48 overflow-auto font-mono">
          {JSON.stringify(changes, null, 2)}
        </pre>
      )}
    </div>
  );
}
```

### Changes Tracking Pattern

Every artifact maintains changes state:

```jsx
const [changes, setChanges] = useState([]);

const recordChange = useCallback((field, from, to, context = '') => {
  setChanges(prev => {
    // Update existing change for this field, or add new
    const existing = prev.findIndex(c => c.field === field);
    if (existing >= 0) {
      // If reverted to original, remove the change
      if (JSON.stringify(to) === JSON.stringify(prev[existing].original)) {
        return prev.filter((_, i) => i !== existing);
      }
      const updated = [...prev];
      updated[existing] = { ...updated[existing], to };
      return updated;
    }
    return [...prev, { field, original: from, to, context }];
  });
}, []);
```

The delta JSON format:
```json
[
  { "field": "funding_stage", "original": "seed", "to": "series-a", "context": "context-profile" },
  { "field": "domain_3_weight", "original": 0.12, "to": 0.15, "context": "framework" },
  { "field": "M4.2_criticality", "original": "optional", "to": "important", "context": "framework" }
]
```

### Shared UI Components

**DeterminationBadge:**
```jsx
function DeterminationBadge({ value, size = 'lg' }) {
  const colors = {
    'GO': 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30',
    'CONDITIONAL-GO': 'bg-amber-500/20 text-amber-400 border-amber-500/30',
    'CONDITIONAL-HOLD': 'bg-orange-500/20 text-orange-400 border-orange-500/30',
    'NO-GO': 'bg-red-500/20 text-red-400 border-red-500/30',
  };
  const sizeClasses = size === 'lg' ? 'text-lg px-4 py-2' : 'text-xs px-2 py-1';
  return (
    <span className={`${colors[value]} ${sizeClasses} font-bold rounded-lg border`}>
      {value}
    </span>
  );
}
```

**ScoreBar:**
```jsx
function ScoreBar({ score, max = 100, label }) {
  const pct = (score / max) * 100;
  const color = pct >= 75 ? 'bg-emerald-500' : pct >= 55 ? 'bg-amber-500' : pct >= 35 ? 'bg-orange-500' : 'bg-red-500';
  return (
    <div className="flex items-center gap-3">
      {label && <span className="text-xs text-slate-400 w-16">{label}</span>}
      <div className="flex-1 h-2 bg-slate-700 rounded-full overflow-hidden">
        <div className={`h-full ${color} rounded-full transition-all`} style={{ width: `${pct}%` }} />
      </div>
      <span className="text-sm font-mono font-medium w-12 text-right">{Math.round(pct)}%</span>
    </div>
  );
}
```

**SeverityBadge:**
```jsx
function SeverityBadge({ severity }) {
  const colors = {
    critical: 'bg-red-500/20 text-red-400',
    significant: 'bg-orange-500/20 text-orange-400',
    moderate: 'bg-amber-500/20 text-amber-400',
    minor: 'bg-slate-500/20 text-slate-400',
  };
  return <span className={`${colors[severity]} text-xs px-2 py-0.5 rounded-full font-medium`}>{severity}</span>;
}
```

**LockedField** (for non-editable display):
```jsx
function LockedField({ label, value }) {
  return (
    <div className="flex items-center gap-2 text-sm">
      <Lock className="w-3 h-3 text-slate-500" />
      <span className="text-slate-400">{label}:</span>
      <span className="text-slate-200 font-medium">{value}</span>
    </div>
  );
}
```

**EditableField** (for inline editing with change tracking):
```jsx
function EditableField({ label, value, onChange, type = 'text', options = [] }) {
  if (type === 'select') {
    return (
      <div className="flex items-center gap-2 text-sm">
        <Edit3 className="w-3 h-3 text-indigo-400" />
        <span className="text-slate-400">{label}:</span>
        <select
          value={value}
          onChange={e => onChange(e.target.value)}
          className="bg-slate-700 border border-slate-600 rounded px-2 py-1 text-slate-200 text-sm"
        >
          {options.map(o => <option key={o} value={o}>{o}</option>)}
        </select>
      </div>
    );
  }
  return (
    <div className="flex items-center gap-2 text-sm">
      <Edit3 className="w-3 h-3 text-indigo-400" />
      <span className="text-slate-400">{label}:</span>
      <input
        type={type}
        value={value}
        onChange={e => onChange(e.target.value)}
        className="bg-slate-700 border border-slate-600 rounded px-2 py-1 text-slate-200 text-sm"
      />
    </div>
  );
}
```

---

## Constraint Enforcement

All business rules from the assessment workflow are enforced directly in the artifact UI:

| Rule | Enforcement |
|------|-------------|
| Mandatory domains cannot be deactivated | Toggle disabled + Lock icon |
| Mandatory modules cannot be deactivated | Checkbox disabled + Lock icon |
| Criticality can only escalate | Dropdown only shows current level and above |
| Domain weights must sum to 100% | Auto-redistribute on change |
| Module weights must sum to 1.0 per domain | Auto-redistribute on change |
| Hard blockers are non-editable | Display only with red lock icon |
| Scores locked at CP3/CP5 | No score edit controls; display only |
| Assessment modes escalate only (CP4) | Dropdown only shows current mode and above |

---

## Generation Instructions

When generating a CP artifact, follow this procedure:

1. **Read the relevant JSON files** from the workspace for this CP
2. **Embed the data directly** into the React component as a const at the top of the artifact
3. **Use the shared design system** — colors, typography, layout, components from this skill
4. **Load the CP-specific reference** from `references/cp{N}-artifact.md` for the detailed layout
5. **Include the ChangesFooter** in every artifact
6. **Include all shared components** (DeterminationBadge, ScoreBar, SeverityBadge, etc.) inline
7. **Enforce all constraints** from the table above in the UI logic
8. **Keep the artifact self-contained** — single React component, all code inline, no external imports beyond the allowed stack

### After Artifact Interaction

After the assessor interacts with the artifact and pastes the delta JSON:

1. **Parse the delta JSON** — validate it's a proper array of change objects
2. **Validate each change** against business rules (e.g., criticality escalation only)
3. **Apply valid changes** to the relevant workspace JSON file(s)
4. **Log all changes** in the session audit trail with timestamps
5. **Report back** what was applied, what was rejected (if any), and why
6. **Proceed** to the next pipeline step

---

## CP Reference Index

Detailed artifact specifications for each CP are in the `references/` directory:

| File | CP | Data Sources |
|------|----|-------------|
| `references/cp1-artifact.md` | CP1: Context & Assessor Profile | context-profile.json, assessor-profile.json |
| `references/cp2-artifact.md` | CP2: Assessment Framework | framework.json |
| `references/cp3-artifact.md` | CP3: Scored Findings | readiness-register.json, fit-to-purpose-register.json, gap-register.json, dependency-map.json, go-nogo-determination.json |
| `references/cp4-artifact.md` | CP4: Assessment Scope | assessment-scope-plan.json |
| `references/cp5-artifact.md` | CP5: Reconciled Findings | integrated-findings-register.json, domain-findings-*.json, updated-go-nogo-determination.json |
| `references/sensitivity-selector.md` | Sensitivity Methodology | updated-go-nogo-determination.json, integrated-findings-register.json |
