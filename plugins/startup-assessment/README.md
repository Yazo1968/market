# startup-assessment

AI-powered startup business case assessment plugin. Four sequential phases — each invoked by a single command — covering pre-assessment, full assessment, sensitivity analysis, and investment recommendations.

---

## Overview

This plugin accepts a startup business case document and guides the assessor through a structured, professionally defensible assessment workflow. It adapts to any assessor type (VC, PE, credit, strategic), any funding stage (pre-seed through growth), and any geography.

The plugin distinguishes three types of content throughout: **what the submitter claims**, **what external research confirms or contradicts**, and **what research adds that the submission does not address**. This distinction governs every score, gap classification, and determination produced.

---

## Workflow

```
/pre-assess  →  [Human reviews Pre-Assessment Report]
     ↓
/assess      →  [Human reviews Assessment Report]
     ↓
/sensitivity →  [Human reviews Sensitivity Analysis]
     ↓
/recommend   →  [Human reviews Recommendations]
```

Each phase requires the prior phase's structured output (`.md` data file) to be uploaded as input.

---

## Commands

### `/pre-assess [business-case-document] [assessor-criteria-document-optional]`

Runs the complete pre-assessment workflow:
1. Extracts context signals (funding stage, vertical, commercial model, geography, ask)
2. Resolves assessor mandate (from uploaded criteria document and/or structured dialogue)
3. Builds dynamic assessment framework calibrated to the submission
4. Conducts external research across all five research categories
5. Scores all active modules on Readiness and Fit-to-Purpose tracks
6. Classifies gaps and builds cross-domain dependency map
7. Runs holistic QA/QC
8. Produces go/no-go determination
9. Delivers 2 user-facing outputs: HTML dashboard + editable Word memo

**Review Points:** 3 — Context Review, Framework Review, Scores Review

**User-facing deliverables:**
- `[CompanyName]_PreAssessment_[YYYY-MM-DD].html` — Interactive multi-tab dashboard
- `[CompanyName]_PreAssessment_[YYYY-MM-DD].docx` — Editable memo for review, comments, and collaboration

---

### `/assess [pre-assessment-data-md-file]`

Runs the full assessment phase. Requires a GO or CONDITIONAL GO pre-assessment determination.

1. Validates pre-assessment data and determination gate
2. Determines assessment scope (domain modes: Deep Independent / Verification / Gap-Focused)
3. Runs domain assessors in parallel where dependency map allows; queues dependent domains
4. Runs domain-level QA/QC after each domain
5. Reconciles cross-domain conflicts, compounding risks, and reinforcing strengths
6. Produces final assessment determination
7. Delivers 2 user-facing outputs: HTML dashboard + editable Word memorandum

**Review Points:** 2 — Scope Review, Findings Review

---

### `/sensitivity [assessment-data-md-file]`

Runs sensitivity analysis on the locked assessment determination.

- Plugin evaluates the determination outcome and presents 2–3 methodology options (scenario analysis, boundary/flip-point analysis, Monte Carlo simulation)
- Assessor selects methodology; plugin executes and delivers results
- Outputs 2 user-facing deliverables: HTML dashboard + editable Word summary

---

### `/recommend [assessment-data-md-file] [sensitivity-analysis-json]`

Generates recommendations based on the full assessment + sensitivity outcomes.

- **Path A** (always available): Submitter improvement roadmap — gaps to address, priority order, evidence required, impact on determination
- **Path B** (available when determination is GO or CONDITIONAL GO and sensitivity confirms robustness): Deal terms and investment structure alternatives — realistic, implementable structures appropriate to the sector, stage, commercial model, and ask; based on industry standards; for professional investor use

---

## Components

| Type | Count | Names |
|------|-------|-------|
| Commands | 4 | pre-assess, assess, sensitivity, recommend |
| Agents | 15 | context-extractor, criteria-resolver, framework-builder, research-agent, module-mapper, scorer, gap-analyst, qaqc-agent, pre-assess-output-agent, scope-determinator, domain-assessor, reconciliation-agent, assess-output-agent, sensitivity-agent, recommendations-agent |
| Skills | 9 | domain-taxonomy, scoring-rubric, stage-calibration, vertical-calibration, research-protocol, qaqc-rubric, html-dashboard, sensitivity-methodology, recommendations-framework |
| Python Scripts | 5 | score_calculator.py, gap_classifier.py, confidence_router.py, go_nogo_determinator.py, json_validator.py |
| JSON Schemas | 14 | See `schemas/` directory |
| MCP Connectors | 5 research categories | See `.mcp.json` |

---

## Setup

### Environment Variables

| Variable | Required | Used By | Description |
|----------|----------|---------|-------------|
| `BRAVE_API_KEY` | Recommended | research-agent | Brave Search API key for web retrieval. Free tier available at search.brave.com/api |
| `CRUNCHBASE_API_KEY` | Optional | research-agent | Crunchbase Basic API for startup/funding data |
| `OPENCORPORATES_API_KEY` | Optional | research-agent | OpenCorporates API for company registry data |

To set environment variables, add them to your shell profile or Claude's environment configuration.

### Connector Configuration

The `.mcp.json` file contains five research category entries. Each connector marked `_disabled: true` is a placeholder — enable it by:
1. Removing the `_disabled` field
2. Setting the required environment variable
3. Updating the URL or command as needed for your specific API access

Web retrieval (Brave Search) is the active fallback for all categories when structured connectors are unavailable. Note that web retrieval sources receive lower confidence classifications in the research provenance log.

---

## Usage Guide

### Running your first pre-assessment

1. Have your business case document ready (PDF, DOCX, or MD)
2. Optionally prepare a criteria document (your investment thesis, credit policy, etc.)
3. Run: `/pre-assess [business-case-document]` or `/pre-assess [business-case-document] [criteria-document]`
4. Respond to the three confirmation points as they appear
5. Review the HTML dashboard and Word memo when delivered
6. When ready to proceed, run `/assess`

### Review Points Guide

| Review | When | What You See | What You Can Do |
|--------|------|-------------|-----------------|
| Context Review | After context extraction | Company context profile + assessor mandate | Correct any extraction errors; adjust geographic frame |
| Framework Review | After framework construction | Active domains, modules, weights, rationale | Add modules; adjust criticality within bounds; cannot remove mandatory modules |
| Scores Review | After scoring | Scored registers, gap register, dependency map | Flag items for reconsideration; provide additional context |
| Scope Review | After scope determination | Assessment mode per domain, sequencing plan | Escalate modes (never reduce); confirm or adjust |
| Findings Review | After reconciliation | Cross-domain conflicts and resolutions | Flag any unresolved items; document overrides |

---

## QA/QC

The plugin runs automated QA/QC at two points:
- **Holistic QA/QC**: once at end of pre-assessment (before report generation) — checks for cross-module gaps, discrepancies, and conflicting information
- **Domain-level QA/QC**: after each domain assessment in the assessment phase

If QA/QC identifies an issue it cannot resolve in 2 iterations, it presents you with multiple-choice options (including "Keep as-is but flag in report" and a free-text input option). Your resolution is documented in the report appendix.

---

## Output File Naming

All output files follow the convention: `[CompanyName]_[Phase]_[YYYY-MM-DD].[ext]`

Example:
- `ZeroToN_PreAssessment_2026-03-08.html`
- `ZeroToN_Assessment_2026-03-08.docx`
- `ZeroToN_Sensitivity_2026-03-08.docx`

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 0.1.0 | 2026-03-08 | Initial build |
