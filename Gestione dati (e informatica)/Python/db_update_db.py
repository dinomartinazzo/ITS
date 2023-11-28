import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Update the email of the user with id 1
cursor.execute('UPDATE users SET email = ? WHERE id = ?', ('new_email@example.com', 1))

# Commit the changes
conn.commit()

# Close the connection
conn.close()