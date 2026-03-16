# CP1 Artifact: Context & Assessor Profile Review

## Data Sources

- `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
- `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`

## Artifact Structure

### Header

```
[Company Name]                                    [Funding Stage Badge]
Pre-Assessment · Confirmation Point 1
```

### Tabs

**Tab 1: Company Context**

Render all fields from `context-profile.json` as editable cards:

**Company Identity Card:**
- Company name: inline text edit
- Funding stage: dropdown (`pre-seed`, `seed`, `series-a`, `series-b`, `series-c-plus`, `growth`, `debt`, `venture-debt`, `revenue-based-financing`)
- Vertical: dropdown with common verticals + custom text input
- Sub-vertical: text input
- Commercial model: dropdown (`B2B`, `B2C`, `B2B2C`, `B2G`, `marketplace`, `platform`, `hybrid`)
- Traction status: dropdown (`pre-revenue`, `pre-product`, `revenue-generating`, `profitability-approaching`, `profitable`)

**Revenue Architecture Card:**
- Primary model: text input
- Secondary models: tag-style input (add/remove strings)
- Recurring revenue: toggle switch (boolean)

**Geography Card:**
- Primary market: text input
- Secondary markets: tag-style input
- Assessor geographic frame: text input

**Ask Card:**
- Amount: text input (string, supports ranges)
- Currency: dropdown (USD, EUR, GBP, AED, SAR, etc.)
- Instrument: dropdown (`equity`, `convertible-note`, `SAFE`, `debt`, `venture-debt`, `revenue-based-financing`, `grant`, `mixed`, `unspecified`)
- Use of proceeds: textarea

**Regulatory Exposure Card:**
- Has regulatory exposure: toggle switch
- Regulatory domain active: toggle switch (shown only if exposure = true)
- Applicable frameworks: tag-style input (add/remove: GDPR, HIPAA, FDA, EU MDR, SAMA, SFDA, PCI-DSS, etc.)
- Activation rationale: textarea

**Team Structure Card:**
- Founder count: number input
- Has technical cofounder: toggle
- Team size total: number input
- Key hires identified: toggle

**Tab 2: Assessor Profile**

Render all fields from `assessor-profile.json`:

**Assessor Identity Card:**
- Assessor type: dropdown (`venture-capital`, `angel-investor`, `private-equity`, `credit-debt`, `corporate-strategic`, `family-office`, `sovereign-wealth`, `accelerator`)
- Transaction type: text input
- Institutional context: textarea

**Priorities Card:**
- Primary priorities: rendered as a ranked list
  - Each priority row: priority name (text) + weight modifier (slider, range 0.5–2.0, step 0.1) + rationale (text)
  - Add button to add new priority
  - Remove button (X) on each row

**Non-Negotiables Card:**
- Rendered as a list of criterion cards
  - Each: criterion (text) + domain (text) + consequence if absent (text)
  - Add/remove buttons

**Firm-Specific Standards Card:**
- Rendered as editable table rows
  - Columns: Standard | Applies To | Threshold
  - Add/remove rows

**Tab 3: Confidence Flags**

Render from `context-profile.json.extraction_basis`:

**Extracted from submission** (green section):
- List of field names with green check icon — display only

**Inferred with uncertainty** (amber section):
- Each field shown as an amber card with:
  - Field name + current inferred value
  - "Confirm" button (marks as confirmed) or edit control to correct
  - Extraction notes shown as muted text below

**Missing from submission** (red section):
- List of absent fields with red X icon — display only, informational

## Visual Highlights

- Fields with `extraction_basis.inferred_with_uncertainty` get an amber left-border on their card
- Fields with contradictions between documents get a red info tooltip
- Each editable field shows a small pencil (Edit3) icon; locked fields show Lock icon
- The overall confidence assessment is displayed as a mini stat bar at the top of Tab 3

## Changes Delta Format

```json
[
  { "field": "funding_stage", "original": "seed", "to": "series-a", "context": "context-profile" },
  { "field": "vertical", "original": "SaaS", "to": "FinTech", "context": "context-profile" },
  { "field": "assessor_type", "original": "venture-capital", "to": "private-equity", "context": "assessor-profile" },
  { "field": "priorities[0].weight_modifier", "original": 1.0, "to": 1.5, "context": "assessor-profile" }
]
```
