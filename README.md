# Password Strength Checker

A simple Python script to check the strength of a password based on various criteria.

## Features

- Checks password length (minimum 8 characters)
- Verifies presence of uppercase and lowercase letters
- Ensures inclusion of digits and special characters
- Provides feedback on how to improve weak passwords
- Categorizes password strength as Weak, Medium, or Strong

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/password_strength.git
   cd password_strength
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script interactively:

```bash
python password_strength_checker.py
```

Or check a specific password:

```bash
python password_strength_checker.py --password "YourPassword123!"
```

## Examples

```bash
$ python password_strength_checker.py
Enter a password to check its strength: weak
Password Strength: Weak
Feedback:
- Password should be at least 8 characters long.
- Password should include at least one uppercase letter.
- Password should include at least one number.
- Password should include at least one special character.

$ python password_strength_checker.py --password "StrongPass123!"
Password Strength: Strong
```

## Testing

Run the unit tests:

```bash
python -m pytest tests.py
```

## License

This project is licensed under the MIT License.
