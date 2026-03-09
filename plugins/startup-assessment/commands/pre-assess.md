---
description: Run pre-assessment on a startup business case document
allowed-tools: Read, Write, Bash(python3:*), Bash(find:*), Agent
model: sonnet
argument-hint: (no arguments required — reads from assessment/business-case-docs/)
---

## /pre-assess Command: Initial Readiness & Fit Assessment

### Usage

```
/pre-assess
```

### Overview

The `/pre-assess` command executes the initial assessment phase. It reads your business case, extracts critical context, builds a dynamic assessment framework tuned to your investor profile, conducts research, scores your readiness across five assessment domains, and produces preliminary go/no-go guidance with detailed gap analysis.

**What you get:** A comprehensive pre-assessment report with scored findings, gap registers, and dependency maps—plus confirmation checkpoints at three critical moments so you can verify accuracy before moving deeper analysis.

---

### Output Folder Paths

All outputs are written to the workspace folder created by `/initiate`:

| Output type | Destination |
|---|---|
| HTML, PDF, MD reports | `$WORKSPACE/assessment/pre-assessment/reports/` |
| JSON data files (all) | `$WORKSPACE/assessment/pre-assessment/data/` |

**Base paths** (used throughout this command — `$WORKSPACE` is resolved in Pre-Flight Step 0):
- Reports: `$WORKSPACE/assessment/pre-assessment/reports/`
- Data: `$WORKSPACE/assessment/pre-assessment/data/`

---

### Global File Format Standard

**This standard governs all agents in the `/pre-assess` workflow.**

All user-readable files written during this workflow MUST be saved as `.md` — never `.txt` or any other plain-text format. This applies to every agent that saves extracted, synthesised, or narrative content.

| File type | Format required | Notes |
|---|---|---|
| Extracted document content | `.md` | Must mirror source structure: headings, subheadings, bullet points, tables, lists. |
| Charts / infographics | Converted to markdown tables | Each table must be followed by an italicised footnote: `*[Original format: <chart-type> — <description>]*` |
| Agent summaries / narratives | `.md` | Use proper heading hierarchy; no flat plain text blocks. |
| Machine-readable data | `.json` | JSON data files are exempt — keep as `.json`. |
| Final reports | `.html`, `.pdf`, `.md` | As specified in the output generation steps below. |

If any agent produces a `.txt` file at any point, that is a bug — the responsible agent must re-save its output as a correctly structured `.md` file before the workflow continues.

---

### Pre-Flight Checks

**Step 0: Discover workspace root and verify business-case-docs (run first)**

Run the following Python script. It discovers the absolute workspace path and lists all files in business-case-docs:

```python
import os, glob

mounts = glob.glob('/sessions/*/mnt/*/')
workspace = mounts[0].rstrip('/') if mounts else ''
print(f'WORKSPACE={workspace}')

if not workspace:
    print('ERROR: No workspace found. Please select a folder in Cowork mode.')
else:
    docs = os.path.join(workspace, 'assessment', 'business-case-docs')
    if os.path.isdir(docs):
        files = os.listdir(docs)
        print(f'Found {len(files)} file(s) in business-case-docs:')
        for f in files: print(f'  {f}')
    else:
        print('ERROR: business-case-docs folder not found. Run /initiate first.')
```

Use the `WORKSPACE` value printed above for all subsequent file paths in this command. If WORKSPACE is empty or business-case-docs is missing, stop and follow the error instructions above.

---

**Step 1: Read all business case documents into context (mandatory — do this before anything else)**

Navigate to `$WORKSPACE/assessment/business-case-docs/` and read every file found there. Do not proceed to any agent or processing step until all documents are fully loaded into context.

For each file in `$WORKSPACE/assessment/business-case-docs/`:

- **PDF files:** PDFs in this folder are typically image-based (scanned). Run OCR extraction using the following Python script, then read the extracted text:

