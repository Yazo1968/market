# Domain-Level QA/QC Checklist

This checklist is used after each domain assessment is complete, before the output is passed downstream to the next domain or to report generation.

## Section 1: Finding Completeness Checks

### Module Finding Coverage Checklist

**Step 1: Verify every active module has a finding**

For the domain being assessed:

- [ ] List all active modules in the domain framework (from framework configuration)
- [ ] Count modules with finding_classification entry in domain-finding JSON
- [ ] Compare counts: active_modules = modules_with_findings

**Check method:** Extract domain-finding JSON; count elements; compare to framework module list.

**Threshold:** All active modules must have finding_classification entry. 0 missing = PASS; ≥1 missing = FAIL

**Example:**
```
Domain: D3 (Business Model)
Active modules in framework: D3-revenue-model, D3-unit-economics, D3-pricing-strategy, D3-gross-margin (4 modules)

Domain-finding JSON entries:
1. D3-revenue-model: finding_classification = "confirmed"
2. D3-unit-economics: finding_classification = "fragmentary"
3. D3-pricing-strategy: finding_classification = "unverifiable"
[Missing: D3-gross-margin]

Status: FAIL
Issue: Module D3-gross-margin has no finding_classification
Fix: Add finding entry for D3-gross-margin (even if "no data available" or "unassessed")
```

---

**Step 2: Verify finding structure completeness**

For each finding_classification entry:

- [ ] finding_classification has conclusion field (not empty)
- [ ] conclusion field is substantive (not "unknown" or "N/A")
- [ ] finding has quality_score (0.0–1.0)
- [ ] finding has evidence_sources array (not empty)

**Check method:** For each finding, verify required fields are populated.

**Example failure:**
```
Finding: D6-team-composition
- conclusion: "N/A" ← FAIL (empty/meaningless)
- quality_score: 0.0
- evidence_sources: []

Fix: Either (a) populate with actual assessment conclusion and evidence, or (b) use explicit placeholder like "assessment deferred" with justification
```

---

### Evidence Source Attribution Checklist

**Step 1: Verify every finding has at least one evidence source**

For each finding_classification:

- [ ] evidence_sources array is not empty
- [ ] Each evidence_source contains source_id, evidence_type, and source_quote (if available)
- [ ] Each source_id references valid research-log entry_id

**Check method:** For each finding, examine evidence_sources array; validate each source_id exists in research-log.

**Threshold:** Every finding must have ≥1 evidence_source. Finding with 0 sources = FAIL

**Example failure:**
```
Finding: D4-go-to-market-strategy
- conclusion: "GTM strategy is B2B enterprise sales with focus on Fortune 500 targets"
- quality_score: 0.7
- evidence_sources: [] ← FAIL (empty)

Issue: Conclusion is present but no source attribution
Fix: Add evidence_source entries; examples:
  - source_id: "research-004-submission", evidence_type: "from_submission", source_quote: "Our enterprise sales strategy targets CFO spending..."
  - source_id: "research-012-founder-interview", evidence_type: "verified", source_quote: "We've already engaged 3 CFO advisors..."
```

---

**Step 2: Validate source_id references**

For each evidence_source.source_id:

- [ ] Cross-reference source_id in research-log
- [ ] Confirm research-log entry exists with matching entry_id
- [ ] If source_id cannot be found, flag as "broken reference"

**Check method:** For each evidence_source, query research-log by source_id; verify match.

**Example failure:**
```
Finding evidence_source:
- source_id: "research-047-press-article"
Research-log search: No entry with entry_id = "research-047-press-article"
Available entries: research-001 through research-045 (max ID = 045)

Issue: source_id references non-existent research-log entry
Fix: Either (a) locate correct source_id in research-log and correct reference, or (b) remove evidence_source with broken reference
```

---

### Confirmation Classification Integrity Checklist

**Step 1: Verify finding classification consistency with evidence types**

Evidence types in research-log:

| Evidence Type | Definition |
|---|---|
| Verified (V) | Third-party, objective, independent confirmation |
| Corroborated (C) | Multiple sources align; mutually supportive |
| Speculative (S) | Single source, self-reported, or assumption-based |
| Contradicted (X) | Evidence contradicts the claim |
| Unverifiable (U) | No external evidence available; claim cannot be verified |

**Finding Classification Logic:**

