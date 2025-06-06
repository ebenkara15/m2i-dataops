import os

from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable
from pyspark.sql import SparkSession

print("JAVA_HOME =", os.environ.get("JAVA_HOME"))

# Init SparkSession avec support Delta Lake
builder = (
    SparkSession.builder.appName("SimpleDeltaExample")
    .master("local[*]")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Répertoire Delta local
path = "./tmp/delta"

# Nettoyage si relance
if os.path.exists(path):
    import shutil

    shutil.rmtree(path)

# Création de données
# df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
input_path = "data/input.json"
df = spark.read.option("multiline", "true").json(input_path)

# Sauvegarde au format Delta
df.write.format("delta").save(path)

# Lecture
print("Données initiales :")
spark.read.format("delta").load(path).show()

# Données à merger
update_path = "data/update.json"
df_new = spark.read.option("multiline", "true").json(update_path)

# Upsert (merge)
delta_table = DeltaTable.forPath(spark, path)
delta_table.alias("old").merge(
    df_new.alias("new"), "old.id = new.id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()

# Résultat
print("Données après merge :")
spark.read.format("delta").load(path).show()


# Visualiser l'historique
print("Historique de la table: ")
DeltaTable.forPath(spark, path).history().show(truncate=True)

# Visualiser une version antérieur
print("Version initale de la table: ")
spark.read.format("delta").option("versionAsOf", 0).load(path).show()


spark.stop()
