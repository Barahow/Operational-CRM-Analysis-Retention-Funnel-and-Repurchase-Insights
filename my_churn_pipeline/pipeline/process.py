import os

def process_chunks(chunks, current_date):
    """
    chunks: dict of {table_name: dataframe}
    current_date: datetime of the chunk being processed
    """

    print("\n📦 Processing chunk for date:", current_date.date())

    os.makedirs("output", exist_ok=True)

    for table_name, df in chunks.items():
        if df.empty:
            print(f"   {table_name}: 0 rows (skipped)")
            continue

        print(f"  {table_name}: {len(df)} rows")

        # Save each chunk to CSV
        date_str = current_date.strftime('%Y-%m-%d')
        table_dir = os.path.join("output", table_name)
        os.makedirs(table_dir, exist_ok=True)

        output_path = os.path.join(table_dir, f"{table_name}_{date_str}.csv")
        df.to_csv(output_path, index=False)

    return chunks
