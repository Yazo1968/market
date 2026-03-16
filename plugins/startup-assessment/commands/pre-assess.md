---
description: Run pre-assessment on a startup business case document
allowed-tools: Read, Write, Bash(python3:*), Bash(find:*), Agent, AskUserQuestion
model: sonnet
argument-hint: (no arguments required — reads from assessment/business-case-docs/)
---

<!-- Review points defined in this command:
     Context Review — Context & Assessor Profile review (line ~178)
     Framework Review — Framework review (line ~229)
     Scores Review — Scored Findings review (line ~352)
-->

## /pre-assess Command: Initial Readiness & Fit Assessment

### Usage

```
/pre-assess
```

### Overview

The `/pre-assess` command executes the initial assessment phase. It reads your business case, extracts critical context, builds a dynamic assessment framework tuned to your investor profile, conducts research, scores your readiness across ten assessment domains, and produces preliminary go/no-go guidance with detailed gap analysis.

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

## Step 1: Context Extraction

Agent: **context-extractor**
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

Wait for context-extractor to complete before proceeding.

---

## Step 1b: Assessor Profile — Interactive Questions

**Check first:** If a criteria document was uploaded to `$WORKSPACE/assessment/business-case-docs/`, skip this section and pass it directly to criteria-resolver to extract the profile automatically.

**If no criteria document was provided**, collect the assessor profile using an interactive artifact.

**Generate the Assessor Profile Collector Artifact:**

Load the `interactive-review` skill and its `references/assessor-profile-collector.md` reference. Then generate a **self-contained React artifact** using the Cowork artifact rendering system. The artifact must:

1. **Follow the assessor-profile-collector specification** in `skills/interactive-review/references/assessor-profile-collector.md` exactly — the form is **adaptive**: the assessor first selects their type (VC, Angel, PE, Credit, Corporate Strategic, Family Office, Sovereign Wealth, Accelerator, Other), then type-specific sections animate in with questions tailored to that assessor type (e.g., VC sees stage/thesis/burn-multiple fields; Credit sees facility-type/coverage-ratios/collateral fields; Corporate Strategic sees strategic-fit/integration-risk fields)
2. **Use the shared design system** from `skills/interactive-review/SKILL.md`
3. **Include validation** — type-specific required fields must be completed before Copy is enabled
4. **Include the profile footer** with completion progress and Copy to Clipboard button

The artifact renders inline. The assessor selects their type, sees only the questions relevant to their mandate, fills out their profile using the interactive controls, then copies the completed profile JSON.

**After artifact is rendered:**

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "Assessor Profile — Paste your completed profile from the artifact."
- options: ["I've pasted my profile above"]

**What happens:**
- Parse the pasted profile JSON
- Validate required fields are present (assessor_type, target_stage, must_haves)
- Pass the profile data to the **criteria-resolver** agent to produce `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`. The agent resolves the raw inputs into the full schema format (priorities, non-negotiables, weight modifiers) and outputs the profile.

---

## CONTEXT REVIEW: Context & Assessor Profile

**What you see:** An interactive review artifact rendered inline in the conversation.

**Generate the Context Review Interactive Artifact:**

Load the `interactive-review` skill and its `references/context-review-artifact.md` reference. Then generate a **self-contained React artifact** using the Cowork artifact rendering system. The artifact must:

1. **Embed the actual data** from `$WORKSPACE/assessment/pre-assessment/data/context-profile.json` and `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json` as constants at the top of the React component
2. **Follow the Context Review artifact specification** in `skills/interactive-review/references/context-review-artifact.md` exactly — three tabs (Company Context, Assessor Profile, Confidence Flags) with all editable fields
3. **Use the shared design system** from `skills/interactive-review/SKILL.md` — dark theme, color palette, shared components (DeterminationBadge, EditableField, LockedField, ChangesFooter)
4. **Include the Changes Footer** (collapsed by default) with change counter and Copy to Clipboard button
5. **Enforce all field constraints** — dropdown enums from the JSON schemas, required fields, data types

The artifact renders inline. The assessor reviews the extracted context and assessor profile, makes any corrections using the interactive controls (dropdowns, text inputs, toggles, sliders), and sees their changes tracked in the footer.

**After artifact is rendered:**

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "Context Review — Review complete. Paste your changes from the artifact, or confirm no changes needed."
- options: ["Confirm — No changes needed, proceed to framework construction", "I've pasted my changes above"]

**What happens:**
- If the assessor pastes a delta JSON from the artifact's Copy to Clipboard: parse the delta, validate each change against schema constraints, apply valid changes to `context-profile.json` and `assessor-profile.json`, confirm what was applied, and proceed
- If the assessor selects **Confirm**: proceed with no changes
- All corrections are recorded in the session audit trail with timestamps
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

## FRAMEWORK REVIEW: Assessment Framework

**What you see:**
- **Domain Activation Table:** domain name | activation status (mandatory/optional) | criticality | weight (%) | module count
- **Hard Blocker List:** conditions that auto-trigger no-go
- **Calibration Notes:** any assumptions or reasoning behind framework design

**Before presenting to the assessor, save a review file:**

Save the full Framework Review summary as a formatted markdown file to the reports folder:

```
$WORKSPACE/assessment/pre-assessment/reports/FrameworkReview_[YYYY-MM-DD].md
```

**Generate the Framework Review Interactive Artifact:**

Load the `interactive-review` skill and its `references/framework-review-artifact.md` reference. Then generate a **self-contained React artifact** using the Cowork artifact rendering system. The artifact must:

