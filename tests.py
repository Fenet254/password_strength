
import unittest
from password_strength_checker import check_password_strength, calculate_entropy

class TestPasswordStrengthChecker(unittest.TestCase):

    def test_strong_password(self):
        strength, feedback = check_password_strength("StrongPass123!")
        self.assertEqual(strength, "Strong")
        self.assertEqual(feedback, [])


    def test_medium_password(self):
        strength, feedback = check_password_strength("MediumPass123")
        self.assertEqual(strength, "Medium")
        self.assertIn("Password should include at least one special character.", feedback)

    def test_weak_password(self):
        strength, feedback = check_password_strength("weak")
        self.assertEqual(strength, "Weak")
        self.assertGreater(len(feedback), 0)

    def test_empty_password(self):
        strength, feedback = check_password_strength("")
        self.assertEqual(strength, "Weak")
        self.assertIn("Password cannot be empty.", feedback)

    def test_common_password(self):
        strength, feedback = check_password_strength("password")
        self.assertEqual(strength, "Weak")
        self.assertIn("Password is a common password. Choose a more unique one.", feedback)

    def test_long_password(self):
        long_pass = "A" * 130
        strength, feedback = check_password_strength(long_pass)
        self.assertIn("Password is too long. Consider shortening it for better usability.", feedback)

    def test_entropy_calculation(self):
        entropy = calculate_entropy("abc")
        self.assertGreater(entropy, 0)
        entropy_empty = calculate_entropy("")
        self.assertEqual(entropy_empty, 0)

if __name__ == '__main__':
    unittest.main()
