# F1 Analytics Platform

End-to-end data engineering portfolio project built around Formula 1 data. The platform extracts race data from a public API, loads it into a database, and transforms it into analytical models.

## Architecture

```
Jolpica F1 API → Extract (Python) → Load (DuckDB) → Transform (dbt)
```

## Tech Stack

- **Python** — data extraction, API clients, Pydantic models
- **DuckDB** — local analytical database
- **dbt** — SQL transformations and data models
- **PySpark + Databricks** — cloud platform with Delta Lake (in progress)

## Project Structure

```
src/f1_analytics_platform/
├── config/         # configuration (env-based)
├── decorators/     # reusable decorators (error handling)
├── exceptions/     # custom exception hierarchy
├── extraction/     # API clients and mappers
│   ├── clients/    # one client per resource
│   └── mappers/    # JSON → Pydantic model
├── loading/        # DuckDB database layer
└── models/         # Pydantic data models
f1_transform/
└── models/         # dbt SQL transformations
```

## Data Sources

All data comes from the [Jolpica F1 API](https://api.jolpi.ca) (no API key required):

- Races
- Drivers
- Driver standings (per round)
- Lap times
- Pit stops

## dbt Models

| Model | Description |
|---|---|
| `fastest_laps` | Fastest lap per driver (with ms conversion) |
| `driver_position_changes` | Position changes across rounds using `LAG()` |
| `fastest_pit_stops` | Fastest pit stop per circuit using CTE + JOIN |

## Running Locally

```bash
# Install dependencies
poetry install

# Set environment
cp .env.example .env.prod
# Fill in values in .env.prod

# Run pipeline
ENV=prod poetry run python test_run.py

# Run dbt transformations
cd f1_transform
poetry run dbt run
```

## Environment Variables

```
F1_BASE_URL=https://api.jolpi.ca/ergast/f1
F1_TIMEOUT=10
F1_MAX_RETRIES=3
F1_BACKOFF_FACTOR=1
F1_DUCK_DB_PATH=data/f1.duckdb
```