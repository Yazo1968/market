---
name: qaqc-rubric
description: >
  This skill should be used by the QA/QC agent when running quality checks on pre-assessment outputs
  (holistic) or domain assessment outputs (domain-level). Covers gap detection, discrepancy identification,
  conflicting information checks, fix instruction format, and escalation criteria. Trigger phrases:
  "QA/QC check", "quality check", "validate outputs", "check for gaps", "check for discrepancies",
  "qaqc rubric", "holistic QA", "domain QA".
version: 0.1.0
---

# QA/QC Rubric

This rubric defines quality assurance and quality control procedures for the startup assessment framework. Two operating modes apply: holistic (end of pre-assessment) and domain-level (after each domain in assessment phase). Both modes follow systematic check categories and escalation criteria.

## Mode 1: Holistic QA/QC (Pre-Assessment)

Run once after all modules are scored and the gap register and dependency map are produced, but before report generation.

### Check 1: Internal Consistency Checks

**Check 1.1 — Score-to-Gap Consistency**

Verify that completeness and quality scores align with gap register classification:

- Every module scored 0 (zero completeness) must appear in the gap register as "absent"
- Every module scored >0 and <0.5 (completeness) must appear as "fragmentary" in gap type
- Every module scored ≥0.8 completeness must NOT be listed as "critical" in gap register
- Inverse: if gap register lists a module as "absent," verify completeness score is 0

**Failure condition:** Module appears in gap register with status inconsistent with scored completeness

**Resolution:** Ask QA/QC agent to reconcile score and gap classification

---

**Check 1.2 — Track and Fit-to-Purpose Consistency**

Verify that assessment justifications and scores are coherent with stage calibration:

- A pre-seed submission scored with high "Stage Appropriateness" on Series B financial content is internally inconsistent
- Example: Pre-seed company with Series B-level financial model (5-year detailed projections with cohort analysis) should be flagged: "Pre-seed company demonstrating Series B financial rigor; either mispositioned or exceptionally well-prepared"
- Series A submission lacking any revenue should be flagged inconsistently if scored as "meeting Series A traction expectations"

**Failure condition:** Assessment justification contradicts stage calibration or internal logic

**Resolution:** Escalate to assessor with specific contradiction flagged

---

**Check 1.3 — Gap Type Classification Validity**

Verify gap type classifications (absent, fragmentary, resolvable, unresolvable) are supported by research effort:

- Module classified as "absent-externally-resolvable" must have a research attempt logged in the research-log for it
- If module is classified as "absent" but zero research attempts exist, classification is invalid; must be classified as "absent-unresolvable" or re-attempt research
- Module classified as "fragmentary-with-mitigation" must have explicit mitigation strategy documented

**Failure condition:** Gap classification claimed but research attempt absent; or classification conflicts with research effort

**Resolution:** Either log missing research attempt or correct gap classification

---

**Check 1.4 — Dependency Map Completeness**

Verify dependency map includes all active domains:

- Every active domain in the framework must appear as a node in the dependency map
- Any domain listed in "Secondary" or "Primary" status but absent from dependency map is an error
- Circular dependencies (Domain A → B → C → A) must be detected and flagged

**Failure condition:** Active domain missing from dependency map or circular dependency present

**Resolution:** Rebuild or correct dependency map; escalate if circular dependency is strategic (e.g., "product quality affects traction which affects market positioning which affects product roadmap")

---

### Check 2: Research Coverage Checks

**Check 2.1 — Research Attempt Completeness**

Verify every active module has research documented:

- Count active modules in the framework
- Count modules with at least one research attempt in research-log
- Flagged domains: any active module with zero research attempts

**Failure condition:** Active module exists with no research attempts logged

**Resolution:** Log at least one research attempt (even if "submission document searched; no external data found") or deactivate module if not applicable

---

**Check 2.2 — Research Category Coverage**

Verify that all five required research categories are represented in the research-log:

Five required research categories:
1. Submission Document (internal)
2. Company Website and Public Marketing
3. Third-Party Validation (press, analyst reports, awards, certifications)
4. Founder/Team Background Research
5. Market and Competitive Landscape Research

**Failure condition:** Any of the five categories has zero entries across entire research-log

**Resolution:** Conduct research in missing category before finalizing pre-assessment

---

**Check 2.3 — Missing Source Attribution**

