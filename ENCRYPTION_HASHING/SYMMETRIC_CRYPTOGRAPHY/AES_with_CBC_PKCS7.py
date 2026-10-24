from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16) #128-bit key
iv = get_random_bytes(16)# initialisation vector
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = b"Hello, AES CBC!"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Ciphertext: ", ciphertext.hex())

decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted: ", decrypted.decode())