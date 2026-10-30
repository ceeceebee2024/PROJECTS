import hashlib
import hmac

def generate_mac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()

def verify_mac(key, message, given_mac):
    computed_mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_mac, given_mac)

key = input("Enter secret key: ").encode()
message = input("Enter message: ").encode()

mac_value = generate_mac(key, message)
print("Generated MAC:", mac_value)

user_mac = input("Enter MAC to verify: ")

if verify_mac(key, message, user_mac):
    print("MAC verified successfully!")
else:
    print("MAC verification failed!")