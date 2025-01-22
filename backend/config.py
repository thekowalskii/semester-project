import os

from dotenv import load_dotenv


load_dotenv(override=True)

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