Verify all data points in module-content-map have source attribution:

- Every claim, metric, or finding in module-content-map must reference at least one source_id from research-log
- Claims without source attribution are flagged as "unsourced"
- Unsourced claims <3 total: acceptable if brief contextual statements
- Unsourced claims ≥3 total: flag as QA/QC failure

**Failure condition:** ≥3 unsourced claims in module-content-map

**Resolution:** Either add source attribution (trace to research-log entry) or remove unsourced claim

---

### Check 3: Cross-Module Conflict Detection

**Check 3.1 — Numerical Claim Conflicts**

Scan all modules for quantitative claim conflicts:

- If Domain 1 (Market) reports TAM of $5B but Domain 7 (Financial Performance) revenue projections imply TAM of $500M (or $50B), this is a conflict
- If Domain 2 (Product) reports MVP stage but Domain 5 (Traction) reports $2M annual revenue, verify timing (product could have gone from MVP to revenue in 6 months)
- If Domain 3 (Business Model) identifies 30% gross margin but Domain 7 projects 60% gross margin at scale, document the assumed improvement basis

**Failure condition:** Numerical claim conflict detected without explanation or documented assumption

**Resolution:** Flag conflict and request reconciliation. If resolvable (e.g., "revenue projection assumes price increase from $100 to $200 at scale"), document assumption. If irreconcilable, escalate.

---

**Check 3.2 — Logical Claim Conflicts**

Scan for logical contradictions:

- Domain 1 claims "saturated market with limited growth" but Domain 4 (Go-to-Market) claims "significant white space for new entrants"
- Domain 2 claims "product has no defensible IP" but Domain 10 (Legal) claims "3 patents granted and 2 pending"
- Domain 6 claims "founder has no prior startup experience" but Domain 5 claims "demonstrated ability to close enterprise deals" (possible if founder has corporate sales background)

**Failure condition:** Logical contradiction detected without contextual explanation

**Resolution:** Flag and request clarification. Resolve via documented evidence or assessor judgment.

---

### Check 4: Missing Required Content

**Check 4.1 — Hard-Blocker Module Completeness**

Verify all hard-blocker modules have completeness score > 0:

- Hard-blocker modules (as defined per stage calibration) must have completeness ≥0.3 minimum (some evidence collected, even if fragmentary)
- Hard-blocker module with completeness = 0 means data cannot be assessed; must be escalated

**Failure condition:** Hard-blocker module scored at 0 completeness

**Resolution:** Either locate data to score module above 0, or escalate to assessor with justification for zero score (e.g., "founder background not made available despite multiple requests")

---

**Check 4.2 — Go/No-Go Gate Determination**

Verify go/no-go determination JSON is complete:

```json
{
  "go_no_go_gates": [
    {
      "gate_id": "hard_blocker_1",
      "gate_name": "[module name]",
      "result": "pass|fail|unresolved",
      "justification": "[reason]"
    }
  ],
  "overall_determination": "go|conditional_go|no_go"
}
```

**Failure condition:** Any gate has result "unresolved" or overall determination is missing

**Resolution:** Complete all gate determinations or escalate unresolved gates with explanation

---

## Mode 2: Domain-Level QA/QC (Assessment Phase)

Run after each domain assessment is complete before output is passed downstream to next domain or to report generation.

### Check 1: Finding Completeness

**Check 1.1 — Module Finding Coverage**

Verify every active module in the domain has a finding:

- Count active modules in domain framework
- Count modules with finding_classification in domain-finding JSON
- Flagged modules: any active module without finding_classification

**Failure condition:** Active module in domain framework has no finding_classification recorded

**Resolution:** Create finding_classification for missing module, even if "no data collected; module remains unscored"

---

**Check 1.2 — Evidence Source Attribution**

Verify every finding has at least one evidence source:

- Every finding_classification must list at least one evidence_source
- Each evidence_source must reference valid source_id from research-log
- Finding without evidence_source is flagged as "unsourced"

**Failure condition:** Finding exists without evidence_source OR referenced source_id does not exist in research-log

**Resolution:** Either add valid evidence_source or escalate as unsupported finding

---

**Check 1.3 — Confirmation Classification Integrity**

Verify findings classified as "confirmed" or "corroborated" have appropriate evidence:

