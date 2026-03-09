# Holistic QA/QC Checklist for Pre-Assessment

This checklist is used at the end of the pre-assessment phase, after all modules have been scored and before report generation.

## Section 1: Internal Consistency Checks

### Score-to-Gap Consistency Checklist

**Step 1: Verify completeness score vs. gap register gap_type**

For each module in the assessment:

- [ ] Module with completeness = 0 → Gap register lists gap_type = "absent"
- [ ] Module with completeness 0.1–0.4 → Gap register lists gap_type = "fragmentary"
- [ ] Module with completeness 0.5–0.79 → Gap register lists gap_type varies ("partial," "conflicting," etc.)
- [ ] Module with completeness ≥0.8 → Gap register gap_type is NOT "critical" (by definition)

**Check method:** Sort gap register by module_id; cross-reference each entry against module-content-map completeness score.

**Example failure:**
```
Module: D3 Unit Economics
- Completeness score: 0.15 (fragmentary evidence)
- Gap register entry: gap_type = "critical-financial-gap"
- Issue: Fragmentary evidence (0.15) should not be classified as "critical"; should be "fragmentary"
- Fix: Correct gap_type to "fragmentary-low-quality" OR increase completeness score with additional research
```

**Example pass:**
```
Module: D5 Traction
- Completeness score: 0.0 (no evidence collected)
- Gap register entry: gap_type = "absent-research-conducted"
- Status: Valid (absent completeness aligns with absent gap classification)
```

---

**Step 2: Verify quality score alignment with evidence quality**

- [ ] Module scored Quality = 0.8+ has quality_notes that cite primary sources (company data, third-party validation)
- [ ] Module scored Quality = 0.4–0.6 has quality_notes that cite mixed sources (submission + limited validation)
- [ ] Module scored Quality = 0–0.3 has quality_notes that acknowledge limitations (e.g., "single source," "self-reported")

**Check method:** Sample 5 modules across domains; verify quality_notes support quality score.

**Example failure:**
```
Module: D6 Management Team
- Quality score: 0.8
- quality_notes: "Founder claims extensive startup experience; no external validation available"
- Issue: Score of 0.8 implies strong evidence, but notes show limited validation (red flag)
- Fix: Reduce quality score to 0.5 OR add third-party validation (news coverage, reference calls)
```

---

### Track and Fit-to-Purpose Consistency Checklist

**Step 1: Verify stage-appropriate score distribution**

For the identified stage (pre-seed, seed, Series A, Series B):

**Pre-Seed Stage Check:**
- [ ] Domains 1, 2, 6 (Market, Product, Management) are primary focus of scores
- [ ] Domains 7, 9 (Financial Performance, Capital Structure) have minimal weight
- [ ] No modules scored high on financials unless explicitly noted as "exceptional for pre-seed"
- [ ] If revenue is present, note as "pre-seed with traction signal" (not expected)

**Seed Stage Check:**
- [ ] Domains 1, 2, 5, 6 (Market, Product, Traction, Management) are primary
- [ ] Domain 3 (Business Model) is secondary but present
- [ ] Revenue or customer signals are present (if entirely absent, flag stage accuracy)
- [ ] Financials (Domain 7) are directional, not detailed

**Series A Stage Check:**
- [ ] Domains 3, 4, 5, 7 (Business Model, GTM, Traction, Financial) are strong
- [ ] Revenue is material (>$100K ARR for SaaS; proportional for other models)
- [ ] Unit economics (Domain 3) are visible, even if not perfect
- [ ] Team (Domain 6) includes VP-level functional expertise

**Series B Stage Check:**
- [ ] All domains are active with meaningful assessment
- [ ] Revenue is >$1M ARR (or >$100K MRR)
- [ ] Financials are detailed (audited or management accounts)
- [ ] Unit economics and path to profitability are clear

**Check method:** Review scoring summary table; verify score distribution matches stage profile.

---

**Step 2: Verify consistency between narrative and scores**

- [ ] Assessment narrative justifies why domains were weighted as indicated
- [ ] Narrative explains any stage-atypical scores (e.g., "Series A company with minimal GTM metrics due to early-stage distribution partnership")
- [ ] Assessment narrative does not contradict the scored framework

