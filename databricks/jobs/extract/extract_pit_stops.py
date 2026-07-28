from pyspark.sql import Row

from f1_analytics_platform.config.http_config import HttpClientConfig
from f1_analytics_platform.extraction.client.pit_stop_client import PitStopClient
from f1_analytics_platform.extraction.http_client import HttpClient

config = HttpClientConfig()
http_client = HttpClient(config)

pit_stop_client = PitStopClient(http_client)
pit_stops = pit_stop_client.get_pit_stops(2024, 1)

rows = []
for pit_stop in pit_stops:
    for pit in pit_stop.pit_stops:
        rows.append(
            Row(
                season=pit_stop.season,
                round=pit_stop.round,
                race_name=pit_stop.race_name,
                driver_id=pit.driver_id,
                lap=pit.lap,
                stop=pit.stop,
                duration=pit.duration,
            )
        )

spark.createDataFrame(rows).write.format("delta").mode("overwrite").saveAsTable(
    "f1.pit_stops"
)
print("Saved pit_stops to Delta Lake!")
