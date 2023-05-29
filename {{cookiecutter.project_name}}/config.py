import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    APP = os.environ.get("APP")
    APP_ENV = os.environ.get("APP_ENV")

    # authentication related configuration
    AUTH_DOMAIN = os.environ.get("AUTH_DOMAIN")
    CLIENT_ID = os.environ.get("CLIENT_ID")
    API_TOKEN = os.environ.get("API_TOKEN")
    USER_IDENTIFIER = os.environ.get("USER_IDENTIFIER")
    CACHE_PREFIX = os.environ.get("CACHE_PREFIX")

    # DB Credentials
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    DB_DRIVER = os.environ.get("DB_DRIVER")

    SQLALCHEMY_DATABASE_URI = (f"{DB_DRIVER}:"
                               f"//{DB_USERNAME}:{DB_PASSWORD}"
                               f"@{DB_HOST}:"
                               f"{DB_PORT}/{DB_NAME}")

    REDIS_URL = os.environ.get("REDIS_URL")
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")

    CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/1"
    CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/2"
    REDIS_CACHE_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
    MAIL_USE_SSL = True if os.environ.get("MAIL_USE_SSL") == "True" else False
    MAIL_USE_TLS = True if os.environ.get("MAIL_USE_TLS") == "True" else False


class DevConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    pass

