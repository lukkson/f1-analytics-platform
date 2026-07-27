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
from f1_analytics_platform.extraction.client.race_client import RaceClient

config = HttpClientConfig()
http_client = HttpClient(config)

race_client = RaceClient(http_client)
races = race_client.get_races(2024)
print(f"Fetched {len(races)} races")

rows = [
    Row(
        season=r.season,
        round=r.round,
        race_name=r.race_name,
        circuit_id=r.circuit.circuit_id,
        circuit_name=r.circuit.circuit_name,
        country=r.circuit.location.country,
        date=r.date,
    )
    for r in races
]

spark.sql("CREATE DATABASE IF NOT EXISTS f1")
spark.createDataFrame(rows).write.format("delta").mode("overwrite").saveAsTable(
    "f1.races"
)
print("Saved races to Delta Lake!")
