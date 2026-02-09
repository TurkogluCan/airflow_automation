from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


"""
Retrieves the first_name and last_name from XComs using the TaskInstance (ti) object
and prints a greeting message along with the age provided via op_kwargs.

:param age: Age of the person (passed via op_kwargs)
:param ti: TaskInstance object (automatically passed by Airflow)
"""
def print_hello(age, ti):
    first_name = ti.xcom_pull(task_ids='task_write_xcom', key='first_name')
    last_name = ti.xcom_pull(task_ids='task_write_xcom', key='last_name')
    print(f'hello name is {first_name} {last_name}, and i am {age} years old')


"""
Pushes first_name and last_name into XComs using the TaskInstance (ti) object.
These values can be retrieved by downstream tasks.

:param ti: TaskInstance object (automatically passed by Airflow)
"""
def set_xcom_value(ti):
    ti.xcom_push(key='first_name', value='CAN')
    ti.xcom_push(key='last_name', value='TURKOGLU')
    

with DAG(
    dag_id='python_callback',
    description='my first python callback dag',
    start_date=datetime(2026,2,9),
    schedule='@daily',
    default_args={
        'owner':'by_ect',
        'retries':1,
        'retry_delay':timedelta(minutes=5)
    }
)as dag:
    task_get_xcom = PythonOperator(
        task_id='task_get_xcom',
        python_callable=print_hello,
        op_kwargs={'age':27},
    )
    task_write_xcom = PythonOperator(
        task_id='task_write_xcom',
        python_callable=set_xcom_value
    )


task_write_xcom >> task_get_xcom

    