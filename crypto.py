### Thanks to Abdou Rockikz guide on Python Code "How to Encrypt and Decrypt Files in Python"
from cryptography.fernet import Fernet
import os.path


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


def encrypt(filename):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    key = load_key()
    f = Fernet(key)

    # read all file data
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    key = load_key()
    f = Fernet(key)
    # read the encrypted data
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def key_check():
    """
    Check if key.key exists, else write_key
    """
    if os.path.isfile('key.key'):
        return
    else:
        write_key()
