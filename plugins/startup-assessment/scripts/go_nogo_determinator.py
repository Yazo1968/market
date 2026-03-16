#!/usr/bin/env python3
"""
go_nogo_determinator.py

Applies 3-gate logic to determine go/no-go status for startup assessment.

Gate 1 — Hard Blocker Check:
  Any gap with gap_type = "absent-unresolvable" AND module.hard_blocker = true → NO-GO

Gate 2 — Domain Floor Check:
  Hard-blocker domain < 40% floor → CONDITIONAL-HOLD minimum
  Critical domain < 30% floor → CONDITIONAL-HOLD minimum
  Standard domain < 20% floor → CONDITIONAL-HOLD minimum

Gate 3 — Fit-to-Purpose Threshold:
  Overall fit < 40% OR primary domain fit < 50% → CONDITIONAL-HOLD minimum

Readiness Score Bands:
  readiness >= 75% → GO
  readiness 55-74% → CONDITIONAL-GO
  readiness 35-54% → CONDITIONAL-HOLD
  readiness < 35% → NO-GO

Fit-to-Purpose Modifier:
  fit 50-69% → downgrade by one level
  fit < 50% → CONDITIONAL-HOLD minimum

Final determination = worst of all gates and modifiers

Author: Startup Assessment Plugin
Version: 0.2.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List
from enum import Enum


class Determination(Enum):
    """Enumeration of go/no-go determinations (matches go-nogo-determination.json schema)."""
    GO = "GO"
    CONDITIONAL_GO = "CONDITIONAL-GO"
    CONDITIONAL_HOLD = "CONDITIONAL-HOLD"
    NO_GO = "NO-GO"

    def __lt__(self, other: "Determination") -> bool:
        """Enable ordering by severity (worst first)."""
        order = [Determination.NO_GO, Determination.CONDITIONAL_HOLD,
                 Determination.CONDITIONAL_GO, Determination.GO]
        return order.index(self) < order.index(other)


class GoNoGoDeterminationError(Exception):
    """Raised when go/no-go determination fails."""
    pass


class GoNogoDeterminator:
    """
    Applies 3-gate logic to produce go/no-go determination.
    """

    READINESS_GO_THRESHOLD = 75
    READINESS_CONDITIONAL_GO_MIN = 55
    READINESS_CONDITIONAL_HOLD_MIN = 35

    # Domain floor thresholds per criticality (per go-nogo-logic.md)
    DOMAIN_FLOOR_HARD_BLOCKER = 40
    DOMAIN_FLOOR_CRITICAL = 30
    DOMAIN_FLOOR_STANDARD = 20

    # Fit-to-purpose thresholds
    FIT_OVERALL_FLOOR = 40
    FIT_PRIMARY_DOMAIN_FLOOR = 50
    FIT_MODIFIER_THRESHOLD_HIGH = 69
    FIT_MODIFIER_THRESHOLD_LOW = 50

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize determinator with scores and gaps.

        Args:
            data: Dict with 'scores' and 'gaps' keys

        Raises:
            GoNoGoDeterminationError: If input is invalid
        """
        self.scores = data.get("scores", {})
        self.gaps = data.get("gaps", {})
        self.domains = data.get("domains", {})
        self.modules = data.get("modules", [])
        self.company_name = data.get("company_name", "")

        self.gate_1_passed = True
        self.gate_1_triggers: List[Dict[str, Any]] = []
        self.gate_2_passed = True
        self.gate_2_triggers: List[Dict[str, Any]] = []
        self.gate_3_passed = True
        self.gate_3_triggers: List[Dict[str, Any]] = []
        self.readiness_percentage = 0.0
        self.fit_percentage = 0.0
        self.fit_modifier_applied = False
        self.fit_modifier_direction = None
        self.conditions: List[Dict[str, Any]] = []
        self.condition_counter = 0

        self._validate_input()

    def _validate_input(self) -> None:
        """
        Validate input structure.

        Raises:
            GoNoGoDeterminationError: If validation fails
        """
        if not isinstance(self.scores, dict):
            raise GoNoGoDeterminationError("'scores' must be a dict")
        if not isinstance(self.gaps, dict):
            raise GoNoGoDeterminationError("'gaps' must be a dict")

    def _get_domain_floor(self, criticality: str) -> int:
        """Get the floor threshold for a domain criticality level."""
        floors = {
            "hard-blocker": self.DOMAIN_FLOOR_HARD_BLOCKER,
            "critical": self.DOMAIN_FLOOR_CRITICAL,
            "standard": self.DOMAIN_FLOOR_STANDARD,
        }
        return floors.get(criticality, self.DOMAIN_FLOOR_STANDARD)

    def _gate_1_hard_blocker_check(self) -> bool:
        """
        Gate 1: Check for hard blocker gaps.

        Returns:
            True if passed, False if failed
        """
        gaps_list = self.gaps.get("gaps", [])

        # Build module lookup for O(1) access
        module_map = {m.get("module_id"): m for m in self.modules}

        for gap in gaps_list:
            gap_type = gap.get("gap_type")
            module_id = gap.get("module_id", "")
            module = module_map.get(module_id)

            if module and gap_type == "absent-unresolvable" and module.get("hard_blocker"):
                self.gate_1_triggers.append({
                    "gap_id": gap.get("gap_id"),
                    "description": f"Hard blocker module '{module_id}' has absent-unresolvable gap"
                })

        if self.gate_1_triggers:
            return False
        return True

    def _gate_2_domain_floor_check(self) -> bool:
        """
        Gate 2: Check if domains meet minimum floor based on criticality.
        Checks hard-blocker, critical, AND standard domains.

        Returns:
            True if passed, False if failed
        """
        domain_scores = self.scores.get("domain_scores", {})

        for domain_id, domain_data in self.domains.items():
            criticality = domain_data.get("criticality", "standard")
            floor = self._get_domain_floor(criticality)
            domain_name = domain_data.get("domain_name", f"Domain {domain_id}")

            # Get domain score — handle both dict-keyed and int-keyed scores
            score_dict = domain_scores.get(domain_id, domain_scores.get(str(domain_id), {}))
            if isinstance(score_dict, dict):
                readiness_score = score_dict.get("readiness_score", 0.0)
                # Score may be 0-1 normalized or 0-100 percentage
                readiness_percentage = readiness_score * 100 if readiness_score <= 1.0 else readiness_score
            else:
                readiness_percentage = 0.0

            if readiness_percentage < floor:
                self.gate_2_triggers.append({
                    "domain_id": int(domain_id) if str(domain_id).isdigit() else domain_id,
                    "domain_name": domain_name,
                    "score": round(readiness_percentage, 2),
                    "floor_threshold": floor,
                    "criticality": criticality
                })

        if self.gate_2_triggers:
            return False
        return True

    def _gate_3_fit_threshold_check(self) -> bool:
        """
        Gate 3: Check fit-to-purpose thresholds.
        Overall fit < 40% OR primary domain fit < 50% → CONDITIONAL-HOLD minimum.

        Returns:
            True if passed, False if failed
        """
        self.fit_percentage = self.scores.get("overall_fit_percentage", 0.0)

        passed = True

        # Check overall fit floor
        if self.fit_percentage < self.FIT_OVERALL_FLOOR:
            self.gate_3_triggers.append({
                "type": "overall_fit_below_floor",
                "fit_score": round(self.fit_percentage, 2),
                "threshold": self.FIT_OVERALL_FLOOR
            })
            passed = False

        # Check primary domain fit
        primary_domain_id = self.scores.get("primary_domain_id")
        if primary_domain_id:
            domain_scores = self.scores.get("domain_scores", {})
            primary_score = domain_scores.get(primary_domain_id, domain_scores.get(str(primary_domain_id), {}))
            if isinstance(primary_score, dict):
                primary_fit = primary_score.get("fit_score", 0.0)
                primary_fit_pct = primary_fit * 100 if primary_fit <= 1.0 else primary_fit
                if primary_fit_pct < self.FIT_PRIMARY_DOMAIN_FLOOR:
                    self.gate_3_triggers.append({
                        "type": "primary_domain_fit_below_floor",
                        "domain_id": primary_domain_id,
                        "fit_score": round(primary_fit_pct, 2),
                        "threshold": self.FIT_PRIMARY_DOMAIN_FLOOR
                    })
                    passed = False

        return passed

    def _score_band_determination(self) -> Determination:
        """
        Determine baseline from readiness score bands.

        Returns:
            Baseline Determination
        """
        self.readiness_percentage = self.scores.get("overall_readiness_percentage", 0.0)

        if self.readiness_percentage >= self.READINESS_GO_THRESHOLD:
            return Determination.GO
        elif self.readiness_percentage >= self.READINESS_CONDITIONAL_GO_MIN:
            return Determination.CONDITIONAL_GO
        elif self.readiness_percentage >= self.READINESS_CONDITIONAL_HOLD_MIN:
            return Determination.CONDITIONAL_HOLD
        else:
            return Determination.NO_GO

    def _apply_fit_modifier(self, determination: Determination) -> Determination:
        """
        Apply fit-to-purpose modifier to determination.

        Args:
            determination: Current determination

        Returns:
            Modified determination
        """
        # No modifier if fit >= 70%
        if self.fit_percentage >= 70:
            return determination

        # Hard floor: if fit < 50%, determination cannot be better than CONDITIONAL-HOLD
        if self.fit_percentage < self.FIT_MODIFIER_THRESHOLD_LOW:
            self.fit_modifier_applied = True
            self.fit_modifier_direction = "downgrade-to-minimum"
            if determination > Determination.CONDITIONAL_HOLD:
                return Determination.CONDITIONAL_HOLD
            return determination

        # Downgrade by one level if 50-69%
        if self.fit_percentage <= self.FIT_MODIFIER_THRESHOLD_HIGH:
            self.fit_modifier_applied = True
            self.fit_modifier_direction = "downgrade-one-level"

            downgrade_map = {
                Determination.GO: Determination.CONDITIONAL_GO,
                Determination.CONDITIONAL_GO: Determination.CONDITIONAL_HOLD,
                Determination.CONDITIONAL_HOLD: Determination.NO_GO,
                Determination.NO_GO: Determination.NO_GO
            }
            return downgrade_map.get(determination, determination)

        return determination

    def _add_condition(self, description: str, gap_reference: str = "",
                       responsible_party: str = "submitter",
                       resolution_required_before: str = "assessment") -> None:
        """Add a condition to the conditions list (matches schema structure)."""
        self.condition_counter += 1
        self.conditions.append({
            "condition_id": f"COND-{self.condition_counter:03d}",
            "condition_description": description,
            "gap_reference": gap_reference,
            "responsible_party": responsible_party,
            "resolution_required_before": resolution_required_before
        })

    def _generate_conditions(self, determination: Determination) -> None:
        """
        Generate conditions/remediation requirements based on determination.

        Args:
            determination: Final determination
        """
        gaps_list = self.gaps.get("gaps", [])

        if determination == Determination.CONDITIONAL_GO:
            for gap in gaps_list:
                if gap.get("severity") in ("critical", "significant"):
                    self._add_condition(
                        f"Resolve {gap.get('gap_type')} gap before proceeding",
                        gap_reference=gap.get("gap_id", ""),
                        responsible_party="submitter",
                        resolution_required_before="assessment"
                    )

        elif determination == Determination.CONDITIONAL_HOLD:
            critical_gaps = [g for g in gaps_list if g.get("severity") == "critical"]
            for gap in critical_gaps:
                self._add_condition(
                    f"Critical remediation required: {gap.get('description', gap.get('gap_type', ''))}",
                    gap_reference=gap.get("gap_id", ""),
                    responsible_party="submitter",
                    resolution_required_before="resubmission"
                )

            if self.readiness_percentage < 75:
                self._add_condition(
                    f"Increase readiness from {self.readiness_percentage:.1f}% to >= 75%",
                    responsible_party="submitter",
                    resolution_required_before="resubmission"
                )

        elif determination == Determination.NO_GO:
            for trigger in self.gate_1_triggers:
                self._add_condition(
                    f"Hard blocker must be resolved: {trigger.get('description', '')}",
                    gap_reference=trigger.get("gap_id", ""),
                    responsible_party="submitter",
                    resolution_required_before="resubmission"
                )
            for trigger in self.gate_2_triggers:
                self._add_condition(
                    f"Domain '{trigger.get('domain_name', trigger.get('domain_id'))}' "
                    f"must reach {trigger.get('floor_threshold')}% floor "
                    f"(currently {trigger.get('score')}%)",
                    responsible_party="submitter",
                    resolution_required_before="resubmission"
                )

    def determine(self) -> Dict[str, Any]:
        """
        Run 3-gate logic and produce determination.

        Returns:
            Dict matching go-nogo-determination.json schema
        """
        # Gate 1 — Hard Blocker Check
        self.gate_1_passed = self._gate_1_hard_blocker_check()

        # Gate 2 — Domain Floor Check
        self.gate_2_passed = self._gate_2_domain_floor_check()

        # Gate 3 — Fit-to-Purpose Threshold
        self.gate_3_passed = self._gate_3_fit_threshold_check()

        # Score band baseline
        determination = self._score_band_determination()

        # Apply fit modifier
        determination = self._apply_fit_modifier(determination)

        # Gate 1 FAIL → NO-GO (overrides everything)
        if not self.gate_1_passed:
            determination = Determination.NO_GO

        # Gate 2 FAIL → CONDITIONAL-HOLD minimum
        if not self.gate_2_passed:
            if determination > Determination.CONDITIONAL_HOLD:
                determination = Determination.CONDITIONAL_HOLD

        # Gate 3 FAIL → CONDITIONAL-HOLD minimum
        if not self.gate_3_passed:
            if determination > Determination.CONDITIONAL_HOLD:
                determination = Determination.CONDITIONAL_HOLD

        # Generate conditions
        self._generate_conditions(determination)

        return {
            "company_name": self.company_name,
            "determination": determination.value,
            "overall_weighted_score": round(self.readiness_percentage, 2),
            "readiness_track_score": round(self.readiness_percentage, 2),
            "fit_to_purpose_track_score": round(self.fit_percentage, 2),
            "gate_results": {
                "hard_blocker_check": {
                    "passed": self.gate_1_passed,
                    "hard_blockers_triggered": self.gate_1_triggers
                },
                "domain_floor_check": {
                    "passed": self.gate_2_passed,
                    "domains_below_floor": self.gate_2_triggers
                },
                "fit_to_purpose_threshold": {
                    "passed": self.gate_3_passed,
                    "fit_score": round(self.fit_percentage, 2),
                    "threshold": self.FIT_OVERALL_FLOOR,
                    "domains_below_threshold": [
                        str(t.get("domain_id", ""))
                        for t in self.gate_3_triggers
                        if t.get("type") == "primary_domain_fit_below_floor"
                    ]
                }
            },
            "conditions": self.conditions,
            "computation_metadata": {
                "script_version": "0.2.0",
                "readiness_weight_applied": 1.0,
                "fit_weight_applied": 1.0
            }
        }


