# F1 Analytics Platform

End-to-end data engineering portfolio project built around Formula 1 data. The platform extracts race data from a public API, loads it into a database, and transforms it into analytical models — both locally and on Databricks.

## Architecture

**Local:**
```
Jolpica F1 API → Extract (Python) → Load (DuckDB) → Transform (dbt)
```

**Cloud (Databricks):**
```
Jolpica F1 API → Extract (Python) → Load (Delta Lake) → Transform (PySpark)
```

## Tech Stack

- **Python** — data extraction, API clients, Pydantic models
- **DuckDB** — local analytical database
- **dbt** — SQL transformations and data models
- **PySpark** — large-scale data processing
- **Delta Lake** — cloud data storage on Databricks
- **Databricks** — cloud platform with automated workflow scheduling
- **Streamlit** — interactive analytics dashboard

## Databricks

The full pipeline runs on Databricks with Delta Lake as the storage layer and PySpark for transformations. A scheduled Databricks Workflow runs the pipeline automatically every night.

👉 [View Databricks Notebook](https://dbc-97897a73-b66b.cloud.databricks.com/editor/notebooks/636926413060967?o=7474654766055251)

**Delta Lake tables:**

| Table | Description |
|---|---|
| `f1.races` | All races in the 2024 season |
| `f1.drivers` | Driver details |
| `f1.driver_standings` | Standings after each round |
| `f1.lap_times` | Lap times per driver |
| `f1.pit_stops` | Pit stop data |
| `f1.fastest_laps` | Fastest lap per driver (PySpark transform) |
| `f1.driver_position_changes` | Position changes across rounds (window functions) |
| `f1.fastest_pit_stops` | Fastest pit stop per circuit (JOIN transform) |

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

# Run dashboard
poetry run streamlit run streamlit_app.py
```

## Environment Variables

```
F1_BASE_URL=https://api.jolpi.ca/ergast/f1
F1_TIMEOUT=10
F1_MAX_RETRIES=3
F1_BACKOFF_FACTOR=1
F1_DUCK_DB_PATH=data/f1.duckdb
```
