#!/usr/bin/env python3
"""
confidence_router.py

Routes research log entries to appropriate confidence classification based on
source type, corroboration, conflicts, and data currency.

Confidence levels:
- "verified": High-confidence, corroborated structured data
- "corroborated": Multiple sources confirm the value
- "conflicted": Conflicting sources detected
- "unverified": Single source or insufficient corroboration
- "training-derived": Cannot be elevated beyond this level

Data currency:
- Primary value within 2 years: use primary value
- Primary value > 2 years old: flag as historical
- No date: flag as undated

Author: Startup Assessment Plugin
Version: 0.1.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta
from pathlib import Path


class ConfidenceRoutingError(Exception):
    """Raised when confidence routing fails."""
    pass


class ConfidenceRouter:
    """
    Routes research entries to confidence levels based on source and corroboration.
    """

    DATA_CURRENCY_THRESHOLD_YEARS = 2
    CORROBORATION_VERIFIED_THRESHOLD = 1
    CORROBORATION_CORROBORATED_WEB_THRESHOLD = 2
    CORROBORATION_UNVERIFIED_WEB_THRESHOLD = 1

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize router with research log data.

        Args:
            data: Dict with 'research_log' key containing list of entries

        Raises:
            ConfidenceRoutingError: If input is invalid
        """
        self.research_log = data.get("research_log", [])
        self.enhanced_log: List[Dict[str, Any]] = []
        self.conflicts: List[Dict[str, Any]] = []

        self._validate_input()

    def _validate_input(self) -> None:
        """
        Validate input structure.

        Raises:
            ConfidenceRoutingError: If validation fails
        """
        if not isinstance(self.research_log, list):
            raise ConfidenceRoutingError("'research_log' must be a list")

    def _is_within_currency_window(self, date_str: Optional[str]) -> bool:
        """
        Check if a date is within the currency window (2 years).

        Args:
            date_str: ISO format date string or None

        Returns:
            True if within window, False otherwise
        """
        if not date_str:
            return False

        try:
            date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            cutoff = datetime.now(date.tzinfo) - timedelta(days=365 * 2)
            return date >= cutoff
        except (ValueError, TypeError):
            return False

    def _assess_data_currency(
        self,
        entry: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess data currency for an entry.

        Args:
            entry: Research entry dict

        Returns:
            Dict with currency assessment
        """
        primary_date = entry.get("primary_value_date")

        if not primary_date:
            return {
                "currency_status": "undated",
                "is_current": False,
                "recommendation": "Verify date or obtain current data"
            }

        if self._is_within_currency_window(primary_date):
            return {
                "currency_status": "current",
                "is_current": True,
                "recommendation": None
            }

        return {
            "currency_status": "historical",
            "is_current": False,
            "recommendation": "Primary data is > 2 years old; consider obtaining current data"
        }

    def _detect_conflicts(
        self,
        entries: List[Dict[str, Any]],
        field_key: str
    ) -> List[Dict[str, Any]]:
        """
        Detect conflicts among entries for a given field.

        Args:
            entries: List of entries for same field
            field_key: Field name being compared

        Returns:
            List of conflicting entry IDs
        """
        if len(entries) < 2:
            return []

        # Group by primary value
        values = {}
        for entry in entries:
            val = entry.get("primary_value")
            entry_id = entry.get("entry_id", "unknown")

            if val not in values:
                values[val] = []
            values[val].append(entry_id)

        # Conflicts exist if multiple distinct values
        if len(values) > 1:
            # Return all entries that differ
            conflict_entries = []
            for v, ids in values.items():
                conflict_entries.extend(ids)
            return conflict_entries

        return []

    def _classify_confidence(
        self,
        entry: Dict[str, Any],
        all_entries: List[Dict[str, Any]]
    ) -> str:
        """
        Classify confidence level for an entry.

        Args:
            entry: Research entry dict
            all_entries: All entries (for conflict detection)

        Returns:
            Confidence level string
        """
        source_type = entry.get("source_type", "unknown")
        corroborated_by = entry.get("corroborated_by", 0)
        entry_id = entry.get("entry_id", "")

        # Training-derived cannot be elevated
        if source_type == "training-derived":
            return "training-derived"

        # Check for conflicts
        field_key = entry.get("field_key", "")
        field_entries = [e for e in all_entries if e.get("field_key") == field_key]
        conflicts = self._detect_conflicts(field_entries, field_key)
        if entry_id in conflicts and len(conflicts) > 1:
            return "conflicted"

        # Structured connector logic
        if source_type == "structured-connector":
            if corroborated_by >= self.CORROBORATION_VERIFIED_THRESHOLD:
                return "verified"
            return "corroborated"

        # Web retrieval logic
        if source_type == "web-retrieval":
            if corroborated_by >= self.CORROBORATION_CORROBORATED_WEB_THRESHOLD:
                return "corroborated"
            return "unverified"

        # Default
        return "unverified"

    def route(self) -> Dict[str, Any]:
        """
        Route all entries and generate enhanced research log.

        Returns:
            Dict with enhanced entries and provenance summary
        """
        # First pass: classify all entries
        for entry in self.research_log:
            confidence = self._classify_confidence(entry, self.research_log)
            currency = self._assess_data_currency(entry)

            enhanced_entry = entry.copy()
            enhanced_entry["confidence_level"] = confidence
            enhanced_entry["data_currency_assessment"] = currency

            self.enhanced_log.append(enhanced_entry)

        # Generate provenance summary
        summary = self._generate_provenance_summary()

        return {
            "enhanced_research_log": self.enhanced_log,
            "provenance_summary": summary
        }

    def _generate_provenance_summary(self) -> Dict[str, Any]:
        """
        Generate summary of confidence and currency across log.

        Returns:
            Summary dict
        """
        confidence_counts = {}
        currency_counts = {}
        source_type_counts = {}

        for entry in self.enhanced_log:
            # Count by confidence
            conf = entry.get("confidence_level", "unknown")
            confidence_counts[conf] = confidence_counts.get(conf, 0) + 1

            # Count by currency
            curr_status = entry.get("data_currency_assessment", {}).get(
                "currency_status",
                "unknown"
            )
            currency_counts[curr_status] = currency_counts.get(curr_status, 0) + 1

            # Count by source type
            source = entry.get("source_type", "unknown")
            source_type_counts[source] = source_type_counts.get(source, 0) + 1

        return {
            "total_entries": len(self.enhanced_log),
            "by_confidence": confidence_counts,
            "by_currency_status": currency_counts,
            "by_source_type": source_type_counts,
            "currency_window_years": self.DATA_CURRENCY_THRESHOLD_YEARS
        }


def main() -> int:
    """
    Main entry point. Accepts JSON from stdin or file argument.

    Returns:
        Exit code (0 = success, 1 = error)
    """
    parser = argparse.ArgumentParser(
        description="Route research entries to confidence classifications"
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

        # Route
        router = ConfidenceRouter(data)
        result = router.route()

        # Output
        print(json.dumps(result, indent=2))
        return 0

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        return 1
    except ConfidenceRoutingError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
