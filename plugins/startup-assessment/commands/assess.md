---
description: Run full assessment on a pre-assessed submission
allowed-tools: Read, Write, Bash(python3:*), Bash(find:*), Agent, AskUserQuestion
model: sonnet
argument-hint: (no arguments required — reads automatically from workspace folders)
---

## /assess Command: Full Domain Assessment & Reconciliation

### Usage

```
/assess
```

### Overview

The `/assess` command executes the full assessment phase. It automatically reads your pre-assessment findings from the workspace, determines which domains require verification or deep-independent analysis based on pre-assessment scores, orchestrates in-depth domain assessments in waves, reconciles cross-domain conflicts and reinforcing patterns, and produces a final go/no-go determination with integrated findings.

**What you get:** A comprehensive assessment report with domain-by-domain findings, cross-domain risk analysis, and final investment determination—with confirmation checkpoints at scope and reconciliation.

---

### Output Folder Paths

All outputs are written to:

| Output type | Destination |
|---|---|
| HTML, PDF, MD reports | `$WORKSPACE/assessment/assessment/reports/` |
| JSON data files (all) | `$WORKSPACE/assessment/assessment/data/` |

**Base paths** (used throughout this command):
- Reports: `$WORKSPACE/assessment/assessment/reports/`
- Data: `$WORKSPACE/assessment/assessment/data/`

---

### Pre-Flight Checks

**Step 0: Discover workspace root and verify pre-assessment outputs (run first)**

Run the following Python script:

```python
import os, glob, json

mounts = glob.glob('/sessions/*/mnt/*/')
workspace = mounts[0].rstrip('/') if mounts else ''
print(f'WORKSPACE={workspace}')

if not workspace:
    print('ERROR: No workspace found. Please select a folder in Cowork mode.')
else:
    pre_data = os.path.join(workspace, 'assessment', 'pre-assessment', 'data')
    if os.path.isdir(pre_data):
        files = os.listdir(pre_data)
        print(f'Found {len(files)} file(s) in pre-assessment/data:')
        for f in files: print(f'  {f}')
        # Read company name
        cp = os.path.join(pre_data, 'context-profile.json')
        if os.path.exists(cp):
            with open(cp) as fh:
                data = json.load(fh)
            print(f'Company: {data.get("company_name", "unknown")}')
    else:
        print('ERROR: pre-assessment/data not found. Run /pre-assess first.')
```

Use the `WORKSPACE` value above for all file paths. If WORKSPACE is empty or pre-assessment/data is missing, stop and follow the error instructions.

---

**Step 1: Read all required files into context (mandatory — do this before anything else)**

Use the `Read` tool to open and read every file listed below. Do not invoke any agent or processing step until all files are fully loaded into context.

Read these files in order:

1. `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
2. `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
3. `$WORKSPACE/assessment/pre-assessment/data/framework.json`
4. `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json`
5. `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json`
6. `$WORKSPACE/assessment/pre-assessment/data/gap-register.json`
7. `$WORKSPACE/assessment/pre-assessment/data/dependency-map.json`
8. `$WORKSPACE/assessment/pre-assessment/data/module-content-map.json`
9. `$WORKSPACE/assessment/pre-assessment/data/research-log.json`
10. `$WORKSPACE/assessment/pre-assessment/data/preliminary-go-nogo-determination.json`

Also read any `.md` files in `$WORKSPACE/assessment/pre-assessment/reports/` (CP1, CP2, CP3 review files) for audit trail context.

For the original business case documents in `$WORKSPACE/assessment/business-case-docs/`: read MD/DOCX/TXT files directly with the `Read` tool. PDFs are image-based — if their extracted text is not already in `$WORKSPACE/assessment/pre-assessment/data/business-case.md`, re-run OCR extraction (see `/pre-assess` Step 1 for the OCR script).

Confirm in chat: "Loaded [N] pre-assessment files for [Company Name]" before proceeding.

**Determination Gate Check:**
- Pre-assessment determination must be **GO** or **CONDITIONAL GO** to proceed to full assessment
- If determination is **CONDITIONAL HOLD** or **NO-GO:**
  - The gate is explained with reasons
  - You are offered a targeted option: gap-only analysis (deep dive on critical gaps only, skipping other domains)
  - If you decline gap-only analysis: command stops here
  - If you accept: `/assess` continues with gap-focused domain assessments only

---

## Step 1: Scope Determination

Agent: **scope-determinator**
- Input (all read automatically from workspace):
  - `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json`
  - `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json`
  - `$WORKSPACE/assessment/pre-assessment/data/framework.json`
  - `$WORKSPACE/assessment/pre-assessment/data/preliminary-go-nogo-determination.json`
- Determines assessment scope for each domain:
  - **Gap-Focused Mode:** for domains with moderate scores; focuses on gap remediation options
  - **Verification Mode:** for domains with mixed signals; confirms readiness claims and tests edge cases
  - **Deep-Independent Mode:** for domains with low scores or high uncertainty; conducts independent investigation with minimal reliance on submission data
