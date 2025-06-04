from datetime import datetime

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

IMAGE_NAME = "europe-docker.pkg.dev/dataops-m2i/dataops-registry/jaffle-shop"


with DAG(
    dag_id="dbt_dag_erwan",
    description="A DAG running DBT tasks.",
    schedule_interval=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:
    check_config = KubernetesPodOperator(
        task_id="debug-config",
        kubernetes_conn_id="kubernetes_default",
        namespace="composer-user-workloads",
        name="debug-config",
        image=IMAGE_NAME,
        env_vars={"DATE_INGEST": "{{ ds }}"},
        arguments=["debug"],
    )

    check_config
