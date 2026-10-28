import io
import unittest
from unittest.mock import patch
from src.triage_checklist import main

class TriageChecklistTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["2"])
    def test_unverified_caller_stops(self, _input):
        output = io.StringIO()
        with patch("sys.stdout", new=output):
            main()
        self.assertIn("STOP", output.getvalue())

    @patch("builtins.input", side_effect=["1", "1"])
    def test_inactive_account_escalates(self, _input):
        output = io.StringIO()
        with patch("sys.stdout", new=output):
            main()
        self.assertIn("Do not reactivate", output.getvalue())

    @patch("builtins.input", side_effect=["1", "4"])
    def test_authorization_issue_at_right_layer(self, _input):
        output = io.StringIO()
        with patch("sys.stdout", new=output):
            main()
        self.assertIn("Treat as authorization", output.getvalue())

if __name__ == "__main__":
    unittest.main()
