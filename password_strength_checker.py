

import re
import argparse
import math

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123", "password123",
    "admin", "letmein", "welcome", "monkey", "1234567890", "iloveyou",
    "princess", "rockyou", "1234567", "12345678", "password1", "123123",
    "football", "baseball", "welcome1", "admin123", "qwerty123"
]

def calculate_entropy(password):
    """Calculate the entropy of the password."""
    if not password:
        return 0
    char_set_size = 0
    if re.search(r'[a-z]', password):
        char_set_size += 26
    if re.search(r'[A-Z]', password):
        char_set_size += 26
    if re.search(r'[0-9]', password):
        char_set_size += 10
    if re.search(r'[^A-Za-z0-9]', password):
        char_set_size += 32  # Approximate for special chars
    if char_set_size == 0:
        return 0
    entropy = len(password) * math.log2(char_set_size)
    return entropy

def check_password_strength(password):
    feedback = []
    strength_points = 0

    # Handle edge cases
    if not password:
        return "Weak", ["Password cannot be empty."]

    if len(password) > 128:
        feedback.append("Password is too long. Consider shortening it for better usability.")

    # Check for common passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Password is a common password. Choose a more unique one.")
        strength_points -= 2  # Penalize heavily

    # Check length (weighted)
    if len(password) >= 12:
        strength_points += 2
    elif len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase letters
    if re.search(r'[A-Z]', password):
        strength_points += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r'[a-z]', password):
        strength_points += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check digits
    if re.search(r'[0-9]', password):
        strength_points += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check special characters
    if re.search(r'[^A-Za-z0-9]', password):
        strength_points += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Bonus for entropy
    entropy = calculate_entropy(password)
    if entropy > 50:
        strength_points += 1
    elif entropy < 20:
        feedback.append("Password has low entropy. Use a mix of characters.")

    # Determine strength
    if strength_points >= 7:
        strength = "Strong"
    elif 4 <= strength_points < 7:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    parser = argparse.ArgumentParser(description="Check password strength.")
    parser.add_argument("--password", type=str, help="Password to check")
    args = parser.parse_args()

    if args.password:
        password = args.password
    else:
        password = input("Enter a password to check its strength: ")

    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
