def encrypt_file(input_file, output_file,key):
    from Crypto.Cipher import AES 
    from Crypto.Util.Padding import pad
    from Crypto.Random import get_random_bytes

    iv = get_random_bytes(16)
    cipher = AES.new(key,AES.MODE_CBC, iv)

    with open(input_file, 'rb') as f:
        plaintext = f.read

    ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))

    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

def decrypt_file(input_file,outputfile,key):
    from Crypto.Cipher import AES 
    from Crypto.Util.Padding import unpad

    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(outputfile,'wb') as f:
        f.write(plaintext)
