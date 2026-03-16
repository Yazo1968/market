#!/usr/bin/env python3
"""
json_validator.py

Validates JSON files against their corresponding schemas. Supports two schema sources:
1. Built-in inline schemas (for business case input data)
2. External JSON schema files from the schemas/ directory (for workflow output data)

Built-in schemas (business case inputs):
  context-profile, investor-profile, startup-metrics, market-analysis,
  team-composition, financial-projections, product-roadmap, competitive-landscape,
  risk-assessment, revenue-model, growth-strategy, exit-plan,
  governance-structure, sustainability-plan

External schemas (workflow outputs — loaded from schemas/ directory):
  assessor-profile, framework, readiness-register, fit-to-purpose-register,
  gap-register, dependency-map, module-content-map, research-log,
  go-nogo-determination, domain-finding, integrated-findings-register,
  sensitivity-analysis, recommendations

Usage:
  python json_validator.py --schema context-profile --input data.json
  python json_validator.py --schema gap-register --input gap-register.json --schema-dir /path/to/schemas/

Exit codes:
  0 = validation passed
  1 = validation errors found
  2 = schema not found
  3 = input file not found

Author: Startup Assessment Plugin
Version: 0.2.0
"""

import json
import sys
import argparse
from typing import Any, Dict, List, Optional
from pathlib import Path
from enum import Enum


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


class SchemaNotFoundError(ValidationError):
    """Raised when schema is not found."""
    pass


class ValidationCheck(Enum):
    """Enumeration of validation checks."""
    JSON_PARSE = "JSON parse"
    REQUIRED_FIELDS = "Required fields"
    FIELD_TYPES = "Field types"
    ENUM_VALUES = "Enum values"
    NUMERIC_RANGES = "Numeric ranges"
    ARRAY_ITEMS = "Array items"


