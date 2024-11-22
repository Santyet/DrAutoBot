import unittest
from expert import CarDiagnostic, Symptom

class TestCarDiagnostic(unittest.TestCase):
    def setUp(self):
        self.engine = CarDiagnostic()

    def test_battery_issue(self):
        self.engine.reset()
        self.engine.declare(Symptom(fail_start=True))
        self.engine.run()
        expected_diagnosis = "• Diagnosis: Battery issue causing failure to start."
        expected_suggestion = "• Probability of battery issue: 92.27%\n• Suggestion: Check the battery connections and charge or replace the battery if necessary."
        self.assertIn(expected_diagnosis, self.engine.diagnoses)
        self.assertIn(expected_suggestion, self.engine.diagnoses[expected_diagnosis])

    def test_long_charge_issue(self):
        self.engine.reset()
        self.engine.declare(Symptom(long_charge=True))
        self.engine.run()
        expected_diagnosis = "• Diagnosis: Battery issue causing long charge times."
        expected_suggestion = "• Probability of long charge issue: 70.48%\n• Suggestion: Check the battery and charging system for issues."
        self.assertIn(expected_diagnosis, self.engine.diagnoses)
        self.assertIn(expected_suggestion, self.engine.diagnoses[expected_diagnosis])

    def test_combined_issues(self):
        self.engine.reset()
        self.engine.declare(Symptom(fail_start=True))
        self.engine.declare(Symptom(long_charge=True))
        self.engine.run()
        expected_diagnosis_fail_start = "• Diagnosis: Battery issue causing failure to start."
        expected_suggestion_fail_start = "• Probability of battery issue: 92.27%\n• Suggestion: Check the battery connections and charge or replace the battery if necessary."
        expected_diagnosis_long_charge = "• Diagnosis: Battery issue causing long charge times."
        expected_suggestion_long_charge = "• Probability of long charge issue: 70.48%\n• Suggestion: Check the battery and charging system for issues."
        self.assertIn(expected_diagnosis_fail_start, self.engine.diagnoses)
        self.assertIn(expected_suggestion_fail_start, self.engine.diagnoses[expected_diagnosis_fail_start])
        self.assertIn(expected_diagnosis_long_charge, self.engine.diagnoses)
        self.assertIn(expected_suggestion_long_charge, self.engine.diagnoses[expected_diagnosis_long_charge])

    def test_multiple_diagnoses(self):
        self.engine.reset()
        self.engine.declare(Symptom(fail_start=True))
        self.engine.declare(Symptom(motor_noises=True))
        self.engine.run()
        expected_diagnosis_fail_start = "• Diagnosis: Battery issue causing failure to start."
        expected_suggestion_fail_start = "• Probability of battery issue: 92.27%\n• Suggestion: Check the battery connections and charge or replace the battery if necessary."
        expected_diagnosis_motor_noises = "• Diagnosis: Motor noises indicating potential motor issues."
        expected_suggestion_motor_noises = "• Probability of motor noises issue: 93.84%\n• Suggestion: Inspect the motor for loose components or damage and perform a diagnostic test."
        self.assertIn(expected_diagnosis_fail_start, self.engine.diagnoses)
        self.assertIn(expected_suggestion_fail_start, self.engine.diagnoses[expected_diagnosis_fail_start])
        self.assertIn(expected_diagnosis_motor_noises, self.engine.diagnoses)
        self.assertIn(expected_suggestion_motor_noises, self.engine.diagnoses[expected_diagnosis_motor_noises])

if __name__ == '__main__':
    unittest.main()