import random
import string

def generate_pwd(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True

        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number

        if special_chars:
            meets_criteria = meets_criteria and has_special
    return pwd

min_length = int(input("Enter the minimum length of your password: "))
has_number = str(input("Would you like to use numbers: \t (y/n)?" )).lower() == "y"
has_special = str(input("Would you like to use special characters: \t (y/n)?" )).lower() == "y"

pwd = generate_pwd(min_length, has_number, has_special)
print(f"Here is your generated password: {pwd}")


