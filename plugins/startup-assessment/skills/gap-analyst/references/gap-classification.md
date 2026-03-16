# Gap Type Classification Rules

## Overview

This reference defines the gap type taxonomy used by the gap-analyst agent and `gap_classifier.py`. Every identified gap must be classified into exactly one type.

## Gap Type Definitions

### absent-unresolvable
**Definition:** Module content is entirely absent from the submission AND external research could not locate comparable data. Represents a material information void.

**Triggers:**
- `content_status = "absent-unresolvable"` in module-content-map
- Research-agent attempted external resolution and failed
- No proxy data available from any source category

**Examples:**
- Founder has no public professional history; no LinkedIn, no prior company records
- Proprietary financial data for a private company with no comparable public filings
- Regulated industry compliance status with no public registry entry

**Risk implication:** Assessor cannot evaluate this dimension at all. If in a hard-blocker domain, this triggers Gate 1 NO-GO.

---

### absent-externally-resolvable
**Definition:** Module content is absent from the submission but external research provided partial or full coverage. The gap is reduced but the submission itself is still deficient.

**Triggers:**
- `content_status = "absent-externally-resolvable"` in module-content-map
- Research-agent found comparable data (e.g., market sizing from analyst reports, team credentials from LinkedIn)
- Content quality depends on research confidence level

**Examples:**
- TAM not provided in submission but Statista/IBISWorld data found
- Competitor analysis missing but Crunchbase and public filings available
- Team background absent but LinkedIn profiles verified

**Risk implication:** Assessment can proceed with research data, but confidence is reduced. Scores reflect research quality, not submission quality.

---

### fragmentary
**Definition:** Module content exists but is severely incomplete. Completeness score ≤ 1 AND quality score ≤ 1. Directional assessment is possible but confidence is very low.

**Triggers:**
- `completeness_score <= 1` AND `quality_score <= 1`
- Content present but insufficient for meaningful evaluation
- Key sub-components missing (e.g., TAM claim with no methodology)

**Examples:**
- Market section mentions "$5B TAM" with no methodology, source, or geographic breakdown
- Team section lists names and titles but no experience details, backgrounds, or track record
- Financial projections show top-line revenue only, no unit economics or assumptions

**Risk implication:** Assessment proceeds with heavy caveats. Score reflects the fragmentary nature.

---

### unverified
**Definition:** Module content is present and reasonably complete (completeness ≥ 2) but claims are not independently corroborated (quality ≤ 1). Reliability risk.

**Triggers:**
- `completeness_score > 1` AND `quality_score <= 1`
- Content appears substantive but no external evidence supports the claims
- Research-agent found no corroborating sources

**Examples:**
- Detailed financial projections but no comparable company data to validate assumptions
- Customer testimonials claimed but no verifiable references
- Patent claims listed but no patent office records found

**Risk implication:** Content may be accurate but cannot be relied upon. Assessor should flag for verification during due diligence.

---

### misaligned
**Definition:** Module content exists and may be complete, but does not address the assessor's priorities or the startup's stage. A fit-to-purpose gap rather than a readiness gap.

**Triggers:**
- Any fit dimension = 0: `stage_appropriateness = 0` OR `assessor_alignment = 0` OR `ask_coherence = 0`
- Content is present but wrong for context

**Examples:**
- Pre-seed company providing Series C-level financial models (stage misalignment)
- VC assessor evaluating a company focused entirely on debt metrics (assessor misalignment)
- Ask of $10M but business plan supports $500K operations (ask incoherence)

**Risk implication:** Content cannot inform the assessor's decision. Affects fit-to-purpose track only.

---

### conflicted
**Definition:** Submission content directly contradicts research evidence. Both versions are documented; the assessor must resolve which is accurate.

**Triggers:**
- `content_status = "present-conflicting"` in module-content-map
- Research-agent flagged contradictions between submission claims and external data
- Both values documented with sources

**Examples:**
- Submission claims 40% YoY growth; market reports indicate sector average is 15%
- Submission claims 500 active customers; research found only 50 on review platforms
- Submission claims FDA approval; regulatory database shows "pending"

**Risk implication:** One source is wrong. Assessor must determine which during assessment phase.

---

### flagged
**Definition:** Module has an explicit QA/QC flag, attribution issue, or data quality concern raised during the quality assurance process.

**Triggers:**
- `qaqc_flags` array is non-empty
- QA/QC agent identified specific concern
- May overlap with other gap types but the flag takes priority

**Examples:**
- Score appears inconsistent with evidence (QA calibration check failed)
- Source attribution is incomplete or circular
- Data staleness warning (evidence >12 months old)

**Risk implication:** Requires manual review before assessment can proceed.

---

## Classification Priority

When a module could match multiple gap types, apply in this order:

1. **flagged** — explicit QA/QC flags always take priority
2. **absent-unresolvable** / **absent-externally-resolvable** — content status determines
3. **conflicted** — present-conflicting status
4. **misaligned** — any fit dimension = 0
5. **fragmentary** — low completeness + low quality
6. **unverified** — adequate completeness + low quality

Only one gap type is assigned per module. If multiple conditions are met, the highest-priority type is used.
