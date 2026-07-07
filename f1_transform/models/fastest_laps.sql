SELECT
    driver_id,
    MIN((CAST(SPLIT_PART(time, ':', 1) AS INTEGER) * 60000) +
        (CAST(SPLIT_PART(time, ':', 2) AS FLOAT) * 1000)) AS fastest_lap_ms
FROM {{ source('f1', 'lap_times') }}
GROUP BY driver_id