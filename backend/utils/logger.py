import logging


app_log = logging.getLogger(name=' Application ')
pg_log = logging.getLogger(name=' PostgreSQL ')
redis_log = logging.getLogger(name=' Redis ')

logging.basicConfig(level=logging.INFO)
