from datetime import timedelta, datetime
from airflow import DAG
from random import randint

#Operators
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago

#pick best loan
def best_loan(ti):
    predictions = ti.xcom_pull(task_ids=[
        'loan_A',
        'loan_B',
        'loan_C'
    ])
    best_prediction = max(predictions)
    if best_prediction > 8:
        return 'good'
    return 'bad'

def predict():
    return randint(1, 10)



with DAG(
    'loan_review',
    start_date=days_ago(1),
    schedule_interval=timedelta(days=1),
) as dag:
    
    loan_A = PythonOperator(
        task_id='loan_A',
        python_callable=predict
    )

    loan_B = PythonOperator(
        task_id='loan_B',
        python_callable=predict
    )

    loan_C = PythonOperator(
        task_id='loan_C',
        python_callable=predict
    )

    choose_best_loan = BranchPythonOperator(
        task_id='choose_best_loan',
        python_callable=best_loan
    )

    good = BashOperator(
        task_id='good',
        bash_command='echo "good"',
    )

    bad = BashOperator(
        task_id='bad',
        bash_command='echo "bad"',
    )

[loan_A, loan_B, loan_C] >> choose_best_loan >> [good, bad]