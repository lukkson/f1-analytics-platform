from pyspark.sql import Row

from f1_analytics_platform.config.http_config import HttpClientConfig
from f1_analytics_platform.extraction.client.lap_time_client import LapTimeClient
from f1_analytics_platform.extraction.http_client import HttpClient

config = HttpClientConfig()
http_client = HttpClient(config)

lap_client = LapTimeClient(http_client)
laps = lap_client.get_laps(2024, 1)

rows = []
for lap_time in laps:
    for lap in lap_time.laps:
        for timing in lap.timings:
            rows.append(
                Row(
                    season=lap_time.season,
                    round=lap_time.round,
                    lap_number=lap.number,
                    driver_id=timing.driver_id,
                    position=timing.position,
                    time=timing.time,
                )
            )

spark.createDataFrame(rows).write.format("delta").mode("overwrite").saveAsTable(
    "f1.lap_times"
)
print("Saved lap_times to Delta Lake!")