**Example failure:**
```
Stage identified: Pre-Seed
Assessment narrative: "Strong unit economics with LTV:CAC ratio of 5.2:1 and 18-month payback period"
Framework weights: Domain 3 (Business Model/Unit Economics) weighted at 0.08 (minimal)
Issue: Narrative highlights unit economics but framework treats them as secondary
Fix: Either (a) explain why unit economics are secondary despite being strong, or (b) elevate Domain 3 weight
```

---

### Gap Type Classification Validity Checklist

**Step 1: Verify gap classification matches research effort**

For each gap in the gap register:

- [ ] Gap classified "absent-externally-resolvable" has at least one research_attempt in research-log
- [ ] Gap classified "absent-unresolvable" has attempted research and notes explain why unresolvable (e.g., "founder declined to discuss")
- [ ] Gap classified "fragmentary-with-mitigation" has explicit mitigation strategy documented in gap_entry.mitigation field
- [ ] Gap classified "conflicting-evidence" cites both conflicting sources in evidence fields

**Check method:** For each gap, trace gap_id to research-log entries; verify research_attempt exists and notes support classification.

**Example failure:**
```
Gap register entry: ID = D8-risk-profile, gap_type = "absent-externally-resolvable", gap_priority = "high"
Research-log search: No entries for "risk," "risk-profile," or "D8 risk"
Issue: Gap is classified as externally-resolvable but no research attempt exists
Fix: Either log research attempt (even if unsuccessful) OR reclassify gap as "absent-unresolvable"
```

**Example pass:**
```
Gap register entry: ID = D10-ip-patents, gap_type = "fragmentary-with-mitigation"
Gap entry includes: mitigation = "IP strategy confirmed via founder interview; defensibility built on data moat, not patents"
Research-log entry: source_id = "research-005-founder-call", details = "Founder call 2024-03-05; IP strategy discussed"
Status: Valid (fragmentary evidence exists, mitigation strategy documented)
```

---

### Dependency Map Completeness Checklist

**Step 1: Verify all active domains appear in map**

- [ ] Count active domains in framework (all domains with status "Active" or "Hard Blocker")
- [ ] Count unique domain nodes in dependency map
- [ ] Verify counts match

**Check method:** Extract domain list from framework; extract domain nodes from dependency map; compare lists.

**Example failure:**
```
Active domains in framework: D1, D2, D3, D4, D5, D6, D8 (7 domains active)
Domains in dependency map: D1, D2, D3, D4, D5, D6, D8, D10 (8 domains)
Issue: D10 appears in map but is not active in framework
Fix: Either activate D10 in framework OR remove D10 node from dependency map
```

---

**Step 2: Detect circular dependencies**

- [ ] Scan dependency map for cycles (A → B → C → A)
- [ ] Flagged cycles: review with assessor to determine if legitimate feedback loop or error

**Check method:** Topological sort of dependency graph; flag any unsortable (cyclic) subgraph.

**Interpretation:**
- Legitimate cycle: "Market dynamics affect Product strategy; Product improvements expand addressable market"
- Error cycle: "Domain 5 (Traction) depends on Domain 7 (Financials); Domain 7 depends on Domain 5" (circular logic)

---

## Section 2: Research Coverage Checks

### Research Attempt Completeness Checklist

**Step 1: Verify every active module has research**

For each active module in framework:

- [ ] Search research-log for entries related to module_id or module_name
- [ ] Flag modules with zero entries

**Check method:** Filter research-log by module_id; count entries per module.

**Threshold:** 0 entries = FAIL; ≥1 entry = PASS

**Example:**
```
Active modules in D1 (Market): D1-tam, D1-customer-segment, D1-validation-evidence
Research attempts logged:
- D1-tam: 3 entries (company website, analyst report, founder interview)
- D1-customer-segment: 2 entries (submission, customer conversations log)
- D1-validation-evidence: 0 entries ← FLAG

Status: Domain D1 has research gap; module D1-validation-evidence not researched
Fix: Conduct research attempt for D1-validation-evidence (even if result is "no external validation data found")
```

