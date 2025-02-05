import pyodbc

# Define the connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your_server_name;"
    "DATABASE=your_database_name;"
    "UID=your_username;"
    "PWD=your_password"
)

# Establish the connection
try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")

# Close the connection
finally:
    if 'conn' in locals():
        conn.close()
        print("Connection closed")