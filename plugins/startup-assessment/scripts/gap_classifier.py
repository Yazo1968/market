#!/usr/bin/env python3
"""
gap_classifier.py

Classifies gaps in startup assessment data based on content status, module scores,
and QA flags. Produces a structured gap register with severity classification.

Gap types (per gap-register.json schema):
- absent-unresolvable: Unresolvable missing content
- absent-externally-resolvable: Externally resolvable missing content
- fragmentary: Present but incomplete (low completeness and quality)
- unverified: Present but not independently corroborated (low quality)
- misaligned: Fit-to-purpose track issues
- conflicted: Present but conflicting information
- flagged: Explicit QA flag

Severity levels (per gap-register.json schema):
- critical: Hard blockers or critical domains with hard gaps
- significant: Critical domains with absent gaps
- moderate: Critical domains with thin/conflicted gaps
- minor: All other gaps

Usage:
  python gap_classifier.py [input.json]
  python gap_classifier.py --module-content-map input.json [--readiness readiness.json] [--framework framework.json]
  cat input.json | python gap_classifier.py

Author: Startup Assessment Plugin
Version: 0.2.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List
from enum import Enum


class GapType(Enum):
    """Enumeration of gap type classifications (matches gap-register.json schema)."""
    ABSENT_UNRESOLVABLE = "absent-unresolvable"
    ABSENT_EXTERNALLY_RESOLVABLE = "absent-externally-resolvable"
    FRAGMENTARY = "fragmentary"
    UNVERIFIED = "unverified"
    MISALIGNED = "misaligned"
    CONFLICTED = "conflicted"
    FLAGGED = "flagged"


class Severity(Enum):
    """Enumeration of gap severity levels (matches gap-register.json schema)."""
    CRITICAL = "critical"
    SIGNIFICANT = "significant"
    MODERATE = "moderate"
    MINOR = "minor"

    def __lt__(self, other: "Severity") -> bool:
        """Enable sorting by severity."""
        severity_order = [Severity.CRITICAL, Severity.SIGNIFICANT, Severity.MODERATE, Severity.MINOR]
        return severity_order.index(self) < severity_order.index(other)


class GapClassificationError(Exception):
    """Raised when gap classification fails."""
    pass


class GapClassifier:
    """
    Classifies gaps based on module scores, content status, and QA flags.
    """

    COMPLETENESS_THRESHOLD_LOW = 1
    QUALITY_THRESHOLD_LOW = 1

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize classifier with module and domain data.

        Args:
            data: Dict with 'modules' and optional 'domains' keys

        Raises:
            GapClassificationError: If input is invalid
        """
        self.modules = data.get("modules", [])
        self.domains = data.get("domains", {})
        self.company_name = data.get("company_name", "")
        self.gaps: List[Dict[str, Any]] = []
        self.gap_counter = 0

        self._validate_input()

    def _validate_input(self) -> None:
        """
        Validate input structure.

        Raises:
            GapClassificationError: If validation fails
        """
        if not isinstance(self.modules, list):
            raise GapClassificationError("'modules' must be a list")

    def _classify_gap_type(self, module: Dict[str, Any]) -> str:
        """
        Determine the gap type for a module.

        Args:
            module: Module data dict

        Returns:
            Gap type string or None if no gap detected
        """
        content_status = module.get("content_status", "unknown")
        completeness = module.get("completeness_score", 0)
        quality = module.get("quality_score", 0)
        qaqc_flags = module.get("qaqc_flags", [])

        # Check explicit QA flag first
        if qaqc_flags:
            return GapType.FLAGGED.value

        # Check content status
        if content_status == "absent-unresolvable":
            return GapType.ABSENT_UNRESOLVABLE.value
        elif content_status in ("absent-externally-resolvable", "absent-soft"):
            return GapType.ABSENT_EXTERNALLY_RESOLVABLE.value
        elif content_status == "present-conflicting":
            return GapType.CONFLICTED.value

        # Check fit-to-purpose issues (any dimension = 0)
        stage_app = module.get("stage_appropriateness", 0)
        align = module.get("assessor_alignment", 0)
        coherence = module.get("ask_coherence", 0)

        if stage_app == 0 or align == 0 or coherence == 0:
            return GapType.MISALIGNED.value

        # Check quality issues
        if completeness <= self.COMPLETENESS_THRESHOLD_LOW and \
           quality <= self.QUALITY_THRESHOLD_LOW:
            return GapType.FRAGMENTARY.value

        if completeness > self.COMPLETENESS_THRESHOLD_LOW and \
           quality <= self.QUALITY_THRESHOLD_LOW:
            return GapType.UNVERIFIED.value

        # No gap detected
        return None

    def _classify_severity(
        self,
        gap_type: str,
        module: Dict[str, Any],
        domain_id: Any
    ) -> str:
        """
        Determine the severity level for a gap.

        Args:
            gap_type: The classified gap type
            module: Module data dict
            domain_id: Domain identifier

        Returns:
            Severity string
        """
        # Check hard blocker status
        if module.get("hard_blocker", False):
            return Severity.CRITICAL.value

        # Get domain criticality — handle both dict and int/str keys
        domain_key = str(domain_id) if not isinstance(domain_id, str) else domain_id
        domain = self.domains.get(domain_key, self.domains.get(domain_id, {}))
        criticality = domain.get("criticality", "standard")

        # Hard-blocker domain + absent or conflicted gap
        if criticality == "hard-blocker":
            if gap_type in (GapType.ABSENT_UNRESOLVABLE.value, GapType.CONFLICTED.value):
                return Severity.CRITICAL.value

        # Critical domain + absent gap
        if criticality == "critical":
            if gap_type in (GapType.ABSENT_UNRESOLVABLE.value, GapType.ABSENT_EXTERNALLY_RESOLVABLE.value):
                return Severity.SIGNIFICANT.value
            if gap_type in (GapType.FRAGMENTARY.value, GapType.CONFLICTED.value):
                return Severity.MODERATE.value

        # Standard domain + absent gap
        if criticality == "standard":
            if gap_type in (GapType.ABSENT_UNRESOLVABLE.value, GapType.UNVERIFIED.value):
                return Severity.MODERATE.value

        # Default to minor
        return Severity.MINOR.value

    def _determine_track(self, gap_type: str, module: Dict[str, Any]) -> str:
        """
        Determine which track(s) the gap affects.

        Args:
            gap_type: The classified gap type
            module: Module data dict

        Returns:
            Track: "readiness", "fit-to-purpose", or "both"
        """
        if gap_type == GapType.MISALIGNED.value:
            return "fit-to-purpose"

        if gap_type == GapType.FLAGGED.value:
            # Check what was flagged
            flags = module.get("qaqc_flags", [])
            if any("quality" in str(f).lower() for f in flags):
                return "readiness"
            if any("fit" in str(f).lower() for f in flags):
                return "fit-to-purpose"
            return "both"

        return "readiness"

    def classify(self) -> Dict[str, Any]:
        """
        Classify all gaps and generate gap register.

        Returns:
            Dict with gaps list and summary statistics (matches gap-register.json schema)
        """
        for module in self.modules:
            gap_type = self._classify_gap_type(module)

            # Skip if no gap detected
            if gap_type is None:
                continue

            domain_id = module.get("domain_id", 0)
            severity = self._classify_severity(gap_type, module, domain_id)
            track = self._determine_track(gap_type, module)

            self.gap_counter += 1
            gap_id = f"GAP-{self.gap_counter:03d}"

            # Generate description
            description = self._generate_description(gap_type, module)

            gap = {
                "gap_id": gap_id,
                "gap_type": gap_type,
                "severity": severity,
                "module_id": module.get("module_id", ""),
                "domain_id": domain_id,
                "description": description,
                "research_resolution_status": module.get(
                    "research_resolution_status",
                    "not-applicable"
                ),
                "track": track,
                "assessor_action_required": severity in (
                    Severity.CRITICAL.value, Severity.SIGNIFICANT.value
                )
            }

            self.gaps.append(gap)

        # Sort by severity
        severity_order = {
            Severity.CRITICAL.value: 0,
            Severity.SIGNIFICANT.value: 1,
            Severity.MODERATE.value: 2,
            Severity.MINOR.value: 3
        }
        self.gaps.sort(key=lambda g: severity_order.get(g["severity"], 4))

        # Generate summary
        gap_summary = self._generate_summary()

        return {
            "company_name": self.company_name,
            "gaps": self.gaps,
            "gap_summary": gap_summary
        }

    def _generate_description(self, gap_type: str, module: Dict[str, Any]) -> str:
        """
        Generate a human-readable description of the gap.

        Args:
            gap_type: The classified gap type
            module: Module data dict

        Returns:
            Description string
        """
        module_id = module.get("module_id", "unknown")

        descriptions = {
            GapType.ABSENT_UNRESOLVABLE.value:
                f"Module {module_id}: Required content is absent and cannot be "
                "resolved externally",
            GapType.ABSENT_EXTERNALLY_RESOLVABLE.value:
                f"Module {module_id}: Content is missing but can be resolved through "
                "external research or data collection",
            GapType.CONFLICTED.value:
                f"Module {module_id}: Present content contains conflicting information "
                "from multiple sources",
            GapType.FRAGMENTARY.value:
                f"Module {module_id}: Content is incomplete and of low quality "
                f"(completeness: {module.get('completeness_score', 0)}, "
                f"quality: {module.get('quality_score', 0)})",
            GapType.UNVERIFIED.value:
                f"Module {module_id}: Content is present but not independently "
                f"corroborated (quality: {module.get('quality_score', 0)})",
            GapType.MISALIGNED.value:
                f"Module {module_id}: Content is misaligned with stage, assessor, or ask "
                f"(stage: {module.get('stage_appropriateness', 0)}, "
                f"alignment: {module.get('assessor_alignment', 0)}, "
                f"coherence: {module.get('ask_coherence', 0)})",
            GapType.FLAGGED.value:
                f"Module {module_id}: Flagged for manual review "
                f"(flags: {', '.join(str(f) for f in module.get('qaqc_flags', []))})"
        }

        return descriptions.get(gap_type, f"Module {module_id}: Unknown gap type")

    def _generate_summary(self) -> Dict[str, Any]:
        """
        Generate summary statistics about gaps (matches gap_summary schema).

        Returns:
            Summary dict
        """
        severity_counts = {
            "critical": 0,
            "significant": 0,
            "moderate": 0,
            "minor": 0
        }
        type_counts = {
            "absent_unresolvable": 0,
            "absent_externally_resolvable": 0,
            "fragmentary": 0,
            "unverified": 0,
            "misaligned": 0,
            "conflicted": 0,
            "flagged": 0
        }
        domains_with_critical = set()

        for gap in self.gaps:
            # Count by severity
            severity = gap["severity"]
            if severity in severity_counts:
                severity_counts[severity] += 1

            # Count by type (convert hyphens to underscores for schema keys)
            gap_type_key = gap["gap_type"].replace("-", "_")
            if gap_type_key in type_counts:
                type_counts[gap_type_key] += 1

            # Track domains with critical gaps
            if severity == "critical":
                domains_with_critical.add(gap["domain_id"])

        return {
            "total_gaps": len(self.gaps),
            "by_severity": severity_counts,
            "by_type": type_counts,
            "domains_with_critical_gaps": sorted(domains_with_critical)
        }


