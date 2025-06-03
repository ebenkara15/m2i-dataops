# TP DBT / DuckDB

## Consignes

1. Checkout la branche `feat/tp-dbt`.
2. Se placer dans le répertoire `jaffle_shop_duckdb`
3. Vérifier l’installation avec: `poetry run dbt debug`.
4. Initialiser la base de données: `poetry run dbt seed`.
   *Que constituent les seeds dans notre exemple par rapport à un cas réel ?*
5. Lancer le pipeline de transformation: `poetry run dbt run`
   Pour visualiser la base de données: `poetry run duckdb \-ui`.
   Puis importer le fichier de base de données **jaffle\_shop.duckdb**.
5. (bis) Comment DBT gère
6. Visualiser les schémas de transformations: `poetry run dbt docs generate && poetry run dbt docs serve.`
7. Étudier les fichiers SQL en partant des sources (dossiers `seeds`) jusqu’aux models finaux (`orders.sql` et `customers.sql`).
   *Que dire de l’interprétabilité et l’utilisabilité des différents models ?*
   *Est-ce judicieux de lancer toutes les transformations d’un seul coup ?*
8. Quelles sont les tables sources susceptibles de grossir exponentiellement ?
   Que se passe-t-il alors: 10Go, 100Go, 1 To, 100 To ? Comment résoudre le problème ?
9. Décrire finalement le pipeline idéal ? Comment le faire avec DBT ?
10. Proposer les requêtes SQL correspondant à votre solution. Quels sont les potentiels problèmes rencontrés ?
