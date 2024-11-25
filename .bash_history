source ../.venv/bin/activate
source .venv/bin/activate
airflow webserver --port 8080
exit
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate
ls
pip install "apache-airflow[celery]==2.9.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.8.txt"
airflow version
ls
cd airflow/
ls
pwd
export AIRFLOW_HOME=/home/ghifariyadi_muhammad/airflow
airflow db init
ls
nano airflow.cfg
airflow users create --username admin --firstname admin --lastname skills --role Admin --email ghifariyadi.muhammad@gmail.com
airflow users list
airflow scheduler
exit
ls
nano startup.sh
. startup.sh 
cd ..
nano startup.sh 
. startup.sh 
pip install "apache-airflow==2.9.2" apache-airflow-providers-google==10.17.0
ls
mkdir dags
cd dags/
ls
nano first.py
ls
cd ..
ls
nano service-account.json
pwd
exit
ls
. startup.sh 
airflow scheduler
. startup.sh 
airflow webserver --port 8080
. startup.sh 
airflow users create --username admin --firstname admin --lastname skills --role Admin --email ghifariyadi.muhammad@gmail.com
airflow users create --username admin2 --firstname admin --lastname skills --role Admin --email ghifariyadi.muhammad@gmail.com
airflow users create --username admin2 --firstname admin2 --lastname skills --role Admin --email ghiccount@gmail.com
pip list
ls
nano service-account.json 
. startup.sh 
ls
cd dags/
ls
nano first.py 
. startup.sh 
airflow scheduler
airflow webserver --port 8080
ls
cd dags/
ls
nano first.py 
ls
cd dags/
ls
nano first.py 
.star
. startup.sh 
cd ..
ls
cd my_dbt_project/
ls
cd mode
cd models/
ls
cd example/
pwd
ls
rm my_second_dbt_model.sql 
ls
. startup.sh 
ls
cd dags/
ls
nano first.py 
airflow scheduler
ls
cd ..
ls
pip install dbt-core
pip install dbt-bigquery
dbt init my_dbt_project
ls
cd my_dbt_project/
ls
nano dbt_project.yml 
dbt debug
dbt run
ls
cd models/
ls
cd example/
ls
nano my_first_dbt_model.sql 
pip install airflow-dbt-python
ls
nano my_first_dbt_model.sql 
dbt run
cd ..
ls
cd airflow/
airflow webserver --port 8080
. startup.sh 
airflow webserver --port 8080
ls
cd dags/
nano first.py 
airflow webserver --port 8080
pip install dbt-core
cd ..
ls
pwd
ls
cd dags/
ls
nano first.py 
airflow scheduler
nano first.py 
airflow scheduler
pip install apache-airflow-providers-dbt
airflow version
nano first.py 
airflow scheduler
nano first.py 
airflow scheduler
nano first.py 
airflow scheduler
