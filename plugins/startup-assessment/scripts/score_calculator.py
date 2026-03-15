#!/usr/bin/env python3
"""
score_calculator.py

Computes per-module, per-domain, and overall scores on both the Readiness and
Fit-to-Purpose tracks. This is a deterministic calculation that normalizes scores
and produces weighted aggregates across the module hierarchy.

Usage:
  python score_calculator.py [input.json]
  python score_calculator.py --readiness readiness.json --fit fit.json --framework framework.json
  cat input.json | python score_calculator.py

Author: Startup Assessment Plugin
Version: 0.2.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List


class ScoreCalculationError(Exception):
    """Raised when score calculation fails validation or computation."""
    pass


class ScoreCalculator:
    """
    Calculates readiness and fit-to-purpose scores across modules and domains.

    Readiness Track:
    - Completeness (0-3) + Quality (0-2) = 0-5 per module
    - Normalized to 0-1 per module
    - Weighted by module_weight within domain
    - Domain score: weighted avg of modules
    - Overall: weighted avg of domains

    Fit-to-Purpose Track:
    - Stage Appropriateness (0-2) + Assessor Alignment (0-2) + Ask Coherence (0-2) = 0-6
    - Normalized to 0-1 per module
    - Weighted by module_weight within domain
    - Domain score: weighted avg of modules
    - Overall: weighted avg of domains
    """

    READINESS_MAX = 5.0
    FIT_MAX = 6.0
    WEIGHT_TOLERANCE = 0.001

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize calculator with input data.

        Args:
            data: Dict with 'modules' and 'domains' keys.
                  'domains' can be a list of dicts or a dict keyed by domain_id.

        Raises:
            ScoreCalculationError: If input structure is invalid
        """
        self.data = data
        self.modules = data.get("modules", [])
        self.company_name = data.get("company_name", "")

        # Accept domains as either list or dict
        raw_domains = data.get("domains", [])
        if isinstance(raw_domains, dict):
            self.domains = list(raw_domains.values())
        else:
            self.domains = raw_domains

        self.module_scores: List[Dict[str, Any]] = []
        self.domain_scores: List[Dict[str, Any]] = []
        self.overall_readiness = 0.0
        self.overall_fit = 0.0

        self._validate_input()

    def _validate_input(self) -> None:
        """
        Validate input structure and values.

        Raises:
            ScoreCalculationError: If validation fails
        """
        if not isinstance(self.modules, list):
            raise ScoreCalculationError("'modules' must be a list")
        if not isinstance(self.domains, list):
            raise ScoreCalculationError("'domains' must be a list (or dict)")

        # Check domain weights sum to 1.0 (only for active domains)
        active_domains = [d for d in self.domains if d.get("active", True)]
        domain_weight_sum = sum(d.get("domain_weight", 0) for d in active_domains)
        if active_domains and abs(domain_weight_sum - 1.0) > self.WEIGHT_TOLERANCE:
            raise ScoreCalculationError(
                f"Active domain weights must sum to 1.0 ±0.001, got {domain_weight_sum}"
            )

        # Validate modules
        for i, module in enumerate(self.modules):
            self._validate_module(module, i)

    def _validate_module(self, module: Dict[str, Any], index: int) -> None:
        """
        Validate a single module record.

        Args:
            module: Module data dict
            index: Module index in list

        Raises:
            ScoreCalculationError: If module is invalid
        """
        required = ["module_id", "domain_id", "module_weight"]
        for field in required:
            if field not in module:
                raise ScoreCalculationError(
                    f"modules[{index}]: missing required field '{field}'"
                )

        # Validate readiness scores (must be numeric)
        completeness = module.get("completeness_score", -1)
        quality = module.get("quality_score", -1)
        if not isinstance(completeness, (int, float)) or not (0 <= completeness <= 3):
            raise ScoreCalculationError(
                f"modules[{index}].completeness_score must be numeric 0-3, got {completeness}"
            )
        if not isinstance(quality, (int, float)) or not (0 <= quality <= 2):
            raise ScoreCalculationError(
                f"modules[{index}].quality_score must be numeric 0-2, got {quality}"
            )

        # Validate fit scores
        for field, max_val in [
            ("stage_appropriateness", 2),
            ("assessor_alignment", 2),
            ("ask_coherence", 2)
        ]:
            val = module.get(field, -1)
            if not isinstance(val, (int, float)) or not (0 <= val <= max_val):
                raise ScoreCalculationError(
                    f"modules[{index}].{field} must be numeric 0-{max_val}, got {val}"
                )

    def _validate_domain_weights(self, domain_id: Any) -> None:
        """
        Validate that module weights within a domain sum to 1.0.

        Args:
            domain_id: Domain identifier

        Raises:
            ScoreCalculationError: If weights don't sum correctly
        """
        domain_modules = [m for m in self.modules if m["domain_id"] == domain_id]
        weight_sum = sum(m.get("module_weight", 0) for m in domain_modules)

        if domain_modules and abs(weight_sum - 1.0) > self.WEIGHT_TOLERANCE:
            raise ScoreCalculationError(
                f"Domain {domain_id}: module weights must sum to 1.0 ±0.001, "
                f"got {weight_sum}"
            )

    def calculate_module_readiness(self, module: Dict[str, Any]) -> float:
        """
        Calculate normalized readiness score for a module.

        Args:
            module: Module data dict

        Returns:
            Normalized readiness (0.0-1.0)
        """
        completeness = module.get("completeness_score", 0)
        quality = module.get("quality_score", 0)
        raw_score = completeness + quality
        return raw_score / self.READINESS_MAX

    def calculate_module_fit(self, module: Dict[str, Any]) -> float:
        """
        Calculate normalized fit-to-purpose score for a module.

        Args:
            module: Module data dict

        Returns:
            Normalized fit-to-purpose (0.0-1.0)
        """
        stage = module.get("stage_appropriateness", 0)
        alignment = module.get("assessor_alignment", 0)
        coherence = module.get("ask_coherence", 0)
        raw_score = stage + alignment + coherence
        return raw_score / self.FIT_MAX

    def calculate_module_scores(self) -> None:
        """Calculate readiness and fit scores for all modules."""
        for module in self.modules:
            readiness = self.calculate_module_readiness(module)
            fit = self.calculate_module_fit(module)

            self.module_scores.append({
                "module_id": module["module_id"],
                "module_name": module.get("module_name", ""),
                "domain_id": module["domain_id"],
                "completeness_score": module.get("completeness_score", 0),
                "quality_score": module.get("quality_score", 0),
                "combined_score": round(readiness, 4),
                "readiness_score": round(readiness, 4),
                "fit_score": round(fit, 4)
            })

    def calculate_domain_scores(self) -> None:
        """Calculate weighted domain scores across all modules."""
        for domain in self.domains:
            domain_id = domain["domain_id"]
            is_active = domain.get("active", True)

            if not is_active:
                continue

            # Validate module weights for this domain
            self._validate_domain_weights(domain_id)

            # Get modules in this domain
            domain_modules = [m for m in self.modules if m["domain_id"] == domain_id]

            if not domain_modules:
                self.domain_scores.append({
                    "domain_id": domain_id,
                    "domain_name": domain.get("domain_name", f"Domain {domain_id}"),
                    "weighted_readiness_score": 0.0,
                    "weighted_fit_score": 0.0,
                    "active_module_count": 0,
                    "scored_module_count": 0
                })
                continue

            # Calculate weighted averages
            readiness_sum = 0.0
            fit_sum = 0.0

            for module in domain_modules:
                weight = module.get("module_weight", 0)
                readiness = self.calculate_module_readiness(module)
                fit = self.calculate_module_fit(module)

                readiness_sum += readiness * weight
                fit_sum += fit * weight

            self.domain_scores.append({
                "domain_id": domain_id,
                "domain_name": domain.get("domain_name", f"Domain {domain_id}"),
                "weighted_readiness_score": round(readiness_sum, 4),
                "weighted_fit_score": round(fit_sum, 4),
                "active_module_count": len(domain_modules),
                "scored_module_count": len(domain_modules)
            })

    def calculate_overall_scores(self) -> None:
        """Calculate overall readiness and fit-to-purpose scores."""
        active_domains = [d for d in self.domains if d.get("active", True)]

        if not active_domains:
            self.overall_readiness = 0.0
            self.overall_fit = 0.0
            return

        readiness_sum = 0.0
        fit_sum = 0.0

        # Build domain score lookup
        domain_score_map = {ds["domain_id"]: ds for ds in self.domain_scores}

        for domain in active_domains:
            domain_id = domain["domain_id"]
            weight = domain.get("domain_weight", 0)

            if domain_id in domain_score_map:
                ds = domain_score_map[domain_id]
                readiness_sum += ds["weighted_readiness_score"] * weight
                fit_sum += ds["weighted_fit_score"] * weight

        self.overall_readiness = round(readiness_sum, 4)
        self.overall_fit = round(fit_sum, 4)

    def calculate(self) -> Dict[str, Any]:
        """
        Run the complete calculation pipeline.

        Returns:
            Dict with all calculated scores and metadata
        """
        self.calculate_module_scores()
        self.calculate_domain_scores()
        self.calculate_overall_scores()

        return {
            "company_name": self.company_name,
            "modules": self.module_scores,
            "domain_scores": self.domain_scores,
            "overall_readiness_score": self.overall_readiness,
            "overall_readiness_percentage": round(self.overall_readiness * 100, 2),
            "readiness_score_percentage": round(self.overall_readiness * 100, 2),
            "overall_fit_score": self.overall_fit,
            "overall_fit_percentage": round(self.overall_fit * 100, 2),
            "computation_metadata": {
                "active_domains": len([d for d in self.domains if d.get("active", True)]),
                "active_modules": len(self.modules),
                "total_domain_weight": round(
                    sum(d.get("domain_weight", 0) for d in self.domains if d.get("active", True)), 4
                ),
                "script_version": "0.2.0"
            }
        }


def main() -> int:
    """
    Main entry point. Accepts JSON from stdin or file argument.
    Supports both positional input and named flags.

    Returns:
        Exit code (0 = success, 1 = error)
    """
    parser = argparse.ArgumentParser(
        description="Calculate readiness and fit-to-purpose scores"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="Input JSON file (if omitted, reads from stdin)"
    )
    parser.add_argument(
        "--readiness",
        help="Path to readiness-register JSON (alternative input)"
    )
    parser.add_argument(
        "--fit",
        help="Path to fit-to-purpose-register JSON (alternative input)"
    )
    parser.add_argument(
        "--framework",
        help="Path to framework JSON (provides domain structure)"
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

        # Merge framework data if provided separately
        if args.framework:
            with open(args.framework, "r") as f:
                framework_data = json.load(f)
            data.setdefault("domains", framework_data.get("domains", []))
            data.setdefault("company_name", framework_data.get("company_name", ""))

        # Calculate
        calculator = ScoreCalculator(data)
        result = calculator.calculate()

        # Output
        print(json.dumps(result, indent=2))
        return 0

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        return 1
    except ScoreCalculationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
