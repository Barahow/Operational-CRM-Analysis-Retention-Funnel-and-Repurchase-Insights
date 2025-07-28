import pandas as pd
from sqlalchemy import create_engine
from datetime import timedelta, datetime

def get_db_engine():
    connection_url = (
    "mssql+pyodbc://docker_user:root@host.docker.internal:1433/CustomerChurnPrediction"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&TrustServerCertificate=yes"
    "&Encrypt=no"
)

    engine = create_engine(connection_url)
    return engine




def fetch_chunk(engine, table, date_col, start, end):
    query = f"""
        SELECT * FROM {table}
        WHERE {date_col} >= '{start}' AND {date_col} < '{end}'
    """
    df = pd.read_sql(query, engine)
    return df

# ────────────────────────────────────────────────
# MAIN ENTRY POINT
# ────────────────────────────────────────────────
if __name__ == "__main__":
    print("Connecting to database...")
    engine = get_db_engine()
    print("Connected.")

    # Example: get usage_events in 1-month chunks
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 2, 1)

    print(f"Fetching data from {start_date} to {end_date}...")
    df = fetch_chunk(engine, "usage_events", "timestamp", start_date, end_date)

    print(f"Fetched {len(df)} rows.")
    print(df.head())  # Show sample data
