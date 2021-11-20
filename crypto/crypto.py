# pip install cryptography

from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

from getpass import getpass

backend = default_backend()

def pad(key, length=16):
    n = len(key)
    if n == 16:
        return key
    else:
        num_of_chars = length - n
        return  key + ('0' * num_of_chars)

def aes_ecb_encrypt(message, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(cipher.algorithm.block_size).padder()
    padded = padder.update(message.encode()) + padder.finalize()
    return b64e(encryptor.update(padded) + encryptor.finalize())

def aes_ecb_decrypt(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(cipher.algorithm.block_size).unpadder()
    padded = decryptor.update(b64d(ciphertext)) + decryptor.finalize()
    return unpadder.update(padded) + unpadder.finalize()

def main():
    menu = '''
1. Encrypt(plaintext, key)
2. Decrypt(ciphertext, key)
3. Show GitHub token(key)
4. Exit
    '''

    print(menu)

    choice = int(input("\nEnter your choice: "))

    if choice == 4:
        exit(0)

    # print("Enter password: ", end="")
    key = getpass()
    key = pad(key).encode()

    if choice == 1:
        message = input("Enter message to be encrypted: ")

        cipher = aes_ecb_encrypt(message, key)

        print(f"Encrypted string: {cipher}\n")

    elif choice == 2:
        message = input("Enter message to be decrypted: ").encode()

        plaintext = aes_ecb_decrypt(message, key)

        print(f"Decrypted string = {plaintext.decode()}\n")

    elif choice == 3:
        enc_token = b'Bz9Q-B-tXhUIdf0dOMl-nAfJF27WLDnoAaw1vN74rgifhYXrsgT5uJXBLld9C38c'

        token = aes_ecb_decrypt(enc_token, key)

        print(f"Your token is:\n{token.decode()}\n")

    else:
        print("Pick a valid option.\n\n")

        exit(1)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")