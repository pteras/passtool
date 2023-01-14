import re
import pyperclip


def check_password_strength(password):
    strength = {'Length': 0, 'Lowercase': 0,
                'Uppercase': 0, 'Digits': 0, 'Special': 0}
    strength['Length'] = len(password)

    if re.search("[a-z]", password):
        strength['Lowercase'] = 1
    if re.search("[A-Z]", password):
        strength['Uppercase'] = 1
    if re.search("[0-9]", password):
        strength['Digits'] = 1
    if re.search("[!@#$%^&*()_+-=\[\]{};':\"\\|,.<>/?]", password):
        strength['Special'] = 1

    rating = 0
    if strength['Length'] >= 8:
        rating += 1
    if strength['Lowercase'] == 1:
        rating += 1
    if strength['Uppercase'] == 1:
        rating += 1
    if strength['Digits'] == 1:
        rating += 1
    if strength['Special'] == 1:
        rating += 1

    if rating < 3:
        return "Weak"
    elif rating < 4:
        return "Moderate"
    else:
        return "Strong"


def generate_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password



password = input("Enter a password: ")
print("Password strength:", check_password_strength(password))


def passgen():
    length = int(input("Enter the desired password length: "))
    generated_password = generate_password(length)
    print("Generated password:", generated_password)
    print("Password strength:", check_password_strength(generated_password))
    copy = input("Do you want to copy the password to the clipboard? (y/n): ")
    if copy == 'y':
      pyperclip.copy(generated_password)
      print("Password copied to clipboard.")
    new_pass = input("Do you want to generate another password? (y/n): ")
    if new_pass == 'y':
        passgen()
    elif new_pass == 'n':
        print("Goodbye.")


user_choice = input("Do you want to generate a strong password? (y/n): ")
if user_choice == 'y':
  passgen()
elif user_choice == 'n':
    print("Goodbye.")
