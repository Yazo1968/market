---
name: design-system
description: >
  Centralized visual identity and quality contract for all assessment outputs —
  both interactive CP artifacts (Cowork React) and final HTML/PDF reports.
  This is the single source of truth for colors, typography, component specs,
  chart palettes, and quality standards. Referenced by interactive-review and
  html-dashboard skills. Trigger phrases: "design system", "visual identity",
  "brand standards", "style guide", "quality standards".
version: 1.0.0
---

# Assessment Design System

## Purpose

This is the **single source of truth** for visual identity across the entire assessment workflow. Both interactive CP artifacts (rendered in Cowork) and final HTML/PDF deliverables reference this file to ensure one consistent, professional brand from first interaction to final report.

**Two rendering contexts, one visual identity:**

| Context | Technology | Theme | Skill |
|---------|-----------|-------|-------|
| CP Artifacts (in-conversation) | React 18, Tailwind, Shadcn, Recharts | Dark (slate-900 base) | `interactive-review` |
| Final Reports (standalone files) | Self-contained HTML, Chart.js | Light (white base) | `html-dashboard` |

The theme differs by context (dark UI for Cowork's dark conversation pane, light for standalone files optimized for reading and print). But the **semantic colors, typography, component proportions, and chart palettes are identical** across both.

---

## 1. Semantic Color Tokens

These are absolute. Every surface that renders a determination, severity, confidence, or assessment mode **must** use exactly these values. No approximations.

### Determination Colors

| Determination | Hex | RGB | Usage |
|---------------|-----|-----|-------|
| **GO** | `#22c55e` | `34, 197, 94` | Proceed with confidence |
| **CONDITIONAL GO** | `#3b82f6` | `59, 130, 246` | Proceed with identified conditions |
| **CONDITIONAL HOLD** | `#f59e0b` | `245, 158, 11` | Hold pending resolution |
| **NO-GO** | `#ef4444` | `239, 68, 68` | Do not proceed |

**Backgrounds (10% opacity of determination color):**
- GO: `rgba(34, 197, 94, 0.1)`
- CONDITIONAL GO: `rgba(59, 130, 246, 0.1)`
- CONDITIONAL HOLD: `rgba(245, 158, 11, 0.1)`
- NO-GO: `rgba(239, 68, 68, 0.1)`

**Borders (30% opacity):**
- GO: `rgba(34, 197, 94, 0.3)`
- CONDITIONAL GO: `rgba(59, 130, 246, 0.3)`
- CONDITIONAL HOLD: `rgba(245, 158, 11, 0.3)`
- NO-GO: `rgba(239, 68, 68, 0.3)`

### Severity Colors

| Severity | Hex | RGB |
|----------|-----|-----|
| **Critical** | `#ef4444` | `239, 68, 68` |
| **Significant** | `#f97316` | `249, 115, 22` |
| **Moderate** | `#f59e0b` | `245, 158, 11` |
| **Minor** | `#94a3b8` | `148, 163, 184` |

### Confidence Colors

| Level | Hex | RGB |
|-------|-----|-----|
| **High** | `#22c55e` | `34, 197, 94` |
| **Medium** | `#f59e0b` | `245, 158, 11` |
| **Low** | `#ef4444` | `239, 68, 68` |

### Assessment Mode Colors

| Mode | Hex | RGB |
|------|-----|-----|
| **Gap-Focused** | `#3b82f6` | `59, 130, 246` |
| **Verification** | `#f59e0b` | `245, 158, 11` |
| **Deep-Independent** | `#ef4444` | `239, 68, 68` |

### Score-to-Color Gradient

Scores (0-100) map to a continuous color gradient:

```
0%  ─── #ef4444 (red) ─── 50% ─── #f59e0b (amber) ─── 100% ─── #22c55e (green)
```

**Implementation (use in both contexts):**

```javascript
function scoreToColor(score) {
  score = Math.max(0, Math.min(100, score));
  if (score < 50) {
    const ratio = score / 50;
    const r = 239;
    const g = Math.round(68 + (158 - 68) * ratio);
    const b = Math.round(68 + (11 - 68) * ratio);
    return `rgb(${r}, ${g}, ${b})`;
  } else {
    const ratio = (score - 50) / 50;
    const r = Math.round(245 - (245 - 34) * ratio);
    const g = Math.round(158 + (197 - 158) * ratio);
    const b = Math.round(11 + (94 - 11) * ratio);
    return `rgb(${r}, ${g}, ${b})`;
  }
}
```

### Chart Data Series Colors

When rendering multi-series charts (radar, bar, line), always use this palette in order:

| Series | Hex | Usage |
|--------|-----|-------|
| Series 1 (Readiness) | `#3b82f6` (blue-500) | Primary data track |
| Series 2 (Fit-to-Purpose) | `#a855f7` (purple-500) | Secondary data track |
| Series 3 | `#f59e0b` (amber-500) | Tertiary |
| Series 4 | `#22c55e` (green-500) | Quaternary |
| Series 5 | `#ef4444` (red-500) | Fifth series |
| Series 6 | `#06b6d4` (cyan-500) | Sixth series |

Fill areas: 10% opacity of the series color.

### Accent Color

| Token | Hex | Usage |
|-------|-----|-------|
| **Accent** | `#6366f1` (indigo-500) | Interactive elements, selection highlights, primary buttons |
| **Accent hover** | `#4f46e5` (indigo-600) | Hover state |

### Theme-Specific Surface Colors

**Dark theme (CP artifacts in Cowork):**

| Token | Hex | Tailwind |
|-------|-----|----------|
| Background | `#0f172a` | slate-900 |
| Surface | `#1e293b` | slate-800 |
| Elevated | `#334155` | slate-700 |
| Border | `#475569` | slate-600 |
| Text primary | `#f8fafc` | slate-50 |
| Text secondary | `#94a3b8` | slate-400 |
| Text muted | `#64748b` | slate-500 |

**Light theme (HTML/PDF reports):**

| Token | Hex | CSS |
|-------|-----|-----|
| Background | `#ffffff` | white |
| Surface | `#f9fafb` | gray-50 |
| Elevated | `#f3f4f6` | gray-100 |
| Border | `#e5e7eb` | gray-200 |
| Text primary | `#111827` | gray-900 |
| Text secondary | `#6b7280` | gray-500 |
| Text muted | `#9ca3af` | gray-400 |

---

## 2. Typography

**Primary font:** `Inter` — loaded via Google Fonts CDN in both contexts.

```
CDN: https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap
```

**Monospace font:** `JetBrains Mono, SF Mono, Monaco, Consolas, monospace` — for scores, IDs, JSON, code.

### Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| Page title (h1) | 24px / 1.5rem | 700 | 1.2 | -0.025em |
| Section heading (h2) | 18px / 1.125rem | 600 | 1.3 | -0.02em |
| Subsection (h3) | 15px / 0.9375rem | 600 | 1.4 | -0.01em |
| Body | 14px / 0.875rem | 400 | 1.5 | 0 |
| Small / caption | 12px / 0.75rem | 500 | 1.4 | 0 |
| Micro (badges, labels) | 11px / 0.6875rem | 600 | 1.2 | 0.05em |
| Score display (large) | 32px / 2rem | 700 | 1.1 | -0.03em |
| Score display (inline) | 14px / 0.875rem | 600 | 1.2 | 0 (monospace) |

---

## 3. Spacing & Layout

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Badge padding, inline gaps |
| sm | 8px | Tight element gaps |
| md | 12px | Standard card padding, section gaps |
| lg | 16px | Section padding |
| xl | 24px | Section separation |
| 2xl | 32px | Major section breaks |
| 3xl | 48px | Page-level section separation |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| sm | 4px | Badges, pills, small chips |
| md | 6px | Buttons, inputs |
| lg | 8px | Cards, panels |
| xl | 12px | Hero badges, feature cards |
| full | 9999px | Circular elements, pills |

### Component Proportions

These proportions are consistent across both themes:

| Component | Min Height | Padding | Border Width |
|-----------|-----------|---------|--------------|
| Determination badge (hero) | 80px | 24px 32px | 2px |
| Determination badge (inline) | 28px | 4px 12px | 1px |
| Score bar | 8px track | — | 0 (rounded-full) |
| Score ring (SVG) | 120px diameter | — | 6px stroke |
| Card (standard) | 60px | 16px | 1px |
| Card (feature/selection) | 120px | 20px 24px | 2px |
| Tab bar | 48px | 12px 20px | 3px bottom (active) |
| Table header row | 44px | 12px 16px | 2px bottom |
| Table data row | 40px | 12px 16px | 1px bottom |
| Button (primary) | 36px | 8px 16px | 0 |
| Button (secondary) | 36px | 8px 16px | 1px |
| Input / textarea | 36px | 8px 12px | 1px |
| Badge / pill (severity) | 22px | 2px 8px | 0 |

---

## 4. Component Visual Specs

These define the **visual appearance** of shared components. Implementation differs (React/Tailwind vs raw HTML/CSS) but the rendered result must be visually identical.

### Determination Badge

```
┌──────────────────────────────────────┐
│            [ICON/CIRCLE]             │
│                                      │
│         CONDITIONAL GO               │  ← Score display size, bold
│                                      │
│    Company Name · 2026-03-15         │  ← Small, secondary text
└──────────────────────────────────────┘
```

- Background: 10% determination color
- Border: 30% determination color, 2px
- Text: determination color
- Border radius: xl (12px)
- Icon circle: 64px, filled with determination color, white icon inside

### Score Bar

```
[Label]  ████████████████░░░░░░░  78%
```

- Track: 8px height, rounded-full, surface color
- Fill: scoreToColor(value), rounded-full, smooth transition (200ms)
- Label: small text, secondary color, fixed width
- Value: monospace, semi-bold, fixed width right-aligned

### Score Ring (SVG)

- 120px diameter (responsive down to 80px on mobile)
- Background circle: border color, 6px stroke
- Progress circle: scoreToColor(value), 6px stroke, rounded cap
- Center text: score display (large), bold
- Percent symbol: small text below score

### Severity Badge

```
[CRITICAL]  [SIGNIFICANT]  [MODERATE]  [MINOR]
```

- Pill shape: rounded-full (9999px)
- Height: 22px
- Font: micro (11px), uppercase, 600 weight, 0.05em spacing
- Background: severity color at full opacity
- Text: white

### Card

- Background: surface color
- Border: 1px border color
- Radius: lg (8px)
- Padding: lg (16px)
- Hover: slight elevation (shadow), border lightens
- Active/selected: accent border (2px), accent background at 10%

### Data Table

- Header: elevated background, bold text, 2px bottom border
- Rows: alternating surface/background colors
- Hover: subtle highlight
- Numeric columns: right-aligned, tabular-nums, monospace
- Sortable headers: cursor pointer, arrow indicators

### Tab Bar

- Horizontal, sticky top, scrollable overflow
- Inactive: secondary text, no bottom border
- Hover: primary text, subtle background
- Active: primary text, bold, 3px accent-colored bottom border
- Focus: 2px accent outline
- Keyboard: arrow keys navigate, Home/End jump

---

## 5. Chart Standards

### General Chart Config

All charts (Chart.js or Recharts) must use:

- Font: Inter at 11-13px for labels, 12px for tooltips
- Grid lines: 10% opacity of border color
- Tooltip: dark background (`rgba(15, 23, 42, 0.9)`), white text, 12px padding, rounded corners
- Legend: top position, point-style markers, 16px padding
- Animations: 300ms default duration
- Responsive: `responsive: true, maintainAspectRatio: true`

### Chart Type Usage

| Data Pattern | Chart Type | When to Use |
|-------------|-----------|-------------|
| Multi-domain comparison (2 tracks) | Radar | Domain scores overview |
| Single-dimension comparison | Horizontal bar | Gap severity distribution, domain ranking |
| Side-by-side comparison | Grouped vertical bar | Readiness vs Fit per domain |
| Part-of-whole | Donut/Pie | Mode distribution, determination probability |
| Trend / timeline | Line | Score progression, scenario curves |
| Dense multi-variable overview | Heatmap grid (CSS) | 10-domain at-a-glance |
| Probability distribution | Histogram | Monte Carlo results |

Agents choose which charts best serve each case. These are guidelines, not mandates — if a case calls for a visualization not listed here, create it using the design system colors and typography.

### Accessibility

- Never rely on color alone to convey meaning — always pair with text labels, icons, or patterns
- Minimum contrast ratio: 4.5:1 for text, 3:1 for graphical elements
- All charts must have text alternatives (summary below chart or ARIA labels)
- Color-blind safe: the score-to-color gradient (red-amber-green) is always accompanied by numeric values

---

## 6. Quality Contract

This is the minimum quality bar for all outputs. Agents have full creative freedom on content structure and emphasis — but every output must meet these standards.

### Visual Quality Floor

- [ ] **Typography**: Inter font loaded and rendering. Clear heading hierarchy. No font fallback visible.
- [ ] **Color consistency**: All determination, severity, confidence, and mode colors match this design system exactly. No approximations, no hardcoded alternates.
- [ ] **Component proportions**: Badges, cards, tables, score bars use the proportions defined above.
- [ ] **Spacing**: Consistent use of spacing scale. No cramped layouts. Generous whitespace between sections.
- [ ] **Responsive**: HTML reports render correctly at 1200px+, 768px, and 480px breakpoints. Charts resize. Tables scroll horizontally on mobile. No horizontal page overflow.

### Interactivity Floor (HTML reports)

- [ ] **Tab navigation**: Keyboard-accessible (arrow keys, Home/End). Active state clearly visible. Sticky header.
- [ ] **Expandable sections**: Smooth expand/collapse. Arrow rotation animation. ARIA attributes.
- [ ] **Charts**: Hover tooltips with formatted values. Legend click to toggle series. Responsive resize.
- [ ] **Sortable tables**: Click-to-sort headers with visual indicator (arrow direction).

### Print Readiness (PDF/print)

- [ ] **Page breaks**: Logical breaks before major sections. No orphaned headings.
- [ ] **Charts preserved**: Canvas elements render in print. Colors not lost.
- [ ] **Margins**: Adequate margins for binding (left: 25mm, others: 20mm).
- [ ] **Headers/footers**: Company name, date, "CONFIDENTIAL" footer, page numbers.
- [ ] **Typography**: Print-optimized sizes (body 11pt, headings proportional).

### Professional Standards

These are the benchmarks. Outputs should be indistinguishable in quality from reports produced by:
- Top-tier management consultancies (McKinsey, BCG, Bain)
- Leading VC firms (Sequoia, a16z, Benchmark)
- Major credit agencies (S&P, Moody's, Fitch)
- Certified valuation professionals (CFA, ASA, CVA)

This means:

**Information architecture:**
- Executive summary that stands alone — a decision-maker reads only this page and gets the full picture
- Progressive disclosure — high-level first, drill into detail on demand
- Every chart and table has a clear "so what" — data supports a narrative, not the other way around
- No orphaned data — every metric is contextualized (benchmarks, thresholds, trends)

**Narrative quality:**
- Findings are actionable, not descriptive ("Revenue growth is decelerating and will miss breakeven by Q3 if trend continues" not "Revenue growth is 15%")
- Risk language is precise ("material risk to debt service coverage if customer churn exceeds 8% annually" not "churn is a risk")
- Strengths are substantiated ("3 enterprise contracts worth $2.1M ARR provide 18 months of revenue visibility" not "strong customer base")
- Conditions are specific and measurable ("Achieve $500K MRR within 6 months" not "improve revenue")

**Data visualization:**
- Charts tell a story — axis labels, titles, annotations, reference lines, callouts where needed
- No chart junk — remove unnecessary gridlines, legends for single-series, redundant labels
- Consistent scale across comparable charts (don't let auto-scaling mislead)
- Dual-axis charts used sparingly and only when clearly labeled

**Formatting:**
- Consistent number formatting throughout (commas for thousands, 1 decimal for percentages, $M/$K for currencies)
- Dates in consistent format (ISO 8601 or localized, not mixed)
- Table alignment: text left, numbers right, badges center
- White space used deliberately — dense where data requires it, spacious where narrative needs breathing room

### Assessor-Type Tone Adaptation

The same data is framed differently based on the assessor's world:

| Assessor Type | Tone | Emphasis | Language |
|---------------|------|----------|----------|
| Venture Capital | Forward-looking, opportunity-focused | Market size, team, growth potential, defensibility | "Addressable market", "burn multiple", "product-market fit" |
| Angel Investor | Founder-focused, conviction-driven | People, vision, early traction, capital efficiency | "Founder-market fit", "conviction", "inflection point" |
| Private Equity | Performance-focused, value-creation | EBITDA, margins, operational levers, de-risking | "Value creation plan", "multiple expansion", "operating leverage" |
| Credit / Debt | Risk-focused, downside-protective | Cash flow, debt service, collateral, covenants | "Coverage ratios", "debt service capacity", "stress scenario" |
| Corporate Strategic | Synergy-focused, integration-aware | Strategic fit, technology stack, talent, market access | "Synergy realization", "integration risk", "strategic value" |
| Family Office | Relationship-focused, values-aligned | Capital preservation, alignment, long-term value | "Generational wealth", "alignment with values", "capital preservation" |
| Sovereign Wealth | Mandate-focused, policy-aligned | National priorities, technology transfer, scale | "Strategic mandate", "national interest", "knowledge transfer" |
| Accelerator | Potential-focused, coaching-oriented | Coachability, founder quality, market timing | "Founder potential", "velocity of learning", "coaching leverage" |

---

## 6b. Known Limitations (Documented per AICPA VS 100 / IVS 106)

The following limitations are inherent to the current system and are **documented transparently** rather than remediated. These must be disclosed in every report's Limitations section.

| Limitation | Standard | Status | Mitigation |
|-----------|----------|--------|-----------|
| **No outcome validation** — The scoring methodology has not been validated against actual investment outcomes (back-tested). | IOSCO CRA Code (annual methodology validation) | Acknowledged | Methodology is systematically constructed and peer-reviewed against professional standards. Outcome validation requires post-investment tracking data not currently available. |
| **Audit trail is session-based** — The audit trail is maintained in the Cowork session state and exported to the final PDF. It is not stored in an append-only immutable log during the session. | SOC 2 Type II (processing integrity), ISAE 3402 | Acknowledged | Audit trail is sealed at CP5 and embedded in the final PDF appendix. Within-session integrity depends on the Cowork platform's session management. Post-session, the PDF audit trail is the authoritative record. |
| **No real-time monitoring** — Assessments are point-in-time snapshots. No continuous monitoring of the assessed company occurs post-assessment. | COSO ERM (monitoring and review) | Out of scope | The tool's scope ends at recommendation delivery. Post-investment monitoring is the assessor's responsibility. Re-assessment is available via `/pre-assess` at any time. |
| **AI model limitations** — The AI model has a training knowledge cutoff and may not reflect the most recent market developments, regulatory changes, or industry events. | EU AI Act Article 15 (accuracy, robustness) | Acknowledged | All scoring-eligible evidence is obtained via live retrieval (not training knowledge). The 3H Principle and Training-Derived exclusion rule mitigate this risk. |
| **Single-assessor workflow** — The current workflow supports a single human assessor. Multi-party IC committee review, formal red-team panels, and multi-assessor consensus are not natively supported. | PE IC conventions (committee review) | Partial | The red-team challenge (Step 3b) provides an adversarial perspective. The final PDF is designed for IC circulation and can be reviewed by a committee externally. |

---

## 7. Implementation Notes

### For `interactive-review` (CP artifacts)

- Import this design system's color tokens directly as Tailwind classes
- Map semantic tokens to Tailwind: `#22c55e` → `green-500`, `#3b82f6` → `blue-500`, etc.
- Dark theme surface colors map naturally to Tailwind slate scale
- Use Recharts with chart data series colors from this system
- Component proportions translate directly to Tailwind spacing/sizing utilities

### For `html-dashboard` (final reports)

- Embed this design system's color tokens as CSS custom properties in the `<style>` block
- Light theme surface colors are the default
- Use Chart.js with the same hex values for chart data series
- Component proportions translate to explicit CSS px/rem values
- Score-to-color function is identical JavaScript in both contexts

### CSS Custom Properties Template (for HTML reports)

```css
:root {
  /* Determination */
  --color-go: #22c55e;
  --color-conditional-go: #3b82f6;
  --color-conditional-hold: #f59e0b;
  --color-no-go: #ef4444;

  /* Severity */
  --color-critical: #ef4444;
  --color-significant: #f97316;
  --color-moderate: #f59e0b;
  --color-minor: #94a3b8;

  /* Confidence */
  --color-confidence-high: #22c55e;
  --color-confidence-medium: #f59e0b;
  --color-confidence-low: #ef4444;

  /* Assessment modes */
  --color-gap-focused: #3b82f6;
  --color-verification: #f59e0b;
  --color-deep-independent: #ef4444;

  /* Chart series */
  --color-series-1: #3b82f6;
  --color-series-2: #a855f7;
  --color-series-3: #f59e0b;
  --color-series-4: #22c55e;
  --color-series-5: #ef4444;
  --color-series-6: #06b6d4;

  /* Accent */
  --color-accent: #6366f1;
  --color-accent-hover: #4f46e5;

  /* Surfaces (light theme) */
  --surface-bg: #ffffff;
  --surface-card: #f9fafb;
  --surface-elevated: #f3f4f6;
  --surface-border: #e5e7eb;
  --text-primary: #111827;
  --text-secondary: #6b7280;
  --text-muted: #9ca3af;

  /* Typography */
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'SF Mono', Monaco, Consolas, monospace;
}
```

---

## References

This design system is implemented by:

- `skills/interactive-review/SKILL.md` — CP artifact rendering (React/Tailwind)
- `skills/html-dashboard/SKILL.md` — Final report rendering (HTML/CSS/Chart.js)
- `skills/html-dashboard/references/chart-patterns.md` — Chart implementations
- `skills/html-dashboard/references/component-library.md` — HTML/CSS component library
