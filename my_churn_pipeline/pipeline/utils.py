print("utils.py loaded")
import os 
def log(message):
    print(f"[LOG] {message}")

def sleep(seconds=2):
    import time
    time.sleep(seconds)
    # utils.py

from datetime import datetime

STATE_FILE = "last_processed_date.txt"

def read_last_processed_date(default_start):
    if not os.path.exists(STATE_FILE):
        return default_start
    with open(STATE_FILE, 'r') as f:
        return datetime.strptime(f.read().strip(), "%Y-%m-%d")

def save_last_processed_date(date):
    with open(STATE_FILE, 'w') as f:
        f.write(date.strftime("%Y-%m-%d"))

