
# ==========================================
# TASK 5: BASIC TEXT FILE ENCRYPTION USING XOR
# SAM AI Technologies - Cyber Security Internship
# ==========================================

from pathlib import Path
import hashlib
import getpass


def xor_data(data, key):
    """
    Encrypt or decrypt data using XOR.
    The same function performs both operations.
    """

    if not key:
        raise ValueError("Encryption key cannot be empty.")

    key_bytes = key.encode("utf-8")

    result = bytearray()

    for index, byte in enumerate(data):
        key_byte = key_bytes[index % len(key_bytes)]
        result.append(byte ^ key_byte)

    return bytes(result)


def encrypt_file(input_file, key, output_file):
    """Read a file, encrypt its content and save it."""

    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.is_file():
        raise FileNotFoundError("Input file does not exist.")

    if input_path.resolve() == output_path.resolve():
        raise ValueError("Input and output files must be different.")

    original_data = input_path.read_bytes()

    encrypted_data = xor_data(original_data, key)

    output_path.write_bytes(encrypted_data)

    return encrypted_data


def decrypt_file(input_file, key, output_file):
    """Read an encrypted file, decrypt it and save it."""

    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.is_file():
        raise FileNotFoundError("Encrypted file does not exist.")

    if input_path.resolve() == output_path.resolve():
        raise ValueError("Input and output files must be different.")

    encrypted_data = input_path.read_bytes()

    decrypted_data = xor_data(encrypted_data, key)

    output_path.write_bytes(decrypted_data)

    return decrypted_data


def calculate_hash(data):
    """Calculate SHA-256 hash for verification."""

    return hashlib.sha256(data).hexdigest()


def main():

    print("\n========================================")
    print("       XOR FILE ENCRYPTION TOOL")
    print("========================================")

    try:
        input_file = input("\nEnter input text file path: ").strip()

        key = getpass.getpass("Enter encryption key: ")

        if not key:
            raise ValueError("Encryption key cannot be empty.")

        encrypted_file = "encrypted.enc"
        decrypted_file = "decrypted.txt"

        # Read original content
        original_data = Path(input_file).read_bytes()

        print("\nEncrypting file...")

        # Encrypt original file
        encrypt_file(input_file, key, encrypted_file)

        print("Encryption successful!")
        print("Encrypted file:", encrypted_file)

        print("\nDecrypting file...")

        # Decrypt encrypted file
        decrypted_data = decrypt_file(
            encrypted_file,
            key,
            decrypted_file
        )

        print("Decryption successful!")
        print("Decrypted file:", decrypted_file)

        # Verify original and decrypted content
        original_hash = calculate_hash(original_data)
        decrypted_hash = calculate_hash(decrypted_data)

        print("\n========== VERIFICATION ==========")

        if original_hash == decrypted_hash:
            print("File Integrity: VERIFIED")
            print("Original and decrypted contents match.")
        else:
            print("File Integrity: FAILED")
            print("Original and decrypted contents do not match.")

        print("==================================")

    except (ValueError, OSError) as error:
        print("\nError:", error)


# Program execution starts here
if __name__ == "__main__":
    main()
