import hmac
import hashlib

def load_key(filename):
    with open(filename, "rb") as file:
        return file.read()

def create_hmac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()

def verify_hmac(key, message, mac):
    computed_mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_mac, mac)

key = load_key("key.bin")
message = input("Enter message: ").encode()

mac = create_hmac(key, message)
print("Generated HMAC:", mac)

user_mac = input("Enter MAC to verify: ")

if verify_hmac(key, message, user_mac):
    print("HMAC verified successfully!")
else:
    print("HMAC verification failed!")