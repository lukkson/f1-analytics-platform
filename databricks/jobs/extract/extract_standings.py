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
from f1_analytics_platform.extraction.client.standing_client import StandingsClient

config = HttpClientConfig()
http_client = HttpClient(config)

standings_client = StandingsClient(http_client)

rows = []
for round_num in range(1, 25):
    standings = standings_client.get_standings(2024, round_num)
    for standing in standings:
        for ds in standing.driver_standings:
            for constructor in ds.constructor:
                rows.append(
                    Row(
                        season=standing.season,
                        round=standing.round,
                        driver_id=ds.driver.driver_id,
                        position=ds.position,
                        points=ds.points,
                        wins=ds.wins,
                        constructor_id=constructor.constructor_id,
                    )
                )
    print(f"Fetched standings for round {round_num}")

spark.createDataFrame(rows).write.format("delta").mode("overwrite").saveAsTable(
    "f1.driver_standings"
)
print("Saved driver_standings to Delta Lake!")
