# Sensitivity Methodology Selector Artifact

## Data Sources

- `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
- `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`

## Artifact Structure

### Header

```
[Company Name]                                          [DETERMINATION BADGE]
Sensitivity Analysis · Methodology Selection

Overall Score: NN%     Readiness: NN%     Fit: NN%
```

### Main Content — Methodology Cards

Based on the determination type, render 2–3 large methodology selection cards. This is a **radio-button style selector** — only one methodology can be chosen.

**Card Layout:**
```
┌────────────────────────────────────────────────────────────────────┐
│ ○  [Methodology Name]                          [Recommended] badge │
│                                                                    │
│    Description paragraph explaining what this methodology does     │
│    and what kind of insights it produces...                        │
│                                                                    │
│    What it tests:                                                  │
│    • Bullet point 1                                                │
│    • Bullet point 2                                                │
│                                                                    │
│    What you'll learn:                                              │
│    • Insight 1                                                     │
│    • Insight 2                                                     │
│                                                                    │
│    Path B impact:                                                  │
│    "How this methodology affects Path B eligibility..."            │
└────────────────────────────────────────────────────────────────────┘
```

**Card states:**
- Unselected: `bg-slate-800 border-slate-700` — subtle, recessed
- Hover: `bg-slate-750 border-slate-600` — slight lift
- Selected: `bg-indigo-500/10 border-indigo-500/50` — highlighted with indigo glow + filled radio button
- Recommended: has a small indigo "Recommended" badge in top-right corner

### Methodology Options by Determination Type

**GO Determination:**

Card 1: **Boundary/Flip-Point Analysis** (Recommended)
- Tests: How close the determination is to dropping to CONDITIONAL GO
- Learns: Safety margin, minimum evidence deterioration to trigger flip
- Path B: All GO determinations qualify for Path B

Card 2: **Scenario Analysis**
- Tests: Determination resilience under pessimistic assumptions
- Learns: Whether GO holds under challenging market/execution scenarios
- Path B: All GO determinations qualify for Path B

**CONDITIONAL GO Determination:**

Card 1: **Scenario Analysis** (Recommended)
- Tests: Whether stated conditions can realistically be met
- Learns: Assumption sensitivity, condition achievability
- Path B: Depends on condition attainability assessment

Card 2: **Boundary/Flip-Point Analysis**
- Tests: Distance from full GO (upward) and CONDITIONAL HOLD (downward)
- Learns: How much improvement needed for GO, how much deterioration to HOLD
- Path B: Depends on flip distance analysis

Card 3: **Monte Carlo Simulation**
- Tests: Probability distribution across all determination levels
- Learns: Confidence intervals, key uncertainty drivers
- Path B: Depends on probability analysis

**CONDITIONAL HOLD / NO-GO Determination:**

Card 1: **Gap Closure Feasibility** (Recommended)
- Tests: Timeline and effort to close critical gaps
- Learns: Which gaps are closeable vs fundamental, impact of closure
- Path B: Eligible only if critical gaps deemed closeable

Card 2: **Pivot Sensitivity**
- Tests: How pivots to alternative markets/products affect assessment
- Learns: Whether strategic pivots could change determination
- Path B: Depends on pivot viability

### Selection Behavior

```jsx
const [selected, setSelected] = useState(null);

// Card click handler
const handleSelect = (methodologyId) => {
  setSelected(methodologyId);
};
```

### Footer

The ChangesFooter for this artifact is simplified:
- No "changes" tracking — just a single selection
- Footer shows: `Selected: [Methodology Name]` · [Copy to Clipboard]
- Copy produces:

```json
{ "methodology": "boundary-analysis", "determination": "GO" }
```

### Visual Design Notes

- Cards should be large and well-spaced — this is a critical decision point
- Each card should be at least 200px tall with generous padding
- Use clear visual hierarchy: methodology name (text-lg, font-bold), description (text-sm), bullets (text-sm, muted)
- The recommended card should have a subtle pulse animation on the badge on first render
- Selection transition should be smooth (200ms border/background color change)