- Finding marked "confirmed" must have at least one Verified (V) or Corroborated (C) evidence_source
- Finding marked "unverifiable" must NOT have V or C evidence sources
- Finding marked "contradicted" must have contradicting evidence source

**Failure condition:** Finding classification contradicts evidence source types (e.g., finding marked "confirmed" with only Speculative sources)

**Resolution:** Correct finding classification to match evidence sources, or add/change evidence source

---

### Check 2: Attribution Integrity

**Check 2.1 — Submission-Derived vs. Independent**

Verify distinction between submission claims and independently generated findings:

- Every finding_classification must indicate source origin: "from_submission" or "independently_generated"
- Independently generated findings must cite external evidence (not the submission document itself)

**Failure condition:** Finding marked "independently_generated" but only sources are the submission document

**Resolution:** Reclassify as "from_submission" or add external evidence source

---

**Check 2.2 — Independent Finding Validation**

If assessment is Deep Independent Analysis mode, verify findings are truly independent:

- Sample 3 findings marked "independently_generated"
- Verify each has substantive external evidence (not restating submission claim)
- Example of INVALID independent finding: "Submission claims product has patent protection; research confirms this"
- Example of VALID independent finding: "Submission claims product has patent protection; patent search reveals patent issued 2023, covering core technology, with 17-year remaining term"

**Failure condition:** Findings marked "independently_generated" are functionally restatements of submission claims

**Resolution:** Reclassify findings to "from_submission" with validation notes, OR request assessor recollect independent evidence

---

### Check 3: Cross-Domain Flag Accuracy

**Check 3.1 — Dependency Flag Validity**

Verify cross-domain dependency flags reference active domains:

- Every cross_domain_flag must reference a target_domain_id
- Target domain must be active in the current framework (not deactivated)
- Flagged issue: cross-domain flag references inactive domain

**Failure condition:** Cross-domain flag references domain not in active framework

**Resolution:** Either correct target_domain_id or remove flag if target domain is inactive

---

**Check 3.2 — Circular Dependency Detection**

Detect circular dependency flags:

- If Domain A flags Domain B as dependency
- AND Domain B flags Domain A as dependency
- This is a circular dependency

**Failure condition:** Circular dependency detected

**Resolution:** Escalate to assessor for strategic resolution (e.g., "Market risk affects Go-to-Market strategy which affects Market positioning" is legitimate feedback loop, not a blocker)

---

### Check 4: Assessment Mode Compliance

**Check 4.1 — Deep Independent Analysis Mode**

If assessment is operating in Deep Independent Analysis mode:

- Findings must represent independently developed views, not verification of submission claims
- Sample findings: verify that conclusions are not simply "submission claim X is correct"
- Check for evidence of analytical work: comparison to benchmarks, industry standards, competitive analysis

**Failure condition:** Assessment is labeled "Deep Independent Analysis" but findings are primarily verification-focused

**Resolution:** Reclassify to "Verification Analysis" mode OR request reassessment with deeper independent analysis

---

**Check 4.2 — Verification Analysis Mode**

If assessment is operating in Verification Analysis mode:

- Every major submission claim should have explicit verification status
- Status options: "verified/confirmed," "contradicted," "unverifiable," "partially verified"
- Check for completeness: no claim left with status "unknown"

**Failure condition:** Major submission claim has no verification status recorded

**Resolution:** Add verification status or document reason claim cannot be verified

---

## Mode 3: AI Bias Testing Protocol (EU AI Act / NIST AI RMF Compliance)

Run as part of holistic QA/QC (Mode 1). Detects systematic bias patterns in AI-generated assessment outputs.

### Check B1: Confirmation Bias Detection

Verify the AI has not systematically favored the submission's narrative:

- Count findings classified as "confirmed" vs "contradicted" vs "partially-confirmed"
- If confirmed:contradicted ratio exceeds 5:1 AND multiple Conflicted research entries exist, flag: "Possible confirmation bias — AI may be systematically favoring submission claims over contradicting evidence"
- Sample 3 "confirmed" findings and verify each has genuinely independent corroboration (not restating the submission)

**Failure condition:** Confirmed:contradicted ratio >5:1 with Conflicted evidence present but not reflected in findings

**Resolution:** Re-examine contradicted evidence; ensure all Conflicted research entries are surfaced in findings

---

### Check B2: Anchoring Bias Detection

