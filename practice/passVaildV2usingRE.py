import re


def is_strong_password(password: str) -> bool:
    """
    Check if the given password is strong.

    A strong password should have:
    - At least 8 characters
    - At least one uppercase letter
    - At least one digit

    :param password: The password string to validate
    :return: True if the password is strong, False otherwise
    """
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):  # Check for at least one uppercase letter
        return False

    if not re.search(r"\d", password):  # Check for at least one digit
        return False

    return True


def main():
    """
    Main function to test the password strength checker.
    """
    password = input("Enter your password: ").strip()

    if is_strong_password(password):
        print("✅ Strong Password")
    else:
        print("❌ Weak Password")


if __name__ == "__main__":
    main()
