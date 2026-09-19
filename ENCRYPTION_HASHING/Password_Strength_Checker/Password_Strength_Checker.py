import string
from pathlib import Path


def strength_checker(password):
    score = 0
    categories = 0

    password_file = Path(__file__).with_name("common_passwords.txt")
    with password_file.open("r", encoding="utf-8") as file:
        common_passwords = file.read().splitlines()

    if password in common_passwords:
        print("This password is too common. Your strength is 0. Try again!")
        return 0

    if any(char.isupper() for char in password):
        score += 1
        categories += 1
    if any(char.islower() for char in password):
        score += 1
        categories += 1
    if any(char in string.punctuation for char in password):
        score += 1
        categories += 1
    if any(char.isdigit() for char in password):
        score += 1
        categories += 1

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    if score <= 2:
        feedback = "Weak"
    elif score <= 4:
        feedback = "Medium"
    elif score <= 5:
        feedback = "Strong"
    else:
        feedback = "Very strong"

    print(f"{feedback}! Your score is {score}.")
    return score


if __name__ == "__main__":
    password = input("Enter your password: ")
    strength_checker(password)