- Sequences domains into assessment waves:
  - Wave 1: foundational domains (Context & Market, Team & Execution) – no dependencies
  - Wave 2: dependent domains (Product & Technology, Financial Projections) – depend on Wave 1 findings
  - Wave 3: synthesis domain (Risk & Dependencies) – depends on all prior waves
- Output: `$WORKSPACE/assessment/assessment/data/assessment-scope-plan.json`
  - domain | pre_assessment_score | assessment_mode | wave | estimated_duration

---

## CONFIRMATION POINT 4: Assessment Scope

**What you see:**
- **Domain Mode Table:** domain name | pre-assessment readiness | pre-assessment fit | assigned mode | wave
- **Sequencing Plan:** which domains assess in parallel (same wave) vs. sequentially
- **Estimated Duration:** rough timeline for full assessment

**Before presenting to the assessor, save a review file:**

Save the full CP4 summary as a formatted markdown file:

```
assessment/assessment/reports/CP4_AssessmentScope_[YYYY-MM-DD].md
```

The file must contain:
- `# CP4 Review — Assessment Scope`
- `## Domain Mode Table` section: all domains as a markdown table with columns: Domain | Pre-Assess Readiness | Pre-Assess Fit | Assigned Mode | Wave
- `## Sequencing Plan` section: which domains run in parallel per wave, as a table (Wave | Domains | Notes)
- `## Estimated Duration` section: rough timeline
- `## What You May Adjust` section: stating that modes may only be escalated, not reduced
- `## Your Escalation Requests` section: blank placeholder for assessor to fill in
- `## Instructions` section explaining how to submit escalations (see below)

Present the summary in chat and provide a download link to the saved file.

**Your instruction to the assessor:**

A review file has been saved to: **`$WORKSPACE/assessment/assessment/reports/CP4_AssessmentScope_[YYYY-MM-DD].md`**

You may escalate assessment modes (gap-focused → verification → deep-independent). You may **NOT** reduce modes.

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "CP4 — Assessment Scope is ready for review. How would you like to proceed?"
- options: ["Edit & re-upload — I'll open the scope file, add my escalation requests, and re-upload it here", "Confirm — The scope looks correct, proceed with domain assessment"]

**What happens:**
- If the assessor selects **Edit & re-upload**: wait for the re-uploaded file, read escalation requests, validate each (only escalations allowed — reject reductions with explanation), apply valid ones to `assessment-scope-plan.json`, and proceed
- If the assessor selects **Confirm**: proceed with no changes
- All changes logged in session audit trail
- Proceed to Step 2

---

## Step 2: Domain Assessment (by wave)

For each wave in the sequencing plan:

**Wave Execution:**
- Invoke **domain-assessor** for each domain in the wave in parallel
- Each domain-assessor invocation receives (all read automatically from workspace):
  - domain_id (e.g., "context-market", "product-technology", etc.)
  - assessment_mode (gap-focused / verification / deep-independent) — from `$WORKSPACE/assessment/assessment/data/assessment-scope-plan.json`
  - `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/module-content-map.json` (filtered to relevant domain)
  - `$WORKSPACE/assessment/pre-assessment/data/research-log.json` (filtered to relevant domain)
  - `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json` (filtered to relevant domain)
  - `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json` (filtered to relevant domain)
  - `$WORKSPACE/assessment/pre-assessment/data/gap-register.json` (filtered to relevant domain)
  - `$WORKSPACE/assessment/business-case-docs/` (all original business case files)

**Domain-Assessor Behavior:**
- Conducts mode-appropriate investigation
- For **gap-focused:** identifies remediation pathways for each gap
- For **verification:** tests readiness claims; conducts independent spot-checks; identifies risks in pre-assessment narratives
- For **deep-independent:** conducts fresh investigation minimally reliant on submission; assembles independent evidence
- Produces `$WORKSPACE/assessment/assessment/data/domain-findings-[domain_id].json` (domain_id | module_scores | strengths | weaknesses | risks | verification_notes | mode_justification)
- Runs domain-level QA/QC; resolves issues or flags for reconciliation

**Wave Completion:**
- Waits for all domains in wave to complete before starting next wave
- Session maintains active status display showing domain completion progress

---

## Step 3: Reconciliation

Agent: **reconciliation-agent**
- Input (all read automatically from workspace):
  - `$WORKSPACE/assessment/assessment/data/domain-findings-[domain_id].json` (all domain files)
  - `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/framework.json`
  - `$WORKSPACE/assessment/pre-assessment/data/preliminary-go-nogo-determination.json`
- Analyzes cross-domain patterns:
  - Identifies conflicts (e.g., strong product differentiation but weak go-to-market capability)
  - Identifies compounding risks (e.g., execution risk + founder concentration + cash burn acceleration)
  - Identifies reinforcing strengths (e.g., founder execution track record + strong team + robust burn metrics)
  - Maps dependencies and causality chains
- Resolves conflicts through logical frameworks (e.g., if two domains disagree, reconciliation-agent determines root cause and adjusts scores)
- Runs scoring logic:
  - Invokes **score_calculator.py** with all domain findings
  - Calculates weighted domain scores
  - Calculates overall readiness and fit-to-purpose
