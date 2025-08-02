import pyodbc

server   = 'host.docker.internal,1433'  # Instead of 'localhost,1433'
     
database = 'Operations_Retention'
username = 'docker_user'
password = 'root'                        # simple for testing

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "TrustServerCertificate=yes;"
    "Connection Timeout=5;"
    "Encrypt=no;"
)

print("Host → Attempting to connect...")

try:
    conn = pyodbc.connect(conn_str)
    print("Host → Connection succeeded!")
    conn.close()
except Exception as e:
    print("Host → Connection failed:")
    print(e)
