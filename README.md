# Python Random Password Generator

This project is a simple password generator built using Python. It creates strong, random passwords that include a combination of uppercase and lowercase letters, digits, and special characters. This tool can be used for generating secure passwords for applications, improving security practices in password management.

## Features
- **Random Password Generation:** Generates a random password using letters, digits, and special characters.
- **Customizable Length:** The length of the password can be specified, with a default length of 14 characters.
- **Security Focused:** Helps users create strong, non-predictable passwords suitable for securing accounts and applications.

## How It Works
1. **Character Set:**
   - The password is created using a mix of uppercase letters, lowercase letters, digits, and punctuation characters from the `string` module.

2. **Random Selection:**
   - Python’s `random.choice()` function is used to randomly select characters from the defined character set.

3. **Password Length:**
   - The function can generate passwords of any specified length, with a default of 14 characters to ensure strong security.

## Requirements
- Python 3.x

## Usage
1. Clone the repository or download the `password_generator.py` file.
2. Run the script using Python:
   ```bash
   python password_generator.py

