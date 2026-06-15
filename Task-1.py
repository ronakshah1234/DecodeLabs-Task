# Password Strength Checker
# Internship Project 1
# Made by Ronak Shah

# Password Strength Checker
# Internship Project 1
# Made by Ronak Shah

import string

print("===== Password Strength Checker =====")

password = input("Enter your password: ")

strength = 0

# checking password length
if len(password) >= 8:
    strength += 1
else:
    print("Password should have at least 8 characters")

# checking uppercase letters
if any(ch.isupper() for ch in password):
    strength += 1
else:
    print("Add at least one uppercase letter")

# checking numbers
if any(ch.isdigit() for ch in password):
    strength += 1
else:
    print("Add at least one number")

# checking special characters
if any(ch in string.punctuation for ch in password):
    strength += 1
else:
    print("Add at least one special symbol")

print("\nPassword Strength Result:")

if strength == 4:
    print("Strong Password")

elif strength >= 2:
    print("Medium Password")

else:
    print("Weak Password")
