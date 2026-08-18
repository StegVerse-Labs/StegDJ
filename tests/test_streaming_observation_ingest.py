import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
MODULE_PATH = ROOT / "script" / "ingest_streaming_observation.py"
SPEC = importlib.util.spec_from_file_location("ingest_streaming_observation", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class StreamingObservationIngestTests(unittest.TestCase):
    def fixture(self):
        path = ROOT / "fixtures" / "streaming" / "authorized_observation.json"
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def test_authorized_export_ingests_without_network(self):
        result = MODULE.ingest(self.fixture())
        self.assertEqual(result["credential_requirement"], "NONE_FOR_BOUNDED_IMPORT")
        self.assertFalse(result["network_required"])
        self.assertFalse(result["authority_effect"])
        self.assertEqual(len(result["observation_sha256"]), 64)

    def test_unknown_metric_is_preserved(self):
        result = MODULE.ingest(self.fixture())
        self.assertEqual(result["metrics"]["repeat_listening"], "UNKNOWN")

    def test_observation_cannot_grant_authority(self):
        value = self.fixture()
        value["audience_response_grants_authority"] = True
        with self.assertRaises(MODULE.StreamingObservationError):
            MODULE.ingest(value)

    def test_source_authorization_is_required(self):
        value = self.fixture()
        del value["source_authorization_ref"]
        with self.assertRaises(MODULE.StreamingObservationError):
            MODULE.ingest(value)


if __name__ == "__main__":
    unittest.main()
