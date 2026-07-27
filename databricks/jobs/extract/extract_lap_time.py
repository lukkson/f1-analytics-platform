import sys
import os
from pyspark.sql import Row

sys.path.insert(
    0, "/Workspace/Users/lukasz.dlugosz091@gmail.com/Drafts/f1-analytics-platform/src"
)

os.environ["F1_BASE_URL"] = "https://api.jolpi.ca/ergast/f1"
os.environ["F1_TIMEOUT"] = "10"
os.environ["F1_MAX_RETRIES"] = "3"
os.environ["F1_BACKOFF_FACTOR"] = "1"

from f1_analytics_platform.extraction.http_client import HttpClient
from f1_analytics_platform.config.http_config import HttpClientConfig
from f1_analytics_platform.extraction.client.lap_time_client import LapTimeClient

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
