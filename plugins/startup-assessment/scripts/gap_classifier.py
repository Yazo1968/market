#!/usr/bin/env python3
"""
gap_classifier.py

Classifies gaps in startup assessment data based on content status, module scores,
and QA flags. Produces a structured gap register with severity classification.

Gap types:
- absent-hard: Unresolvable missing content
- absent-soft: Externally resolvable missing content
- conflicted: Present but conflicting information
- thin: Low completeness and quality
- present-low-quality: High completeness but low quality
- misaligned: Fit-to-purpose track issues
- flagged: Explicit QA flag

Severity levels:
- critical: Hard blockers or critical domains with hard gaps
- high: Critical domains with absent-hard gaps
- medium: Critical domains with thin/conflicted gaps
- low: All other gaps

Author: Startup Assessment Plugin
Version: 0.1.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List, Optional
from pathlib import Path
from enum import Enum


class GapType(Enum):
    """Enumeration of gap type classifications."""
    ABSENT_HARD = "absent-hard"
    ABSENT_SOFT = "absent-soft"
    CONFLICTED = "conflicted"
    THIN = "thin"
    PRESENT_LOW_QUALITY = "present-low-quality"
    MISALIGNED = "misaligned"
    FLAGGED = "flagged"


class Severity(Enum):
    """Enumeration of gap severity levels."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    def __lt__(self, other: "Severity") -> bool:
        """Enable sorting by severity."""
        severity_order = [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW]
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
    FIT_DIMENSION_ZERO_THRESHOLD = 0

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
            Gap type string
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
            return GapType.ABSENT_HARD.value
        elif content_status == "absent-externally-resolvable":
            return GapType.ABSENT_SOFT.value
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
            return GapType.THIN.value

        if completeness > self.COMPLETENESS_THRESHOLD_LOW and \
           quality <= self.QUALITY_THRESHOLD_LOW:
            return GapType.PRESENT_LOW_QUALITY.value

        # No gap detected
        return None

    def _classify_severity(
        self,
        gap_type: str,
        module: Dict[str, Any],
        domain_id: int
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

        # Get domain criticality
        domain = self.domains.get(domain_id, {})
        criticality = domain.get("criticality", "standard")

        # Critical domain + hard gap
        if criticality == "hard-blocker":
            if gap_type == GapType.ABSENT_HARD.value:
                return Severity.CRITICAL.value

        # Critical domain + medium gap
        if criticality == "critical":
            if gap_type == GapType.ABSENT_HARD.value:
                return Severity.HIGH.value
            if gap_type in [GapType.THIN.value, GapType.CONFLICTED.value]:
                return Severity.MEDIUM.value

        # Default to low
        return Severity.LOW.value

    def _determine_track(self, gap_type: str, module: Dict[str, Any]) -> str:
        """
        Determine which track(s) the gap affects.

        Args:
            gap_type: The classified gap type
            module: Module data dict

        Returns:
            Track: "readiness", "fit", or "both"
        """
        if gap_type == GapType.MISALIGNED.value:
            return "fit"

        if gap_type == GapType.FLAGGED.value:
            # Check what was flagged
            flags = module.get("qaqc_flags", [])
            if any("quality" in str(f).lower() for f in flags):
                return "readiness"
            if any("fit" in str(f).lower() for f in flags):
                return "fit"
            return "both"

        return "readiness"

    def classify(self) -> Dict[str, Any]:
        """
        Classify all gaps and generate gap register.

        Returns:
            Dict with gaps list and summary statistics
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
                    "unassigned"
                ),
                "track": track
            }

            self.gaps.append(gap)

        # Sort by severity
        severity_order = {
            Severity.CRITICAL.value: 0,
            Severity.HIGH.value: 1,
            Severity.MEDIUM.value: 2,
            Severity.LOW.value: 3
        }
        self.gaps.sort(key=lambda g: severity_order.get(g["severity"], 4))

        # Generate summary
        summary = self._generate_summary()

        return {
            "gaps": self.gaps,
            "summary": summary
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
            GapType.ABSENT_HARD.value:
                f"Module {module_id}: Required content is absent and cannot be "
                "resolved externally",
            GapType.ABSENT_SOFT.value:
                f"Module {module_id}: Content is missing but can be resolved through "
                "external research or data collection",
            GapType.CONFLICTED.value:
                f"Module {module_id}: Present content contains conflicting information "
                "from multiple sources",
            GapType.THIN.value:
                f"Module {module_id}: Content is incomplete and of low quality "
                f"(completeness: {module.get('completeness_score', 0)}, "
                f"quality: {module.get('quality_score', 0)})",
            GapType.PRESENT_LOW_QUALITY.value:
                f"Module {module_id}: Content is complete but quality is low "
                f"(quality: {module.get('quality_score', 0)})",
            GapType.MISALIGNED.value:
                f"Module {module_id}: Content is misaligned with stage, assessor, or ask "
                f"(stage: {module.get('stage_appropriateness', 0)}, "
                f"alignment: {module.get('assessor_alignment', 0)}, "
                f"coherence: {module.get('ask_coherence', 0)})",
            GapType.FLAGGED.value:
                f"Module {module_id}: Flagged for manual review "
                f"(flags: {', '.join(module.get('qaqc_flags', []))})"
        }

        return descriptions.get(gap_type, f"Module {module_id}: Unknown gap type")

    def _generate_summary(self) -> Dict[str, Any]:
        """
        Generate summary statistics about gaps.

        Returns:
            Summary dict
        """
        gap_types = {}
        severity_counts = {}
        track_counts = {}

        for gap in self.gaps:
            # Count by type
            gap_type = gap["gap_type"]
            gap_types[gap_type] = gap_types.get(gap_type, 0) + 1

            # Count by severity
            severity = gap["severity"]
            severity_counts[severity] = severity_counts.get(severity, 0) + 1

            # Count by track
            track = gap["track"]
            track_counts[track] = track_counts.get(track, 0) + 1

        return {
            "total_gaps": len(self.gaps),
            "by_type": gap_types,
            "by_severity": severity_counts,
            "by_track": track_counts
        }


def main() -> int:
    """
    Main entry point. Accepts JSON from stdin or file argument.

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

    args = parser.parse_args()

    try:
        # Read input
        if args.input:
            with open(args.input, "r") as f:
                data = json.load(f)
        else:
            data = json.load(sys.stdin)

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
