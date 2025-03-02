"""Reader of secrets from .env file."""

from os import getenv

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

AUTH_KEY = getenv("AUTHORIZATION_KEY")
