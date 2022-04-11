import json
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd

def csv_to_json():
    df = pd.read_csv('data.json', 'r')
    for i, r in pd.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.json', orient='records')

default_args = {
    'owner': 'mike',
    'start_date': dt.datetime(2022, 4, 11),
    'retires': 1,
    'retry_delay': dt.timedelta(minutes=5)
}

with DAG('my_csv_DAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5)) as dag:

    # Define your tasks:

    print_starting = BashOperator(task_id='starting', bash_command = 'echo "I am reading the csv now...."')
    csv_json = PythonOperator(task_id='convert_csv_to_json', python_callable=csv_to_json)

    #different ways to describe connections between the tasks:

    # print_starting.set_downstream(csv_json)
    # csv_json.set_upstream(print_starting)
    print_starting >> csv_json    # indicates downstream
    # csv_json << print_starting    # indicates upstream
