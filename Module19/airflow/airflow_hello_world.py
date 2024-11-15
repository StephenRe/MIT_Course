#DAG object
from datetime import timedelta, datetime
from airflow import DAG


#Operators
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

#sample function
def getNum():
    return 5

#args passed to each operator
with DAG(
    'abel',
    start_date=days_ago(2),
    schedule_interval=timedelta(days=1),
) as dag:

    #sample tasks
    t1 = BashOperator(
        task_id='task_one',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='task_two',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t3 = PythonOperator(
        task_id='task_three',
        depends_on_past=False,
        python_callable=getNum,
    )

    t1 >> [t2, t3]