---

### Research Category Coverage Checklist

**Step 1: Verify five research categories are represented**

Count research-log entries by source_category:

- [ ] Submission Document (internal): ≥1 entry
- [ ] Company Website and Public Marketing: ≥1 entry
- [ ] Third-Party Validation (press, analyst, awards, certifications): ≥1 entry
- [ ] Founder/Team Background Research: ≥1 entry
- [ ] Market and Competitive Landscape Research: ≥1 entry

**Check method:** Tally research-log entries by source_category; identify any category with 0 entries.

**Threshold:** All five categories must have ≥1 entry. If any category = 0, this is a QA/QC failure.

**Example failure:**
```
Research-log entries by category:
1. Submission Document: 12 entries
2. Company Website: 8 entries
3. Third-Party Validation: 3 entries
4. Founder/Team Background: 5 entries
5. Market/Competitive Landscape: 0 entries ← FAIL

Issue: No market or competitive research conducted
Fix: Conduct competitive landscape research; document findings and update research-log
```

---

### Source Attribution Checklist

**Step 1: Identify and count unsourced claims**

For each entry in module-content-map:

- [ ] Verify field source_id contains valid reference to research-log entry
- [ ] If source_id is missing or invalid, flag as "unsourced"

**Check method:** For each data point in module-content-map, verify source_id can be resolved to a research-log entry_id.

**Threshold:** ≤2 unsourced claims = PASS; ≥3 unsourced claims = FAIL

**Example failure:**
```
Module-content-map entries (D3 Business Model):
1. "Revenue model: SaaS subscription, $99/month per user"
   - source_id: "research-003-submission" ✓
2. "Customer acquisition cost estimated at $450"
   - source_id: missing ← UNSOURCED
3. "Gross margin projected at 72%"
   - source_id: missing ← UNSOURCED
4. "3-year financial model with detailed unit economics"
   - source_id: "research-008-company-data" ✓
5. "Market opportunity in HR tech estimated at $40B"
   - source_id: "research-012-analyst-report" ✓
6. "Competitor pricing averages $150/month"
   - source_id: missing ← UNSOURCED

Status: 3 unsourced claims ≥ threshold of 3 → FAIL
Fix: Either (a) source each claim from research-log, or (b) remove unsourced claims
```

---

## Section 3: Cross-Module Conflict Detection

### Numerical Claim Conflicts Checklist

**Step 1: Identify critical numerical claims across domains**

Extract quantitative claims and their domains:

- [ ] TAM (Target Addressable Market) — typically Domain 1
- [ ] Revenue (historical and projected) — typically Domain 5 and Domain 7
- [ ] Customer metrics (count, CAC, LTV) — typically Domain 4, Domain 5
- [ ] Unit economics (margins, ratios) — typically Domain 3, Domain 7
- [ ] Team size and cost — typically Domain 6, Domain 7

**Check method:** Search module-content-map for numerical values; note which domain they appear in; cross-reference.

---

**Step 2: Check for conflicts in scale**

Compare quantitative claims across domains:

- [ ] TAM claim in D1 vs. revenue projections in D7: Do projections align with TAM? (If D1 TAM = $1B and D7 projects $500M revenue at 50% market share, this is consistent. If D7 projects $100B revenue, this is inconsistent.)
- [ ] Revenue growth rate in D5 vs. D7: Do historical growth rates in D5 match projection assumptions in D7?
- [ ] Customer count in D5 vs. D3 CAC: Does customer acquisition cost make sense given customer count growth?

**Example conflict:**
```
Claim A (Domain 1): "TAM for cloud HR software in North America is $8B"
Claim B (Domain 7): "Our 5-year financial model projects $5B in revenue by Year 5"
Apparent conflict: Can a $8B TAM support $5B in revenue (62.5% market share)?
Resolution: Check if projections assume geographic expansion. If Year 5 projections assume global (not just North America), TAM may be $30B+ globally, making $5B achievable.
Fix: Update narrative to clarify TAM definition (North America vs. global) in both D1 and D7.
```

---

**Step 3: Flag and document conflicts**

For each detected conflict:

- [ ] Record conflict_id, conflicting claims, affected modules, severity (critical / moderate / minor)
- [ ] Determine if conflict is resolvable (documentation/clarification) or analytical (genuine inconsistency)
- [ ] If resolvable, document the resolution
- [ ] If analytical inconsistency, escalate to assessor

**Example documentation:**
```
CONFLICT-001:
Conflicting claims:
- D5 (Traction): "Company has 150 paying customers with $25K average annual revenue"
- D7 (Financial): "Projected ARR = $4.2M by end of Year 1"
Calculation: 150 customers × $25K = $3.75M (not $4.2M)
Variance: $450K gap (12% discrepancy)
Severity: Moderate
Resolution: Request clarification on either (a) customer count, (b) ACV, or (c) Year 1 projection.
Possible explanations: Upwelling of new customers not yet counted in "150 paying customers" figure; ACV expected to increase to $28K by year-end.
```

---

### Logical Claim Conflicts Checklist

**Step 1: Scan narrative for logical contradictions**

Read through assessment narrative looking for contradictory statements:

- [ ] Domain emphasis contradicts framework weights (narrative emphasizes A but framework weighs B heavily)
- [ ] Team expertise vs. product: Does team background match product complexity? (e.g., team with no hardware experience building complex hardware device)
- [ ] Market size vs. customer acquisition strategy: Does acquisition strategy (e.g., enterprise sales) fit market definition (e.g., SMB market)?
- [ ] IP/defensibility claims: Does claimed defensibility align with actual IP portfolio?

**Check method:** Skim assessment narrative for conditional statements ("although," "despite," "despite no experience in"); review justifications; identify contradictions.

**Example contradiction:**
```
Domain 2 (Product): "Technical architecture leverages proprietary ML model trained on unique dataset"
Domain 10 (Legal): "No patents filed; IP protection relies on trade secret status of dataset"
Domain 8 (Risk): "Key risk: If competitor obtains dataset, defensibility is eliminated"
Logical issue: If IP protection is trade secret only (not patents), and dataset access is the moat, then dataset security is critical single point of failure.
Resolution: Confirm risk mitigation strategy (data security, access controls, etc.) or document trade secret risk in go/no-go determination.
```

---

## Section 4: Missing Required Content Checklist

### Hard-Blocker Module Completeness Checklist

**Step 1: Identify hard-blocker modules for the identified stage**

List all hard-blocker modules for the stage:

**Pre-Seed hard-blockers:**
- [ ] Problem Validation (D1) completeness ≥0.5
- [ ] Founder Background (D6) completeness ≥0.5

**Seed hard-blockers:**
- [ ] Problem Validation (D1) completeness ≥0.5
- [ ] Revenue or Traction Evidence (D5) completeness ≥0.4
- [ ] Team Execution Evidence (D6) completeness ≥0.5

**Series A hard-blockers:**
- [ ] Unit Economics (D3) completeness ≥0.6
- [ ] Revenue Consistency (D5) completeness ≥0.6
- [ ] Financial Model (D7) completeness ≥0.6
- [ ] Management Team (D6) completeness ≥0.5

**Series B hard-blockers:**
- [ ] Unit Economics (D3) completeness ≥0.7
- [ ] Revenue Performance (D5) completeness ≥0.7
- [ ] Financial Accounts (D7) completeness ≥0.7
- [ ] Management and Organizational (D6) completeness ≥0.6

---

**Step 2: Verify each hard-blocker module has completeness ≥ threshold**

- [ ] For each hard-blocker module, check completeness score
- [ ] If completeness < threshold, flag as FAIL

**Check method:** Query module-content-map for each hard-blocker module; retrieve completeness score.

**Example failure:**
```
Stage: Series A
Hard-blocker: Financial Model (D7) with minimum threshold 0.6
Actual completeness score: 0.3
Status: FAIL
Reason: Company provided high-level financial summary only; 3-year detailed model not available
Action: Escalate to assessor: Either request detailed model from company OR accept no-go determination on financial readiness
```

---

### Go/No-Go Gate Determination Checklist

**Step 1: Verify go_no_go_gates JSON is complete**