```python
import os, glob, pytesseract
from pdf2image import convert_from_path

workspace = glob.glob('/sessions/*/mnt/*/')[0].rstrip('/')
docs_path = os.path.join(workspace, 'assessment', 'business-case-docs')

for fname in os.listdir(docs_path):
    if fname.lower().endswith('.pdf'):
        pdf_path = os.path.join(docs_path, fname)
        print(f'Extracting: {fname}')
        images = convert_from_path(pdf_path, dpi=200)
        text = ''
        for i, img in enumerate(images):
            page_text = pytesseract.image_to_string(img)
            text += f'\n--- Page {i+1} ---\n{page_text}'
        print(f'Extracted {len(text)} chars from {fname}')
        print(text)
```

- **DOCX, MD, TXT files:** Use the `Read` tool directly on each file path.
- **XLSX files:** Use the `Read` tool or Python to extract tabular content.

Confirm in chat: "Read [N] document(s): [list filenames]" before proceeding.

**Optional:** If the assessor has also uploaded a criteria document (PDF, DOCX, or MD), read it now using the same method.

---

## Step 1: Parallel Context Extraction & Criteria Resolution

Two agents initialize in parallel:

**Agent 1: context-extractor**
- Reads all files in `$WORKSPACE/assessment/business-case-docs/`
- Extracts structured context data
- Populates `$WORKSPACE/assessment/pre-assessment/data/context-profile.json` with fields:
  - Company name, founding date, stage (Seed/Series A/B/C+)
  - Product/service description
  - Vertical (technology, healthcare, fintech, etc.)
  - Geography (primary market)
  - Current revenue/traction (if disclosed)
  - Funding ask and use of proceeds
  - Any disclosed risks or material uncertainties
- Notes extraction confidence scores

**Agent 2: criteria-resolver**
- If assessor criteria document provided: reads document, extracts investor profile (type, transaction size, sector focus, red flags, non-negotiables)
- If no document: conducts interactive dialogue with assessor to determine:
  - Assessor type (VC, corporate venture, angel, acquisitor, strategic partner)
  - Typical transaction size and stage focus
  - Top 3 investment priorities
  - Top 3 non-negotiables
  - Any sector exclusions or geographic constraints
- Populates `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`

Both agents complete before proceeding.

---

## CONFIRMATION POINT 1: Context & Assessor Profile

**What you see:**
- **Context Profile Summary:** company name, stage, vertical, geography, revenue (if disclosed), ask amount, key uncertainties
- **Assessor Profile Summary:** assessor type, transaction focus, top priorities, non-negotiables, constraints
- **Extraction Flags:** any low-confidence extractions or ambiguities noted

**Before presenting to the assessor, save a review file:**

Save the full CP1 summary as a formatted markdown file to the reports folder:

```
$WORKSPACE/assessment/pre-assessment/reports/CP1_ContextProfile_[YYYY-MM-DD].md
```

The file must contain:
- `# CP1 Review — Context & Assessor Profile`
- `## Context Profile` section: all extracted fields as a markdown table, followed by a `## Extraction Flags` section listing any uncertainties or missing data
- `## Assessor Profile` section: assessor type, ticket size, priorities, deal-breakers, calibration notes as a markdown table
- `## Instructions` section explaining how to submit corrections (see below)

Present the summary in chat and provide a download link to the saved file.

**Your instruction to the assessor:**

> A review file has been saved for your reference:
> **`$WORKSPACE/assessment/pre-assessment/reports/CP1_ContextProfile_[YYYY-MM-DD].md`**
>
> You have two options:
>
> **Option A — Edit & re-upload:** Open the file, make corrections directly in it, save it, and re-upload it here. The updated file will be read and all corrections applied automatically.
>
> **Option B — Confirm in chat:** If everything looks correct, type **`confirm`** to proceed immediately.

**What happens:**
- If the assessor re-uploads an edited CP1 file: read the file, extract all corrections, apply them to `context-profile.json` and `assessor-profile.json`, confirm what changed, and proceed
- If the assessor types `confirm`: proceed with no changes
- If the assessor types corrections as freeform text: apply corrections, confirm what changed, and proceed
- All corrections are recorded in the session audit trail
- Proceed to Step 2

---

## Step 2: Framework Construction