1. **Embed the actual data** from `$WORKSPACE/assessment/pre-assessment/data/framework.json` as a constant at the top of the React component
2. **Follow the Framework Review artifact specification** in `skills/interactive-review/references/framework-review-artifact.md` exactly — domain cards with weight sliders, criticality dropdowns, module tables, hard blockers panel, live radar chart
3. **Use the shared design system** from `skills/interactive-review/SKILL.md`
4. **Include the Changes Footer** (collapsed by default) with change counter and Copy to Clipboard button
5. **Enforce all constraints in the UI:**
   - Mandatory domains cannot be deactivated (toggle disabled + Lock icon)
   - Mandatory modules cannot be deactivated (checkbox disabled + Lock icon)
   - Criticality can only be escalated, never reduced (dropdown shows current level and above only)
   - Domain weights must sum to 100% (auto-redistribute proportionally when one changes)
   - Module weights must sum to 1.0 within each domain (auto-redistribute)
   - Hard blockers are locked (display only with red Lock icon)

The artifact renders inline. The assessor reviews domains, adjusts weights via sliders, escalates criticality, activates optional modules — all with live radar chart updates.

**After artifact is rendered:**

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "Framework Review — Review complete. Paste your changes from the artifact, or confirm no changes needed."
- options: ["Confirm — Framework looks correct, proceed to research", "I've pasted my changes above"]

**What happens:**
- If the assessor pastes a delta JSON: parse the delta, validate each change (reject removal of mandatory modules or hard blockers, reject criticality downgrades — explain why), apply valid adjustments to `framework.json`, confirm what was applied, and proceed
- If the assessor selects **Confirm**: proceed with no changes
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

Agent: **gap-analyst** (continued)
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

## SCORES REVIEW: Scored Findings

**What you see:**
- **Overall Readiness Score** – domain-level scores + overall readiness %
- **Overall Fit-to-Purpose Score** – domain-level fit %
- **Domain Score Summary Table:** domain | readiness | fit | key_strengths | key_gaps
- **Top 5 Gaps by Severity** – ordered by severity, with module, type, and remediation hints
- **Preliminary Go/No-Go Determination** – determination, rationale, any conditions

**Before presenting to the assessor, save a review file:**

Save the full Scores Review summary as a formatted markdown file to the reports folder:

**Generate the Scores Review Interactive Artifact:**

Load the `interactive-review` skill and its `references/scores-review-artifact.md` reference. Then generate a **self-contained React artifact** using the Cowork artifact rendering system. The artifact must:

1. **Embed the actual data** from the following files as constants:
   - `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json`
   - `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json`
   - `$WORKSPACE/assessment/pre-assessment/data/gap-register.json`
   - `$WORKSPACE/assessment/pre-assessment/data/dependency-map.json`
   - `$WORKSPACE/assessment/pre-assessment/data/go-nogo-determination.json`
2. **Follow the Scores Review artifact specification** in `skills/interactive-review/references/scores-review-artifact.md` exactly — executive summary header with determination badge and score gauges, four tabs (Domain Scores with dual-series radar chart, Gap Register with filters, Dependency Map flow visualization, Determination Detail with gate results)
3. **Use the shared design system** from `skills/interactive-review/SKILL.md`
4. **Include the Changes Footer** (collapsed by default)
5. **Scores are NOT editable** — display only. The only interactive elements are:
   - Flag checkboxes per domain and per module (for reconsideration)
   - Assessor note textareas per domain (expandable)
   - Assessor note textarea on the determination

Flags and notes are recorded in the audit trail — they do **not** change scores but carry forward into the full assessment.

**After artifact is rendered:**

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "Scores Review — Review complete. Paste your flags/notes from the artifact, or confirm no changes needed."
- options: ["Confirm — No flags or notes, proceed to QA/QC review", "I've pasted my flags/notes above"]

**What happens:**
- If the assessor pastes a delta JSON: parse all flags and notes, record each in the session audit trail with timestamps, confirm what was recorded, and proceed
- If the assessor selects **Confirm**: proceed with no flags or notes
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
- **Mandatory**: Load the `design-system` skill (`skills/design-system/SKILL.md`) and the `html-dashboard` skill before generating any outputs. Apply the centralized design system's color tokens, typography, component proportions, and CSS custom properties. Meet every requirement in the Quality Contract (Visual Quality Floor, Interactivity Floor, Print Readiness, Professional Standards). Adapt narrative tone to the assessor type per the Assessor-Type Tone Adaptation table.
- **Content freedom**: The agent determines the optimal report structure, sections, tabs, charts, and narrative emphasis for this specific case. The tab structures in `html-dashboard` are reference patterns — adapt as needed.
- Generates 5 deliverable outputs saved to their respective subfolders:

**Reports** → saved to `$WORKSPACE/assessment/pre-assessment/reports/`

1. **[CompanyName]_PreAssessment_[YYYY-MM-DD].html**
   - Self-contained interactive HTML report using the `html-dashboard` skill's component library and chart patterns
   - Content, structure, and emphasis are adaptive to the specific business case — the agent selects which visualizations, sections, and narrative framing best serve the assessor
   - Must meet the design system's quality contract: responsive at all breakpoints, keyboard-accessible tabs, print-ready, professional-grade typography and color consistency

2. **[CompanyName]_PreAssessment_[YYYY-MM-DD].pdf**
   - Agent generates a print-optimized HTML variant; assessor prints to PDF via browser
   - Format adapts to assessor type: Investment Memorandum (VC/PE/Angel), Credit Memorandum (Debt), or Strategic Assessment (Corporate/Family Office/Sovereign Wealth) per `html-dashboard` skill
   - Fully formatted with proper page breaks, margins, headers/footers, confidentiality notice

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