- Runs determination logic:
  - Invokes **go_nogo_determinator.py** with final scores
  - Produces updated go-nogo-determination.json with final determination
- Output: `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
  - Consolidated view of all domain findings, conflicts, compounding risks, reinforcing strengths
  - Cross-domain risk matrix
  - `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
  - determination (GO / CONDITIONAL GO / CONDITIONAL HOLD / NO-GO)
  - determination_rationale
  - changes_from_pre_assessment (if any)

---

## CONFIRMATION POINT 5: Reconciled Findings

**What you see:**
- **Cross-Domain Conflicts:** for each identified conflict, the domain positions and reconciliation logic
- **Top Compounding Risks (up to 5):** ordered by severity; shows how risks interact
- **Top Reinforcing Strengths (up to 5):** ordered by impact; shows why company is well-positioned
- **Domain-by-Domain Summary:** each domain's final findings (readiness, fit, key strengths, key risks)
- **Final Determination vs. Pre-Assessment Determination:** current determination; any changes from pre-assessment with explanations
- **Implementation Path:** if GO or CONDITIONAL GO, brief description of likely investor sequence

**Before presenting to the assessor, save a review file:**

Save the full CP5 summary as a formatted markdown file:

```
assessment/assessment/reports/CP5_ReconciledFindings_[YYYY-MM-DD].md
```

The file must contain:
- `# CP5 Review — Reconciled Findings`
- `## Cross-Domain Conflicts` section: each conflict with domain positions and reconciliation logic
- `## Top Compounding Risks` section: up to 5 risks ordered by severity, showing interaction effects
- `## Top Reinforcing Strengths` section: up to 5 strengths ordered by impact
- `## Domain-by-Domain Summary` section: table with columns Domain | Readiness | Fit | Key Strengths | Key Risks
- `## Final Determination` section: determination label, rationale, and any changes from pre-assessment
- `## Implementation Path` section: if GO or CONDITIONAL GO, likely investor sequence
- `## Your Overrides & Notes` section: blank placeholder for assessor to fill in

Present the summary in chat and provide a download link to the saved file.

**Your instruction to the assessor:**

A review file has been saved to: **`$WORKSPACE/assessment/assessment/reports/CP5_ReconciledFindings_[YYYY-MM-DD].md`**

You may provide overrides or additional context — these are documented in the audit trail but **will not change scores already calculated.**

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "CP5 — Reconciled Findings are ready for review. How would you like to proceed?"
- options: ["Edit & re-upload — I'll open the review file, add my overrides or notes, and re-upload it here", "Confirm — Lock findings and generate final assessment outputs"]

**What happens:**
- If the assessor selects **Edit & re-upload**: wait for the re-uploaded file, read override notes from `## Your Overrides & Notes`, apply each to the session audit trail with timestamp, and proceed
- If the assessor selects **Confirm**: proceed with no overrides
- Session audit trail sealed at this point
- Proceed to Step 4

---

## Step 4: Output Generation

Agent: **assess-output-agent**
- Input (all read automatically from workspace):
  - `$WORKSPACE/assessment/assessment/data/domain-findings-[domain_id].json` (all domain files)
  - `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
  - `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
  - `$WORKSPACE/assessment/assessment/data/assessment-scope-plan.json`
  - `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/framework.json`
  - Session audit trail
- Generates 3 deliverable outputs (all saved to `$WORKSPACE/assessment/assessment/reports/`):

1. **[CompanyName]_Assessment_[YYYY-MM-DD].html**
   - Comprehensive assessment report with all domain findings
   - Cross-domain analysis section
   - Conflict resolution narratives
   - Final determination and rationale
   - Interactive visualizations (domain radar charts, risk matrices, etc.)

2. **[CompanyName]_Assessment_[YYYY-MM-DD].pdf**
   - Agent generates printable HTML version; you can print to PDF via your browser
   - Complete assessment document ready for investment committee or partners

3. **[CompanyName]_Assessment_[YYYY-MM-DD].md**
   - Structured markdown data file with all assessment findings, registers, and determination
   - Used as input to `/sensitivity` command in next phase
   - Preserves all JSON registers and session audit trail

---

## Completion

All three outputs are displayed with download links. Final determination is displayed prominently.

**Output locations:**
```
assessment/assessment/
├── reports/
│   ├── CP4_AssessmentScope_[YYYY-MM-DD].md
│   ├── CP5_ReconciledFindings_[YYYY-MM-DD].md
│   ├── [CompanyName]_Assessment_[YYYY-MM-DD].html
│   ├── [CompanyName]_Assessment_[YYYY-MM-DD].pdf
│   └── [CompanyName]_Assessment_[YYYY-MM-DD].md
└── data/
    ├── assessment-scope-plan.json
    ├── domain-findings-[domain_id].json (one per domain)
    ├── integrated-findings-register.json
    └── updated-go-nogo-determination.json
```

**Next step:** Run `/sensitivity` — no file upload required. It will read from `$WORKSPACE/assessment/assessment/` automatically.
