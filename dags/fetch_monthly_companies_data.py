from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from utils.models.company_intrinsic_value import CompanyIntrinsicValue
from utils.models.company_profile import CompanyProfile
from utils.data_handlers.companies.pipeline import IntrinsicValueDataPipeline
from utils.constants.airflow import AIRFLOW

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 24),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'intrinsic_value_data_pipeline',
    default_args=default_args,
    description='DAG to fetch tickers and calculate scores',
    schedule_interval=timedelta(days=1),
)

# Task to fetch tickers
def fetch_tickers():
    return IntrinsicValueDataPipeline.fetch_tickers()

fetch_tickers_task = PythonOperator(
    task_id='fetch_tickers',
    python_callable=fetch_tickers,
    dag=dag,
)

# Task to calculate scores for a chunk of tickers
def calculate_scores_for_chunk(**kwargs):
    tickers_chunk = kwargs['tickers_chunk']
    for ticker in tickers_chunk:
        print("Ticker: ", ticker)
        IntrinsicValueDataPipeline.calculate_scores(ticker)

calculate_scores_for_chunk_task = PythonOperator(
    task_id='calculate_scores_for_chunk',
    python_callable=calculate_scores_for_chunk,
    op_kwargs={'tickers_chunk': fetch_tickers()},  # Pass fetched tickers as kwargs
    provide_context=True,  # Allows the function to access context variables
    dag=dag,
)

# Define task dependencies
fetch_tickers_task >> calculate_scores_for_chunk_task