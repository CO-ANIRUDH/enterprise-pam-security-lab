
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
import pam_engine
from datetime import datetime

import pam_engine


class TestPAMEngine(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.audit_path = Path(self.temp_dir.name) / "audit.jsonl"
        self.audit_patch = patch.object(
            pam_engine, "AUDIT_FILE", self.audit_path
        )
        self.audit_patch.start()

    def tearDown(self):
        self.audit_patch.stop()
        self.temp_dir.cleanup()

    def test_authorized_approved_access(self):
        result = pam_engine.request_access(
            "rahul", "production_server", True, 30
        )
        self.assertEqual(result["decision"], "ALLOW")

    def test_unauthorized_role_is_denied(self):
        result = pam_engine.request_access(
            "priya", "production_server", True, 30
        )
        self.assertEqual(result["decision"], "DENY")

    def test_missing_approval_is_denied(self):
        result = pam_engine.request_access(
            "rahul", "production_server", False, 30
        )
        self.assertEqual(result["decision"], "DENY")

    def test_unknown_user_is_denied(self):
        result = pam_engine.request_access(
            "unknown_user", "production_server", True, 30
        )
        self.assertEqual(result["decision"], "DENY")

    def test_invalid_duration_is_denied(self):
        result = pam_engine.request_access(
            "rahul", "production_server", True, 120
        )
        self.assertEqual(result["decision"], "DENY")

    def test_audit_event_is_written(self):
        pam_engine.request_access(
            "rahul", "production_server", True, 30
        )
        self.assertTrue(self.audit_path.exists())
        self.assertEqual(len(self.audit_path.read_text().splitlines()), 1)
    
    def test_access_is_active_before_expiry(self):
        event = {
            "decision": "ALLOW",
            "expires_at": "2026-10-09T15:30:00+00:00",
        }
        now = datetime.fromisoformat("2026-10-09T15:00:00+00:00")
        self.assertTrue(pam_engine.is_access_active(event, now))

    def test_access_is_inactive_after_expiry(self):
        event = {
            "decision": "ALLOW",
            "expires_at": "2026-10-09T15:30:00+00:00",
        }
        now = datetime.fromisoformat("2026-10-09T15:31:00+00:00")
        self.assertFalse(pam_engine.is_access_active(event, now))



if __name__ == "__main__":
    unittest.main()
