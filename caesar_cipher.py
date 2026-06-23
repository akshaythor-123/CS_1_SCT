
def encrypt_message(text, shift_value):
    encrypted_text = ""

    for character in text:
        if character.isalpha():

            if character.isupper():
                encrypted_text += chr(
                    (ord(character) - ord('A') + shift_value) % 26 + ord('A')
                )

            else:
                encrypted_text += chr(
                    (ord(character) - ord('a') + shift_value) % 26 + ord('a')
                )

        else:
            encrypted_text += character

    return encrypted_text


def decrypt_message(text, shift_value):
    decrypted_text = ""

    for character in text:
        if character.isalpha():

            if character.isupper():
                decrypted_text += chr(
                    (ord(character) - ord('A') - shift_value) % 26 + ord('A')
                )

            else:
                decrypted_text += chr(
                    (ord(character) - ord('a') - shift_value) % 26 + ord('a')
                )

        else:
            decrypted_text += character

    return decrypted_text


print("===== Caesar Cipher Program =====")

user_message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

encrypted_result = encrypt_message(user_message, shift_value)
decrypted_result = decrypt_message(encrypted_result, shift_value)

print("\n----- Results -----")
print("Encrypted Message :", encrypted_result)
print("Decrypted Message :", decrypted_result)
