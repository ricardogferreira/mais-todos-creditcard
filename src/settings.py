import os

from dotenv import load_dotenv

load_dotenv(".envfile")

POSTGRES_CONNECTION_URL = os.getenv("POSTGRES_CONNECTION_URL")

CRYPTOGRAPHY_KEY = os.getenv("CRYPTOGRAPHY_KEY")
