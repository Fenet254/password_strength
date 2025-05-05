import re

def check_password_strength(password):
    feedback = []
    strength_points = 0

    # Check length
    if len(password) >= 8:
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

    # Determine strength
    if strength_points == 5:
        strength = "Strong"
    elif 3 <= strength_points < 5:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