| Finding Classification | Required Evidence Types | Forbidden Evidence Types |
|---|---|---|
| "confirmed" or "corroborated" | ≥1 V or C | Must NOT include X (contradicted) |
| "unverifiable" | Must have U; no V or C | Must NOT include V or C |
| "contradicted" | ≥1 X | Must NOT include V or C as primary evidence |
| "fragmentary" | S or mixture | Can include U or V if partial |

---

**Step 2: Validation procedure**

For each finding_classification with result = "confirmed" or "corroborated":

- [ ] Examine evidence_sources array
- [ ] Count Verified (V) sources
- [ ] Count Corroborated (C) sources
- [ ] Verify: (V_count + C_count) ≥ 1
- [ ] Verify: X_count (contradicted) = 0

**Example failure:**
```
Finding: D1-market-size-tam
- conclusion: "TAM for cloud HR software in North America is $8B (CONFIRMED)"
- evidence_sources:
  1. source_id: "research-003-submission", evidence_type: "speculative", source_quote: "Company estimates TAM at $8B"
  2. source_id: "research-015-analyst-report", evidence_type: "corroborated", source_quote: "Gartner estimates $7.5B"

Analysis: 1 Corroborated + 0 Verified = 1 C source → "confirmed" classification is appropriate ✓
Status: PASS
```

**Example failure:**
```
Finding: D5-revenue-growth
- conclusion: "Company revenue is declining month-over-month (CONFIRMED)"
- evidence_sources:
  1. source_id: "research-008-submission", evidence_type: "speculative", source_quote: "We expect growth to slow due to market saturation"

Analysis: 0 Verified + 0 Corroborated; only Speculative source
Issue: Classification "confirmed" contradicted by evidence_type "speculative"
Fix: Change classification to "fragmentary" or "unverifiable" to match evidence quality
```

---

**Step 3: Special case — contradicted findings**

For any finding with evidence_type = "contradicted":

- [ ] finding_classification should be "contradicted" or "conflicting"
- [ ] Justification should explain the contradiction
- [ ] Resolution should be documented (accepted, escalated, or unresolved)

**Example:**
```
Finding: D6-founder-startup-experience
- conclusion: "Founder has prior startup experience"
- evidence_sources:
  1. source_id: "research-010-submission", evidence_type: "from_submission", claim: "Founded TechStartup Inc in 2018"
  2. source_id: "research-020-linkedin-search", evidence_type: "corroborated", source_quote: "LinkedIn profile shows TechStartup Inc 2018–2021"
  3. source_id: "research-025-startup-records", evidence_type: "verified", source_quote: "TechStartup Inc dissolved 2021; no evidence of successful exit"

Classification: "Partially confirmed with caveat: Founder has startup founding experience but company did not achieve successful outcome"
Status: PASS (contradiction is documented and resolved)
```

---

## Section 2: Attribution Integrity Checks

### Submission-Derived vs. Independent Finding Classification Checklist

**Step 1: Classify each finding's origin**

For each finding_classification:

- [ ] Specify origin: "from_submission" or "independently_generated"
- [ ] If from_submission: finding is restatement or verification of company's claim
- [ ] If independently_generated: finding is derived from external evidence without primary reference to submission

**Check method:** For each finding, review primary evidence source; if submission document is the primary source, classify as "from_submission"

**Example classifications:**
```
Finding 1 (Unit Economics):
- Claim: "LTV:CAC ratio = 5.2:1"
- Evidence source primary: "research-006-submission" (company financial data)
- Classification: "from_submission" ✓

Finding 2 (Market Size):
- Claim: "Cloud HR market is estimated at $8B annually"
- Evidence sources: "research-015-gartner-analyst-report", "research-018-idc-report"
- Classification: "independently_generated" ✓

Finding 3 (Customer Traction):
- Claim: "50 enterprise customers with 80% retention"
- Evidence: "research-007-submission" + "research-019-customer-calls" (independent verification calls)
- Classification: "from_submission" (with independent corroboration) ✓
```

---

### Independent Finding Validation Checklist

**Only applicable if assessment is operating in Deep Independent Analysis mode**

**Step 1: Verify findings marked "independently_generated" contain substantive independent work**

Sample findings marked "independently_generated":

- [ ] Select 3 findings with independent_generated = true
- [ ] For each finding, examine evidence_sources
- [ ] Verify that primary evidence source is NOT the submission document
- [ ] Verify that conclusion represents independent analytical work, not restatement

**Check method:** For each independent finding, ask: "If I removed the submission, would this finding still be valid based on external evidence alone?" If answer is NO, finding is improperly classified.

---

