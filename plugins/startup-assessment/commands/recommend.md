---
description: Generate investment recommendations from assessment and sensitivity outputs
allowed-tools: Read, Write, Bash(python3:*), Bash(find:*), Agent, AskUserQuestion
model: sonnet
argument-hint: (no arguments required — reads automatically from workspace folders)
---

## /recommend Command: Investment Decision & Path Selection

### Usage

```
/recommend
```

### Overview

The `/recommend` command produces your final investment recommendations and decision paths. It automatically reads your assessment findings and sensitivity analysis from the workspace, and generates two investment pathways: Path A (standard approach) is always available; Path B (alternative approach) is available if you qualified in sensitivity analysis.

**What you get:** A comprehensive final recommendations document with Path A and Path B options, implementation roadmaps for each, and a complete session audit trail—your final deliverable from the full assessment workflow.

---

### Output Folder Paths

All outputs are written to:

| Output type | Destination |
|---|---|
| HTML, PDF reports | `$WORKSPACE/assessment/recommendations/reports/` |
| JSON data files | `$WORKSPACE/assessment/recommendations/data/` |

**Base paths** (used throughout this command):
- Reports: `$WORKSPACE/assessment/recommendations/reports/`
- Data: `$WORKSPACE/assessment/recommendations/data/`

---

### Pre-Flight Checks

**Step 0: Discover workspace root and verify assessment + sensitivity outputs (run first)**

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
    sens_data = os.path.join(workspace, 'assessment', 'sensitivity', 'data')
    
    if not os.path.isdir(assess_data):
        print('ERROR: assessment/data not found. Run /assess first.')
    elif not os.path.isdir(sens_data):
        print('ERROR: sensitivity/data not found. Run /sensitivity first.')
    else:
        cp = os.path.join(workspace, 'assessment', 'pre-assessment', 'data', 'context-profile.json')
        if os.path.exists(cp):
            with open(cp) as fh:
                data = json.load(fh)
            print(f'Company: {data.get("company_name", "unknown")}')
        print(f'assessment/data files: {os.listdir(assess_data)}')
        print(f'sensitivity/data files: {os.listdir(sens_data)}')
