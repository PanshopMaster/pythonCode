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
    query = "SELECT TOP (1) [VOUCHER],[DOCUMENTO],[TIPO],[FECHA DOC],[FECHA POST],[FECHA CREADO],[ID AUX],[RUT],[NOMBRE],[USUARIO],[TIPO CAMBIO],[BATCH],[ROWID],[CUENTA],[DESCRIPTION],[AMOUNT_TYPE],[DEBITO],[CREDITO],[MONEDA],[MAYOR]FROM [VISUAL10].[dbo].[AA_MAYOR]"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows   
 # Example usage
if conn:
    select_data(conn)
if conn:
    conn.close()