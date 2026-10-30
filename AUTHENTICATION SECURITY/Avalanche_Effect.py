import hashlib

message1 = input("Enter the original message: ")
message2 = input("Enter a slightly modified message: ")

hash1 = hashlib.md5(message1.encode()).hexdigest()
hash2 = hashlib.md5(message2.encode()).hexdigest()

print("MD5 of original: ", hash1)
print("MD5 of modified: ", hash2)

if hash1 == hash2:
    print("Hashes match!")
else:
    print("Hashes do not match!")