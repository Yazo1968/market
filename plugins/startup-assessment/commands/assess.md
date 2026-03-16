---
description: Run full assessment on a pre-assessed submission
allowed-tools: Read, Write, Bash(python3:*), Bash(find:*), Agent, AskUserQuestion
model: sonnet
argument-hint: (no arguments required — reads automatically from workspace folders)
---

<!-- Review points defined in this command:
     Scope Review — Assessment Scope review (line ~134)
     Findings Review — Reconciled Findings review (line ~263)
-->

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
| HTML, Word reports | `$WORKSPACE/assessment/assessment/reports/` |
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

Also read any `.md` files in `$WORKSPACE/assessment/pre-assessment/reports/` (Context Review, Framework Review, Scores Review files) for audit trail context.

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

## SCOPE REVIEW: Assessment Scope

**What you see:** An interactive review artifact rendered inline in the conversation.

**Before presenting to the assessor, save a review file:**

Save the full Scope Review summary as a formatted markdown file:

```
assessment/assessment/reports/ScopeReview_[YYYY-MM-DD].md
```

**Generate the Scope Review Interactive Artifact:**

Load the `interactive-review` skill and its `references/scope-review-artifact.md` reference. Then generate a **self-contained React artifact** using the Cowork artifact rendering system. The artifact must:

1. **Embed the actual data** from the following files as constants:
   - `$WORKSPACE/assessment/assessment/data/assessment-scope-plan.json`
   - `$WORKSPACE/assessment/pre-assessment/data/readiness-register.json` (for pre-assess scores display)
   - `$WORKSPACE/assessment/pre-assessment/data/fit-to-purpose-register.json` (for pre-assess scores display)
2. **Follow the Scope Review artifact specification** in `skills/interactive-review/references/scope-review-artifact.md` exactly — scope table with mode escalation dropdowns, wave timeline visualization, mode distribution pie chart, pre-assessment context card
3. **Use the shared design system** from `skills/interactive-review/SKILL.md`
4. **Include the Changes Footer** (collapsed by default) with change counter and Copy to Clipboard button
5. **Enforce all constraints in the UI:**
   - Assessment modes can only be escalated, never reduced (dropdown shows current level and above only: gap-focused → verification → deep-independent)
   - Escalation rationale is required — text input appears when mode is changed, change not recorded until rationale is entered
   - Wave assignments are display-only (auto-computed from dependencies)

The artifact renders inline. The assessor reviews the scope plan, escalates modes where warranted via dropdowns, provides rationale, and sees their changes tracked in the footer.

**After artifact is rendered:**

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "Scope Review — Review complete. Paste your changes from the artifact, or confirm no changes needed."
- options: ["Confirm — The scope looks correct, proceed with domain assessment", "I've pasted my changes above"]

**What happens:**
- If the assessor pastes a delta JSON: parse the delta, validate each change (only escalations allowed — reject mode reductions with explanation, require rationale for each escalation), apply valid escalations to `assessment-scope-plan.json`, confirm what was applied, and proceed
- If the assessor selects **Confirm**: proceed with no changes
- All changes logged in session audit trail
- Proceed to Step 2

---

## Step 2: Domain Assessment (by wave)

For each wave in the sequencing plan:

**Wave Execution:**
- Invoke **domain-assessor** for each domain in the wave in parallel
- Each domain-assessor invocation receives (all read automatically from workspace):
  - domain_id (integer, e.g., 1, 2, 3, etc. — matching the framework domain numbering)
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

## Step 3b: Red-Team Challenge

Agent: **reconciliation-agent** (continued, adversarial mode)

After reconciliation produces the integrated findings and determination, the same agent conducts a structured devil's advocate review before presenting to the assessor. This follows institutional PE/VC best practice for IC-ready analysis.

**Red-Team Procedure:**
1. **Challenge the determination**: Construct the strongest possible counter-argument to the proposed determination. If GO, argue for NO-GO; if NO-GO, argue for GO.
2. **Stress-test key assumptions**: Identify the 3 most consequential assumptions underlying the determination. For each, state what would need to be true for the assumption to fail, and what the impact would be.
3. **Identify blind spots**: Flag any areas where data coverage is thin (confidence < medium) yet the determination relies heavily on the finding.
4. **Document the challenge**: Append a `red_team_challenge` section to `integrated-findings-register.json`:
   - `counter_argument`: the strongest case against the determination (2–3 paragraphs)
   - `key_assumptions_stressed`: array of 3 assumption objects, each with `assumption`, `failure_condition`, `impact_if_failed`
   - `blind_spots`: array of areas with thin evidence that carry outsized determination weight
   - `challenge_survives`: boolean — does the original determination survive the red-team challenge?
   - `challenge_notes`: any modifications or caveats the red-team review suggests

