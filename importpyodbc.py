import pyodbc
import pandas as pd

def create_connection():
    server = 'vm-prod-08'
    database = 'VISUAL10'
    username = 'Finanzas'
    password = 'Fin180724'
    driver = '{ODBC Driver 17 for SQL Server}'

    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
    try:
        connection = pyodbc.connect(connection_string)
        print("Connection successful")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
conn = create_connection()
def select_data(connection):
    cursor = connection.cursor()
    query = "Select * from WORK_ORDER where BASE_ID like 'OT%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        if row.BASE_ID == 'OT126945':
            print(row.BASE_ID)
    return rows   
 # Example usage
if conn:
    select_data(conn)
if conn:
    conn.close()