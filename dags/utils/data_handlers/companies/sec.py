import pandas as pd
import requests
import psycopg2

from utils.constants.urls import URLS
from utils.constants.db import INVESTING_DB
from utils.constants.queries import QUERIES


class SEC:

    @staticmethod
    def save_listed_companies_to_db():
        try:
            response = requests.get(URLS.SEC_JSON_URL, headers=URLS.SEC_HEADER)
            response.raise_for_status()
            companies = response.json()

            conn = psycopg2.connect(
                dbname=INVESTING_DB.PG_DB_NAME,
                user=INVESTING_DB.PG_DB_USER,
                password=INVESTING_DB.PG_DB_PASS,
                host=INVESTING_DB.PG_DB_HOST,
                port=INVESTING_DB.PG_DB_PORT
            )
            cur = conn.cursor()

            for key, value in companies.items():
                cur.execute(QUERIES.INSERT_SEC_DATA, (value['cik_str'], value['ticker'], value['title']))
            conn.commit()
            conn.close()
            return "Companies data fetched and saved successfully!"
        except Exception as e:
            return f"Error fetching or saving companies data: {str(e)}"

    @staticmethod
    def clear_listed_companies():
        try:
            conn = psycopg2.connect(
                dbname=INVESTING_DB.PG_DB_NAME,
                user=INVESTING_DB.PG_DB_USER,
                password=INVESTING_DB.PG_DB_PASS,
                host=INVESTING_DB.PG_DB_HOST,
                port=INVESTING_DB.PG_DB_PORT
            )
            cur = conn.cursor()

            for _ in companies:
                cur.execute(QUERIES.DELETE_SEC_DATA)
            conn.commit()
            conn.close()
            return "Companies data fetched and saved successfully!"
        except Exception as e:
            return f"Error fetching or saving companies data: {str(e)}"
