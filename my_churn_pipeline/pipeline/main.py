import os
from datetime import datetime, timedelta
from extract import get_db_engine, fetch_chunk
from process import process_chunks
from utils import log, sleep

STATE_FILE = '../../last_processed_date.txt'


def get_last_processed_date():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            date_str = f.read().strip()
            try:
                return datetime.strptime(date_str, '%Y-%m-%d')
            except Exception as e:
                log(f"Error parsing date from state file: {e}")
    # Earliest signup date fallback
    return datetime(2024, 7, 1)

def save_last_processed_date(date):
    with open(STATE_FILE, 'w') as f:
        f.write(date.strftime('%Y-%m-%d'))

def add_months(source_date, months):
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, [31,
        29 if year%4==0 and (year%100!=0 or year%400==0) else 28,
        31,30,31,30,31,31,30,31,30,31][month-1])
    return datetime(year, month, day)

def run_pipeline():
    engine = get_db_engine()

    start_date = get_last_processed_date()
    # Stop 3 months after start_date
    end_date = add_months(start_date, 3)
    current_date = start_date

    while current_date < end_date:
        next_date = add_months(current_date, 1)

        # Adjust lookback windows as needed
        usage_window = current_date - timedelta(days=6)  # 7-day window
        support_window = current_date - timedelta(days=2)  # 3-day window

        chunks = {
            'customers': fetch_chunk(engine, 'customers', 'signup_date', current_date, next_date),
            'usage_events': fetch_chunk(engine, 'usage_events', 'timestamp', usage_window, next_date),
            'subscriptions': fetch_chunk(engine, 'subscriptions', 'start_date', current_date, next_date),
            'support_tickets': fetch_chunk(engine, 'support_tickets', 'open_date', support_window, next_date),
            'marketing_events': fetch_chunk(engine, 'marketing_events', 'event_date', current_date, next_date),
            'churn_labels': fetch_chunk(engine, 'churn_labels', 'churn_date', current_date, next_date),
            'time_dim': fetch_chunk(engine, 'time_dim', 'date', current_date, next_date),
        }

        log(f"Processing chunk for {current_date.date()} to {next_date.date()}")
        process_chunks(chunks, current_date)

        save_last_processed_date(current_date)
        current_date = next_date

        sleep(2)  # adjust or remove

if __name__ == "__main__":
    run_pipeline()
