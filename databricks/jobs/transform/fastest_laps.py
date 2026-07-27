from pyspark.sql import functions as F

df_laps = spark.table("f1.lap_times")

df_fastest = (
    df_laps.withColumn(
        "lap_ms",
        (F.split(F.col("time"), ":")[0].cast("int") * 60000)
        + (F.split(F.col("time"), ":")[1].cast("float") * 1000),
    )
    .groupBy("driver_id")
    .agg(F.min("lap_ms").alias("fastest_lap_ms"))
    .orderBy("fastest_lap_ms")
)

df_fastest.write.format("delta").mode("overwrite").saveAsTable("f1.fastest_laps")
print("Saved fastest_laps to Delta Lake!")
