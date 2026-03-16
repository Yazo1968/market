#!/usr/bin/env python3
"""
confidence_router.py

Routes research log entries to appropriate confidence classification based on
source type, corroboration, conflicts, and data currency.

Confidence levels (per research-log.json schema):
- "high": High-confidence, corroborated structured data
- "medium": Multiple web sources confirm the value
- "low": Single source or insufficient corroboration
- "unverifiable": Cannot be elevated beyond this level (training-derived)

Data currency:
- Primary value within 2 years: use primary value
- Primary value > 2 years old: flag as historical
- No date: flag as undated

Author: Startup Assessment Plugin
Version: 0.2.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List
from datetime import datetime, timedelta, timezone


class ConfidenceRoutingError(Exception):
    """Raised when confidence routing fails."""
    pass


class ConfidenceRouter:
    """
    Routes research entries to confidence levels based on source and corroboration.
    """

    DATA_CURRENCY_THRESHOLD_YEARS = 2
    CORROBORATION_HIGH_THRESHOLD = 1
    CORROBORATION_MEDIUM_WEB_THRESHOLD = 2

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize router with research log data.

        Args:
            data: Dict with 'entries' key containing list of entries
                  (matches research-log.json schema)

        Raises:
            ConfidenceRoutingError: If input is invalid
        """
        # Accept both 'entries' (schema) and 'research_log' (legacy) keys
        self.entries = data.get("entries", data.get("research_log", []))
        self.company_name = data.get("company_name", "")
        self.enhanced_entries: List[Dict[str, Any]] = []

        self._validate_input()

    def _validate_input(self) -> None:
        """
        Validate input structure.

        Raises:
            ConfidenceRoutingError: If validation fails
        """
        if not isinstance(self.entries, list):
            raise ConfidenceRoutingError("'entries' must be a list")

    def _is_within_currency_window(self, date_str: str) -> bool:
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
            # Always use UTC for consistent comparison
            now = datetime.now(timezone.utc)
            # Make date timezone-aware if it isn't
            if date.tzinfo is None:
                date = date.replace(tzinfo=timezone.utc)
            cutoff = now - timedelta(days=365 * self.DATA_CURRENCY_THRESHOLD_YEARS)
            return date >= cutoff
        except (ValueError, TypeError):
            return False

    def _assess_data_currency(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess data currency for an entry.

        Args:
            entry: Research entry dict

        Returns:
            Dict with currency assessment
        """
        # Check data_currency.primary_value_date (schema structure)
        data_currency = entry.get("data_currency", {})
        primary_date = data_currency.get("primary_value_date", entry.get("primary_value_date"))

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
    ) -> List[str]:
        """
        Detect conflicts among entries for a given field.

        Args:
            entries: List of entries for same field
            field_key: Field name being compared

        Returns:
            List of conflicting entry IDs (only entries that actually disagree)
        """
        if len(entries) < 2 or not field_key:
            return []

        # Group by primary value
        values: Dict[Any, List[str]] = {}
        for entry in entries:
            data_currency = entry.get("data_currency", {})
            val = data_currency.get("primary_value", entry.get("primary_value"))
            entry_id = entry.get("source_id", entry.get("entry_id", "unknown"))

            if val not in values:
                values[val] = []
            values[val].append(entry_id)

        # Conflicts exist if multiple distinct values
        if len(values) > 1:
            # Return only entries in minority groups (actual disagreements)
            all_ids = []
            for ids in values.values():
                all_ids.extend(ids)
            return all_ids

        return []

    def _classify_confidence(
        self,
        entry: Dict[str, Any],
        all_entries: List[Dict[str, Any]]
    ) -> str:
        """
        Classify confidence level for an entry.
        Returns values matching research-log.json schema: high, medium, low, unverifiable.

        Args:
            entry: Research entry dict
            all_entries: All entries (for conflict detection)

        Returns:
            Confidence level string
        """
        source_type = entry.get("source_type", "unknown")
        corroborated_by = entry.get("corroborated_by", 0)
        if not isinstance(corroborated_by, (int, float)):
            corroborated_by = 0
        entry_id = entry.get("source_id", entry.get("entry_id", ""))

        # Training-derived cannot be elevated
        if source_type == "training-derived":
            return "unverifiable"

        # Check for conflicts using modules_applied_to as grouping key
        field_key = entry.get("field_key", "")
        if field_key:
            field_entries = [e for e in all_entries if e.get("field_key") == field_key]
            conflicts = self._detect_conflicts(field_entries, field_key)
            if entry_id in conflicts and len(conflicts) > 1:
                return "low"  # Conflicted entries get low confidence

        # Structured connector logic
        if source_type == "structured-connector":
            if corroborated_by >= self.CORROBORATION_HIGH_THRESHOLD:
                return "high"
            return "medium"

        # Web retrieval logic
        if source_type == "web-retrieval":
            if corroborated_by >= self.CORROBORATION_MEDIUM_WEB_THRESHOLD:
                return "medium"
            return "low"

        # Default for unknown sources
        return "low"

    def route(self) -> Dict[str, Any]:
        """
        Route all entries and generate enhanced research log.

        Returns:
            Dict matching research-log.json schema structure
        """
        # Pre-group entries by field_key for O(n) conflict detection
        field_groups: Dict[str, List[Dict[str, Any]]] = {}
        for entry in self.entries:
            fk = entry.get("field_key", "")
            if fk:
                if fk not in field_groups:
                    field_groups[fk] = []
                field_groups[fk].append(entry)

        # Classify all entries
        for entry in self.entries:
            confidence = self._classify_confidence(entry, self.entries)
            currency = self._assess_data_currency(entry)

            enhanced_entry = entry.copy()
            enhanced_entry["confidence_level"] = confidence
            enhanced_entry["confidence_rationale"] = self._generate_rationale(
                confidence, entry.get("source_type", "unknown"),
                entry.get("corroborated_by", 0)
            )
            enhanced_entry["data_currency_assessment"] = currency

            self.enhanced_entries.append(enhanced_entry)

        # Generate research summary
        research_summary = self._generate_research_summary()

        return {
            "company_name": self.company_name,
            "entries": self.enhanced_entries,
            "research_summary": research_summary
        }

    def _generate_rationale(self, confidence: str, source_type: str,
                            corroborated_by: Any) -> str:
        """Generate a rationale string for the confidence classification."""
        rationales = {
            "high": f"Structured connector source with {corroborated_by} corroborating source(s)",
            "medium": f"Source type '{source_type}' with corroboration",
            "low": f"Source type '{source_type}' with insufficient corroboration",
            "unverifiable": "Training-derived data; cannot be independently verified"
        }
        return rationales.get(confidence, "Unknown classification basis")

    def _generate_research_summary(self) -> Dict[str, Any]:
        """
        Generate summary of confidence and currency across log.
        Matches research-log.json schema research_summary structure.

        Returns:
            Summary dict
        """
        confidence_counts = {
            "high": 0, "medium": 0, "low": 0, "unverifiable": 0
        }
        source_type_counts = {
            "structured-connector": 0, "web-retrieval": 0
        }
        conflicted_count = 0

        for entry in self.enhanced_entries:
            conf = entry.get("confidence_level", "low")
            if conf in confidence_counts:
                confidence_counts[conf] += 1

            source = entry.get("source_type", "unknown")
            if source in source_type_counts:
                source_type_counts[source] += 1

            # Count conflicted entries
            if entry.get("conflict_with"):
                conflicted_count += 1

        return {
            "total_sources_consulted": len(self.enhanced_entries),
            "structured_connector_sources": source_type_counts.get("structured-connector", 0),
            "web_retrieval_sources": source_type_counts.get("web-retrieval", 0),
            "high_confidence_findings": confidence_counts.get("high", 0),
            "medium_confidence_findings": confidence_counts.get("medium", 0),
            "low_confidence_findings": confidence_counts.get("low", 0),
            "unverifiable_findings": confidence_counts.get("unverifiable", 0),
            "conflicted_findings": conflicted_count
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
