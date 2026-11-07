
# ==========================================
# TASK 3: PASSWORD GENERATOR
# SAM AI Technologies - Cyber Security Internship
# ==========================================

import string
import secrets


def generate_password(length):

    # Minimum length should be 4 to include all character types
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    # Define character categories
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(numbers),
        secrets.choice(special)
    ]

    # Combine all character categories
    all_characters = uppercase + lowercase + numbers + special

    # Fill the remaining password length
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Securely shuffle the password characters
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def generate_multiple_passwords(length, count):

    if count < 1:
        raise ValueError("Number of passwords must be at least 1.")

    passwords = []

    for _ in range(count):
        passwords.append(generate_password(length))

    return passwords


def main():

    print("\n========================================")
    print("          PASSWORD GENERATOR")
    print("========================================")

    try:
        # Get password length
        length = int(input("\nEnter password length (minimum 4): "))

        if length < 4:
            print("Error: Password length must be at least 4.")
            return

        # Ask whether multiple passwords are required
        choice = input(
            "Generate multiple passwords? (yes/no): "
        ).strip().lower()

        if choice == "yes":

            count = int(input("How many passwords do you want? "))

            passwords = generate_multiple_passwords(length, count)

            print("\n========== GENERATED PASSWORDS ==========")

            for index, password in enumerate(passwords, start=1):
                print(f"Password {index}: {password}")

        elif choice == "no":

            password = generate_password(length)

            print("\n========== GENERATED PASSWORD ==========")
            print("Your Password:", password)

        else:
            print("Please enter either yes or no.")

        print("\n========================================")

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()
