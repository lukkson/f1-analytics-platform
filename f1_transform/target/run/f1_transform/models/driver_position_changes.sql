
  
    
    

    create  table
      "f1"."main"."driver_position_changes__dbt_tmp"
  
    as (
      SELECT driver_id, round, position,
LAG(position) OVER (PARTITION BY driver_id  ORDER BY round) as previous_position,
LAG(position) OVER (PARTITION BY driver_id ORDER BY round) - position AS position_change
FROM "f1"."main"."driver_standings"
    );
  
  