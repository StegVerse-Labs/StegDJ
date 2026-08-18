#!/usr/bin/env python3
import json
import pathlib
import sys
from typing import Any, Dict

from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "contracts" / "affective_feedback_session.schema.json"


class AffectiveSessionError(ValueError):
    pass


def _schema() -> Dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(session: Dict[str, Any]) -> None:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(session), key=lambda error: list(error.absolute_path))
    if errors:
        detail = "; ".join(
            f"{'.'.join(str(p) for p in error.absolute_path) or '<root>'}: {error.message}"
            for error in errors
        )
        raise AffectiveSessionError(detail)

    policy = session.get("orchestration_policy") or {}
    transitions = session["transition_sequence"]

    blocked = any(step["status"] == "BLOCKED" for step in transitions)
    review = any(step["status"] == "REVIEW_REQUIRED" for step in transitions)

    if blocked and session["state"] not in {"BLOCKED", "FAILED", "SUPERSEDED"}:
        raise AffectiveSessionError("BLOCKED transition requires blocked terminal orchestration state")

    if review and session["state"] == "ADAPTING":
        raise AffectiveSessionError("REVIEW_REQUIRED transition may not continue adaptive orchestration")

    if policy.get("adaptation_allowed") is False and session["state"] == "ADAPTING":
        raise AffectiveSessionError("adaptive orchestration is outside declared policy")

    if policy.get("maximum_adaptive_steps") is not None:
        supported_or_candidate = sum(step["status"] in {"CANDIDATE", "SUPPORTED"} for step in transitions)
        if supported_or_candidate > policy["maximum_adaptive_steps"] and session["state"] == "ADAPTING":
            raise AffectiveSessionError("adaptive step count exceeds declared maximum")

    authority = session["authority"]
    if any(authority.values()):
        raise AffectiveSessionError("observation/inference may not self-grant downstream authority")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_affective_feedback_session.py <session.json>", file=sys.stderr)
        return 2
    try:
        with pathlib.Path(argv[1]).open("r", encoding="utf-8") as handle:
            session = json.load(handle)
        validate(session)
    except (OSError, json.JSONDecodeError, AffectiveSessionError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
