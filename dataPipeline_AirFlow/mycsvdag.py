import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from airflow.utils.dates import days_ago

def CSVToJson():
    df=pd.read_csv('/usr/local/airflow/dags/data.csv')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.JSON',orient='records')

default_args = {
    'owner': 'nitin',
    'start_date': dt.datetime(2020, 3, 18),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}
with DAG('MyCSVDAG',
        default_args=default_args,
        schedule_interval=timedelta(minutes=5),
        # '0 * * * *',
        ) as dag:
    print_starting = BashOperator(task_id='starting',
                                  bash_command='echo "I am reading the CSV now....."')

    CSVJson = PythonOperator(task_id='convertCSVtoJson',
                             python_callable=CSVToJson)
print_starting >>CSVJson