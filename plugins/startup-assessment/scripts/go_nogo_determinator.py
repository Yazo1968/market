#!/usr/bin/env python3
"""
go_nogo_determinator.py

Applies 3-gate logic to determine go/no-go status for startup assessment.

Gate 1 — Hard Blocker Check:
  Any gap with gap_type = "absent-hard" AND module.hard_blocker = true → FAIL

Gate 2 — Domain Floor Check:
  Any hard-blocker domain scoring < 25% → FAIL (indicates severe deficiency)

Gate 3 — Score-Based Determination:
  readiness ≥ 75% → GO
  readiness 55–74% → CONDITIONAL GO
  readiness 35–54% → CONDITIONAL HOLD
  readiness < 35% → NO-GO

Fit-to-Purpose Modifier:
  fit 50–69% → downgrade by one level
  fit < 50% → determination = CONDITIONAL HOLD minimum

Final determination = worst of Gate 1, Gate 2, Gate 3 + modifier

Author: Startup Assessment Plugin
Version: 0.1.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List, Optional
from enum import Enum


class Determination(Enum):
    """Enumeration of go/no-go determinations."""
    GO = "GO"
    CONDITIONAL_GO = "CONDITIONAL GO"
    CONDITIONAL_HOLD = "CONDITIONAL HOLD"
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
    READINESS_CONDITIONAL_GO_MAX = 74
    READINESS_CONDITIONAL_HOLD_MIN = 35
    READINESS_CONDITIONAL_HOLD_MAX = 54
    READINESS_NO_GO_MAX = 34

    DOMAIN_FLOOR_HARD_BLOCKER = 25

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

        self.gate_1_result = "PASS"
        self.gate_1_triggers = []
        self.gate_2_result = "PASS"
        self.gate_2_triggers = []
        self.gate_3_result = "GO"
        self.readiness_percentage = 0.0
        self.fit_percentage = 0.0
        self.fit_modifier_applied = False
        self.fit_modifier_direction = None
        self.conditions = []

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

    def _gate_1_hard_blocker_check(self) -> str:
        """
        Gate 1: Check for hard blocker gaps.

        Returns:
            "PASS" or "FAIL"
        """
        gaps_list = self.gaps.get("gaps", [])

        for gap in gaps_list:
            gap_type = gap.get("gap_type")
            module_id = gap.get("module_id", "")

            # Find module
            module = None
            for m in self.modules:
                if m.get("module_id") == module_id:
                    module = m
                    break

            if module and gap_type == "absent-hard" and module.get("hard_blocker"):
                self.gate_1_triggers.append({
                    "gap_id": gap.get("gap_id"),
                    "module_id": module_id,
                    "reason": "absent-hard gap with hard_blocker flag"
                })

        if self.gate_1_triggers:
            return "FAIL"
        return "PASS"

    def _gate_2_domain_floor_check(self) -> str:
        """
        Gate 2: Check if hard-blocker domains meet minimum floor.

        Returns:
            "PASS" or "FAIL"
        """
        # Get domain scores
        domain_scores = self.scores.get("domain_scores", {})

        for domain_id, domain_data in self.domains.items():
            criticality = domain_data.get("criticality", "standard")

            # Only check hard-blocker domains
            if criticality != "hard-blocker":
                continue

            # Get domain score
            domain_id_int = int(domain_id) if isinstance(domain_id, str) else domain_id
            score_dict = domain_scores.get(domain_id_int, {})
            readiness_score = score_dict.get("readiness_score", 0.0)
            readiness_percentage = readiness_score * 100

            if readiness_percentage < self.DOMAIN_FLOOR_HARD_BLOCKER:
                self.gate_2_triggers.append({
                    "domain_id": domain_id,
                    "readiness_percentage": readiness_percentage,
                    "reason": f"hard-blocker domain below {self.DOMAIN_FLOOR_HARD_BLOCKER}% floor"
                })

        if self.gate_2_triggers:
            return "FAIL"
        return "PASS"

    def _gate_3_score_based_determination(self) -> str:
        """
        Gate 3: Determine status based on readiness score.

        Returns:
            Determination string
        """
        self.readiness_percentage = self.scores.get("overall_readiness_percentage", 0.0)

        if self.readiness_percentage >= self.READINESS_GO_THRESHOLD:
            return "GO"
        elif self.readiness_percentage >= self.READINESS_CONDITIONAL_GO_MIN:
            return "CONDITIONAL GO"
        elif self.readiness_percentage >= self.READINESS_CONDITIONAL_HOLD_MIN:
            return "CONDITIONAL HOLD"
        else:
            return "NO-GO"

    def _apply_fit_modifier(self, determination: str) -> str:
        """
        Apply fit-to-purpose modifier to determination.

        Args:
            determination: Current determination string

        Returns:
            Modified determination string
        """
        self.fit_percentage = self.scores.get("overall_fit_percentage", 0.0)

        # No modifier if fit >= 70%
        if self.fit_percentage >= 70:
            return determination

        # Hard floor: if fit < 50%, determination cannot be better than CONDITIONAL HOLD
        if self.fit_percentage < self.FIT_MODIFIER_THRESHOLD_LOW:
            self.fit_modifier_applied = True
            self.fit_modifier_direction = "downgrade-to-minimum"

            det_enum = Determination[determination.replace(" ", "_")]
            min_det = Determination.CONDITIONAL_HOLD

            return min_det.value if det_enum > min_det else determination

        # Downgrade by one level if 50–69%
        if self.fit_percentage <= self.FIT_MODIFIER_THRESHOLD_HIGH:
            self.fit_modifier_applied = True
            self.fit_modifier_direction = "downgrade-one-level"

            downgrade_map = {
                "GO": "CONDITIONAL GO",
                "CONDITIONAL GO": "CONDITIONAL HOLD",
                "CONDITIONAL HOLD": "NO-GO",
                "NO-GO": "NO-GO"
            }

            return downgrade_map.get(determination, determination)

        return determination

    def _generate_conditions(self, determination: str) -> None:
        """
        Generate conditions/remediation requirements based on determination.

        Args:
            determination: Final determination string
        """
        gaps_list = self.gaps.get("gaps", [])

        if determination == "CONDITIONAL GO":
            # List specific gaps that are conditions
            for gap in gaps_list:
                if gap.get("severity") in ["critical", "high"]:
                    self.conditions.append({
                        "type": "gap-resolution",
                        "gap_id": gap.get("gap_id"),
                        "gap_type": gap.get("gap_type"),
                        "requirement": f"Resolve {gap.get('gap_type')} gap {gap.get('gap_id')}"
                    })

        elif determination == "CONDITIONAL HOLD":
            # List critical remediation requirements
            critical_gaps = [g for g in gaps_list if g.get("severity") == "critical"]
            for gap in critical_gaps:
                self.conditions.append({
                    "type": "critical-remediation",
                    "gap_id": gap.get("gap_id"),
                    "gap_type": gap.get("gap_type"),
                    "requirement": f"Critical remediation required for {gap.get('gap_id')}"
                })

            # Add readiness threshold condition
            if self.readiness_percentage < 75:
                self.conditions.append({
                    "type": "readiness-threshold",
                    "current_percentage": self.readiness_percentage,
                    "requirement": f"Increase readiness from {self.readiness_percentage}% to ≥75%"
                })

        elif determination == "NO-GO":
            # List hard blockers
            if self.gate_1_triggers:
                for trigger in self.gate_1_triggers:
                    self.conditions.append({
                        "type": "hard-blocker",
                        "gap_id": trigger.get("gap_id"),
                        "reason": trigger.get("reason"),
                        "requirement": "Hard blocker must be resolved before proceeding"
                    })

            if self.gate_2_triggers:
                for trigger in self.gate_2_triggers:
                    self.conditions.append({
                        "type": "domain-floor-violation",
                        "domain_id": trigger.get("domain_id"),
                        "reason": trigger.get("reason"),
                        "requirement": f"Domain {trigger.get('domain_id')} must reach {self.DOMAIN_FLOOR_HARD_BLOCKER}% floor"
                    })

    def determine(self) -> Dict[str, Any]:
        """
        Run 3-gate logic and produce determination.

        Returns:
            Dict with determination and gate results
        """
        # Gate 1
        self.gate_1_result = self._gate_1_hard_blocker_check()

        # Gate 2
        self.gate_2_result = self._gate_2_domain_floor_check()

        # Gate 3
        self.gate_3_result = self._gate_3_score_based_determination()

        # Apply fit modifier
        determination = self.gate_3_result
        determination = self._apply_fit_modifier(determination)

        # Worst of gates
        # Gate 1 FAIL → NO-GO
        if self.gate_1_result == "FAIL":
            determination = Determination.NO_GO.value

        # Gate 2 FAIL → at worst CONDITIONAL HOLD
        if self.gate_2_result == "FAIL":
            det_enum = Determination[determination.replace(" ", "_")]
            min_det = Determination.CONDITIONAL_HOLD
            if det_enum > min_det:
                determination = min_det.value

        # Generate conditions
        self._generate_conditions(determination)

        return {
            "determination": determination,
            "gate_results": {
                "gate_1_hard_blocker": {
                    "result": self.gate_1_result,
                    "triggered_by": self.gate_1_triggers
                },
                "gate_2_domain_floor": {
                    "result": self.gate_2_result,
                    "triggered_by": self.gate_2_triggers
                },
                "gate_3_score_based": {
                    "result": self.gate_3_result,
                    "readiness_percentage": round(self.readiness_percentage, 2)
                }
            },
            "fit_to_purpose_assessment": {
                "fit_percentage": round(self.fit_percentage, 2),
                "modifier_applied": self.fit_modifier_applied,
                "modifier_direction": self.fit_modifier_direction
            },
            "conditions": self.conditions,
            "computation_metadata": {
                "script_version": "0.1.0",
                "readiness_thresholds": {
                    "go": f">= {self.READINESS_GO_THRESHOLD}%",
                    "conditional_go": f"{self.READINESS_CONDITIONAL_GO_MIN}–{self.READINESS_CONDITIONAL_GO_MAX}%",
                    "conditional_hold": f"{self.READINESS_CONDITIONAL_HOLD_MIN}–{self.READINESS_CONDITIONAL_HOLD_MAX}%",
                    "no_go": f"< {self.READINESS_CONDITIONAL_HOLD_MIN}%"
                },
                "fit_modifiers": {
                    "hard_floor": f"< {self.FIT_MODIFIER_THRESHOLD_LOW}%",
                    "downgrade_threshold": f"{self.FIT_MODIFIER_THRESHOLD_LOW}–{self.FIT_MODIFIER_THRESHOLD_HIGH}%"
                }
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

    args = parser.parse_args()

    try:
        # Read input
        if args.input:
            with open(args.input, "r") as f:
                data = json.load(f)
        else:
            data = json.load(sys.stdin)

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
