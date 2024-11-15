from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 're',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['steve-re@hotmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def square(x):
    return x**2

with DAG(
    'python_square_operator',
    description='Squaring a number using Airflow',
    default_args=default_args,
    schedule_interval='0 12 * * *',
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id='square_task',
        python_callable=square,
        op_args=[13],
        dag=dag,
    )
