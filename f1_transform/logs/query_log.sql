-- created_at: 2026-06-09T11:19:00.085031500+00:00
-- finished_at: 2026-06-09T11:19:00.085981800+00:00
-- elapsed: 950us
-- outcome: success
-- dialect: duckdb
-- node_id: not available
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "connection_name": "", "dbt_version": "2.0.0", "profile_name": "f1_transform", "target_name": "dev"} */

    
    select schema_name
    from system.information_schema.schemata
    
    where lower(catalog_name) = '"f1"'
    
  
  ;
-- created_at: 2026-06-09T11:19:00.086378200+00:00
-- finished_at: 2026-06-09T11:19:00.086757200+00:00
-- elapsed: 379us
-- outcome: success
-- dialect: duckdb
-- node_id: not available
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "connection_name": "", "dbt_version": "2.0.0", "profile_name": "f1_transform", "target_name": "dev"} */

    
        select type from duckdb_databases()
        where lower(database_name)='f1'
        and type='sqlite'
    
  ;
-- created_at: 2026-06-09T11:19:00.086948500+00:00
-- finished_at: 2026-06-09T11:19:00.087138200+00:00
-- elapsed: 189us
-- outcome: success
-- dialect: duckdb
-- node_id: not available
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "connection_name": "", "dbt_version": "2.0.0", "profile_name": "f1_transform", "target_name": "dev"} */

    
    
        create schema if not exists "f1"."main"
    ;
-- created_at: 2026-06-09T11:19:00.093485900+00:00
-- finished_at: 2026-06-09T11:19:00.095518800+00:00
-- elapsed: 2ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_laps
-- query_id: not available
-- desc: get_relation > list_relations call
SELECT table_catalog, table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema = 'main';
-- created_at: 2026-06-09T11:19:00.093474200+00:00
-- finished_at: 2026-06-09T11:19:00.095518900+00:00
-- elapsed: 2ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_pit_stops
-- query_id: not available
-- desc: get_relation > list_relations call
SELECT table_catalog, table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema = 'main';
-- created_at: 2026-06-09T11:19:00.092854500+00:00
-- finished_at: 2026-06-09T11:19:00.095970100+00:00
-- elapsed: 3ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.driver_position_changes
-- query_id: not available
-- desc: get_relation > list_relations call
SELECT table_catalog, table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema = 'main';
-- created_at: 2026-06-09T11:19:00.098945700+00:00
-- finished_at: 2026-06-09T11:19:00.106041700+00:00
-- elapsed: 7ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_laps
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_laps", "profile_name": "f1_transform", "target_name": "dev"} */

  
    
    

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
  
  ;
-- created_at: 2026-06-09T11:19:00.099415300+00:00
-- finished_at: 2026-06-09T11:19:00.107411+00:00
-- elapsed: 7ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.driver_position_changes
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.driver_position_changes", "profile_name": "f1_transform", "target_name": "dev"} */

  
    
    

    create  table
      "f1"."main"."driver_position_changes__dbt_tmp"
  
    as (
      SELECT driver_id, round, position,
LAG(position) OVER (PARTITION BY driver_id  ORDER BY round) as previous_position,
LAG(position) OVER (PARTITION BY driver_id ORDER BY round) - position AS position_change
FROM "f1"."main"."driver_standings"
    );
  
  ;
-- created_at: 2026-06-09T11:19:00.107005300+00:00
-- finished_at: 2026-06-09T11:19:00.107829400+00:00
-- elapsed: 824us
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_laps
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_laps", "profile_name": "f1_transform", "target_name": "dev"} */

    SELECT index_name
    FROM duckdb_indexes()
    WHERE schema_name = 'main'
      AND table_name = 'fastest_laps'
  ;
-- created_at: 2026-06-09T11:19:00.108139400+00:00
-- finished_at: 2026-06-09T11:19:00.108600600+00:00
-- elapsed: 461us
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.driver_position_changes
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.driver_position_changes", "profile_name": "f1_transform", "target_name": "dev"} */

    SELECT index_name
    FROM duckdb_indexes()
    WHERE schema_name = 'main'
      AND table_name = 'driver_position_changes'
  ;
