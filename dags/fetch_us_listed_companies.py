import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.dates import days_ago
from utils.constants.email import EMAIL
from utils.data_handlers.companies.sec import SEC

def fetch_and_save_companies():
    SEC.save_listed_companies_to_db()

with DAG(
    'fetch_company_data',
    default_args=EMAIL.DEFAULT_ARGS,
    description='Fetch and save companies data from SEC website',
    schedule_interval='@monthly',
    start_date=days_ago(1),
    tags=['fetch_data'],
) as dag:

    fetch_and_save_task = PythonOperator(
        task_id='fetch_and_save_companies',
        python_callable=fetch_and_save_companies,
    )

    send_email_success = EmailOperator(
        task_id='send_email_success',
        to=EMAIL.ADMIN_EMAIL,
        subject=EMAIL.SUBJECT_SEC_FETCH_SUCCESS,
        html_content=EMAIL.BODY_SEC_FETCH_SUCCESS,
    )

    send_email_failure = EmailOperator(
        task_id='send_email_failure',
        to=EMAIL.ADMIN_EMAIL,
        subject=EMAIL.SUBJECT_SEC_FETCH_FAIL,
        html_content=EMAIL.BODY_SEC_FETCH_SUCCESS,
        trigger_rule='one_failed',
    )

    fetch_and_save_task >> [send_email_success, send_email_failure]