The red-team challenge is **informational only** — it does not change scores or determination. It is surfaced in Findings Review and included in the final report appendix.

---

## FINDINGS REVIEW: Reconciled Findings

**What you see:** An interactive review artifact rendered inline in the conversation.

**Before presenting to the assessor, save a review file:**

Save the full Findings Review summary as a formatted markdown file:

```
assessment/assessment/reports/FindingsReview_[YYYY-MM-DD].md
```

**Generate the Findings Review Interactive Artifact:**

Load the `interactive-review` skill and its `references/findings-review-artifact.md` reference. Then generate a **self-contained React artifact** using the Cowork artifact rendering system. The artifact must:

1. **Embed the actual data** from the following files as constants:
   - `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
   - `$WORKSPACE/assessment/assessment/data/domain-findings-*.json` (all domain files)
   - `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
2. **Follow the Findings Review artifact specification** in `skills/interactive-review/references/findings-review-artifact.md` exactly — final determination header with pre-assess vs assess comparison, five tabs (Cross-Domain Conflicts, Compounding Risks, Reinforcing Strengths, Domain-by-Domain Summary with expandable detail, Final Determination)
3. **Use the shared design system** from `skills/interactive-review/SKILL.md`
4. **Include the Changes Footer** (collapsed by default) with change counter and Copy to Clipboard button
5. **Scores are NOT editable** — display only. The only interactive elements are:
   - Override note textarea per conflict card (collapsed by default, expand on click)
   - Flag checkbox per compounding risk
   - General assessor notes textarea at the bottom (outside tabs)

Override notes and flags are recorded in the audit trail — they do **not** change scores but carry forward into the final report.

**After artifact is rendered:**

> ⚠️ **STRICT RULE — Interactive Questions:** Do NOT write question text as prose. Invoke `AskUserQuestion` silently — the widget renders automatically.

Invoke AskUserQuestion — type: single-select
- question: "Findings Review — Review complete. Paste your overrides/notes from the artifact, or confirm no changes needed."
- options: ["Confirm — Lock findings and generate final assessment outputs", "I've pasted my overrides/notes above"]

**What happens:**
- If the assessor pastes a delta JSON: parse all override notes and flags, record each in the session audit trail with timestamps, confirm what was recorded, and proceed
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
- **Mandatory**: Load the `design-system` skill and the `html-dashboard` skill before generating. Apply the centralized design system's tokens and meet the Quality Contract. Adapt tone to assessor type.
- **Content freedom**: The agent determines optimal structure, sections, charts, and narrative emphasis for this specific case.
- Generates 3 output files. Only the first two are **user-facing deliverables** presented to the assessor; the third is an **internal pipeline file** generated silently.

**User-facing deliverables** (saved to `$WORKSPACE/assessment/assessment/reports/`):

1. **[CompanyName]_Assessment_[YYYY-MM-DD].html**
   - Self-contained interactive HTML report using the `html-dashboard` skill's component library and chart patterns
   - Content and structure adaptive to the specific business case — agent selects which domain findings to emphasize, which cross-domain patterns to visualize, how to frame the determination narrative
   - Must meet the design system's quality contract

2. **[CompanyName]_Assessment_[YYYY-MM-DD].docx**
   - Editable Word document generated using `python-docx`; format adapts to assessor type per `html-dashboard` skill
   - Complete assessment document for review, comments, track changes, and stakeholder collaboration
   - Export to PDF from Word when ready to lock

**Internal pipeline file (generated but not surfaced to user):**

3. **[CompanyName]_Assessment_[YYYY-MM-DD].md**
   - Structured markdown data file with all assessment findings, registers, and determination
   - Used as input to `/sensitivity` command in next phase

---

## Completion

The two user-facing deliverables (HTML + Word) are presented to the assessor with the final determination displayed prominently. Internal pipeline files are saved silently.

**Output locations:**
```
assessment/assessment/
├── reports/
│   ├── ScopeReview_[YYYY-MM-DD].md                      (internal)
│   ├── FindingsReview_[YYYY-MM-DD].md                    (internal)
│   ├── [CompanyName]_Assessment_[YYYY-MM-DD].html        ← USER-FACING
│   ├── [CompanyName]_Assessment_[YYYY-MM-DD].docx        ← USER-FACING
│   └── [CompanyName]_Assessment_[YYYY-MM-DD].md          (internal)
└── data/
    ├── assessment-scope-plan.json                         (internal)
    ├── domain-findings-[domain_id].json (one per domain)  (internal)
    ├── integrated-findings-register.json                  (internal)
    └── updated-go-nogo-determination.json                 (internal)
```

**Next step:** Run `/sensitivity` — no file upload required. It will read from `$WORKSPACE/assessment/assessment/` automatically.