def main() -> int:
    """
    Main entry point. Accepts JSON from stdin or file argument.
    Supports both positional input and named --module-content-map flag.

    Returns:
        Exit code (0 = success, 1 = error)
    """
    parser = argparse.ArgumentParser(
        description="Classify gaps in startup assessment data"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Input JSON file (if omitted, reads from stdin)"
    )
    parser.add_argument(
        "--module-content-map",
        help="Path to module-content-map JSON (alternative to positional input)"
    )
    parser.add_argument(
        "--readiness",
        help="Path to readiness-register JSON (optional, merged into input)"
    )
    parser.add_argument(
        "--framework",
        help="Path to framework JSON (optional, provides domain criticality)"
    )

    args = parser.parse_args()

    try:
        # Determine input source
        input_path = args.module_content_map or args.input
        if input_path:
            with open(input_path, "r") as f:
                data = json.load(f)
        else:
            data = json.load(sys.stdin)

        # Merge readiness data if provided
        if args.readiness:
            with open(args.readiness, "r") as f:
                readiness_data = json.load(f)
            # Merge readiness scores into modules
            readiness_by_module = {}
            for mod in readiness_data.get("modules", []):
                readiness_by_module[mod.get("module_id")] = mod
            for mod in data.get("modules", []):
                mid = mod.get("module_id")
                if mid in readiness_by_module:
                    r = readiness_by_module[mid]
                    mod.setdefault("completeness_score", r.get("completeness_score", 0))
                    mod.setdefault("quality_score", r.get("quality_score", 0))

        # Merge framework data if provided
        if args.framework:
            with open(args.framework, "r") as f:
                framework_data = json.load(f)
            data.setdefault("domains", framework_data.get("domains", {}))
            data.setdefault("company_name", framework_data.get("company_name", ""))

        # Classify
        classifier = GapClassifier(data)
        result = classifier.classify()

        # Output
        print(json.dumps(result, indent=2))
        return 0

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        return 1
    except GapClassificationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
