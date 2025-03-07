import sqlite3

# Connect to SQLite database (it'll create the file if it doesn't exist)
conn = sqlite3.connect('database/routes.db')
cursor = conn.cursor()

# Create the table to store routes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS routes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        difficulty TEXT,
        status TEXT
    );
''')

conn.commit()
conn.close()

print("Database initialized.")