Agent: **framework-builder**
- Input: confirmed `$WORKSPACE/assessment/pre-assessment/data/context-profile.json` + `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
- Builds a dynamic assessment framework:
  - Evaluates which domains are mandatory vs. optional given context
  - Sets domain weights based on assessor priorities
  - Designates hard blockers (domains/criteria that trigger immediate no-go)
  - Assigns criticality levels (must-have, should-have, nice-to-have)
  - Identifies optional module packages for deeper dives
- Output: `$WORKSPACE/assessment/pre-assessment/data/framework.json` (domain registry, module list, weights, hard blockers, calibration notes)

---

## CONFIRMATION POINT 2: Assessment Framework

**What you see:**
- **Domain Activation Table:** domain name | activation status (mandatory/optional) | criticality | weight (%) | module count
- **Hard Blocker List:** conditions that auto-trigger no-go
- **Calibration Notes:** any assumptions or reasoning behind framework design

**Before presenting to the assessor, save a review file:**

Save the full CP2 summary as a formatted markdown file to the reports folder:

```
$WORKSPACE/assessment/pre-assessment/reports/CP2_Framework_[YYYY-MM-DD].md
```

The file must contain:
- `# CP2 Review — Assessment Framework`
- `## Domain Activation Table` section: all domains as a markdown table with columns: Domain | Status (mandatory/optional) | Criticality | Weight (%) | Module Count
- `## Hard Blockers` section: each hard blocker as a bullet point with trigger condition and consequence
- `## Calibration Notes` section: reasoning behind framework design choices
- `## What You May Adjust` section: clearly stating what the assessor can and cannot change (see constraints below)
- `## Instructions` section explaining how to submit adjustments (see below)

Present the summary in chat and provide a download link to the saved file.

**Your instruction to the assessor:**

> A review file has been saved for your reference:
> **`$WORKSPACE/assessment/pre-assessment/reports/CP2_Framework_[YYYY-MM-DD].md`**
>
> You may adjust:
> - Add optional modules within a domain for deeper analysis
> - Adjust criticality levels within reasonable bounds (must-have ↔ should-have only)
>
> You may **NOT** adjust:
> - Remove mandatory modules
> - Remove hard blockers
>
> You have two options:
>
> **Option A — Edit & re-upload:** Open the file, annotate your adjustments in the `## Instructions` section, save it, and re-upload it here. All valid adjustments will be applied automatically; any invalid adjustments (removing mandatory modules or hard blockers) will be flagged and rejected.
>
> **Option B — Confirm in chat:** If the framework looks correct, type **`confirm`** to proceed immediately.

**What happens:**
- If the assessor re-uploads an edited CP2 file: read the file, extract all requested adjustments, validate each against the constraints above, apply valid adjustments to `framework.json`, reject and explain any invalid ones, and proceed
- If the assessor types `confirm`: proceed with no changes
- If the assessor types adjustments as freeform text: apply valid adjustments, reject invalid ones with explanation, and proceed
- All adjustments are logged in the session audit trail
- Proceed to Step 3

---

## Step 3: Research

Agent: **research-agent**
- Input: confirmed `$WORKSPACE/assessment/pre-assessment/data/framework.json` + files in `$WORKSPACE/assessment/business-case-docs/`
- Conducts research across all 5 assessment categories:
  1. **Context & Market** – market sizing, TAM/SAM/SOM, competitive positioning, regulatory environment
  2. **Product & Technology** – product-market fit signals, technical differentiation, IP landscape
  3. **Team & Execution** – founder/leadership backgrounds, org structure, execution track record
  4. **Financial Projections & Unit Economics** – revenue model, CAC/LTV, burn rate, runway, path to profitability
  5. **Risk & Dependencies** – key dependencies, technical risks, market risks, operational risks
- Compiles findings into `$WORKSPACE/assessment/pre-assessment/data/research-log.json` with sources and confidence scores
- Note: This step may take several minutes

---

## Step 4: Module Mapping

Agent: **module-mapper**
- Input: `$WORKSPACE/assessment/pre-assessment/data/framework.json` + files in `$WORKSPACE/assessment/business-case-docs/` + `$WORKSPACE/assessment/pre-assessment/data/research-log.json`
- Maps research findings against each domain's modules
- For each module: identifies source data, completeness, quality
- Produces `$WORKSPACE/assessment/pre-assessment/data/module-content-map.json`:
  - module_id | domain | content_available (yes/partial/no) | source | quality_score | notes

