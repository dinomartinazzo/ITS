import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Ask user for input data
user_id = int(input("Enter user ID: "))
username = input("Enter username: ")
email = input("Enter email: ")

# Insert user input into the 'users' table
cursor.execute('INSERT INTO users (id, username, email) VALUES (?, ?, ?)', (user_id, username, email))
conn.commit()

# Select and display all rows from the 'users' table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("\nSelected Data:")
for row in rows:
    print(row)

# Close the connection
conn.close()
