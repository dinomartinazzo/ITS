import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Delete the user with id 2
cursor.execute('DELETE FROM users WHERE id = ?', (2,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()