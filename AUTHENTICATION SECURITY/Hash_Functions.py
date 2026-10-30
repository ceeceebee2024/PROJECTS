import hashlib

message = input("Enter a messgae: ")

message_bytes = message.encode()


# compute sha 256 hash
hash_object = hashlib.sha256(message_bytes)
hash_value = hash_object.hexdigest()

print("Generated SHA-256: ", hash_value)

expected_hash = input("Enter expected hash: ")

# Compare generated hash with expected hash

if hash_value.lower() == expected_hash.strip().lower():
    print("Hash values match!")
else:
    print("Hash values do not match!")