#!/usr/bin/env python3
from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
import datetime
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2020, 9, 29, 18, 28, 26, 103156),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
dag = DAG(
    'number_of_emojis',
    default_args=default_args,
    description='who uses the most emojis?',
    schedule_interval=timedelta(days=7),
)

HOME = "/home/geofflangenderfer/work/howToWinFreelanceDeveloperJobs"
t1 = BashOperator(
    task_id='SaveTweets',
    bash_command=f'{HOME}/src/SaveTweets.py',
    dag=dag,
)

t2 = BashOperator(
    task_id='SaveNumberOfEmojis',
    depends_on_past=False,
    bash_command=f'{HOME}/src/SaveNumberOfEmojis.py',
    dag=dag,
)

t3 = BashOperator(
    task_id='log_number_of_emojis',
    bash_command=f"psql -c 'select count(*) from numberofemojis;' 'postgresql://postgres:postgres@localhost:5432/tweets' > {HOME}/logs/$(date -I).txt",
    dag=dag,
)
dag.doc_md = __doc__

t1.doc_md = """\
#### Task Documentation
Check source code
"""

t1 >> t2 >> t3
