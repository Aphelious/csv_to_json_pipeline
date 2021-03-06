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

def clean_scooter():
    scooter_csv = r'/Users/mike/Desktop/Main/Programming/Projects/Tutorials/dataeng/CleaningData/escooter/scooter.csv'
    df = pd.read_csv(scooter_csv)   # Read in csv file
    df.drop(columns=['region_id'], inplace=True)    # Drop the region_id column
    df.columns = [x.lower() for x in df.columns]    # Reformat the column names to lowercase
    df['started_at'] = pd.to_datetime(df['started_at'], format= '%m/%d/%Y %H:%M')   # Cast generic object to dt object
    df.to_csv(r'/Users/mike/Desktop/Main/Programming/Projects/Tutorials/dataeng/CleaningData/escooter/clean_scooter.csv')


def filter_data():
    df = pd.read_csv(
        r'/Users/mike/Desktop/Main/Programming/Projects/Tutorials/dataeng/CleaningData/escooter/clean_scooter.csv')
    from_date = '2019-05-23'
    to_date = '2019-06-03'
    to_from_df = df[(df['started_at'] > from_date) & (df['started_at'] < to_date)]
    to_from_df.to_csv(r'/Users/mike/Desktop/Main/Programming/Projects/Tutorials/dataeng/CleaningData/escooter/may23_to_june3.csv')


with DAG('scooter_dag',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5)) as dag:

    cleanData = PythonOperator(task_id='clean', python_callable=clean_scooter)

    selectData = PythonOperator(task_id='filter', python_callable=filter_data)

    copyfile = BashOperator(
        task_id='copy',
        bash_command='cp /Users/mike/Desktop/Main/Programming/Projects/Tutorials/dataeng/CleaningData/escooter/may23_to_june3.csv /Users/mike/Desktop')

    cleanData >> selectData >> copyfile
