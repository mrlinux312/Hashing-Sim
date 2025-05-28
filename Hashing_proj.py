print("Hashing Simulator")

#importing haslib module
import hashlib

#user enters message for hashing
User_mesg = input("Please enter a message you would like to hash: ")

#message converted and encoded
hash_msg = hashlib.sha256(User_mesg.encode())

#message is converted from byte string to hex string
hashout = hash_msg.hexdigest()

#final hashed output
print(f"SHA-256 output: {hashout}")
