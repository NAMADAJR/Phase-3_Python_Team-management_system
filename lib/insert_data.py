import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('football_management.db')
cursor = conn.cursor()

# Insert data into coaches table
cursor.execute("INSERT INTO coaches (name, experience) VALUES (?, ?)", ('John Doe', 10))
cursor.execute("INSERT INTO coaches (name, experience) VALUES (?, ?)", ('Jane Smith', 8))

# Insert data into players table
cursor.execute("INSERT INTO players (name, position, coach_id) VALUES (?, ?, ?)", ('Nam', 'Forward', 1))
cursor.execute("INSERT INTO players (name, position, coach_id) VALUES (?, ?, ?)", ('Alex', 'Goalkeeper', 2))
cursor.execute("INSERT INTO players (name, position, coach_id) VALUES (?, ?, ?)", ('Bob', 'Defender', 1))
cursor.execute("INSERT INTO players (name, position, coach_id) VALUES (?, ?, ?)", ('Steve', 'Midfielder', 2))

# Commit the changes and close the connection
conn.commit()
conn.close()
