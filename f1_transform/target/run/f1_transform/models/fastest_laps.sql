
  
    
    

    create  table
      "f1"."main"."fastest_laps__dbt_tmp"
  
    as (
      SELECT
    driver_id,
    MIN((CAST(SPLIT_PART(time, ':', 1) AS INTEGER) * 60000) +
        (CAST(SPLIT_PART(time, ':', 2) AS FLOAT) * 1000)) AS fastest_lap_ms
FROM "f1"."main"."lap_times"
GROUP BY driver_id
    );
  
  