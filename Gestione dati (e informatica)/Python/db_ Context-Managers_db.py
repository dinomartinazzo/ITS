import sqlite3

# Using a context manager to ensure proper resource cleanup
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()

    # Inserting data into the 'users' table
    new_user = (3, 'alice_smith', 'alice@example.com')
    cursor.execute('INSERT INTO users (id, username, email) VALUES (?, ?, ?)', new_user)

    # Querying data from the 'users' table
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    # Displaying the results
    for row in rows:
        print(row)
