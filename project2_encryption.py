# Basic Encryption and Decryption
# Internship Project 2
# Made by Ronak Shah

def encrypt(text, shift):

    encrypted_text = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):

    decrypted_text = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)

            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted_text += char

    return decrypted_text


print("===== Basic Encryption and Decryption =====")

message = input("Enter text: ")

shift = 3

encrypted = encrypt(message, shift)

decrypted = decrypt(encrypted, shift)

print("\nOriginal Text :", message)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)