def main() -> int:
    """
    Main entry point. Accepts JSON from stdin or file argument.

    Returns:
        Exit code (0 = success, 1 = error)
    """
    parser = argparse.ArgumentParser(
        description="Determine go/no-go status using 3-gate logic"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Input JSON file (if omitted, reads from stdin)"
    )
    parser.add_argument(
        "--readiness",
        help="Path to readiness-register JSON (optional)"
    )
    parser.add_argument(
        "--fit",
        help="Path to fit-to-purpose-register JSON (optional)"
    )
    parser.add_argument(
        "--framework",
        help="Path to framework JSON (optional, provides domain criticality)"
    )

    args = parser.parse_args()

    try:
        # Read primary input
        input_path = args.input
        if input_path:
            with open(input_path, "r") as f:
                data = json.load(f)
        else:
            data = json.load(sys.stdin)

        # Merge readiness data if provided separately
        if args.readiness:
            with open(args.readiness, "r") as f:
                readiness_data = json.load(f)
            data.setdefault("scores", {})
            data["scores"]["overall_readiness_percentage"] = readiness_data.get(
                "readiness_score_percentage",
                readiness_data.get("overall_readiness_score", 0) * 100
            )

        # Merge fit data if provided separately
        if args.fit:
            with open(args.fit, "r") as f:
                fit_data = json.load(f)
            data.setdefault("scores", {})
            data["scores"]["overall_fit_percentage"] = fit_data.get(
                "fit_score_percentage",
                fit_data.get("overall_fit_score", 0) * 100
            )

        # Merge framework data if provided separately
        if args.framework:
            with open(args.framework, "r") as f:
                framework_data = json.load(f)
            data.setdefault("domains", framework_data.get("domains", {}))
            data.setdefault("company_name", framework_data.get("company_name", ""))

        # Determine
        determinator = GoNogoDeterminator(data)
        result = determinator.determine()

        # Output
        print(json.dumps(result, indent=2))
        return 0

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        return 1
    except GoNoGoDeterminationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
