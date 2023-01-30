from os import environ

from dotenv import load_dotenv

# Load .env variables (then put into settings.py)
load_dotenv()


SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
