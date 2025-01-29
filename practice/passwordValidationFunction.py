def strength(password):
    # Initialize conditions
    length = 1 if len(password) >= 8 else 0
    upper = 0
    digit = 0

    # Upper case and number check
    for char in password:
        if char.isupper():
            upper = 1
        if char.isdigit():
            digit = 1

    if length == 1 and upper == 1 and digit == 1:
        return "Strong Password"
    else:
        return "Weak Password"

# Test case
get_password = strength("Password123")
print(get_password)  # Output: Strong Password

get_password = strength("weakpass")
print(get_password)  # Output: Weak Password
