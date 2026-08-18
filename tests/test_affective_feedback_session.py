import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).parents[1] / "script" / "validate_affective_feedback_session.py"
SPEC = importlib.util.spec_from_file_location("validate_affective_feedback_session", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def session():
    return {
        "session_id": "session-001",
        "experiment_id": "exp-001",
        "state_family_id": "family-001",
        "stimulus_receipt_ids": ["receipt://music/001"],
        "observation_refs": ["observation://001"],
        "transition_sequence": [
            {
                "from_state": "baseline",
                "stimulus_receipt_id": "receipt://music/001",
                "to_state": "engagement-candidate",
                "confidence": 0.62,
                "status": "CANDIDATE",
                "observation_refs": ["observation://001"]
            }
        ],
        "consent_receipt_id": "receipt://consent/001",
        "orchestration_policy": {
            "adaptation_allowed": True,
            "maximum_adaptive_steps": 3,
            "blocked_inference_stops_session": True,
            "review_required_stops_adaptation": True
        },
        "state": "OBSERVING",
        "authority": {
            "emotion_inference_grants_action_authority": False,
            "audience_response_grants_publication_authority": False,
            "sensor_observation_grants_licensing_authority": False
        }
    }


class AffectiveFeedbackSessionTests(unittest.TestCase):
    def test_candidate_observation_passes(self):
        MODULE.validate(session())

    def test_blocked_transition_requires_blocked_session(self):
        value = session()
        value["transition_sequence"][0]["status"] = "BLOCKED"
        with self.assertRaises(MODULE.AffectiveSessionError):
            MODULE.validate(value)
        value["state"] = "BLOCKED"
        MODULE.validate(value)

    def test_review_required_stops_adaptation(self):
        value = session()
        value["transition_sequence"][0]["status"] = "REVIEW_REQUIRED"
        value["state"] = "ADAPTING"
        with self.assertRaises(MODULE.AffectiveSessionError):
            MODULE.validate(value)

    def test_adaptation_policy_is_enforced(self):
        value = session()
        value["orchestration_policy"]["adaptation_allowed"] = False
        value["state"] = "ADAPTING"
        with self.assertRaises(MODULE.AffectiveSessionError):
            MODULE.validate(value)

    def test_inference_cannot_self_grant_authority(self):
        value = session()
        value["authority"]["emotion_inference_grants_action_authority"] = True
        with self.assertRaises(MODULE.AffectiveSessionError):
            MODULE.validate(value)

    def test_transition_must_bind_declared_stimulus_receipt(self):
        value = session()
        value["transition_sequence"][0]["stimulus_receipt_id"] = "receipt://music/undeclared"
        with self.assertRaises(MODULE.AffectiveSessionError):
            MODULE.validate(value)

    def test_transition_must_bind_declared_observation(self):
        value = session()
        value["transition_sequence"][0]["observation_refs"] = ["observation://undeclared"]
        with self.assertRaises(MODULE.AffectiveSessionError):
            MODULE.validate(value)


if __name__ == "__main__":
    unittest.main()
