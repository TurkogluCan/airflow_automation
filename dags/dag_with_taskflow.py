from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'by_ect',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id='dag_with_taskflow',
    description='my first dag with taskflow',
    start_date=datetime(2026,2,9),
    schedule='@once',
    default_args=default_args
    )
def dag_with_taskflow():

    @task
    def get_age():
        return 27
    
    @task
    def get_name():
        return 'CAN TURKOGLU'   

    @task
    def greet(name, age):
        print(f'hello {name}, i am {age} years old')

    name = get_name()
    age = get_age()
    greet(name, age)
    
my_dag = dag_with_taskflow()