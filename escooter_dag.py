import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd

default_args = {
    'owner':'mike',
    'start_date': dt.datetime(2022, 4, 19),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5)
}

