# dags/example.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'example_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
) as dag:
    task = BashOperator(
        task_id='hello',
        bash_command='echo "Hello World"'
    )
