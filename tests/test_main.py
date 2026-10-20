import sys
import unittest
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from main import descriptive_summary, load_data


class TestStudentPerformanceAnalyzer(unittest.TestCase):
    def test_dataset_loads_and_has_expected_rows(self):
        df = load_data()
        self.assertEqual(len(df), 20)
        self.assertIn("exam_score", df.columns)

    def test_summary_counts_match_dataset(self):
        df = pd.DataFrame({
            "student_id": ["A", "B", "C"],
            "study_hours_per_week": [2, 4, 6],
            "attendance_percent": [60, 80, 90],
            "exam_score": [50, 60, 90],
        })
        summary = descriptive_summary(df)
        self.assertEqual(summary["student_count"], 3)
        self.assertEqual(summary["below_threshold_count"], 1)
        self.assertEqual(summary["at_or_above_threshold_count"], 2)
        self.assertAlmostEqual(summary["mean_score"], 200 / 3)


if __name__ == "__main__":
    unittest.main()
