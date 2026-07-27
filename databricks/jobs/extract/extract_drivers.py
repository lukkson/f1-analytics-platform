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
from f1_analytics_platform.extraction.client.driver_client import DriverClient

config = HttpClientConfig()
http_client = HttpClient(config)

driver_client = DriverClient(http_client)
drivers = driver_client.get_drivers(2024)
print(f"Fetched {len(drivers)} drivers")

rows = [
    Row(
        driver_id=d.driver_id,
        permanent_number=d.permanent_number,
        code=d.code,
        given_name=d.given_name,
        family_name=d.family_name,
        date_of_birth=d.date_of_birth,
        nationality=d.nationality,
    )
    for d in drivers
]

spark.createDataFrame(rows).write.format("delta").mode("overwrite").saveAsTable(
    "f1.drivers"
)
print("Saved drivers to Delta Lake!")
