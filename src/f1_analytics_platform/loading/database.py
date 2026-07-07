import duckdb

from f1_analytics_platform.config.database_config import DatabaseConfig
from f1_analytics_platform.models import (
    Race,
    Driver,
    LapTime,
    DriverStanding,
)
from f1_analytics_platform.models.pit_stop import PitStop


class F1Database:
    def __init__(self):
        self._config = DatabaseConfig()
        self._conn = duckdb.connect(self._config.duck_db_path)
        self._init_tables()

    def _init_tables(self):
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS races (
                season INTEGER,
                round INTEGER,
                race_name STRING,
                date DATE,
                circuit_id VARCHAR,
                circuit_name STRING,
                country STRING,
                PRIMARY KEY (season, round)
            )
        """)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                driver_id VARCHAR,
                permanent_number STRING,
                code STRING,
                given_name STRING,
                family_name STRING,
                date_of_birth DATE,
                nationality STRING,
                PRIMARY KEY (driver_id)
            )
        """)

        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS lap_times (
                driver_id VARCHAR,
                position INTEGER,
                time STRING,
                number STRING,
                season INTEGER,
                round INTEGER,
                PRIMARY KEY (season, round, driver_id, number)
            )
        """)

        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS pit_stops (
                driver_id VARCHAR,
                lap INTEGER,
                stop INTEGER,
                duration STRING,
                season INTEGER,
                round INTEGER,
                race_name STRING,
                PRIMARY KEY (season, round, driver_id, stop)
            )
        """)

        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS driver_standings (
                constructor_id VARCHAR,
                wins INTEGER,
                position INTEGER,
                points FLOAT,
                season INTEGER,
                round INTEGER,
                driver_id VARCHAR, 
                PRIMARY KEY (season, round, driver_id)
            )
        """)

    def insert_races(self, races: list[Race]) -> None:
        self._conn.executemany(
            "INSERT OR REPLACE INTO races VALUES (?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    r.season,
                    r.round,
                    r.race_name,
                    r.date,
                    r.circuit.circuit_id,
                    r.circuit.circuit_name,
                    r.circuit.location.country,
                )
                for r in races
            ],
        )

    def insert_drivers(self, drivers: list[Driver]) -> None:
        self._conn.executemany(
            "INSERT OR REPLACE INTO drivers VALUES (?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    r.driver_id,
                    r.permanent_number,
                    r.code,
                    r.given_name,
                    r.family_name,
                    r.date_of_birth,
                    r.nationality,
                )
                for r in drivers
            ],
        )

    def insert_lap_times(self, lap_times: list[LapTime]) -> None:
        row = []
        for lap_time in lap_times:
            for lap in lap_time.laps:
                for timing in lap.timings:
                    row.append(
                        (
                            timing.driver_id,
                            timing.position,
                            timing.time,
                            lap.number,
                            lap_time.season,
                            lap_time.round,
                        )
                    )
        self._conn.executemany(
            "INSERT OR REPLACE INTO lap_times VALUES (?, ?, ?, ?, ?, ?)", row
        )

    def insert_pit_stops(self, pit_stops: list[PitStop]) -> None:
        row = []
        for pit_stop in pit_stops:
            for pit in pit_stop.pit_stops:
                row.append(
                    (
                        pit.driver_id,
                        pit.lap,
                        pit.stop,
                        pit.duration,
                        pit_stop.season,
                        pit_stop.round,
                        pit_stop.race_name,
                    )
                )
        self._conn.executemany(
            "INSERT OR REPLACE INTO pit_stops VALUES (?, ?, ?, ?, ?, ?, ?)", row
        )

    def insert_standings(self, driver_standings: list[DriverStanding]) -> None:
        row = []
        for pit_stop in driver_standings:
            for driver_standing in pit_stop.driver_standings:
                for constructor in driver_standing.constructor:
                    row.append(
                        (
                            constructor.constructor_id,
                            driver_standing.wins,
                            driver_standing.position,
                            driver_standing.points,
                            pit_stop.season,
                            pit_stop.round,
                            driver_standing.driver.driver_id,
                        )
                    )
        self._conn.executemany(
            "INSERT OR REPLACE INTO driver_standings VALUES (?, ?, ?, ?, ?, ?, ?)", row
        )
