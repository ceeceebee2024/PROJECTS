from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
plaintext = b"Hello, AES GCM!"

cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

nonce = cipher.nonce

print("Ciphertext: ", ciphertext.hex())
print("Nonce: ", nonce.hex())
print("Authentication Tag: ", tag.hex())


decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

try:
    decrypted = decipher.decrypt_and_verify(ciphertext, tag)
    print("Decrypted: ", decrypted.decode())
    print("Authentication successful!")
except ValueError:
    print("Authentication failed!")