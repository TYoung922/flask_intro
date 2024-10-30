import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# List all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Loop through tables and print each table's data
for table_name in tables:
    table_name = table_name[0]  # Extract table name from tuple
    print(f"\nContents of table '{table_name}':")
    cursor.execute(f"SELECT * FROM {table_name}")
    
    # Fetch all rows from the table
    rows = cursor.fetchall()

    # Fetch column names for readability
    column_names = [description[0] for description in cursor.description]
    print("Columns:", column_names)

    # Print each row
    for row in rows:
        print(row)

# Close the connection
conn.close()

