def caesar_cipher(text,shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char)- ord('A') + shift) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char

    return encrypted_text

print(caesar_cipher("Hello world", 3))

def caesar_decrypt(text, shift):
    return caesar_cipher(text, -shift)

print(caesar_decrypt("Khoor zruog", 3))