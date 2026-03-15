# Assessor Profile Collector Artifact

## Purpose

Adaptive interactive artifact that collects assessor profile inputs. The form **dynamically reconfigures** based on the selected assessor type — a VC sees different questions than a credit lender or a corporate strategic buyer. This follows the fit-to-purpose principle: each assessor type poses its own set of relevant questions.

## Data Sources

- No pre-existing data — this is a collection artifact, not a review artifact
- Schema reference: `schemas/assessor-profile.json`
- Priority hierarchy reference: `agents/criteria-resolver.md` (Priority Domain Hierarchy by Assessor Type)

## Artifact Structure

### Header

```
Startup Assessment                                          [Setup]
Assessor Profile · Investment Criteria Collection

Tell us about your investment mandate so we can calibrate the assessment.
```

- Subtitle text in `text-slate-400`, providing context
- No determination badge (profile hasn't been created yet)

### Main Content — Adaptive Profile Form

The form has two phases:

1. **Phase 1 (always visible):** Assessor type selection — a single selector card grid
2. **Phase 2 (appears after type selected):** Type-specific sections animate in, tailored to the selected assessor type

When the assessor changes their type selection, Phase 2 sections smoothly transition out, reset, and re-render with the new type's sections (300ms crossfade).

---

### Phase 1: Assessor Type (Always Visible)

```
┌────────────────────────────────────────────────────────────────────┐
│ What best describes your role?                                     │
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
- **Values:** `venture-capital`, `angel-investor`, `private-equity`, `credit-debt`, `corporate-strategic`, `family-office`, `sovereign-wealth`, `accelerator`, `other`
- If "Other" selected, show a text input: "Please describe your assessor role:"
- **On selection:** Phase 2 sections animate in below (slide-down + fade, 300ms)

---

### Phase 2: Type-Specific Sections

Each assessor type renders a **different set of sections** below the type selector. Sections are defined per type in the configuration table below. The form only shows sections relevant to the selected type.

#### Section Registry

Each section is a reusable component. The type configuration determines which sections appear, in what order, with what label/placeholder overrides.

| Section ID | Component | Description |
|------------|-----------|-------------|
| `stage` | Card grid (single-select) | Target funding stage |
| `transaction` | Card grid (single-select) | Transaction type |
| `deal-structure` | Card grid (single-select) | Deal structure preference |
| `thesis` | Textarea | Investment/lending thesis |
| `must-haves` | Checkbox list + custom add | Non-negotiable criteria |
| `financial-thresholds` | Structured inputs | Quantitative financial requirements |
| `team-requirements` | Checkbox list + custom add | Team composition requirements |
| `strategic-fit` | Textarea + checkbox tags | Strategic alignment criteria |
| `risk-tolerance` | Slider + checkboxes | Risk appetite and limits |
| `timeline` | Card grid (single-select) | Expected hold period / exit timeline |
| `geographic` | Multi-select tags + textarea | Geographic focus/exclusions |
| `sector` | Multi-select tags + textarea | Sector focus/exclusions |
| `portfolio-context` | Textarea | Fund/portfolio context |

---

### Type Configurations

#### Venture Capital

Sections (in order):
1. **`stage`** — "What stage do you typically invest?"
   - Options: `Pre-Seed`, `Seed`, `Series A`, `Series B+`, `Growth Stage`
2. **`thesis`** — "Describe your investment thesis"
   - Placeholder: "e.g., We invest in B2B SaaS companies with strong founder-market fit, targeting $1-3M initial checks at Seed..."
3. **`must-haves`** — "What are your deal-breakers?"
   - Pre-populated options: `Strong technical founder`, `Product-market fit signals`, `Minimum MRR/ARR`, `Defensible moat or IP`, `Large addressable market (>$1B TAM)`, `Capital-efficient growth`, `None — I evaluate holistically`
   - Custom add enabled
4. **`financial-thresholds`** — "Financial requirements"
   - Fields: Min ARR/MRR (text input), Max burn multiple (dropdown: 1x/2x/3x/5x/No limit), Min runway (dropdown: 6mo/12mo/18mo/24mo), Check size range (two text inputs: min-max)
5. **`sector`** — "Sector focus"
   - Tags: `SaaS`, `Fintech`, `Healthtech`, `AI/ML`, `Climate`, `Consumer`, `Enterprise`, `Marketplace`, `Hardware`, `Biotech`, `Crypto/Web3`
   - Textarea: "Exclusions (if any):"
6. **`geographic`** — "Geographic preferences"
   - Tags: `US only`, `US + Canada`, `North America`, `Europe`, `MENA`, `APAC`, `LATAM`, `Global — no restriction`
7. **`portfolio-context`** — "Fund context (optional)"
   - Placeholder: "e.g., $50M Fund III, 30 portfolio companies, focused on capital-efficient seed-stage B2B..."

#### Angel Investor

Sections (in order):
1. **`stage`** — "What stage do you invest at?"
   - Options: `Pre-Seed`, `Seed`, `Series A`
2. **`thesis`** — "What do you look for in a deal?"
   - Placeholder: "e.g., I invest in founders I know personally, typically in fintech or healthcare. $25-100K checks..."
3. **`must-haves`** — "What are your deal-breakers?"
   - Pre-populated options: `Founder I know or was referred`, `Domain expertise in team`, `Working product or prototype`, `Some traction or revenue`, `Co-investors or lead investor attached`, `None — I evaluate case by case`
   - Custom add enabled
4. **`financial-thresholds`** — "Financial parameters"
   - Fields: Check size range (two text inputs), Valuation cap preference (text input), Instrument preference (dropdown: SAFE/Convertible Note/Equity/Flexible)
5. **`sector`** — "Sectors of interest"
   - Same tags as VC
   - Textarea: "Exclusions:"
6. **`geographic`** — "Geographic preferences"
   - Same tags as VC

#### Private Equity

Sections (in order):
1. **`stage`** — "Target company maturity"
   - Options: `Growth Stage`, `Established / Profitable`, `Buyout`, `Carve-out`, `Restructuring / Turnaround`
2. **`transaction`** — "Transaction type"
   - Options: `Majority Acquisition`, `Minority Growth Equity`, `Leveraged Buyout`, `Management Buyout`, `Platform / Add-on`, `Recapitalization`
3. **`must-haves`** — "Investment criteria"
   - Pre-populated: `Minimum EBITDA threshold`, `Positive cash flow`, `Proven management team`, `Market leadership position`, `Recurring revenue base`, `Clear value creation levers`, `Defined exit pathway`
   - Custom add enabled
4. **`financial-thresholds`** — "Financial requirements"
   - Fields: Min revenue ($M text input), Min EBITDA ($M text input), EBITDA margin floor (% dropdown), Max leverage ratio (dropdown: 2x/3x/4x/5x/6x), Target IRR (% text input), Hold period (dropdown: 3-5yr/5-7yr/7-10yr)
5. **`risk-tolerance`** — "Risk parameters"
   - Slider: Risk appetite (Conservative — Moderate — Aggressive)
   - Checkboxes: `Turnaround situations OK`, `Customer concentration OK if mitigated`, `Cyclical industries OK`, `Regulatory-heavy sectors OK`
6. **`sector`** — "Sector focus"
   - Tags: `Manufacturing`, `Business Services`, `Healthcare Services`, `Technology`, `Financial Services`, `Consumer`, `Industrial`, `Distribution`, `Food & Beverage`
   - Textarea: "Exclusions:"
7. **`geographic`** — "Geographic focus"
   - Same tags structure
8. **`portfolio-context`** — "Fund context (optional)"
   - Placeholder: "e.g., $500M Fund V, mid-market buyout focus, 10-15 platform companies per fund..."

#### Credit / Debt

Sections (in order):
1. **`transaction`** — "Facility type"
   - Options: `Venture Debt`, `Revenue-Based Financing`, `Term Loan`, `Asset-Based Lending`, `Convertible Debt`, `Mezzanine / Subordinated`, `Working Capital Line`
2. **`must-haves`** — "Underwriting requirements"
   - Pre-populated: `Minimum revenue run-rate`, `Positive gross margin`, `Minimum runway post-draw`, `Personal guarantee or collateral`, `Financial covenants compliance`, `Monthly financial reporting`, `Board observation rights`, `Senior lien position`
   - Custom add enabled
3. **`financial-thresholds`** — "Credit parameters"
   - Fields: Min annual revenue ($M text input), Min months of revenue history (dropdown: 6/12/18/24), Interest coverage ratio floor (text input), Debt service coverage ratio floor (text input), Max loan-to-value (% dropdown), Facility size range ($M two text inputs), Interest rate range (% two text inputs)
4. **`risk-tolerance`** — "Risk parameters"
   - Slider: Risk appetite (Conservative — Moderate — Aggressive)
   - Checkboxes: `Pre-revenue companies OK`, `Negative EBITDA OK if growth trajectory strong`, `Customer concentration >30% OK`, `Cyclical revenue OK`
5. **`sector`** — "Sector focus"
   - Tags: `SaaS`, `Technology`, `Healthcare`, `Financial Services`, `E-commerce`, `Manufacturing`, `Professional Services`
   - Textarea: "Sector exclusions:"
6. **`geographic`** — "Geographic requirements"
   - Same tags structure
   - Additional checkbox: `Jurisdiction-specific requirements (describe below)`

#### Corporate Strategic

Sections (in order):
1. **`transaction`** — "Transaction type"
   - Options: `Strategic Acquisition`, `Strategic Investment (minority)`, `Joint Venture`, `Licensing / Partnership`, `Acqui-hire`, `Technology Acquisition`
2. **`strategic-fit`** — "Strategic alignment"
   - Textarea: "Describe what you're looking for and how it fits your strategic goals"
   - Placeholder: "e.g., Looking for AI/ML capabilities to integrate into our enterprise product suite. Must complement our existing customer base of 500+ enterprise accounts..."
   - Checkbox tags: `Product synergy`, `Customer base access`, `Geographic expansion`, `Technology/IP acquisition`, `Talent acquisition`, `Competitive positioning`, `New market entry`
3. **`must-haves`** — "Requirements"
   - Pre-populated: `Technology compatible with our stack`, `Culture fit with parent organization`, `Key personnel retention commitment`, `Clean IP ownership`, `No competing partnerships`, `Regulatory alignment with parent`
   - Custom add enabled
4. **`financial-thresholds`** — "Financial parameters"
   - Fields: Budget range ($M two text inputs), Revenue contribution target ($M text input), Integration timeline (dropdown: 6mo/12mo/18mo/24mo), Earn-out acceptable (Yes/No radio)
5. **`risk-tolerance`** — "Integration risk tolerance"
   - Slider: Integration complexity appetite (Low — Medium — High)
   - Checkboxes: `Pre-revenue targets OK`, `Cross-border OK`, `Earn-out / milestone structures OK`, `Regulatory approval delays acceptable`
6. **`timeline`** — "Decision timeline"
   - Options: `Urgent (<3 months)`, `Near-term (3-6 months)`, `Standard (6-12 months)`, `Exploratory (no timeline)`

#### Family Office

Sections (in order):
1. **`stage`** — "What stage interests you?"
   - Options: `Pre-Seed / Seed`, `Series A-B`, `Growth Stage`, `Established / Profitable`, `Diversified (multiple stages)`
2. **`deal-structure`** — "Preferred deal structure"
   - Options: `Direct equity investment`, `Co-invest alongside lead`, `Fund LP commitment`, `Structured / hybrid`, `Flexible — depends on opportunity`
3. **`thesis`** — "Investment philosophy"
   - Placeholder: "e.g., Preservation of capital with selective growth exposure. Prefer companies with clear path to profitability and alignment with family values..."
4. **`must-haves`** — "Requirements"
   - Pre-populated: `Capital preservation priority`, `Regular distributions / dividends`, `Board seat or governance rights`, `Co-investment alongside institutional lead`, `ESG / values alignment`, `Founder relationship and trust`, `None — flexible approach`
   - Custom add enabled
5. **`financial-thresholds`** — "Financial parameters"
   - Fields: Check size range ($M two text inputs), Target return profile (dropdown: Capital preservation/Moderate growth/High growth/Venture-like), Liquidity preference (dropdown: Quarterly distributions/Annual/At exit/Flexible)
6. **`sector`** — "Sector preferences"
   - Same tags structure as VC plus: `Real Estate`, `Agriculture`, `Impact / ESG`
   - Textarea: "Exclusions (values-based or otherwise):"
7. **`geographic`** — "Geographic preferences"
   - Same tags structure
8. **`portfolio-context`** — "Family office context (optional)"
   - Placeholder: "e.g., Single-family office, $200M AUM, 15% allocated to direct investments. Generational focus with 10+ year horizons..."

#### Sovereign Wealth

Sections (in order):
1. **`stage`** — "Target maturity"
   - Options: `Growth Stage`, `Late Stage`, `Pre-IPO`, `Established / Public`, `Infrastructure / Platform`
2. **`transaction`** — "Investment approach"
   - Options: `Direct Investment`, `Co-Investment`, `Fund Commitment`, `Strategic Partnership`, `Public Market Position`
3. **`strategic-fit`** — "Strategic mandate"
   - Textarea: "Describe your fund's strategic mandate and national priorities"
   - Placeholder: "e.g., Technology transfer and job creation in domestic market. Focus on AI, renewable energy, and fintech infrastructure..."
   - Checkbox tags: `Technology transfer`, `Job creation`, `National priority sector`, `Domestic market development`, `Export capability`, `Knowledge economy`, `Sustainability / ESG`
4. **`must-haves`** — "Mandate requirements"
   - Pre-populated: `Governance and transparency standards`, `ESG compliance`, `Domestic economic impact`, `Minimum investment size`, `Co-investment partner required`, `Government approval pathway clear`
   - Custom add enabled
5. **`financial-thresholds`** — "Financial parameters"
   - Fields: Min investment size ($M text input), Target return (% text input), Min company valuation ($M text input), Acceptable ownership range (% two inputs)
6. **`geographic`** — "Geographic mandate"
   - Same tags structure
   - Additional textarea: "Domestic content requirements:"
7. **`timeline`** — "Investment horizon"
   - Options: `3-5 years`, `5-10 years`, `10+ years`, `Perpetual / no fixed horizon`

#### Accelerator

Sections (in order):
1. **`stage`** — "Cohort stage focus"
   - Options: `Idea Stage`, `Pre-Seed`, `Seed`, `Post-Seed / Series A prep`
2. **`thesis`** — "Program thesis"
   - Placeholder: "e.g., Industry-specific accelerator focused on climate tech. 12-week program, $150K investment for 7% equity. Looking for technically strong founders with validated problem..."
3. **`must-haves`** — "Selection criteria"
   - Pre-populated: `Full-time committed founders`, `Technical co-founder`, `Validated problem (customer discovery done)`, `Working prototype or MVP`, `Coachability and openness to feedback`, `Relevant domain expertise`, `Diverse founding team`
   - Custom add enabled
4. **`financial-thresholds`** — "Program terms"
   - Fields: Standard investment amount (text input), Equity taken (% text input), Program duration (dropdown: 6wk/8wk/12wk/16wk/6mo), Cohort size (text input)
5. **`sector`** — "Vertical focus"
   - Same tags structure
   - Textarea: "Verticals NOT accepted:"
6. **`geographic`** — "Geographic scope"
   - Same tags structure
   - Additional checkbox: `Relocation to program city required`

#### Other

Sections (in order):
1. **`thesis`** — "Describe your assessment context"
   - Placeholder: "Describe your role, what you're evaluating, and what matters most to your decision..."
2. **`must-haves`** — "Key requirements"
   - Pre-populated: `Custom criteria only — use the add button below`
   - Custom add enabled (primary interaction)
3. **`financial-thresholds`** — "Financial parameters (if applicable)"
   - Single textarea: "Describe any quantitative requirements or thresholds..."
4. **`sector`** — "Sector focus (if applicable)"
   - Same tags structure
5. **`geographic`** — "Geographic scope (if applicable)"
   - Same tags structure

---

### Shared Section Component Specs

#### `stage` — Card Grid (single-select)

Same card states as Phase 1. Options vary by type (see above). If "Other" appears as an option, show text input on selection.

#### `transaction` / `deal-structure` — Card Grid (single-select)

Same component as `stage`. Different label, options per type.

#### `thesis` / `portfolio-context` — Textarea

- `bg-slate-800 border-slate-700 rounded-lg`
- 4 rows, auto-expand to content
- Placeholder varies by type (see above)
- Character count shown subtly in bottom-right: `text-xs text-slate-500`

#### `must-haves` — Checkbox List + Custom Add

- Checkboxes with type-specific pre-populated options
- **Checkbox states:**
  - Unchecked: `border-slate-600` empty box
  - Checked: `bg-indigo-500 border-indigo-500` with checkmark
- Selecting "None" / "Evaluate holistically" clears all others (and vice versa)
- **+ Add custom criterion:** click reveals text input + "Add" button; custom items appear as chips above the list with × remove button
- Custom criteria chips: `bg-slate-700 border-slate-600 text-slate-200`

#### `financial-thresholds` — Structured Inputs

Type-specific field set (see type configurations above). Layout:
- Fields arranged in a responsive 2-column grid
- Each field: label (`text-sm text-slate-400`), input (`bg-slate-800 border-slate-700`)
- Dropdowns use same style as other selectors
- Text inputs have type-appropriate placeholders

#### `strategic-fit` — Textarea + Checkbox Tags

- Textarea (same as `thesis` component)
- Below textarea: row of selectable tag chips
- Tag states: unselected (`bg-slate-800 border-slate-700`), selected (`bg-indigo-500/20 border-indigo-500/50`)

#### `risk-tolerance` — Slider + Checkboxes

- Slider: track `bg-slate-700`, filled portion `bg-indigo-500`, thumb `bg-white`
- 3 labeled stops: Conservative — Moderate — Aggressive
- Below slider: checkbox list with type-specific risk acceptance options

#### `timeline` — Card Grid (single-select)

Same component as `stage`. Options vary by type.

#### `geographic` — Multi-select Tags + Textarea

- Tag chips in a wrapping row (multi-select)
- Tag states: same as `strategic-fit` tags
- Optional textarea below for additional detail
- Any additional checkboxes per type shown below tags

#### `sector` — Multi-select Tags + Textarea

- Same component pattern as `geographic`
- Type-specific tag options
- "Exclusions" textarea below

---

### Form State Management

```jsx
const [assessorType, setAssessorType] = useState(null);
const [sectionData, setSectionData] = useState({});

// When assessor type changes, reset section data
useEffect(() => {
  setSectionData({});
}, [assessorType]);

// Get sections for current type
const getSections = (type) => TYPE_CONFIGS[type]?.sections || [];

// Update a section's data
const updateSection = (sectionId, data) => {
  setSectionData(prev => ({ ...prev, [sectionId]: data }));
};
```

### Validation

Validation rules are type-specific. Each type configuration defines which sections are required vs optional.

**Universal required:**
- `assessor_type` must be selected

**Per-type required sections** (marked with `*` in type configs above):
- All types: first section after type (stage or transaction) is required
- `must-haves` is always required (at minimum, select "None" / holistic)
- `thesis` / `strategic-fit` is required when present

**Optional sections:**
- `portfolio-context` is always optional
- `geographic` is optional (defaults to "Global — no restriction")
- `sector` is optional (defaults to "All sectors")

Show validation:
- Incomplete required sections: section header has amber dot
- Complete sections: section header has green check
- Footer Copy button disabled until all required sections valid

### Footer

```
┌────────────────────────────────────────────────────────────────────┐
│  ✓ N of M sections complete                     [Copy to Clipboard]│
└────────────────────────────────────────────────────────────────────┘
```

- M = total sections for selected type
- N = completed sections
- Amber while incomplete, green when all required fields are done
- Copy disabled until valid

### Copy Output Format

The output JSON includes the assessor type and all section data, structured for the criteria-resolver agent:

```json
{
  "assessor_type": "venture-capital",
  "sections": {
    "stage": "seed",
    "thesis": "We invest in B2B SaaS companies with strong founder-market fit...",
    "must_haves": ["Strong technical founder", "Minimum MRR/ARR", "Large addressable market"],
    "custom_criteria": ["Must have at least 2 technical co-founders"],
    "financial_thresholds": {
      "min_arr": "$200K",
      "max_burn_multiple": "3x",
      "min_runway": "18mo",
      "check_size_min": "$500K",
      "check_size_max": "$2M"
    },
    "sector_focus": ["SaaS", "Fintech", "AI/ML"],
    "sector_exclusions": "No crypto or cannabis",
    "geographic": ["US only"],
    "portfolio_context": "..."
  }
}
```

- Only includes sections that have data (empty/skipped optional sections omitted)
- `financial_thresholds` is a flat object with field keys matching the input labels
- Multi-select fields are arrays; text fields are strings

### Visual Design Notes

- Phase 1 (type selector) always visible at top; Phase 2 scrolls below
- When type is selected, Phase 2 animates in with slide-down + fade (300ms ease-out)
- If type changes, Phase 2 crossfades to new sections (old fade-out 150ms, new fade-in 150ms)
- Each section wrapped in a subtle card (`bg-slate-800/50 border-slate-700/50 rounded-lg p-6`)
- Section headings: `text-base font-semibold text-slate-200`
- Helper text: `text-sm text-slate-400`
- Generous vertical spacing (24px between sections)
- The form should feel like a professional onboarding flow tailored to the assessor's world
- Sticky footer at bottom of viewport