```

Use the `WORKSPACE` value above for all file paths. If WORKSPACE is empty or prerequisite folders are missing, stop and follow the error instructions.

---

**Step 1: Read all required files into context (mandatory — do this before anything else)**

Use the `Read` tool to open and read every file listed below. Do not invoke the recommendations-agent until all files are fully loaded into context.

Read these files in order:

1. `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
2. `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
3. `$WORKSPACE/assessment/pre-assessment/data/framework.json`
4. `$WORKSPACE/assessment/pre-assessment/data/gap-register.json`
5. `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
6. `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
7. All `$WORKSPACE/assessment/assessment/data/domain-findings-*.json` files — use the `Read` tool on each one found
8. `$WORKSPACE/assessment/sensitivity/data/sensitivity-results.json`

Also read any CP review files in `$WORKSPACE/assessment/assessment/reports/` and `$WORKSPACE/assessment/sensitivity/reports/` for full audit trail context.

Confirm in chat: "Loaded all data for [Company Name] — Path B eligible: [yes/no]" before proceeding.

---

## Step 1: Recommendations Generation

Agent: **recommendations-agent**
- Input (all read automatically from workspace):
  - `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
  - `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
  - `$WORKSPACE/assessment/assessment/data/domain-findings-[domain_id].json` (all domain files)
  - `$WORKSPACE/assessment/sensitivity/data/sensitivity-results.json`
  - `$WORKSPACE/assessment/pre-assessment/data/framework.json`
  - `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/gap-register.json`
- Reads Path B eligibility from `sensitivity-results.json`
- Constructs recommendations:

**Path A (Always Available):**
- Generates standard investment recommendation
- Recommendation level: GO / CONDITIONAL GO / PASS
- Rationale: rooted in assessment findings and final determination
- Investment approach:
  - Deal structure (equity size, valuation frame, governance)
  - Key conditions precedent (if CONDITIONAL GO)
  - Monitoring requirements (key metrics, board observation rights, etc.)
  - Value-add strategy (introductions, recruitment support, operational guidance, etc.)
- Implementation roadmap:
  - Week 1–2: due diligence completion and condition verification
  - Week 3–4: term sheet negotiation and signing
  - Week 5–6: closing and deployment
  - Post-close: monitoring, support, governance participation
- Success criteria: metrics that indicate investment is tracking
- Risk mitigation: top 3 risks identified in assessment; how they'll be monitored and managed

**Path B (If Eligible):**
- Generates alternative investment recommendation
- Reflects structured approach or alternative strategy from sensitivity analysis
- May include:
  - Tranched investment structure (initial tranche + additional tranches tied to milestones)
  - Earnout conditions (additional investment or enhanced terms based on performance)
  - Partnership opportunities (non-dilutive revenue sources, strategic relationships)
  - Extended timeline (phased entry with option to increase)
  - Governance provisions (advisory board seats, operational metrics reporting)
- Path B is designed to address conditions or risks that were identified in assessment
- Implementation roadmap specific to Path B structure
- Success metrics and gating criteria for Path B progression

**recommendations-agent:**
- Determines Path A recommendation level based on final assessment determination
- Determines Path B structure and recommendation level (if Path B eligible)
- Cross-checks Path B rationale against assessment and sensitivity findings
- Produces `$WORKSPACE/assessment/recommendations/data/recommendations.json`:
  - path_a_recommendation (GO / CONDITIONAL GO / PASS)
  - path_a_rationale
  - path_a_deal_structure
  - path_a_conditions (if CONDITIONAL GO)
  - path_a_monitoring_framework
  - path_a_implementation_roadmap
  - path_a_value_add_strategy
  - path_b_eligible (true / false)
  - path_b_recommendation (if eligible) (GO / CONDITIONAL GO)
  - path_b_rationale
  - path_b_structure
  - path_b_gating_criteria
  - path_b_implementation_roadmap
  - comparative_analysis (if both paths available): pros/cons of each approach

---

## Step 2: Output Generation

Agent: **recommendations-output-agent**
- Input (all read automatically from workspace):
  - `$WORKSPACE/assessment/recommendations/data/recommendations.json`
  - `$WORKSPACE/assessment/assessment/data/integrated-findings-register.json`
  - `$WORKSPACE/assessment/assessment/data/updated-go-nogo-determination.json`
  - `$WORKSPACE/assessment/sensitivity/data/sensitivity-results.json`
  - `$WORKSPACE/assessment/pre-assessment/data/context-profile.json`
  - `$WORKSPACE/assessment/pre-assessment/data/assessor-profile.json`
  - Session audit trail (CP1–CP5 confirmations and all adjustments)
- Generates 3 deliverable outputs (all saved to `$WORKSPACE/assessment/recommendations/reports/`):

1. **[CompanyName]_Recommendations_[YYYY-MM-DD].html**
   - Beautiful, executive-focused recommendations report
   - Path A recommendation with full rationale, deal structure, roadmap
   - Path B recommendation (if applicable) with comparative analysis
   - Key metrics dashboard (pre-assessment, assessment, sensitivity outcomes)
   - Implementation roadmap with timeline
   - Success criteria and risk monitoring framework
   - Interactive Path comparison tool (if both paths available)

2. **[CompanyName]_Recommendations_[YYYY-MM-DD].pdf**
   - Agent generates printable HTML version; you can print to PDF via your browser
   - **FINAL DELIVERABLE** – includes complete session audit trail in appendix
   - Audit trail documents:
     - CP1 (Context & Assessor Profile) confirmation
     - CP2 (Framework) confirmation and any adjustments
     - CP3 (Scored Findings) confirmation and any notes
     - CP4 (Assessment Scope) confirmation and any escalations
     - CP5 (Reconciled Findings) confirmation and any overrides
     - All research sources and confidence scores
     - All scoring logic and determination pathways
     - All sensitivity methodology and Path B eligibility logic
   - Ready for regulatory filing, LP reporting, or deal documentation

3. **recommendations.json** → saved to `$WORKSPACE/assessment/recommendations/data/`
   - Machine-readable recommendations export
   - Contains all structured recommendation data, paths, and rationale
   - Useful for downstream workflow integration

---

## Workflow Completion

**Output locations:**
```
assessment/recommendations/
├── reports/
│   ├── [CompanyName]_Recommendations_[YYYY-MM-DD].html
│   └── [CompanyName]_Recommendations_[YYYY-MM-DD].pdf  ← FINAL DELIVERABLE
└── data/
    └── recommendations.json
```

**Summary of All Deliverables:**

You now have a complete assessment file set across all 4 phases:

**Pre-Assessment Phase (5 files):**
1. [CompanyName]_PreAssessment_[YYYY-MM-DD].html
2. [CompanyName]_PreAssessment_[YYYY-MM-DD].pdf
3. [CompanyName]_PreAssessment_[YYYY-MM-DD].md
4. [CompanyName]_ScoredRegister_[YYYY-MM-DD].json
5. [CompanyName]_ResearchProvenance_[YYYY-MM-DD].json

**Assessment Phase (3 files):**
6. [CompanyName]_Assessment_[YYYY-MM-DD].html
7. [CompanyName]_Assessment_[YYYY-MM-DD].pdf
8. [CompanyName]_Assessment_[YYYY-MM-DD].md

**Sensitivity Phase (3 files):**
9. [CompanyName]_Sensitivity_[YYYY-MM-DD].html
10. [CompanyName]_Sensitivity_[YYYY-MM-DD].pdf
11. [CompanyName]_Sensitivity_[YYYY-MM-DD].md

**Recommendations Phase (3 files):**
12. [CompanyName]_Recommendations_[YYYY-MM-DD].html
13. [CompanyName]_Recommendations_[YYYY-MM-DD].pdf ← FINAL DELIVERABLE with complete audit trail
14. recommendations.json

**Total: 14 files across all phases**

---

**Congratulations!** You have completed the full startup assessment workflow. Your Recommendations PDF is your final deliverable—it contains your investment decision, implementation roadmap, and complete session audit trail documenting every confirmation point and adjustment made throughout the process.

---

**Next Steps:**

- **If you have an updated business case or submission:** You may run `/pre-assess` again at any time with the revised document. This will create a new assessment session with fresh findings, allowing you to track changes over time.

- **If you want to explore alternative scenarios:** You can re-run `/sensitivity` with different methodology options, or adjust assessment scope and re-run `/assess` to test alternative assessment hypotheses.

- **For external sharing:** All PDF outputs are ready for investor review, board presentation, or partnership discussions. The Recommendations PDF includes complete audit trail for transparency and compliance.
