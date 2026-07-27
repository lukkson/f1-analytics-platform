from pyspark.sql import functions as F

df_pit_stops = spark.table("f1.pit_stops")
df_races = spark.table("f1.races")

df_fastest_pit_stops = (
    df_pit_stops.join(df_races, on=["season", "round"], how="inner")
    .groupBy("circuit_name", "driver_id")
    .agg(F.min("duration").alias("fastest_pit_stop"))
    .orderBy("fastest_pit_stop")
)

df_fastest_pit_stops.write.format("delta").mode("overwrite").saveAsTable(
    "f1.fastest_pit_stops"
)
print("Saved fastest_pit_stops to Delta Lake!")
