from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from airflow.utils.dates import days_ago
import os 
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG object
dag = DAG(
    'gcs_to_bq',  # DAG name can be kept if not sensitive
    default_args=default_args,
    description='',
    schedule_interval='0 0 * * *',
    start_date=datetime(2024, 10, 12),
    catchup=False,
)

# Define task: GCS to BQ
product = GCSToBigQueryOperator(
    task_id='product',
    bucket='your_bucket_name',  # Censored
    gcp_conn_id='google_cloud_default',
    source_objects=['your_file_name.csv'],  # Censored
    source_format="CSV",
    create_disposition="CREATE_IF_NEEDED",
    write_disposition="WRITE_TRUNCATE",
    destination_project_dataset_table='your_project:your_dataset.product',  # Censored
    dag=dag
)

transactions = GCSToBigQueryOperator(
    task_id='transactions',
    bucket='your_bucket_name',
    gcp_conn_id='google_cloud_default',
    source_objects=['your_file_name.csv'],
    source_format="CSV",
    create_disposition="CREATE_IF_NEEDED",
    write_disposition="WRITE_TRUNCATE",
    destination_project_dataset_table='your_project:your_dataset.transactions',
    dag=dag
)

user = GCSToBigQueryOperator(
    task_id='user',
    bucket='your_bucket_name',
    gcp_conn_id='google_cloud_default',
    source_objects=['your_file_name.csv'],
    source_format="CSV",
    create_disposition="CREATE_IF_NEEDED",
    write_disposition="WRITE_TRUNCATE",
    destination_project_dataset_table='your_project:your_dataset.user',
    dag=dag
)

events = GCSToBigQueryOperator(
    task_id='events',
    bucket='your_bucket_name',
    gcp_conn_id='google_cloud_default',
    source_objects=['your_file_name.csv'],
    source_format="CSV",
    create_disposition="CREATE_IF_NEEDED",
    write_disposition="WRITE_TRUNCATE",
    destination_project_dataset_table='your_project:your_dataset.events',
    dag=dag
)

dbt_run_conversion_funnel = BashOperator(
    task_id='dbt_run_conversion_funnel',
    bash_command="cd /path/to/your_dbt_project && dbt run --select conversion_funnel"  # Censored
)

dbt_run_voucher_effectiveness = BashOperator(
    task_id='dbt_run_voucher_effectiveness',
    bash_command="cd /path/to/your_dbt_project && dbt run --select voucher_effectiveness"
)

product >> transactions >> user >> events >> dbt_run_conversion_funnel >> dbt_run_voucher_effectiveness
