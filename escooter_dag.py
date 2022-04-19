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
    df['started_at'] = pd.to_datetime(df['started_at'], format= '%m/%d/%y %H:%M')   # Cast generic object to dt object
    df.to_csv(r'/Users/mike/Desktop/Main/Programming/Projects/Tutorials/dataeng/CleaningData/escooter/clean_scooter.csv')

