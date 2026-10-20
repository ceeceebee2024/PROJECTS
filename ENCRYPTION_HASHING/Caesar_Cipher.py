def caesar_cipher(text,shift):
    encrypted_text = "" #start with empty
    for char in text:
        if char.isalpha(): #check if upper
            if char.islower(): #check if lower
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char)- ord('A') + shift) % 26 + ord('A'))
            encrypted_text += new_char # add shift to result
        else:
            encrypted_text += char # leave non-alph chars unchanged

    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_cipher(text, -shift)
#main interface
print("=" * 10 + "WELCOME TO CAESAR CIPHER" + "=" * 10)
while True:
    choice = int(input("Would you like to 1.Encrypt, 2.Decrypt, 3.Exit"))
    if choice == 3:
        print("Goodbye!")
        break
    if choice not in (1,2):
        print("Please choose 1,2 or 3")
        continue

    message = input("Enter the message: ")
    shift_value = int(input("Enter the shift value (positive or negative): "))
    if choice == 1:
        result = caesar_cipher(message, shift_value)
        print("Encrypted Message:", result)
    else:
        result = caesar_decrypt(message, shift_value)
        print("Decrypted Message:", result)