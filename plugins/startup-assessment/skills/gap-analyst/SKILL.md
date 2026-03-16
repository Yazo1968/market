---
name: gap-analyst
description: >
  This skill should be used when analyzing gaps between submission content and assessment requirements,
  classifying gap types, and mapping cross-domain dependencies. Trigger phrases: "classify gaps",
  "gap analysis", "dependency map", "gap register", "cross-domain dependencies", "compound risk".
version: 0.1.0
---

# Gap Analysis Framework

This skill provides the gap-analyst agent with classification rules and dependency patterns for identifying and categorizing information gaps in startup submissions.

## Gap Classification

Gap types follow a strict taxonomy that determines how each gap is treated in scoring and reporting. Every identified gap must be classified into exactly one type based on content availability and research resolution status.

See `references/gap-classification.md` for the full gap type taxonomy with triggers and examples.

## Cross-Domain Dependencies

Dependencies between assessment domains are classified as structural (hard constraints) or informational (soft constraints). The dependency map identifies compound risk indicators where gaps in upstream domains cascade into downstream assessment limitations.

See `references/dependency-patterns.md` for the complete dependency pattern definitions.

## References

- `references/gap-classification.md` — Gap type classification rules and taxonomy
- `references/dependency-patterns.md` — Cross-domain dependency patterns and compound risk indicators
