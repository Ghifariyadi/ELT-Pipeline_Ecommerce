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
	'gcs_to_bq',
	default_args = default_args,
	description='',
	schedule_interval='0 0 * * *',
	start_date=datetime(2024, 10, 12),
	catchup=False,
)

# Define task: GCS to BQ

product = GCSToBigQueryOperator(
	task_id='product',
	bucket='ghif_portfolio',
	gcp_conn_id='google_cloud_default',
	source_objects = ['sales_data - product.csv'],
	source_format="CSV",
   	create_disposition="CREATE_IF_NEEDED",
   	write_disposition="WRITE_TRUNCATE",
	destination_project_dataset_table='golden-centaur-440309-a9.raw.product',
	dag=dag
)

transactions = GCSToBigQueryOperator(
        task_id='transactions',
        bucket='ghif_portfolio',
        gcp_conn_id='google_cloud_default',
        source_objects = ['sales_data - product.csv'],
        source_format="CSV",
        create_disposition="CREATE_IF_NEEDED",
        write_disposition="WRITE_TRUNCATE",
        destination_project_dataset_table='golden-centaur-440309-a9.raw.product',
        dag=dag
)

user = GCSToBigQueryOperator(
        task_id='user',
        bucket='ghif_portfolio',
        gcp_conn_id='google_cloud_default',
        source_objects = ['sales_data - product.csv'],
        source_format="CSV",
        create_disposition="CREATE_IF_NEEDED",
        write_disposition="WRITE_TRUNCATE",
        destination_project_dataset_table='golden-centaur-440309-a9.raw.product',
        dag=dag
)

events = GCSToBigQueryOperator(
        task_id='events',
        bucket='ghif_portfolio',
        gcp_conn_id='google_cloud_default',
        source_objects = ['sales_data - product.csv'],
        source_format="CSV",
        create_disposition="CREATE_IF_NEEDED",
        write_disposition="WRITE_TRUNCATE",
        destination_project_dataset_table='golden-centaur-440309-a9.raw.product',
        dag=dag
)

# Run dbt models using BashOperator
#dbt_run = BashOperator(
#        task_id='dbt_run',
#        bash_command="cd /home/ghifariyadi_muhammad/my_dbt_project && dbt run",
#    )

# BashOperator untuk Conversion Funnel
dbt_run_conversion_funnel = BashOperator(
        task_id='dbt_run_conversion_funnel',
        bash_command="cd /home/ghifariyadi_muhammad/my_dbt_project && dbt run --select conversion_funnel"
)

# BashOperator untuk Voucher Effectiveness
dbt_run_voucher_effectiveness = BashOperator(
        task_id='dbt_run_voucher_effectiveness',
        bash_command="cd /home/ghifariyadi_muhammad/my_dbt_project && dbt run --select voucher_effectiveness"
    )

product >> transactions >> user >> events >> dbt_run_conversion_funnel >> dbt_run_voucher_effectiveness 
