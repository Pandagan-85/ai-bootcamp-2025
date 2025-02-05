import csv
import sqlite3

# Crea una connessione al database (o lo apre se esiste già)
conn = sqlite3.connect('vendite.db')
cur = conn.cursor()

# Crea una tabella per i dati delle vendite
cur.execute('''
CREATE TABLE IF NOT EXISTS vendite (
    id INTEGER PRIMARY KEY,
    QuotaAmount INTEGER,
    Month INTEGER,
    Agent TEXT,
    Username TEXT  
)
''')

# Carica il file CSV e inserisci i dati nel database
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Salta l'intestazione del CSV
    for row in csv_reader:
        cur.execute('INSERT INTO vendite (QuotaAmount, Month, Agent, Username) VALUES (?, ?, ?, ?)', (row[0], row[1], row[2], row[3]))

conn.commit()



# Mostra la lista dei nomi degli agenti unici con DISTINCT
cur.execute("SELECT DISTINCT Agent FROM vendite")
rows = cur.fetchall()
for row in rows:
    print('Nome agente: ', row)
print("---")

# Mostra il totale delle vendite per ogni agente
cur.execute("SELECT Agent, SUM(QuotaAmount) "
            "FROM vendite "
            "GROUP BY Agent "
            "ORDER BY SUM(QuotaAmount) DESC")
rows = cur.fetchall()
print("Lista degli agenti ordinate per totale delle QuotaAmount:")
for row in rows:
    print(row)
print("---")

# Mostra per i mesi il totale delle vendite ordinandole per la vendita più alta
cur.execute("SELECT Month, SUM(QuotaAmount) "
            "FROM vendite "
            "GROUP BY Month "
            "ORDER BY SUM(QuotaAmount) DESC")
rows = cur.fetchall()
for row in rows:
    print(row)
print("---")

"""
cur.execute("SELECT Month, Agent, MAX(QuotaAmount) "
            "FROM vendite "
            "GROUP BY Month, Agent "
            )
row = cur.fetchall()
for row in rows:
    print(row)

"""
cur.execute("""
    SELECT Month, Agent, MAX(QuotaAmount)
    FROM vendite
    GROUP BY Month, Agent
    ORDER BY Month, MAX(QuotaAmount) DESC
""")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()