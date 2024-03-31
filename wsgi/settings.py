import dotenv
from flask_wtf import CSRFProtect
import os

dotenv.load_dotenv()
csrf = CSRFProtect()


class Conf:
    SECRET_KEY = os.environ["SECRET_KEY"]
    DATABASE_URI = os.environ["DATABASE_URI"]
    DEBUG = True if os.environ["DEBUG"] == "true" else False
    TESTING = True if os.environ["TESTING"] == "true" else False
