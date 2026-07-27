# F1 Analytics Platform

A personal project I built to learn data engineering by working with something I actually care about — Formula 1. The idea was simple: take real F1 data, build a proper pipeline around it, and deploy it to the cloud.

It ended up covering the full DE stack — from raw API extraction through transformation to a cloud deployment on Databricks with CI/CD.

## What it does

Pulls data from the [Jolpica F1 API](https://api.jolpi.ca) (free, no key needed), processes it through a multi-layer pipeline, and stores the results in Delta Lake on Databricks. A GitHub Actions workflow deploys the pipeline automatically on every push.

## Architecture

**Local:**
```
Jolpica F1 API → Python (extraction) → DuckDB → dbt (SQL transforms)
```

**Cloud:**
```
Jolpica F1 API → Python (extraction) → Delta Lake → PySpark (transforms) → Databricks Workflow
```

## Stack

- **Python** — API clients with Pydantic v2 models, custom DI container, decorator-based error handling
- **DuckDB** — local analytical database for development
- **dbt** — SQL-based transformations with window functions and CTEs
- **PySpark** — distributed transformations on Databricks
- **Delta Lake** — cloud storage layer on Databricks
- **Databricks Asset Bundles (DAB)** — infrastructure as code for Databricks jobs
- **GitHub Actions** — CI/CD pipeline that deploys to Databricks on push


## Databricks

The cloud pipeline runs as a Databricks Workflow with 8 tasks — 5 extract jobs and 3 transform jobs, with proper `depends_on` chaining. Everything is defined in `databricks.yml` and deployed via DAB.

👉 [View Databricks Notebook](https://dbc-97897a73-b66b.cloud.databricks.com/editor/notebooks/636926413060967?o=7474654766055251)

## CI/CD

On every push to `main`, GitHub Actions:
1. Installs the Databricks CLI
2. Runs `databricks bundle deploy` to update the Databricks job definition

The job itself runs on a schedule (nightly at 2:00 AM Warsaw time).

## Running locally

```bash
poetry install

# copy and fill in your values
cp .env.example .env.prod

# run the pipeline
ENV=prod poetry run python test_run.py

# run dbt transforms
cd f1_transform
poetry run dbt run
```

## Environment variables

```
F1_BASE_URL=https://api.jolpi.ca/ergast/f1
F1_TIMEOUT=10
F1_MAX_RETRIES=3
F1_BACKOFF_FACTOR=1
F1_DUCK_DB_PATH=data/f1.duckdb
```