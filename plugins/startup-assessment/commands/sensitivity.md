---
description: Run sensitivity analysis on a completed assessment
allowed-tools: Read, Write, Bash(python3:*), Bash(find:*), Agent
model: sonnet
argument-hint: (no arguments required — reads automatically from workspace folders)
---

## /sensitivity Command: Scenario Analysis & Path Qualification

### Usage

```
/sensitivity
```

### Overview

The `/sensitivity` command executes sensitivity analysis on your completed assessment. It automatically reads your assessment findings from the workspace, identifies key value drivers and risk factors, models how changes in assumptions affect your investment thesis, and determines whether you qualify for Path B (alternative investment structures). You'll choose from methodology options tailored to your determination.

**What you get:** Sensitivity analysis report showing scenario impacts, robustness classification, and Path B eligibility—with clear explanation of what Path B means for your next steps.

---

### Output Folder Paths

All outputs are written to:

| Output type | Destination |
|---|---|
| HTML, PDF, MD reports | `$WORKSPACE/assessment/sensitivity/reports/` |
| JSON data files (all) | `$WORKSPACE/assessment/sensitivity/data/` |

**Base paths** (used throughout this command):
- Reports: `$WORKSPACE/assessment/sensitivity/reports/`
- Data: `$WORKSPACE/assessment/sensitivity/data/`

---

### Pre-Flight Checks

**Step 0: Discover workspace root and verify assessment outputs (run first)**

Run the following Python script:

```python
import os, glob, json

mounts = glob.glob('/sessions/*/mnt/*/')
workspace = mounts[0].rstrip('/') if mounts else ''
print(f'WORKSPACE={workspace}')

if not workspace:
    print('ERROR: No workspace found. Please select a folder in Cowork mode.')
else:
    assess_data = os.path.join(workspace, 'assessment', 'assessment', 'data')
    if os.path.isdir(assess_data):
        files = os.listdir(assess_data)
        print(f'Found {len(files)} file(s) in assessment/data:')
        for f in files: print(f'  {f}')
        cp = os.path.join(workspace, 'assessment', 'pre-assessment', 'data', 'context-profile.json')
        if os.path.exists(cp):
            with open(cp) as fh:
                data = json.load(fh)
            print(f'Company: {data.get("company_name", "unknown")}')
    else:
        print('ERROR: assessment/data not found. Run /assess first.')
```

Use the `WORKSPACE` value above for all file paths. If WORKSPACE is empty or assessment/data is missing, stop and follow the error instructions.

---

**Step 1: Read all required files into context (mandatory — do this before anything else)**

Use the `Read` tool to open and read every file listed below. Do not invoke the sensitivity-agent until all files are fully loaded into context.

Read these files in order:

1. `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
2. `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
3. `$WORKSPACE/assessment/pre-assessment/data/framework.json`
4. `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
5. `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
6. `$WORKSPACE/assessment/assessment/data/assessment-scope-plan.json`
7. All `$WORKSPACE/assessment/assessment/data/domain-findings-*.json` files — use the `Read` tool on each one found

Also read any CP4 and CP5 review files in `$WORKSPACE/assessment/assessment/reports/` for audit trail context.

Confirm in chat: "Loaded assessment data for [Company Name] — determination: [GO/CONDITIONAL GO/etc.]" before proceeding.

---

## Step 1: Sensitivity Analysis

