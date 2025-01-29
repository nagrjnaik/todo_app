from os.path import isdir

password = input("Enter a password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

number = False
for digit in password:
    if digit.isdigit():
        number = True
result["number"] = number

upper = False
for character in password:
    if character.isupper():
        upper = True
result["upper"] = upper

print(result)
if all(result):
    print("Strong Password")
else:
    print("Weak password")
