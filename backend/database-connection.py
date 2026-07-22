import psycopg2 as pg
from psycopg2 import Error

# Database parameters
db_params = {
    "database": "local-test-classes",
    "user": "postgres",
    "password": "Lokesh",
    "host": "localhost",
    "port": "5432"
}

connection = None
cursor = None

try:
    # Connect to PostgreSQL
    connection = pg.connect(**db_params)

    print("Successfully Connected")

    # Create a cursor
    cursor = connection.cursor()

    # Execute query
    cursor.execute("SELECT version();")

    # Fetch result
    db_version = cursor.fetchone()

    print(f"PostgreSQL Version: {db_version[0]}")

except Error as error:
    print(f"Error executing the query: {error}")

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None:
        connection.close()

    print("Database connection closed.")