SCHEMAS = {
    "context-profile": {
        "required": ["organization_name", "assessment_date", "assessor_id"],
        "properties": {
            "organization_name": "string",
            "assessment_date": "string",
            "assessor_id": "string",
            "country": "string",
            "industry_code": "string"
        }
    },
    "investor-profile": {
        "required": ["investor_name", "investment_focus"],
        "properties": {
            "investor_name": "string",
            "investment_focus": "string",
            "min_check_size": "number",
            "max_check_size": "number",
            "stage_preference": "string",
            "sector_preferences": ["string"]
        },
        "enums": {
            "stage_preference": ["seed", "pre-seed", "series-a", "series-b", "growth"]
        },
        "ranges": {
            "min_check_size": {"min": 0},
            "max_check_size": {"min": 0}
        }
    },
    "startup-metrics": {
        "required": ["mrr", "arr", "customer_count"],
        "properties": {
            "mrr": "number",
            "arr": "number",
            "customer_count": "integer",
            "churn_rate": "number",
            "growth_rate": "number"
        },
        "ranges": {
            "mrr": {"min": 0},
            "arr": {"min": 0},
            "customer_count": {"min": 0},
            "churn_rate": {"min": 0, "max": 100},
            "growth_rate": {"min": -100, "max": 500}
        }
    },
    "market-analysis": {
        "required": ["tam", "sam", "analysis_date"],
        "properties": {
            "tam": "number",
            "sam": "number",
            "som": "number",
            "analysis_date": "string",
            "market_growth_rate": "number"
        },
        "ranges": {
            "tam": {"min": 0},
            "sam": {"min": 0},
            "som": {"min": 0},
            "market_growth_rate": {"min": -50, "max": 500}
        }
    },
    "team-composition": {
        "required": ["team_members"],
        "properties": {
            "team_members": [{
                "name": "string",
                "role": "string",
                "experience_years": "integer"
            }],
            "total_headcount": "integer"
        },
        "ranges": {
            "total_headcount": {"min": 0}
        }
    },
    "financial-projections": {
        "required": ["projection_date", "projections"],
        "properties": {
            "projection_date": "string",
            "projections": [{
                "year": "integer",
                "revenue": "number",
                "expenses": "number"
            }]
        }
    },
    "product-roadmap": {
        "required": ["current_version", "milestones"],
        "properties": {
            "current_version": "string",
            "milestones": [{
                "name": "string",
                "target_date": "string",
                "status": "string"
            }]
        },
        "enums": {
            "status": ["planned", "in-progress", "completed", "delayed"]
        }
    },
    "competitive-landscape": {
        "required": ["market_position", "competitors"],
        "properties": {
            "market_position": "string",
            "competitors": [{
                "name": "string",
                "strength": "string",
                "weakness": "string"
            }]
        }
    },
    "risk-assessment": {
        "required": ["key_risks"],
        "properties": {
            "key_risks": [{
                "description": "string",
                "probability": "number",
                "impact": "string",
                "mitigation": "string"
            }]
        },
        "enums": {
            "impact": ["low", "medium", "high", "critical"]
        },
        "ranges": {
            "probability": {"min": 0, "max": 1}
        }
    },
    "revenue-model": {
        "required": ["model_type", "pricing_strategy"],
        "properties": {
            "model_type": "string",
            "pricing_strategy": "string",
            "unit_economics": "object"
        },
        "enums": {
            "model_type": ["subscription", "transaction", "hybrid", "freemium"],
            "pricing_strategy": ["value-based", "cost-plus", "competitive", "dynamic"]
        }
    },
    "growth-strategy": {
        "required": ["primary_channels", "target_metrics"],
        "properties": {
            "primary_channels": ["string"],
            "target_metrics": ["string"],
            "timeline_months": "integer"
        },
        "ranges": {
            "timeline_months": {"min": 1, "max": 60}
        }
    },
    "exit-plan": {
        "required": ["exit_type", "target_timeline"],
        "properties": {
            "exit_type": "string",
            "target_timeline": "integer",
            "target_acquirers": ["string"]
        },
        "enums": {
            "exit_type": ["acquisition", "ipo", "secondary", "merger"]
        },
        "ranges": {
            "target_timeline": {"min": 1, "max": 15}
        }
    },
    "governance-structure": {
        "required": ["board_composition", "decision_authority"],
        "properties": {
            "board_composition": ["string"],
            "decision_authority": "object"
        }
    },
    "sustainability-plan": {
        "required": ["sustainability_goals", "implementation_timeline"],
        "properties": {
            "sustainability_goals": ["string"],
            "implementation_timeline": "string",
            "environmental_impact": "string"
        }
    }
}


def load_external_schema(schema_name: str, schema_dir: Optional[str] = None) -> Optional[Dict]:
    """
    Attempt to load a schema from the external schemas/ directory.
    Returns the schema dict if found, None otherwise.
    """
    if schema_dir is None:
        # Default: look relative to this script's location
        schema_dir = str(Path(__file__).parent.parent / "schemas")

    schema_path = Path(schema_dir) / f"{schema_name}.json"
    if schema_path.exists():
        with open(schema_path, "r") as f:
            return json.load(f)
    return None


def convert_json_schema_to_inline(json_schema: Dict) -> Dict:
    """
    Convert a standard JSON Schema to the inline format used by SCHEMAS dict.
    Extracts required fields, property types, enums, and ranges.
    """
    inline = {}

    if "required" in json_schema:
        inline["required"] = json_schema["required"]

    props = json_schema.get("properties", {})
    if props:
        inline["properties"] = {}
        inline["enums"] = {}
        inline["ranges"] = {}

        for field, spec in props.items():
            if isinstance(spec, dict):
                field_type = spec.get("type", "string")
                if field_type == "array":
                    inline["properties"][field] = ["string"]
                elif field_type == "object":
                    inline["properties"][field] = "object"
                else:
                    inline["properties"][field] = field_type

                # Extract enums
                if "enum" in spec:
                    inline["enums"][field] = spec["enum"]

                # Extract ranges
                if "minimum" in spec or "maximum" in spec:
                    range_spec = {}
                    if "minimum" in spec:
                        range_spec["min"] = spec["minimum"]
                    if "maximum" in spec:
                        range_spec["max"] = spec["maximum"]
                    inline["ranges"][field] = range_spec

        # Clean empty dicts
        if not inline["enums"]:
            del inline["enums"]
        if not inline["ranges"]:
            del inline["ranges"]

    return inline