---

## Step 5: Scoring

Agent: **scorer**
- Input: `$WORKSPACE/assessment/pre-assessment/data/framework.json` + `$WORKSPACE/assessment/pre-assessment/data/module-content-map.json`
- Scores readiness across all modules:
  - Readiness register: measures submission completeness and coherence for each module
  - Fit-to-purpose register: measures alignment with assessor criteria for each module
- Produces two JSON registers:
  1. `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json` – readiness scores by module (0–100 scale)
  2. `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json` – fit-to-purpose scores by module (0–100 scale)
- Domain-level aggregates computed for both

---

## Step 6: Gap Analysis

Agent: **gap-analyst**
- Input: `$WORKSPACE/assessment/pre-assessment/data/framework.json` + `$WORKSPACE/assessment/pre-assessment/data/module-content-map.json` + `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json` + `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json`
- Identifies gaps, missing data, and weak signals
- Analyzes module-to-module dependencies and identifies compounding risks
- Produces two outputs:
  1. `$WORKSPACE/assessment/pre-assessment/data/gap-register.json` – gap_id | domain | module | gap_type (missing_data / weak_signal / risk) | severity (critical/high/medium/low) | impact | remediation_hint
  2. `$WORKSPACE/assessment/pre-assessment/data/dependency-map.json` – maps which gaps compound or reinforce others

---

## Step 7: Go/No-Go Determination (Preliminary)

Script: **go_nogo_determinator.py**
- Input: `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json` + `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json` + hard blockers
- Logic:
  - Check for hard blocker triggers → NO-GO
  - Aggregate readiness scores: if <threshold → CONDITIONAL HOLD
  - Aggregate fit-to-purpose scores: if low → CONDITIONAL HOLD
  - Otherwise → GO or CONDITIONAL GO (with conditions noted)
- Output: `$WORKSPACE/assessment/pre-assessment/data/preliminary-go-nogo-determination.json`
  - determination (GO / CONDITIONAL GO / CONDITIONAL HOLD / NO-GO)
  - determination_rationale
  - hard_blocker_status (triggered or not)
  - readiness_score (overall %)
  - fit_to_purpose_score (overall %)
  - conditions (if conditional)

---

## CONFIRMATION POINT 3: Scored Findings

**What you see:**
- **Overall Readiness Score** – domain-level scores + overall readiness %
- **Overall Fit-to-Purpose Score** – domain-level fit %
- **Domain Score Summary Table:** domain | readiness | fit | key_strengths | key_gaps
- **Top 5 Gaps by Severity** – ordered by severity, with module, type, and remediation hints
- **Preliminary Go/No-Go Determination** – determination, rationale, any conditions

**Before presenting to the assessor, save a review file:**

Save the full CP3 summary as a formatted markdown file to the reports folder:

```
assessment/pre-assessment/reports/CP3_ScoredFindings_[YYYY-MM-DD].md
```

The file must contain:
- `# CP3 Review — Scored Findings`
- `## Preliminary Determination` section: determination badge (GO / CONDITIONAL GO / CONDITIONAL HOLD / NO-GO), rationale paragraph, any conditions
- `## Overall Scores` section: overall readiness % and overall fit-to-purpose % as a summary table
- `## Domain Score Summary` section: full domain table with columns: Domain | Readiness | Fit-to-Purpose | Key Strengths | Key Gaps
- `## Top 5 Gaps by Severity` section: ordered gap list as a table with columns: Gap ID | Domain | Module | Type | Severity | Remediation Hint
- `## Your Notes` section: a blank section with a placeholder comment ("Add any flags, corrections, or additional context here") for the assessor to fill in
- `## Instructions` section explaining how to submit notes (see below)

Present the summary in chat and provide a download link to the saved file.

**Your instruction to the assessor:**

> A review file has been saved for your reference:
> **`$WORKSPACE/assessment/pre-assessment/reports/CP3_ScoredFindings_[YYYY-MM-DD].md`**
>
> You may:
> - Flag any modules for reconsideration
> - Provide additional context that was not in your submission
> - Correct any research assumptions
>
> Note: assessor notes at CP3 are recorded in the audit trail. They do **not** change scores — they provide context that carries forward into the full assessment phase.
>
> You have two options:
>
> **Option A — Edit & re-upload:** Open the file, add your notes and flags in the `## Your Notes` section, save it, and re-upload it here. All notes will be read, recorded in the session audit trail, and confirmed back to you before proceeding.
>
> **Option B — Confirm in chat:** If you have no notes or flags, type **`confirm`** to proceed immediately.

