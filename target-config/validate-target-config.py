from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = ROOT / "target-config" / "target-config.example.yaml"
SCHEMA_PATH = ROOT / "target-config" / "target-config.schema.json"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Target config file does not exist: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError("Target config must be a YAML object.")

    return data


def load_schema(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Target config schema does not exist: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Target config schema must be a JSON object.")

    return data


def format_error_path(error_path: Any) -> str:
    parts = [str(part) for part in error_path]

    if not parts:
        return "$"

    return "$." + ".".join(parts)


def validate_config(config_path: Path) -> int:
    config = load_yaml(config_path)
    schema = load_schema(SCHEMA_PATH)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(config), key=lambda error: list(error.path))

    if errors:
        print("Target configuration validation failed.")
        print()

        for error in errors:
            print(f"- {format_error_path(error.path)}: {error.message}")

        return 1

    print(f"Target configuration validation passed: {config_path}")
    return 0


def main() -> int:
    if len(sys.argv) > 2:
        print("Usage: python target-config/validate-target-config.py [config-path]")
        return 2

    config_path = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else DEFAULT_CONFIG_PATH

    try:
        return validate_config(config_path)
    except Exception as exc:
        print(f"Target configuration validation error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