Verify scoring is not anchored to submission framing:

- Compare Readiness scores across domains: if all scores cluster within ±10 points of each other (e.g., all between 60–70), flag: "Possible anchoring — scores are suspiciously uniform across domains with different evidence quality"
- Check if domains with thin evidence (completeness ≤1) have Quality scores > 0 — this suggests the AI inferred quality without evidence

**Failure condition:** Score uniformity across domains with significantly different evidence quality; or Quality > 0 for modules with completeness ≤ 1

**Resolution:** Re-score flagged modules with fresh evaluation; verify Quality scores are grounded in Verified/Corroborated evidence only

---

### Check B3: Severity Calibration Check

Verify gap severity ratings are not systematically over- or under-calibrated:

- If all gaps are rated MEDIUM or below despite hard-blocker modules having completeness = 0, flag: "Possible downward severity bias"
- If all gaps are CRITICAL/HIGH despite most modules having completeness ≥ 2, flag: "Possible upward severity bias"
- Cross-reference: gap severity should correlate with the risk scoring matrix (likelihood x impact)

**Failure condition:** Severity distribution is inconsistent with underlying evidence quality

**Resolution:** Recalibrate severity classifications against gap type definitions and risk matrix

---

### Check B4: Geographic/Demographic Neutrality

Verify the AI has not introduced geographic or demographic bias:

- Check that scoring rationale does not reference founder demographics (age, gender, ethnicity, nationality) as positive or negative signals
- Check that geographic market is evaluated on its merits (market size, regulatory environment, growth) not on stereotypes
- Flag any scoring rationale that contains language indicating bias (e.g., "founders from [region] typically..." or "young founders often...")

**Failure condition:** Scoring rationale references protected characteristics or geographic stereotypes

**Resolution:** Remove biased language; re-score affected modules on evidence-based criteria only

---

### Bias Testing Documentation

All bias checks must be documented in the QA/QC log with:

```json
{
  "check_id": "B1|B2|B3|B4",
  "check_name": "confirmation-bias|anchoring-bias|severity-calibration|neutrality",
  "result": "passed|flagged",
  "details": "Description of finding if flagged",
  "resolution": "Action taken if flagged",
  "timestamp": "ISO-8601"
}
```

**Standards basis:** EU AI Act Article 10 (data governance, bias), NIST AI RMF (Measure function — bias detection), IOSCO AI/ML Principles (continuous monitoring).

---

## Fix Instruction Format

When issuing fix instructions (maximum 2 iterations before user escalation):

Use the following structured format:

```
FIX INSTRUCTION [FI-###]:

Affected component: [module_id | domain_id | agent_name]
Issue type: [consistency-error | missing-attribution | cross-module-conflict |
             missing-finding | mode-compliance | unsourced-claim | dependency-error]
Issue description:
[Clear description of what is wrong, including specific reference to check failed]

Required fix:
[Specific instruction for what must be corrected]
[Include: what data is needed, where to find it, or how to resolve]

Verification:
[How to confirm the fix was applied correctly]
[Include: what the output should look like after fix]

Deadline: [24 hours | before report generation]
```

### Example Fix Instructions

```
FIX INSTRUCTION [FI-001]:
Affected component: D3 (Business Model)
Issue type: missing-attribution
Issue description: Module-content-map lists $45K CAC (customer acquisition cost) with no
source attribution. Research-log shows no entry for CAC research. Cannot verify claim source.

Required fix: Either (a) locate and reference research-log source for CAC figure, or (b)
remove $45K CAC from module-content-map. If CAC figure is from company submission, mark
as "from_submission" with source_id reference to submission document research entry.

Verification: Module-content-map entry for $45K CAC includes source_id field that
references valid research-log entry.

Deadline: Before domain-level QA/QC completion
```

```
FIX INSTRUCTION [FI-002]:
Affected component: D1 (Market) and D7 (Financial Performance)
Issue type: cross-module-conflict
Issue description: Domain 1 reports TAM of $8B; Domain 7 financial projections imply
TAM of $20B based on revenue penetration assumptions. Conflict detected.

Required fix: Reconcile TAM definition. Either: (a) provide basis for $20B TAM in
Domain 1 and revise D1 scoring, or (b) correct Domain 7 projections to align with
$8B TAM assumption. Document any TAM assumption changes in framework construction log.

Verification: Both domains reference same TAM figure and assumptions are consistent
across projection drivers.

Deadline: Before holistic QA/QC completion
```

