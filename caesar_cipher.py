def encrypt_message(message, shift):
    encrypted_message = ""
    shift = shift % 26

    for char in message:

        if char.isupper():
            encrypted_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A')
            )
            encrypted_message += encrypted_char

        elif char.islower():
            encrypted_char = chr(
                (ord(char) - ord('a') + shift) % 26 + ord('a')
            )
            encrypted_message += encrypted_char

        else:
            encrypted_message += char

    return encrypted_message


def decrypt_message(message, shift):
    return encrypt_message(message, -shift)


def main():

    print("\n========================================")
    print("       CAESAR CIPHER TOOL")
    print("========================================")

    message = input("\nEnter your message: ")

    try:
        shift = int(input("Enter shift value: "))

        encrypted = encrypt_message(message, shift)

        decrypted = decrypt_message(encrypted, shift)

        print("\n========== RESULTS ==========")

        print("Original Message  :", message)
        print("Shift Value       :", shift)
        print("Encrypted Message :", encrypted)
        print("Decrypted Message :", decrypted)

        print("=============================")

    except ValueError:
        print("\nError: Please enter a valid numerical shift value.")

if __name__ == "__main__":
    main()
