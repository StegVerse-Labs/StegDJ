#!/usr/bin/env python3
"""Validate and hash authorized streaming observations without platform API dependency."""

import hashlib
import json
import pathlib
import sys
from typing import Any, Dict

from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "contracts" / "streaming_observation.schema.json"


class StreamingObservationError(ValueError):
    pass


def _schema() -> Dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ingest(value: Dict[str, Any]) -> Dict[str, Any]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(value), key=lambda error: list(error.absolute_path))
    if errors:
        detail = "; ".join(
            f"{'.'.join(str(p) for p in error.absolute_path) or '<root>'}: {error.message}"
            for error in errors
        )
        raise StreamingObservationError(detail)

    if value["audience_response_grants_authority"] is not False:
        raise StreamingObservationError("audience response may not grant authority")

    canonical = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "observation_id": value["observation_id"],
        "cohort_id": value["cohort_id"],
        "service": value["service"],
        "source_kind": value.get("source_kind", "OTHER_AUTHORIZED"),
        "observation_sha256": hashlib.sha256(canonical).hexdigest(),
        "credential_requirement": "NONE_FOR_BOUNDED_IMPORT",
        "network_required": False,
        "metrics": value["metrics"],
        "normalization": value.get("normalization", {}),
        "promotion_recommendation": value.get("promotion_recommendation", "NO_RECOMMENDATION"),
        "authority_effect": False,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: ingest_streaming_observation.py <observation.json>", file=sys.stderr)
        return 2
    try:
        with pathlib.Path(argv[1]).open("r", encoding="utf-8") as handle:
            result = ingest(json.load(handle))
    except (OSError, json.JSONDecodeError, StreamingObservationError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
