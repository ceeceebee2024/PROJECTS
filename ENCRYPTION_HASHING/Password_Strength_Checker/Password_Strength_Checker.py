import string

def strength_checker(password):


    password = input("Enter your password: ")

    score = 0
    x = 0

    with open("common_passwords.txt", "r") as file:
        common_passwords = file.read().splitlines()

    if password in common_passwords:
        print("This password is too common. Your strength is 0. Try again!")
        return
    
    if any(char.isupper() for char in password):
        score += 1
        x += 1
    if any(char.islower() for char in password):
        score += 1
        x += 1
    if any(char in string.punctuation for char in password):
        score += 1
        x += 1
    if any(char.isdigit() for char in password):
        score += 1
        x += 1
    if x < 4:
        return score

    if len(password) <= 8:
        score += 1
    elif len(password) <= 12:
        score += 1
    elif len(password) <= 16:
        score += 1
        return score

    
    if score <= 2:
        print("Weak")
    elif score <= 4:
        print("Medium!")
    elif score <= 5:
        print("Strong!")
    else:
        print("Very strong!")
    return score

while True:
    password = input("Enter your password: ")
    strength_checker(password)