**Step 2: Validate substantive independent work**

Threshold for valid independent finding:

**Invalid independent finding (restatement):**
```
Finding: Product market fit evidence
- Submission claim: "We have product-market fit with 85% customer satisfaction"
- Independent finding: "Customer satisfaction is strong at 85%" (source: company self-reported survey)
- Issue: Merely restating submission claim; no independent validation
- Fix: Reclassify to "from_submission" OR add external evidence (e.g., analyst review, customer reference calls)
```

**Valid independent finding (substantive analysis):**
```
Finding: Product market fit evidence
- Submission claim: "We have product-market fit with 85% customer satisfaction"
- Independent research: Conducted 5 customer reference calls; 4/5 confirmed high satisfaction; average NPS = 42
- Finding: "Product-market fit indicators are moderate but not exceptional; NPS of 42 suggests room for improvement despite claimed 85% satisfaction"
- Issue: This is independent, analytical work with original findings
- Status: Valid independent finding ✓
```

---

**Step 3: Assessment mode compliance**

If assessment_mode = "Deep Independent Analysis":

- [ ] Majority of findings should be independently_generated (ideally >60% of findings)
- [ ] Findings that are from_submission should represent facts (e.g., "company was founded in 2019") not interpretations
- [ ] Interpretive findings (quality assessments, risk analysis) should be independently_generated

**Example failure:**
```
Assessment mode: "Deep Independent Analysis"
Finding distribution:
- independently_generated: 15 (35%)
- from_submission: 28 (65%)

Issue: Assessment claims deep independent analysis but majority of findings are from submission
Fix: Either (a) recategorize assessment_mode to "Verification Analysis" OR (b) conduct additional independent research and reclassify findings
```

---

## Section 3: Cross-Domain Flag Accuracy Checks

### Dependency Flag Validity Checklist

**Step 1: Verify cross-domain flags reference active domains**

For each cross_domain_flag in domain-finding output:

- [ ] Extract target_domain_id from flag
- [ ] Verify target_domain_id exists in framework as active domain
- [ ] If domain is inactive/deactivated, flag is invalid

**Check method:** For each cross_domain_flag, query framework domain list; verify target_domain_id is present and active.

**Threshold:** All cross_domain_flags must reference active domains. Invalid flags = FAIL

**Example failure:**
```
Domain D3 (Business Model) finding includes cross_domain_flag:
- flag_id: "xdep-001"
- description: "Unit Economics depend on accurate TAM estimation"
- target_domain_id: "D11-market-opportunities" ← Domain D11 doesn't exist

Issue: Cross-domain flag references non-existent domain
Fix: Either (a) correct target_domain_id to "D1" (Market and Opportunity) OR (b) remove flag if dependency is invalid
```

---

**Step 2: Verify flag justification is meaningful**

For each cross_domain_flag:

- [ ] flag_description explains why the dependency exists
- [ ] description is specific to the assessment context (not generic)
- [ ] description would be useful to assessor of target domain

**Example failure:**
```
Flag description: "This depends on that" ← Too vague; not useful
Fix: "Unit Economics (D3) assumes TAM penetration of 5%; if D1 reassesses TAM downward to $2B (from $5B), revenue projections must be recalibrated"
```

---

### Circular Dependency Detection Checklist

**Step 1: Build cross-domain flag graph**

Create a directed graph where:
- Nodes = active domains
- Edges = cross_domain_flags
- Direction: from source domain to target_domain_id

**Step 2: Detect cycles**

- [ ] Perform depth-first search (DFS) or topological sort
- [ ] Flag any cycles detected (A → B → C → A)

**Example:**
```
Domain D1 flags: D2, D3
Domain D2 flags: D4, D5
Domain D3 flags: D1 ← Creates cycle: D1 → D3 → D1

Cycle detected: D1 ↔ D3
```

---

**Step 3: Classify and escalate cycles**

**Legitimate feedback loops** (not true cycles; strategic dependencies):
- "Market dynamics affect Product roadmap; Product improvements affect Market positioning"
- Usually expressed as: "D1 informs D2, D2 can trigger D1 re-assessment"
- Not an error; document in framework construction log

**Problematic cycles** (logical errors):
- "Traction depends on Financial projections; Financial projections depend on Traction"
- Circular logic; indicates assessment error
- Must be escalated for resolution

---

## Section 4: Assessment Mode Compliance Checks

### Deep Independent Analysis Mode Compliance Checklist

