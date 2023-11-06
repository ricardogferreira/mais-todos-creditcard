from cryptography.fernet import Fernet

from src.settings import CRYPTOGRAPHY_KEY

fernet = Fernet(CRYPTOGRAPHY_KEY.encode())


def encrypt(message):
    token_encrypted = fernet.encrypt(message.encode())
    return token_encrypted.decode()


def decrypt(message_encrypted):
    message = fernet.decrypt(message_encrypted)
    return message.decode()
