from Crypto.Random import get_random_bytes
import binascii
import base64

key = get_random_bytes(16)
print("Hexadecimal: ", binascii.hexlify(key).decode())
print("Base64: ", base64.b64encode(key).decode())