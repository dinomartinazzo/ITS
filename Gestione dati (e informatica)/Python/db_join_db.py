import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create 'users' and 'orders' tables (for demonstration purposes)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

# Insert sample data into 'users' and 'orders' tables
cursor.execute('''
    INSERT INTO users (username, email) VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com')
''')

cursor.execute('''
    INSERT INTO orders (user_id, product) VALUES
    (1, 'Product A'),
    (1, 'Product B'),
    (2, 'Product C')
''')

# Perform an INNER JOIN between 'users' and 'orders' tables
cursor.execute('''
    SELECT users.id, users.username, users.email, orders.product
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
''')

rows = cursor.fetchall()

# Displaying the results of the join operation
for row in rows:
    print(row)

# Close the connection
conn.close()
