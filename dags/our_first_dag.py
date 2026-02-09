from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


default_args = {
    'owner': 'by_ect',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_V2',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2026, 1, 6, 2),
    schedule='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is a task1"
    )
    
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hello world, this is a task2"
    )
       
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hello world, this is a task3"
    )
    
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)
    task1 >> [task2, task3]
    
    
    ###
    # TASK2 is the downstream of TASK1. TASK2 doesn't start before execute the TASK1
    #task1.set_downstream(task2)
    #task2 << task1
    #task2 >> task1
    
    ###
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)
    # is equal to
    # task1 >> task2
    # task1 >> task3
    # or
    # task1 >> [task2,task3]
    
    ###
    #task1.set_downstream(task2)
    #task2.set_downstream(task3)
    # is equal to
    # task1 >> task2
    # task2 >> task3
    # or
    # task1 >> task2 >> task3