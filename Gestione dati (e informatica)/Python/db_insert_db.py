import sqlite3

# Connessione al database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Inserimento di dati nella tabella 'users'
user_data = [
    (1, 'john_doe', 'john@example.com'),
    (2, 'jane_smith', 'jane@example.com'),
    # Puoi aggiungere più tuple con dati per altri utenti
]

# Esempio di inserimento dati nella tabella 'users'
cursor.executemany('''
    INSERT INTO users (id, username, email) VALUES (?, ?, ?)
''', user_data)

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()
