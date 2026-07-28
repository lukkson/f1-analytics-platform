from pyspark.sql import Row

from f1_analytics_platform.config.http_config import HttpClientConfig
from f1_analytics_platform.extraction.client.driver_client import DriverClient
from f1_analytics_platform.extraction.http_client import HttpClient

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
