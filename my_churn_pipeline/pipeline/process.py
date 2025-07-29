import os
import pandas as pd

def process_chunks(chunks, current_date):
    print(f"\nProcessing chunk for date: {current_date.date()}")

    os.makedirs("output", exist_ok=True)

    sort_col_map = {
        'customers': 'signup_date',
        'usage_events': 'timestamp',
        'subscriptions': 'start_date',
        'support_tickets': 'open_date',
        'marketing_events': 'event_date',
        'churn_labels': 'churn_date',
        'time_dim': 'date',
    }

    for table_name, df in chunks.items():
        if df.empty:
            print(f"   {table_name}: 0 rows (skipped)")
            continue

        print(f"  {table_name}: {len(df)} rows")

        output_path = os.path.join("output", f"{table_name}.csv")
        date_col = sort_col_map[table_name]

        # Ensure the new chunk's date column is datetime64[ns]
        df[date_col] = pd.to_datetime(df[date_col])

        if os.path.exists(output_path):
            existing_df = pd.read_csv(output_path, parse_dates=[date_col])
            # Also ensure existing_df's date column is datetime64[ns]
            existing_df[date_col] = pd.to_datetime(existing_df[date_col])

            combined_df = pd.concat([existing_df, df]).drop_duplicates()
            combined_df.sort_values(by=date_col, inplace=True)
        else:
            combined_df = df.sort_values(by=date_col)

        combined_df.to_csv(output_path, index=False)

    return chunks