---

## Escalation Criteria

Escalate to assessor (via AskUserQuestion with multiple choice + free-text option) when any of these conditions apply:

**Escalation Condition 1:** Issue Not Resolved After 2 Fix Iterations
- Same QA/QC failure has been flagged, addressed, and re-flagged in 2+ iterations
- Example: "CAC figure still unsourced after two fix attempts"
- Action: Escalate to assessor with options (see below)

**Escalation Condition 2:** Hard-Blocker Module Affected
- QA/QC failure involves a hard-blocker module
- Example: "Regulatory Status (hard-blocker in FinTech) completeness = 0"
- Action: Escalate immediately; do not retry fix

**Escalation Condition 3:** Score or Determination Already Confirmed at Checkpoint
- Fix would require changing a score/result that was already confirmed at a Confirmation Point
- Example: "Traction domain scored 0.7 and confirmed at Confirmation Point 3; QA/QC now flags as inconsistent"
- Action: Escalate; cannot change confirmed scores without assessor override

**Escalation Condition 4:** Fundamental Analytical Conflict
- Two equally valid research sources contradict each other and QA/QC agent cannot resolve
- Example: "Company press release claims $5M revenue; industry analyst report estimates $8M revenue; both credible sources"
- Action: Escalate to assessor with both sources for judgment call

**Escalation Condition 5:** Missing Critical Data Cannot Be Obtained
- Hard-blocker module cannot be scored; data unavailable and unfeasible to obtain
- Example: "Founder background cannot be researched due to privacy; no LinkedIn, no news coverage"
- Action: Escalate with justification

### Escalation Dialog Format

When escalating to assessor, present options using this dialog:

```
QA/QC ESCALATION [ESC-###]:

Issue: [Brief description of QA/QC failure]
Failed check: [Check category from rubric]
Attempts to resolve: [Number of fix iterations]
Reason for escalation: [Which escalation criterion applies]

Specific details:
[Details of the issue, with references to specific modules/scores]

RECOMMENDED RESOLUTION OPTIONS:

A. Re-run the affected component
   - Instruction: [Specific guidance for reassessment]
   - This will: [What will change]

B. Accept current output and proceed, flagging in report
   - This will: [Describe flag/caveat that will appear in report]
   - Risk: [What could be missed]

C. Override with assessor-provided resolution (free-text input)
   - Provide: [What information assessor should provide]

D. Mark as unresolvable and document
   - This will: [Describe documentation approach]
   - Impact: [Effect on final determination]

Please select option A, B, C, or D, or provide other instruction.
```

### Example Escalation

```
QA/QC ESCALATION [ESC-005]:

Issue: Regulatory Status (D2) hard-blocker module scored completeness = 0
Failed check: Check 4.1 (Hard-Blocker Module Completeness)
Attempts to resolve: 0 (hard-blocker rule prevents fix iteration)
Reason for escalation: Hard-Blocker Module Affected (Escalation Condition 2)

Specific details:
Company is FinTech (raises Series A with debt instrument). Regulatory Status is hard-blocker
with minimum threshold 0.7. Currently scored completeness = 0 with note "Company declined to
disclose regulatory status; states 'not applicable to current operations.'"

RECOMMENDED RESOLUTION OPTIONS:

A. Re-run regulatory assessment with explicit request
   - Instruction: Contact company directly requesting regulatory classification and status
   - This will: Either obtain data to score module above 0, or document refusal in writing

B. Accept 0 score and mark as "unresolvable blocker"
   - This will: Trigger no-go determination in go/no-go gates
   - Risk: Company is rejected before full assessment

C. Assessor judgment: Is regulatory status truly not applicable?
   - Provide: Explanation of why FinTech raising debt does not require regulatory assessment
   - Note: Reviewers may challenge this decision

D. Mark as "data unavailable" and proceed with conditional assessment
   - This will: Assessment continues but flagged as incomplete on critical criterion
   - Impact: Final report includes caveat about missing regulatory assessment

Please select option A, B, C, or D.
```

---

## References

- `references/pre-assess-qaqc-checks.md` — Detailed checklist for holistic QA/QC with examples
- `references/domain-qaqc-checks.md` — Detailed checklist for domain-level QA/QC