Check go/no-go determination structure:

```json
{
  "go_no_go_gates": [
    {
      "gate_id": "hard_blocker_1",
      "gate_name": "[module name]",
      "result": "pass | fail | unresolved",
      "justification": "[reason]",
      "severity": "critical | high | medium | low"
    }
  ],
  "overall_determination": "go | conditional_go | no_go",
  "determination_confidence": "high | medium | low"
}
```

**Checks:**
- [ ] All hard-blocker modules have gate entries
- [ ] Every gate has result = "pass," "fail," or "unresolved" (not blank or other value)
- [ ] Every gate has justification (not empty)
- [ ] overall_determination is populated (not blank)
- [ ] No gates have result = "unresolved" without escalation plan

**Example failure:**
```
Gate entries: 5 hard-blockers
- D3 Unit Economics: result = "pass"
- D5 Traction: result = "fail" (no revenue)
- D6 Management: result = "pass"
- D7 Financial: result = "unresolved" ← Issue: unresolved gate with no escalation
- D10 Legal: result = "pass"

overall_determination: "conditional_go"

Issue: Financial gate is unresolved but overall_determination is conditional_go (inconsistent)
Fix: Either (a) resolve Financial gate (pass/fail) OR (b) change overall_determination to "unresolved" and escalate
```

---

**Step 2: Verify determination logic is consistent**

- [ ] If ANY gate = "fail," overall_determination should be "no_go" (unless explicitly overridden with reasoning)
- [ ] If ALL gates = "pass," overall_determination should be "go"
- [ ] If some gates = "pass" and some = "fail," overall_determination should be "no_go" or "conditional_go" (with clear conditions documented)

**Example consistency check:**
```
Gates:
- D3 Unit Economics: fail (no clear unit economics)
- D5 Traction: pass (meaningful revenue and customer traction)
- D6 Management: pass (strong team)
- D7 Financial: pass (reasonable projections)

Determination: "conditional_go" with condition = "Unit economics must be demonstrated before investment"

Status: Consistent. Fail gate is acknowledged; conditional_go reflects acceptance with clear condition.
```

---

## QA/QC Sign-Off Template

Use this template to document completion of holistic QA/QC:

```
HOLISTIC QA/QC SIGN-OFF

Assessment ID: [assessment_id]
Stage Assessed: [pre-seed | seed | series-a | series-b | growth]
Assessment Completion Date: [date]
QA/QC Completion Date: [date]

CHECKLIST COMPLETION:

Check 1: Internal Consistency Checks
  [ ] Score-to-Gap Consistency: PASS / FAIL
  [ ] Track and Fit-to-Purpose Consistency: PASS / FAIL
  [ ] Gap Type Classification Validity: PASS / FAIL
  [ ] Dependency Map Completeness: PASS / FAIL
  Issues identified: [count] / Resolution status: [resolved | escalated]

Check 2: Research Coverage Checks
  [ ] Research Attempt Completeness: PASS / FAIL
  [ ] Research Category Coverage: PASS / FAIL (categories: 1=✓, 2=✓, 3=✓, 4=✓, 5=✗)
  [ ] Source Attribution: PASS / FAIL (unsourced claims: [count])
  Issues identified: [count] / Resolution status: [resolved | escalated]

Check 3: Cross-Module Conflict Detection
  [ ] Numerical Claim Conflicts: PASS / FAIL (conflicts: [count])
  [ ] Logical Claim Conflicts: PASS / FAIL (conflicts: [count])
  Issues identified: [count] / Resolution status: [resolved | escalated]

Check 4: Missing Required Content
  [ ] Hard-Blocker Module Completeness: PASS / FAIL
  [ ] Go/No-Go Gate Determination: PASS / FAIL
  Issues identified: [count] / Resolution status: [resolved | escalated]

OVERALL QA/QC RESULT: PASS / FAIL / CONDITIONAL_PASS

Critical issues requiring escalation: [list issue IDs]
Minor issues flagged but accepted: [list issue IDs]

Approved for report generation: YES / NO

QA/QC Agent: [name/agent_id]
Signature: [timestamp]
```