-- created_at: 2026-06-09T11:19:00.108487900+00:00
-- finished_at: 2026-06-09T11:19:00.109057400+00:00
-- elapsed: 569us
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_laps
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_laps", "profile_name": "f1_transform", "target_name": "dev"} */

    SELECT COUNT(*) as remaining_indexes
    FROM duckdb_indexes()
    WHERE schema_name = 'main'
      AND table_name = 'fastest_laps'
  ;
-- created_at: 2026-06-09T11:19:00.109502600+00:00
-- finished_at: 2026-06-09T11:19:00.110221200+00:00
-- elapsed: 718us
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.driver_position_changes
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.driver_position_changes", "profile_name": "f1_transform", "target_name": "dev"} */

    SELECT COUNT(*) as remaining_indexes
    FROM duckdb_indexes()
    WHERE schema_name = 'main'
      AND table_name = 'driver_position_changes'
  ;
-- created_at: 2026-06-09T11:19:00.111659200+00:00
-- finished_at: 2026-06-09T11:19:00.113108600+00:00
-- elapsed: 1ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_laps
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_laps", "profile_name": "f1_transform", "target_name": "dev"} */

      alter table "f1"."main"."fastest_laps" rename to "fastest_laps__dbt_backup"
    ;
-- created_at: 2026-06-09T11:19:00.099344400+00:00
-- finished_at: 2026-06-09T11:19:00.114288200+00:00
-- elapsed: 14ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_pit_stops
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_pit_stops", "profile_name": "f1_transform", "target_name": "dev"} */

  
    
    

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
  
  ;
-- created_at: 2026-06-09T11:19:00.112308700+00:00
-- finished_at: 2026-06-09T11:19:00.114643900+00:00
-- elapsed: 2ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.driver_position_changes
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.driver_position_changes", "profile_name": "f1_transform", "target_name": "dev"} */

      alter table "f1"."main"."driver_position_changes" rename to "driver_position_changes__dbt_backup"
    ;
-- created_at: 2026-06-09T11:19:00.115006100+00:00
-- finished_at: 2026-06-09T11:19:00.115805100+00:00
-- elapsed: 799us
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_laps
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_laps", "profile_name": "f1_transform", "target_name": "dev"} */

      alter table "f1"."main"."fastest_laps__dbt_tmp" rename to "fastest_laps"
    ;
-- created_at: 2026-06-09T11:19:00.115538200+00:00
-- finished_at: 2026-06-09T11:19:00.116563400+00:00
-- elapsed: 1ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.driver_position_changes
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.driver_position_changes", "profile_name": "f1_transform", "target_name": "dev"} */

      alter table "f1"."main"."driver_position_changes__dbt_tmp" rename to "driver_position_changes"
    ;
-- created_at: 2026-06-09T11:19:00.115381100+00:00
-- finished_at: 2026-06-09T11:19:00.117082700+00:00
-- elapsed: 1ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_pit_stops
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_pit_stops", "profile_name": "f1_transform", "target_name": "dev"} */

      alter table "f1"."main"."fastest_pit_stops__dbt_tmp" rename to "fastest_pit_stops"
    ;
-- created_at: 2026-06-09T11:19:00.117362300+00:00
-- finished_at: 2026-06-09T11:19:00.118537100+00:00
-- elapsed: 1ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_laps
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_laps", "profile_name": "f1_transform", "target_name": "dev"} */

      drop table if exists "f1"."main"."fastest_laps__dbt_backup" cascade
    ;
-- created_at: 2026-06-09T11:19:00.118107900+00:00
-- finished_at: 2026-06-09T11:19:00.119334500+00:00
-- elapsed: 1ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.driver_position_changes
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.driver_position_changes", "profile_name": "f1_transform", "target_name": "dev"} */

      drop table if exists "f1"."main"."driver_position_changes__dbt_backup" cascade
    ;
-- created_at: 2026-06-09T11:19:00.118668800+00:00
-- finished_at: 2026-06-09T11:19:00.119547600+00:00
-- elapsed: 878us
-- outcome: success
-- dialect: duckdb
-- node_id: model.f1_transform.fastest_pit_stops
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.f1_transform.fastest_pit_stops", "profile_name": "f1_transform", "target_name": "dev"} */

      drop table if exists "f1"."main"."fastest_pit_stops__dbt_backup" cascade
    ;