**Only applicable if assessment_mode = "Deep Independent Analysis"**

**Step 1: Verify findings represent independent analysis**

- [ ] Sample 5 findings across the domain
- [ ] For each finding, ask: "Is this finding original to this assessment, or is it a restatement of company claims?"

**Check method:** Review finding conclusion and evidence sources; verify substantial independent work is present.

---

**Step 2: Verify use of external references and benchmarks**

In Deep Independent Analysis mode, findings should reference:

- [ ] Industry benchmarks (e.g., "SaaS companies in this segment average 40% gross margins; this company claims 45%")
- [ ] Comparable companies (e.g., "Competitor X has similar features and prices at $X; this company prices at $Y")
- [ ] Third-party validation (e.g., "Gartner report identifies these as key criteria; company addresses 3 of 5")
- [ ] Expert assessment (e.g., "Advisory board member from domain notes...")

**Example failure:**
```
Assessment mode: Deep Independent Analysis
Finding: "Product roadmap includes AI-powered analytics"
Analysis: No independent assessment of AI capability, market positioning, or competitive differentiation
Issue: Finding merely confirms submission claim without analytical depth
Fix: Investigate AI market, competitive positioning, technical feasibility; provide independent assessment
```

---

**Step 3: Verification**

- [ ] ≥60% of findings should include external references or benchmarks
- [ ] Findings should contain original analysis or synthesis, not just compilation of facts

---

### Verification Analysis Mode Compliance Checklist

**Only applicable if assessment_mode = "Verification Analysis"**

**Step 1: Verify all major claims have verification status**

For each major submission claim in the domain:

- [ ] Claim has explicit verification status
- [ ] Status = "verified," "contradicted," "unverifiable," or "partially verified"
- [ ] No claim left with status = "unknown" or blank

**Check method:** Extract key claims from submission document for this domain; match each to a finding with verification status.

---

**Step 2: Verify status is justified**

For each claim verification status:

- [ ] "verified" status supported by Verified (V) or Corroborated (C) evidence
- [ ] "contradicted" status supported by Contradicted (X) evidence
- [ ] "unverifiable" status justified (e.g., "no external data available")
- [ ] "partially verified" status explains which parts verified vs. unverifiable

**Example:**
```
Submission claim: "We have achieved product-market fit with 85% NPS"
Verification status: "Partially verified"
Justification: "Company provided internal NPS survey (unverified); independent customer calls with 3 of 10 customers show strong satisfaction but diverse opinions on fit (partially verified). Claim of universal PMF is unverifiable without full customer cohort analysis."
Status: PASS (status is justified and explains nuance)
```

---

## Domain-Level QA/QC Sign-Off Template

```
DOMAIN-LEVEL QA/QC SIGN-OFF

Assessment ID: [assessment_id]
Domain Assessed: [domain_id] - [domain_name]
Assessment Completion Date: [date]
QA/QC Completion Date: [date]

CHECKLIST COMPLETION:

Check 1: Finding Completeness
  [ ] Module Finding Coverage: PASS / FAIL (modules: [count] / findings: [count])
  [ ] Evidence Source Attribution: PASS / FAIL (unsourced findings: [count])
  [ ] Confirmation Classification Integrity: PASS / FAIL (conflicts: [count])
  Issues identified: [count] / Resolution status: [resolved | escalated]

Check 2: Attribution Integrity
  [ ] Submission-Derived vs. Independent Classification: PASS / FAIL
  [ ] Independent Finding Validation: PASS / FAIL (if Deep IA mode)
  Issues identified: [count] / Resolution status: [resolved | escalated]

Check 3: Cross-Domain Flag Accuracy
  [ ] Dependency Flag Validity: PASS / FAIL (invalid flags: [count])
  [ ] Circular Dependency Detection: PASS / FAIL (cycles: [count], legitimate: [count])
  Issues identified: [count] / Resolution status: [resolved | escalated]

Check 4: Assessment Mode Compliance
  [ ] Deep Independent Analysis Mode: PASS / FAIL (if applicable)
  [ ] Verification Analysis Mode: PASS / FAIL (if applicable)
  Issues identified: [count] / Resolution status: [resolved | escalated]

OVERALL QA/QC RESULT: PASS / FAIL / CONDITIONAL_PASS

Critical issues requiring escalation: [list issue IDs]
Minor issues flagged but accepted: [list issue IDs]

Approved for downstream processing: YES / NO

QA/QC Agent: [name/agent_id]
Signature: [timestamp]
```

