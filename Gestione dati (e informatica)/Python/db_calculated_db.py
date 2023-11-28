import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Selecting data with a calculated field
cursor.execute('SELECT id, username, email, username || " - " || email AS user_info FROM users')
rows = cursor.fetchall()

# Displaying the results with the calculated field
for row in rows:
    print(row)

# Close the connection
conn.close()
