import os
from datetime import datetime

class AIRFLOW:
    ADMIN_USER = os.getenv("AIRFLOW_ADMIN_USER")
    ADMIN_PASS = os.getenv("AIRFLOW_ADMIN_PASS")
    DEFAULT_ARGS = {
        'owner': 'airflow',
        'start_date': datetime(2024, 2, 24),
        'retries': 1,
    }
    NUM_CHUNKS = 1