import os

from dotenv import load_dotenv

ENVFILE = os.getenv("ENVFILE", ".envfile")

load_dotenv(ENVFILE)

POSTGRES_CONNECTION_URL = os.getenv("POSTGRES_CONNECTION_URL")

CRYPTOGRAPHY_KEY = os.getenv("CRYPTOGRAPHY_KEY")
