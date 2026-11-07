
# ==========================================
# TASK 4: SIMPLE LOGIN SYSTEM
# SAM AI Technologies - Cyber Security Internship
# ==========================================

import json
import os
import hashlib
import secrets
import hmac
import getpass

# File to store registered users
USER_FILE = "users.json"

# Password hashing configuration
ITERATIONS = 200_000


def load_users(file_path=USER_FILE):
    """Load registered users from JSON file."""

    if not os.path.exists(file_path):
        return {}

    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return {}


def save_users(users, file_path=USER_FILE):
    """Save user information into JSON file."""

    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password, salt=None):
    """Hash password using PBKDF2 with a random salt."""

    if salt is None:
        salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        ITERATIONS
    )

    return salt, password_hash.hex()


def register_user(username, password, file_path=USER_FILE):
    """Register a new user."""

    username = username.strip()

    if not username:
        return False, "Username cannot be empty."

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    users = load_users(file_path)

    if username in users:
        return False, "Username already exists."

    salt, password_hash = hash_password(password)

    users[username] = {
        "salt": salt,
        "password_hash": password_hash
    }

    save_users(users, file_path)

    return True, "Registration successful!"


def login_user(username, password, file_path=USER_FILE):
    """Authenticate an existing user."""

    users = load_users(file_path)

    username = username.strip()

    if username not in users:
        return False, "Invalid username or password."

    stored_salt = users[username]["salt"]
    stored_hash = users[username]["password_hash"]

    _, entered_hash = hash_password(password, stored_salt)

    # Compare hashes securely
    if hmac.compare_digest(stored_hash, entered_hash):
        return True, "Login successful! Welcome, " + username

    return False, "Invalid username or password."


def main():

    print("\n========================================")
    print("          SIMPLE LOGIN SYSTEM")
    print("========================================")

    while True:

        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            print("\n========== USER REGISTRATION ==========")

            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")

            success, message = register_user(username, password)

            print("\n" + message)

        elif choice == "2":

            print("\n============= USER LOGIN =============")

            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")

            success, message = login_user(username, password)

            print("\n" + message)

        elif choice == "3":

            print("\nThank you for using the Login System!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2 or 3.")


# Program execution starts here
if __name__ == "__main__":
    main()
