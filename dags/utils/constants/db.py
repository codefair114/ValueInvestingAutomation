import os

class INVESTING_DB:
    PG_DB_NAME = os.getenv("PG_DB_NAME")
    PG_DB_USER = os.getenv("PG_DB_USER")
    PG_DB_PASS = os.getenv("PG_DB_PASS")
    PG_DB_HOST = os.getenv("PG_DB_HOST")
    PG_DB_PORT = 10511