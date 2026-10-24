from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad

key = b'ThisIsA16ByteKey' # fixed 16-byte key
cipher = AES.new(key,AES.MODE_ECB)
plaintext = b"Hello, AES ECB!"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Ciphertext: ", ciphertext.hex())

decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decyrpted: ", decrypted.decode())