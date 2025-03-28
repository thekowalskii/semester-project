import os

from dotenv import load_dotenv


load_dotenv(override=True)


# DATABASEs DATA

PG_CONFIG: str = 'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}'.format(
    PG_USER=os.getenv('PG_USER'),
    PG_PASSWORD=os.getenv('PG_PASSWORD'),
    PG_HOST=os.getenv('PG_HOST'),
    PG_NAME=os.getenv('PG_NAME'),
    PG_PORT=os.getenv('PG_PORT')
)

REDIS_CONFIG = {
    'user': os.getenv('REDIS_USER'),
    'password': os.getenv('REDIS_PASSWORD'),
    'host': os.getenv('REDIS_HOST'),
    'port': os.getenv('REDIS_PORT')
}

# JWT TOKEN DATA

TOKEN_ALG = os.getenv('JWT_ALG')
TOKEN_TYPE = os.getenv('JWT_TYPE')
TOKEN_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# ADMIN DATA

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

# SESSION DATA

SESSION_MIDDLEWARE_SECRET_KEY = os.getenv('SESSION_MIDDLEWARE_SECRET_KEY')

# API KEY

API_KEY = os.getenv('API_KEY')
