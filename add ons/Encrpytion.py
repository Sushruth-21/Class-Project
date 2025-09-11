import random
import string
import json
import os

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Check if key file exists
if os.path.exists("cipher_key.json"):
    with open("cipher_key.json", "r") as f:
        key = json.load(f)
else:
    key = chars.copy()
    random.shuffle(key)
    with open("cipher_key.json", "w") as f:
        json.dump(key, f)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original text: {plain_text}")
print(f"Cipher text: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Cipher text: {cipher_text}")
print(f"Original text: {plain_text}")