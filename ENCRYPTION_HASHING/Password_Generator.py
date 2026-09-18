import random
import string

def generate_pwd(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers: # if numbers have been requested, add them to the character pool
        characters += digits
    if special_chars:
        characters += special # if special characters have been requested, add them to the character pool

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length: # adds a character to the password until it meets criteria or length
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

# request user input for password criteria

min_length = int(input("Enter the minimum length of your password: "))
has_number = str(input("Would you like to use numbers: \t (y/n)?" )).lower() == "y"
has_special = str(input("Would you like to use special characters: \t (y/n)?" )).lower() == "y"

# prints the generated password

pwd = generate_pwd(min_length, has_number, has_special)
print(f"Here is your generated password: {pwd}")


