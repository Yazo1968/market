# Assessor Profile Collector Artifact

## Purpose

Single interactive artifact that collects all assessor profile inputs in one view, replacing the 5-step sequential AskUserQuestion flow. The assessor fills out their investment profile using professional UI controls, then copies the completed profile JSON via the footer.

## Data Sources

- No pre-existing data — this is a collection artifact, not a review artifact
- Schema reference: `schemas/assessor-profile.json`

## Artifact Structure

### Header

```
Startup Assessment                                          [Setup]
Assessor Profile · Investor Criteria Collection

Tell us about your investment mandate so we can calibrate the assessment.
```

- Subtitle text in `text-slate-400`, providing context
- No determination badge (profile hasn't been created yet)

### Main Content — Profile Form

The form is laid out as a series of well-spaced sections with clear labels. Each section has a heading, optional helper text, and the input control.

**Section 1: Investment Capacity**

```
┌────────────────────────────────────────────────────────────────────┐
│ What is your primary investment or lending capacity?               │
│                                                                    │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────────┐ │
│ │ Venture     │ │ Angel       │ │ Private     │ │ Credit /     │ │
│ │ Capital     │ │ Investor    │ │ Equity      │ │ Debt         │ │
│ └─────────────┘ └─────────────┘ └─────────────┘ └──────────────┘ │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────────┐ │
│ │ Corporate   │ │ Family      │ │ Sovereign   │ │ Accelerator  │ │
│ │ Strategic   │ │ Office      │ │ Wealth      │ │              │ │
│ └─────────────┘ └─────────────┘ └─────────────┘ └──────────────┘ │
│ ┌─────────────┐                                                   │
│ │ Other       │                                                   │
│ └─────────────┘                                                   │
└────────────────────────────────────────────────────────────────────┘
```

- **Control type:** Selectable card grid (radio — single selection)
- **Card states:**
  - Unselected: `bg-slate-800 border-slate-700 text-slate-300`
  - Hover: `bg-slate-750 border-slate-600`
  - Selected: `bg-indigo-500/10 border-indigo-500/50 text-indigo-300`
- **Maps to schema:** `assessor_type`
- **Values:** `venture-capital`, `angel-investor`, `private-equity`, `credit-debt`, `corporate-strategic`, `family-office`, `sovereign-wealth`, `accelerator`, `other`
- If "Other" selected, show a text input below: "Please specify:"

**Section 2: Target Stage**

```
┌────────────────────────────────────────────────────────────────────┐
│ What funding stage and company maturity do you typically target?   │
│                                                                    │
│ ┌───────────┐ ┌──────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐ │
│ │ Pre-Seed  │ │ Seed │ │ Series A │ │ Series B+│ │ Growth     │ │
│ │           │ │      │ │          │ │          │ │ Stage      │ │
│ └───────────┘ └──────┘ └──────────┘ └──────────┘ └────────────┘ │
│ ┌──────────┐ ┌────────────────────┐ ┌─────────┐                  │
│ │ Buyout   │ │ Restructuring /   │ │ Other   │                  │
│ │          │ │ Turnaround        │ │         │                  │
│ └──────────┘ └────────────────────┘ └─────────┘                  │
└────────────────────────────────────────────────────────────────────┘
```

- **Control type:** Selectable card grid (radio — single selection)
- Same card states as Section 1
- If "Other" selected, show a text input: "Please specify:"

**Section 3: Must-Have Criteria / Deal-Breakers**

```
┌────────────────────────────────────────────────────────────────────┐
│ Select your must-have criteria or deal-breakers                   │
│ (choose all that apply)                                           │
│                                                                    │
│ ☐ Minimum recurring revenue (MRR/ARR)                             │
│ ☐ Specific vertical or sector focus                               │
│ ☐ Founder/team sector experience                                  │
│ ☐ Regulatory approval in place                                    │
│ ☐ US-based team only                                              │
│ ☐ No single customer >50% revenue                                 │
│ ☐ Profitability required                                          │
│ ☐ None of the above                                               │
│                                                                    │
│ + Add custom criterion  [text input appears on click]             │
└────────────────────────────────────────────────────────────────────┘
```

- **Control type:** Checkbox list (multi-select)
- **Checkbox states:**
  - Unchecked: `border-slate-600` with empty box
  - Checked: `bg-indigo-500 border-indigo-500` with checkmark
- Selecting "None of the above" clears all other selections (and vice versa)
- **+ Add custom criterion:** clicking reveals a text input + small "Add" button; user can add multiple custom criteria
- **Maps to schema:** `non_negotiables[]`

**Section 4: Quantitative Thresholds**

```
┌────────────────────────────────────────────────────────────────────┐
│ Quantitative thresholds                                           │
│ e.g. minimum revenue, maximum burn rate, team size requirements   │
│                                                                    │
│ ○ No — use standard thresholds                                    │
│ ○ Yes — I have specific thresholds                                │
│                                                                    │
│ [Conditional: if Yes is selected]                                 │
│ ┌──────────────────────────────────────────────────────────────┐  │
│ │ Describe your thresholds...                                  │  │
│ │                                                              │  │
│ │                                                              │  │
│ └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

- **Control type:** Radio buttons (Yes/No) + conditional textarea
- Radio: same style as card selection but inline radio circles
- Textarea: `bg-slate-800 border-slate-700`, 3 rows, placeholder text "Describe your quantitative thresholds (e.g., minimum $500K ARR, max 24-month burn runway, team of 5+)..."
- Textarea only visible when "Yes" is selected (smooth slide-down animation, 200ms)
- **Maps to schema:** `firm_specific_standards[]`

**Section 5: Exclusions & Constraints**

```
┌────────────────────────────────────────────────────────────────────┐
│ Sector exclusions or geographic constraints                       │
│                                                                    │
│ ○ No constraints                                                  │
│ ○ Yes — I have exclusions or constraints                          │
│                                                                    │
│ [Conditional: if Yes is selected]                                 │
│ ┌──────────────────────────────────────────────────────────────┐  │
│ │ Describe your exclusions or constraints...                   │  │
│ │                                                              │  │
│ │                                                              │  │
│ └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

- Same control pattern as Section 4
- Textarea placeholder: "Describe sector exclusions or geographic constraints (e.g., no gambling/cannabis, MENA region only, must operate in EU)..."
- **Maps to schema:** contributes to `firm_specific_standards[]` and `non_negotiables[]`

**Section 6: Institutional Context (Optional)**

```
┌────────────────────────────────────────────────────────────────────┐
│ Institutional context (optional)                                  │
│ Fund thesis, portfolio focus, sector expertise, or other context  │
│                                                                    │
│ ┌──────────────────────────────────────────────────────────────┐  │
│ │ Tell us about your fund or investment context...             │  │
│ │                                                              │  │
│ │                                                              │  │
│ └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

- **Control type:** Textarea (always visible, optional)
- Placeholder: "e.g., $50M seed fund focused on B2B SaaS in fintech and healthtech. Portfolio of 30 companies. Looking for capital-efficient models with clear path to $10M ARR."
- **Maps to schema:** `institutional_context`

### Form State Management

```jsx
const [profile, setProfile] = useState({
  assessor_type: null,
  assessor_type_other: '',
  target_stage: null,
  target_stage_other: '',
  must_haves: [],
  custom_criteria: [],
  has_thresholds: null,      // true/false
  thresholds_text: '',
  has_exclusions: null,       // true/false
  exclusions_text: '',
  institutional_context: '',
});
```

### Validation

Before the profile can be copied, validate:
- `assessor_type` must be selected (required)
- `target_stage` must be selected (required)
- At least one must-have criterion selected OR "None of the above" (required)
- If `has_thresholds === true`, `thresholds_text` must not be empty
- If `has_exclusions === true`, `exclusions_text` must not be empty

Show validation state:
- Incomplete required fields: section header gains a small amber dot indicator
- All required fields complete: section header gains a green check
- Footer "Copy" button disabled until all required fields are valid

### Footer

The footer for this artifact differs from the ChangesFooter used in CP artifacts. Since this is a collection form (not a review-with-delta), the footer shows:

```
┌────────────────────────────────────────────────────────────────────┐
│  ✓ 5 of 5 sections complete                    [Copy to Clipboard]│
└────────────────────────────────────────────────────────────────────┘
```

- Progress indicator: "N of 5 sections complete" (amber if incomplete, green when all done)
- Copy button: disabled + muted until all required fields are valid
- Copy produces the profile JSON (see below)

### Copy Output Format

```json
{
  "assessor_type": "venture-capital",
  "target_stage": "seed",
  "must_haves": ["Minimum recurring revenue (MRR/ARR)", "Founder/team sector experience"],
  "custom_criteria": ["Must have at least 2 technical co-founders"],
  "thresholds": "Minimum $200K ARR, burn multiple under 3x, team of 4+",
  "exclusions": "",
  "institutional_context": "Early-stage B2B SaaS fund focused on fintech..."
}
```

- Compact JSON with only non-empty fields
- `thresholds` and `exclusions` are empty strings if user selected "No"
- `custom_criteria` is an empty array if no custom criteria added

### Visual Design Notes

- Sections should be clearly separated with generous vertical spacing (32px between sections)
- Each section wrapped in a subtle card (`bg-slate-800/50 border-slate-700/50 rounded-lg p-6`)
- Section headings: `text-base font-semibold text-slate-200`
- Helper text: `text-sm text-slate-400`
- Smooth transitions on all conditional reveals (200ms ease-out)
- Card grid items should be at least 120px wide with 8px gap
- The form should feel like a professional onboarding flow, not a survey
- Progress bar or step dots at top are NOT needed — the form is single-page scrollable
