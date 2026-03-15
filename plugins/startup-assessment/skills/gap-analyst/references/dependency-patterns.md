# Cross-Domain Dependency Patterns

## Overview

This reference defines common dependency patterns between assessment domains. The gap-analyst agent uses these patterns to construct the dependency map and identify compound risk indicators.

## Structural Dependencies

Structural dependencies are hard constraints — the target domain **cannot** be meaningfully assessed without first completing the source domain.

| Source Domain | Target Domain | Rationale |
|---|---|---|
| Domain 4 (Product & Technology) | Domain 3 (Go-to-Market) | GTM strategy must account for product capabilities; cannot assess positioning without knowing the feature set |
| Domain 1 (Market Opportunity) | Domain 5 (Traction & Validation) | Cannot evaluate whether traction is meaningful without understanding TAM and market structure |

## Informational Dependencies

Informational dependencies are soft constraints — the target domain's assessment is **enhanced** by upstream completion but is not blocked.

| Source Domain | Target Domain | Rationale |
|---|---|---|
| Domain 1 (Market Opportunity) | Domain 5 (Traction & Validation) | Market sizing provides context for evaluating traction significance |
| Domain 4 (Product & Technology) | Domain 3 (Go-to-Market) | Product capabilities inform whether GTM claims are realistic |
| Domain 3 (Go-to-Market) | Domain 5 (Traction & Validation) | GTM strategy provides context for whether traction matches expected trajectory |
| Domain 5 (Traction & Validation) | Domain 7 (Financials & Unit Economics) | Traction signals inform what unit economics are realistic |
| Domain 7 (Financials & Unit Economics) | Domain 9 (Capital & Ask) | Financial projections inform whether the ask is proportional to financial stage |
| Domain 9 (Capital & Ask) | Domain 8 (Execution & Operations) | Ask coherence informs whether execution plans are adequately funded |
| Domain 6 (Management & Team) | Domain 8 (Execution & Operations) | Team assessment informs confidence in execution capability |

## Assessment Wave Sequencing

### Wave 1 — Independent Domains (assess in parallel)
- Domain 1: Market Opportunity
- Domain 2: Business Model & Revenue Architecture
- Domain 4: Product & Technology
- Domain 6: Management & Team
- Domain 9: Capital & Ask
- Domain 10: Legal, IP & Governance

**Rationale:** These domains have no structural dependencies on other domains. They can be assessed simultaneously.

### Wave 2 — First-Order Dependent Domains
- Domain 3: Go-to-Market (depends on Domain 4)
- Domain 5: Traction & Validation (enhanced by Domains 1, 3)

**Rationale:** Domain 3 structurally requires Domain 4 completion. Domain 5 benefits from Domain 1 and 3 context.

### Wave 3 — Higher-Order Dependent Domains
- Domain 7: Financials & Unit Economics (enhanced by Domain 5)
- Domain 8: Execution & Operations (enhanced by Domains 6, 9)

**Rationale:** These domains are most informative when assessed after their upstream dependencies.

## Compound Risk Indicators

Compound risks emerge when gaps appear in **multiple related domains simultaneously**, suggesting systemic business issues beyond individual module gaps.

### Pattern 1: Market-Product Disconnect
- **Gap in Domain 1** (TAM sizing absent) + **Gap in Domain 4** (competitive differentiation missing)
- **Suggests:** Unclear market fit; company may not understand its addressable market
- **Risk escalation:** If both are critical/significant severity → compound risk is determination-level

### Pattern 2: Revenue Sustainability Risk
- **Gap in Domain 5** (customer concentration data missing) + **Gap in Domain 7** (customer concentration metrics absent)
- **Suggests:** Inability to assess revenue sustainability and churn risk
- **Risk escalation:** Significant for any assessor focused on unit economics

### Pattern 3: Governance Vacuum
- **Gap in Domain 6** (board composition unspecified) + **Gap in Domain 10** (decision-making authority unspecified)
- **Suggests:** Unclear control structure; may indicate founder-controlled entity without checks
- **Risk escalation:** Critical for institutional investors (PE, sovereign wealth)

### Pattern 4: Execution Credibility Gap
- **Gap in Domain 6** (team experience gaps) + **Gap in Domain 8** (operational plan vague) + **Gap in Domain 9** (use of funds unclear)
- **Suggests:** Team may lack capability to execute on the plan they are raising for
- **Risk escalation:** Determination-level for any assessor type

### Pattern 5: Regulatory Exposure
- **Gap in Domain 10** (regulatory compliance missing) + **Gap in Domain 4** (product compliance unclear)
- **Suggests:** Company may be operating in regulatory gray area without awareness
- **Risk escalation:** Critical for regulated verticals (fintech, healthtech, edtech)

## Compound Risk Assessment Rules

1. **Two related gaps** in connected domains = flag as compound risk in gap register
2. **Three or more related gaps** across a dependency chain = determination-level compound risk
3. **Compound risk in hard-blocker domains** = automatic CRITICAL severity escalation
4. All compound risks must be documented in the `compound_gaps` array of each affected gap entry
5. The gap-analyst agent must present compound risks as a separate section in its output, not just as individual gaps
