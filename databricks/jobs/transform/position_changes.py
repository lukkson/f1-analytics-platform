from pyspark.sql import functions as F
from pyspark.sql.window import Window

df_standings = spark.table("f1.driver_standings")

window = Window.partitionBy("driver_id").orderBy("round")

df_position_changes = df_standings.withColumn(
    "previous_position", F.lag("position").over(window)
).withColumn("position_change", F.lag("position").over(window) - F.col("position"))

df_position_changes.write.format("delta").mode("overwrite").saveAsTable(
    "f1.driver_position_changes"
)
print("Saved driver_position_changes to Delta Lake!")
