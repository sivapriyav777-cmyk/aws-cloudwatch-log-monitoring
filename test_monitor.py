
import unittest
from cloudwatch_monitor import analyze_logs


class TestLogMonitoring(unittest.TestCase):

    def test_log_counts(self):
        logs = [
            "INFO Application started",
            "ERROR Database failed",
            "WARNING High CPU usage",
            "INFO Process completed"
        ]

        result = analyze_logs(logs)

        self.assertEqual(result["total_logs"], 4)
        self.assertEqual(result["error_count"], 1)
        self.assertEqual(result["warning_count"], 1)
        self.assertEqual(result["info_count"], 2)
        self.assertEqual(result["other_count"], 0)


if __name__ == "__main__":
    unittest.main()
