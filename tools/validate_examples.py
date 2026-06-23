#!/usr/bin/env python3
"""Validate StegDJ framework examples against local JSON schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:
    raise SystemExit("Missing dependency: jsonschema. Install with `python -m pip install jsonschema`.") from exc

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    ("schemas/listener-event-intent.schema.json", "examples/christmas-listener-event-intent.json"),
    ("schemas/music-selection-request.schema.json", "examples/christmas-music-selection-request.json"),
    ("schemas/playback-receipt.schema.json", "examples/christmas-playback-receipt.json"),
]


def load_json(path: str) -> Any:
    with (ROOT / path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    failed = False
    for schema_path, data_path in CASES:
        validator = Draft202012Validator(load_json(schema_path))
        errors = [error.message for error in sorted(validator.iter_errors(load_json(data_path)), key=str)]
        if errors:
            failed = True
            print(f"FAIL {data_path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {data_path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
