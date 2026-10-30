import os
import secrets

def generate_key(length=16): # generate random key
    return secrets.token_hex(length)

def store_key(filename, key): #store key in file
    with open(filename, "w") as file:
        file.write(key)


def load_key(filename): # read key form file 
    with open(filename, "r") as file:
        return file.read()

key = generate_key()

store_key("key.bin", key)
loaded_key = load_key("key.bin")

print("Generated key: ", key)
print("Loaded key: ", loaded_key)