Agent: **sensitivity-agent**
- Input (all read automatically from workspace):
  - `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
  - `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
  - `$WORKSPACE/assessment/assessment/data/domain-findings-[domain_id].json` (all domain files)
  - `$WORKSPACE/assessment/pre-assessment/data/framework.json`
  - `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
- First: presents methodology options to you based on your determination:

**If determination is GO:**
- **Option A: Robustness Testing**
  - Stress-tests your financial assumptions (CAC, LTV, burn rate, revenue growth)
  - Modifies key operating parameters to identify failure modes
  - Scenario modeling: base case, upside case (2x revenue growth), downside case (50% revenue growth)
  - Output: robustness classification (Robust / Moderately Robust / Fragile)
  - Path B Eligibility: All GO companies qualify for Path B

**If determination is CONDITIONAL GO:**
- **Option A: Condition Sensitivity**
  - Tests whether conditions are achievable with reasonable effort
  - Models timeline to condition resolution
  - Evaluates impact of condition resolution on overall thesis
  - Output: condition attainability assessment (achievable / unclear / at-risk)
  - Path B Eligibility: Depends on condition attainability; strong Path B candidates if all conditions deemed achievable

- **Option B: Alternative Structure Simulation**
  - Explores alternative deal structures that might address conditional requirements
  - Models tranched investment, earnout conditions, or governance provisions
  - Output: structure optionality assessment
  - Path B Eligibility: Determines if alternative structure addresses conditions

**If determination is CONDITIONAL HOLD or NO-GO:**
- **Option A: Gap Closure Feasibility**
  - Models timeline and effort required to close critical gaps
  - Identifies which gaps are closeable vs. fundamental
  - Evaluates impact of gap closure on overall determination
  - Output: gap closure feasibility assessment
  - Path B Eligibility: Eligible only if critical gaps deemed closeable within reasonable timeframe

- **Option B: Pivot Sensitivity**
  - Models how pivot(s) to alternative market(s), product focus, or go-to-market strategy would affect assessment
  - Output: revised thesis under pivot scenarios
  - Path B Eligibility: Depends on pivot viability

**You select methodology:**
- sensitivity-agent displays the applicable options
- You choose which option(s) to model
- sensitivity-agent executes your selection

**Sensitivity-agent execution:**
- Runs scenario modeling and assumption stress-testing
- Identifies key value drivers (assumptions that most affect outcome)
- Identifies key risk factors (variables that create most downside)
- Calculates sensitivity coefficients (how much 10% change in each assumption affects valuation / determination)
- Produces robustness classification and Path B eligibility determination
- Output: `$WORKSPACE/assessment/sensitivity/data/sensitivity-results.json`
  - key_value_drivers (ranked by impact)
  - key_risk_factors (ranked by downside magnitude)
  - scenario_modeling_results (base / upside / downside outcomes)
  - sensitivity_coefficients (assumption → impact)
  - robustness_classification
  - path_b_eligibility (eligible / ineligible)
  - path_b_explanation (why eligible or not)

---

## Step 2: Output Generation

Agent: **sensitivity-output-agent**
- Input (all read automatically from workspace):
  - `$WORKSPACE/assessment/sensitivity/data/sensitivity-results.json`
  - `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
  - `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
  - `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
- Generates 3 deliverable outputs (all saved to `$WORKSPACE/assessment/sensitivity/reports/`):

1. **[CompanyName]_Sensitivity_[YYYY-MM-DD].html**
   - Sensitivity analysis report with scenario tables
   - Key value driver and key risk factor visualizations
   - Sensitivity coefficient matrices
   - Path B eligibility and explanation
   - Interactive scenario explorer (adjust assumptions to see impact)

2. **[CompanyName]_Sensitivity_[YYYY-MM-DD].pdf**
   - Agent generates printable HTML version; you can print to PDF via your browser
   - Ready for board or partnership sharing

3. **[CompanyName]_Sensitivity_[YYYY-MM-DD].md**
   - Structured markdown data file with all sensitivity results and Path B eligibility
   - Used as input to `/recommend` command in next phase
   - Preserves all JSON sensitivity registers

---

## Completion

All three outputs are displayed with download links.

**Output locations:**
```
assessment/sensitivity/
├── reports/
│   ├── [CompanyName]_Sensitivity_[YYYY-MM-DD].html
│   ├── [CompanyName]_Sensitivity_[YYYY-MM-DD].pdf
│   └── [CompanyName]_Sensitivity_[YYYY-MM-DD].md
└── data/
    └── sensitivity-results.json
```

**Path B Availability – Prominently Displayed:**

If **Path B Eligible:**
> **You qualify for Path B.** Path B represents an alternative investment approach tailored to your company's profile. It may include:
> - Structured investment (tranched entry, earnout conditions)
> - Governance or operational requirements tied to milestones
> - Non-dilutive funding alternatives or strategic partnerships
> - Extended timeline or alternative valuation approaches
>
> To explore Path B options, proceed to the next step.

If **Path B Not Eligible:**
> **You do not currently qualify for Path B.** You may:
> - Proceed with Path A recommendations (standard investment approach)
> - Close specific gaps identified in your assessment, then re-run sensitivity analysis
> - Pivot your business model or market focus and restart the assessment

**Next step:** Run `/recommend` — no file upload required. It will read from `$WORKSPACE/assessment/assessment/` and `$WORKSPACE/assessment/sensitivity/` automatically.
