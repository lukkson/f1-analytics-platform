
  
    
    

    create  table
      "f1"."main"."fastest_pit_stops__dbt_tmp"
  
    as (
      WITH pit_stop_data as (
    SELECT driver_id, lap, duration, season, round
    FROM "f1"."main"."pit_stops"
),  race_data as
    (
    SELECT season, round, race_name, circuit_name
    FROM "f1"."main"."races"
)

SELECT MIN(pit_stop_data.duration) as fasetest_pit_stop, pit_stop_data.driver_id, race_data.circuit_name from pit_stop_data join race_data on pit_stop_data.season = race_data.season and pit_stop_data.round = race_data.round
GROUP BY race_data.circuit_name, pit_stop_data.driver_id

    );
  
  