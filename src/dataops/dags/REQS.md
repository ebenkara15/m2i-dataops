# TP Airflow


## Consignes

1. Analyser le DAG fourni. Explorer l'interface Airflow. Explorer l'interface Composer.
  *Comment sont construisent les dépendances entre tâches ?*
  *Où se trouvent les DAGs ?*
  *Où est déployé Airflow ?*
2. Renommer la fonction principale de `users.py` par `users_pipeline_<nom>.py`. Déployer votre DAG en important votre fichier dans le bucket contenant les DAGs sous le répertoire `dags/`.
3. Lancer votre DAG avec un run manuel.
4. Modifier votre DAG pour qu'il soit exécuté automatiquement toutes les 5 minutes par Airflow.
5. Modifier le DAG pour que la tâche `load` écrive véritablement la liste des utilisateurs dans un bucket sous la forme d'un JSON.
6. En imaginant que la tâche `load` prennent les données dans un S3, quel mécanisme d'Airflow permet de s'assurer que les données soient présentes ?
7. Comment déploierait-on un pipeline dans DBT dans Airflow:
    - Quelles tâches ? Avec quelles dépendances ?
    - À quelle fréquence ?
    - Dans le cas d'un refresh incrémental, comment faire pour que les jours où les runs ont échoués soient ratrappés ?
