import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# PostgreSQL database connection parameters
db_params = {
    'database': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port',
}

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Create an audit schema if it doesn't exist
    cursor.execute('CREATE SCHEMA IF NOT EXISTS audit')
    connection.commit()

    # Get a list of tables in the public schema
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        audit_table_name = f'audit.{table_name}_audit'
        
        # Create an audit table for each table in the public schema
        create_audit_table_query = f'''
        CREATE TABLE IF NOT EXISTS {audit_table_name} (
            operation CHAR(1),
            timestamp TIMESTAMPTZ DEFAULT now(),
            user_id INT,
            {table_name}_id INT,
            {table_name}_data JSONB
        )
        '''
        cursor.execute(create_audit_table_query)
        connection.commit()

    print("Audit schema and tables created successfully.")

except Exception as e:
    print(f"Error creating audit schema and tables: {str(e)}")

finally:
    if connection:
        cursor.close()
        connection.close()