**What happens:**
- If the assessor re-uploads an edited CP3 file: read the `## Your Notes` section, record all notes verbatim in the session audit trail, confirm what was recorded, and proceed
- If the assessor types `confirm`: proceed with no notes recorded
- If the assessor types notes as freeform text: record notes in audit trail, confirm, and proceed
- Proceed to Step 8

---

## Step 8: QA/QC Review

Agent: **qaqc-agent** (holistic mode)
- Input: all data structures in `$WORKSPACE/assessment/pre-assessment/data/` produced so far (context-profile, assessor-profile, framework, research-log, module-content-map, readiness-register, fit-to-purpose-register, gap-register, dependency-map, preliminary-go-nogo-determination)
- Runs comprehensive quality checks:
  - Data consistency across all registers
  - Scoring logic validation
  - Framework-to-scoring alignment
  - Gap severity calibration
  - Dependency graph integrity
- If issues found:
  - Automatically resolves routine issues
  - For significant escalations: presents to assessor with explanation and options (accept / override / rework)
  - Waits for assessor response
  - Updates affected data structures
- Produces `$WORKSPACE/assessment/pre-assessment/data/qaqc-report.json` documenting all checks and resolutions

---

## Step 9: Output Generation

Agent: **pre-assess-output-agent**
- Input: all confirmed data structures in `$WORKSPACE/assessment/pre-assessment/data/` + session audit trail
- Generates 5 deliverable outputs saved to their respective subfolders:

**Reports** → saved to `$WORKSPACE/assessment/pre-assessment/reports/`

1. **[CompanyName]_PreAssessment_[YYYY-MM-DD].html**
   - Beautiful, interactive HTML report with charts, tables, and collapsible sections
   - Domain summaries, scored findings, gaps, dependencies
   - Includes executive summary and methodology notes

2. **[CompanyName]_PreAssessment_[YYYY-MM-DD].pdf**
   - Agent generates printable HTML version; assessor can print to PDF via browser
   - Fully formatted, ready for external sharing or filing

3. **[CompanyName]_PreAssessment_[YYYY-MM-DD].md**
   - Structured markdown data file containing all scored findings, registers, and determination
   - Used as input to `/assess` command in next phase
   - Preserves all JSON registers in structured format

**Data files** → saved to `$WORKSPACE/assessment/pre-assessment/data/`

4. **[CompanyName]_ScoredRegister_[YYYY-MM-DD].json**
   - Comprehensive JSON export of all scoring data
   - Useful for external analysis or integration

5. **[CompanyName]_ResearchProvenance_[YYYY-MM-DD].json**
   - Complete research log with sources and confidence scores
   - Enables fact-checking and supports deeper dives in `/assess` phase

---

## Completion

All five outputs are displayed with download links. The final determination is displayed prominently.

**Output locations:**
```
assessment/pre-assessment/
├── reports/
│   ├── [CompanyName]_PreAssessment_[YYYY-MM-DD].html
│   ├── [CompanyName]_PreAssessment_[YYYY-MM-DD].pdf
│   └── [CompanyName]_PreAssessment_[YYYY-MM-DD].md
└── data/
    ├── context-profile.json
    ├── assessor-profile.json
    ├── framework.json
    ├── research-log.json
    ├── module-content-map.json
    ├── readiness-register.json
    ├── fit-to-purpose-register.json
    ├── gap-register.json
    ├── dependency-map.json
    ├── preliminary-go-nogo-determination.json
    ├── qaqc-report.json
    ├── [CompanyName]_ScoredRegister_[YYYY-MM-DD].json
    └── [CompanyName]_ResearchProvenance_[YYYY-MM-DD].json
```

**Next step:** When ready to proceed to full assessment, run `/assess`. It will read from `$WORKSPACE/assessment/pre-assessment/` automatically.
