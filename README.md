# Data Automation Pipeline

A lightweight ETL (Extract, Transform, Load) script built in Python to automate data synchronization between REST APIs and a structured SQL database.

## Features
- **Data Extraction**: Fetches JSON data from remote API endpoints.
- **Data Transformation**: Utilizes Pandas for schema mapping, string normalization, and data cleaning.
- **Automated Storage**: Synchronizes processed data into a local SQLite instance.
- **Efficiency**: Designed for scheduled execution via cron jobs or task schedulers.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
