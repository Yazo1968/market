# CP2 Artifact: Assessment Framework Review

## Data Source

- `$WORKSPACE/assessment/pre-assessment/data/framework.json`

## Artifact Structure

### Header

```
[Company Name]                    [Active Domains: N/10] [Total Modules: N]
Pre-Assessment · Confirmation Point 2
```

**Stats bar** (below header):
- Active domains: N / 10
- Total active modules: N
- Readiness track weight: N% (mini bar)
- Fit-to-Purpose track weight: N% (mini bar)

### Main Content — Two columns

**Left column (70%): Domain Cards**

Render one collapsible card per domain from `framework.json.domains[]`:

**Domain Card Header:**
```
[Domain ID] [Domain Name]               [Criticality Badge] [Weight: N%]
[Active Toggle]                          [Module Count: N]
```

- **Active toggle**: Switch component
  - DISABLED (locked) if domain is mandatory per framework (show Lock icon)
  - Enabled for optional domains
- **Criticality**: Dropdown badge
  - Options shown: only current level and above (escalation only)
  - `contextual` → can go to `standard`, `critical`, `hard-blocker`
  - `standard` → can go to `critical`, `hard-blocker`
  - `critical` → can go to `hard-blocker`
  - `hard-blocker` → locked (cannot change)
- **Weight**: Slider (range 0–40%, step 1%)
  - When adjusted, other active domain weights auto-redistribute proportionally to maintain sum = 100%
  - Live display of new weight value

**Domain Card Body (collapsed by default, expand on click):**

Module table within each domain:

| Column | Content | Editable? | Control |
|--------|---------|-----------|---------|
| Module ID | M1.1 etc | No | Display |
| Module Name | Text | No | Display |
| Active | Checkbox | Yes (if optional) / Locked (if mandatory) | Checkbox or Lock icon |
| Criticality | Badge | Yes (escalate only) | Dropdown: optional → important → mandatory |
| Readiness Weight | Number | Yes | Mini number input (auto-normalize within domain) |
| Fit Weight | Number | Yes | Mini number input (auto-normalize within domain) |
| Professional Standard | Text | No | Tooltip on hover |

**Right column (30%): Sidebar**

**Hard Blockers Panel** (red-tinted card):
- List of all hard blocker conditions from the framework
- Each shows: condition description + trigger consequence
- Locked — display only, red Lock icon
- Red border, `bg-red-500/5`

**Weight Distribution Chart:**
- Recharts RadarChart showing domain weights
- Updates live as user adjusts sliders
- All 10 domains plotted (inactive domains at 0)

**Framework Construction Log** (collapsible):
- Base taxonomy applied
- Stage calibration applied
- Vertical calibration applied
- Assessor adjustments (list)

## Constraint Enforcement

```jsx
// Domain weight auto-redistribution
const handleWeightChange = (domainId, newWeight) => {
  const otherActiveDomains = domains.filter(d => d.active && d.domain_id !== domainId);
  const currentTotal = otherActiveDomains.reduce((sum, d) => sum + d.domain_weight, 0);
  const remaining = 1.0 - newWeight;
  const scale = currentTotal > 0 ? remaining / currentTotal : 0;

  setDomains(prev => prev.map(d => {
    if (d.domain_id === domainId) return { ...d, domain_weight: newWeight };
    if (d.active) return { ...d, domain_weight: d.domain_weight * scale };
    return d;
  }));
};

// Criticality escalation only
const getCriticalityOptions = (current) => {
  const levels = ['contextual', 'standard', 'critical', 'hard-blocker'];
  const idx = levels.indexOf(current);
  return levels.slice(idx); // current and above only
};

// Module criticality escalation only
const getModuleCriticalityOptions = (current) => {
  const levels = ['optional', 'important', 'mandatory'];
  const idx = levels.indexOf(current);
  return levels.slice(idx);
};
```

## Changes Delta Format

```json
[
  { "field": "domain_3.weight", "original": 0.12, "to": 0.15, "context": "framework" },
  { "field": "domain_3.criticality", "original": "standard", "to": "critical", "context": "framework" },
  { "field": "M4.2.criticality", "original": "optional", "to": "important", "context": "framework" },
  { "field": "M4.2.active", "original": false, "to": true, "context": "framework" },
  { "field": "domain_5.weight", "original": 0.10, "to": 0.08, "context": "framework.auto-redistributed" }
]
```

Auto-redistributed weight changes are tagged with `context: "framework.auto-redistributed"` so the validation step knows they are derived, not user-initiated.