class JsonValidator:
    """
    Validates JSON against predefined or external schemas.
    """

    def __init__(self, schema_name: str, schema_dir: Optional[str] = None) -> None:
        """
        Initialize validator with schema.

        Looks up schema in order:
        1. Built-in SCHEMAS dict
        2. External JSON schema file in schemas/ directory

        Args:
            schema_name: Name of schema to validate against
            schema_dir: Optional path to schemas directory

        Raises:
            SchemaNotFoundError: If schema does not exist
        """
        # External schemas take precedence over built-in (they are more complete)
        external = load_external_schema(schema_name, schema_dir)
        if external is not None:
            self.schema = convert_json_schema_to_inline(external)
        elif schema_name in SCHEMAS:
            self.schema = SCHEMAS[schema_name]
        else:
            all_schemas = list(SCHEMAS.keys())
            # List available external schemas
            default_dir = Path(__file__).parent.parent / "schemas"
            if default_dir.exists():
                all_schemas += [f.stem for f in default_dir.glob("*.json")]
            raise SchemaNotFoundError(
                f"Schema '{schema_name}' not found. Available schemas: "
                f"{', '.join(sorted(set(all_schemas)))}"
            )

        self.schema_name = schema_name
        self.errors: List[Dict[str, Any]] = []
        self.checks_passed: List[str] = []

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate data against schema.

        Args:
            data: Data to validate

        Returns:
            Validation report dict
        """
        self._validate_required_fields(data)
        self._validate_field_types(data)
        self._validate_enum_values(data)
        self._validate_numeric_ranges(data)
        self._validate_array_items(data)

        is_valid = len(self.errors) == 0

        return {
            "valid": is_valid,
            "schema": self.schema_name,
            "errors": self.errors,
            "checks_passed": self.checks_passed,
            "error_count": len(self.errors),
            "check_count": len(self.checks_passed) + len(self.errors)
        }

    def _validate_required_fields(self, data: Dict[str, Any]) -> None:
        """
        Check that all required fields are present.

        Args:
            data: Data to validate
        """
        required = self.schema.get("required", [])

        for field in required:
            if field not in data:
                self.errors.append({
                    "check": ValidationCheck.REQUIRED_FIELDS.value,
                    "field": field,
                    "error": f"Required field '{field}' is missing"
                })
            else:
                self.checks_passed.append(f"Required field '{field}' present")

    def _validate_field_types(self, data: Dict[str, Any]) -> None:
        """
        Check that field types match schema.

        Args:
            data: Data to validate
        """
        properties = self.schema.get("properties", {})

        for field, expected_type in properties.items():
            if field not in data:
                continue

            value = data[field]
            if not self._check_type(value, expected_type):
                self.errors.append({
                    "check": ValidationCheck.FIELD_TYPES.value,
                    "field": field,
                    "error": f"Field '{field}' type mismatch. Expected {expected_type}, "
                             f"got {type(value).__name__}"
                })
            else:
                self.checks_passed.append(f"Field '{field}' type valid")

    def _check_type(self, value: Any, expected_type: Any) -> bool:
        """
        Check if value matches expected type.

        Args:
            value: Value to check
            expected_type: Expected type spec

        Returns:
            True if type matches
        """
        if isinstance(expected_type, str):
            type_map = {
                "string": str,
                "integer": int,
                "number": (int, float),
                "boolean": bool,
                "object": dict,
                "array": list
            }
            return isinstance(value, type_map.get(expected_type, object))

        if isinstance(expected_type, list):
            return isinstance(value, list)

        if isinstance(expected_type, dict):
            return isinstance(value, dict)

        return True

    def _validate_enum_values(self, data: Dict[str, Any]) -> None:
        """
        Check that enum fields have allowed values.

        Args:
            data: Data to validate
        """
        enums = self.schema.get("enums", {})

        for field, allowed_values in enums.items():
            if field not in data:
                continue

            value = data[field]

            has_error = False
            if isinstance(value, list):
                for item in value:
                    if item not in allowed_values:
                        self.errors.append({
                            "check": ValidationCheck.ENUM_VALUES.value,
                            "field": field,
                            "error": f"Value '{item}' not in allowed values: {allowed_values}"
                        })
                        has_error = True
            else:
                if value not in allowed_values:
                    self.errors.append({
                        "check": ValidationCheck.ENUM_VALUES.value,
                        "field": field,
                        "error": f"Value '{value}' not in allowed values: {allowed_values}"
                    })
                    has_error = True

            if not has_error:
                self.checks_passed.append(f"Field '{field}' enum values valid")

    def _validate_numeric_ranges(self, data: Dict[str, Any]) -> None:
        """
        Check that numeric fields are within valid ranges.

        Args:
            data: Data to validate
        """
        ranges = self.schema.get("ranges", {})

        for field, range_spec in ranges.items():
            if field not in data:
                continue

            value = data[field]

            if not isinstance(value, (int, float)):
                continue

            min_val = range_spec.get("min")
            max_val = range_spec.get("max")

            if min_val is not None and value < min_val:
                self.errors.append({
                    "check": ValidationCheck.NUMERIC_RANGES.value,
                    "field": field,
                    "error": f"Value {value} is below minimum {min_val}"
                })
            elif max_val is not None and value > max_val:
                self.errors.append({
                    "check": ValidationCheck.NUMERIC_RANGES.value,
                    "field": field,
                    "error": f"Value {value} exceeds maximum {max_val}"
                })
            else:
                self.checks_passed.append(f"Field '{field}' numeric range valid")

    def _validate_array_items(self, data: Dict[str, Any]) -> None:
        """
        Check that array items match schema.

        Args:
            data: Data to validate
        """
        properties = self.schema.get("properties", {})

        for field, field_spec in properties.items():
            if field not in data or not isinstance(field_spec, list):
                continue

            value = data[field]

            if not isinstance(value, list):
                continue

            if not field_spec:
                continue

            item_schema = field_spec[0]
            if not isinstance(item_schema, dict):
                continue

            array_errors = 0
            for i, item in enumerate(value):
                for key, expected_type in item_schema.items():
                    if key not in item:
                        self.errors.append({
                            "check": ValidationCheck.ARRAY_ITEMS.value,
                            "field": f"{field}[{i}]",
                            "error": f"Missing required array item field '{key}'"
                        })
                        array_errors += 1
                    elif not self._check_type(item[key], expected_type):
                        self.errors.append({
                            "check": ValidationCheck.ARRAY_ITEMS.value,
                            "field": f"{field}[{i}].{key}",
                            "error": f"Type mismatch. Expected {expected_type}, "
                                     f"got {type(item[key]).__name__}"
                        })
                        array_errors += 1

            if array_errors == 0:
                self.checks_passed.append(f"Field '{field}' array items valid")


def main() -> int:
    """
    Main entry point.

    Returns:
        Exit code (0 = valid, 1 = errors, 2 = schema not found, 3 = file not found)
    """
    parser = argparse.ArgumentParser(
        description="Validate JSON against schema"
    )
    parser.add_argument(
        "--schema",
        required=True,
        help=f"Schema to validate against: {', '.join(SCHEMAS.keys())}"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input JSON file to validate"
    )
    parser.add_argument(
        "--schema-dir",
        required=False,
        default=None,
        help="Path to external schemas directory (default: ../schemas/ relative to script)"
    )

    args = parser.parse_args()

    try:
        # Load schema
        try:
            validator = JsonValidator(args.schema, schema_dir=args.schema_dir)
        except SchemaNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 2

        # Load input
        try:
            with open(args.input, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found: {args.input}", file=sys.stderr)
            return 3
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {args.input}: {e}", file=sys.stderr)
            return 1

        # Validate
        result = validator.validate(data)

        # Output
        print(json.dumps(result, indent=2))

        # Return appropriate code
        return 0 if result["valid"] else 1

    except Exception as e:
        print(f"Error: Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
