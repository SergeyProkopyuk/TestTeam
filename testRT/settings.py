import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv("valid_email")
valid_password = os.getenv("valid_password")
valid_password_confirmation = os.getenv("valid_password_confirmation")
valid_firstName = os.getenv("valid_firstName")
valid_lastName = os.getenv("valid_lastName")
valid_login = os.getenv("valid_login")

