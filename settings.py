import os
from decouple import Csv, config
from urllib.parse import quote_plus

# Core Settings
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

# MySQL config
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 8889)
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root') 
DB_NAME = os.getenv('DB_NAME', 'test')
DB_POOL_SIZE = config('DB_POOL_SIZE', default=5, cast=int)
DB_MAX_OVERFLOW = config('DB_MAX_OVERFLOW', default=10, cast=int)


# AWS Config
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_REGION = os.getenv('AWS_REGION', '')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME', '')
URL_EXPIRY_TIME = os.getenv('URL_EXPIRY_TIME', 60)

# Logging Configuration
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format":  "[{asctime}] [{process}] [{levelname}] {module}.{funcName}:{lineno} - {message}",
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
    },
}