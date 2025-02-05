import sqlite3
import csv

# Connessione al database unico
conn = sqlite3.connect('school.db')
cur = conn.cursor()

# Creazione della tabella 'studenti' se non esiste
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti_drop (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        year_of_birth INTEGER,
        gender TEXT DEFAULT 'Non specificato',
        email TEXT
    )
''')

conn.commit()

# Popolamento della tabella 'studenti' dal CSV
with open('splitted_csv/students_without_assignments.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Salta l'intestazione
    for row in reader:
        cur.execute('''
            INSERT OR IGNORE INTO studenti_drop(id, first_name, last_name, year_of_birth, gender, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row[0], row[1], row[2], row[3], row[4], row[5]))

conn.commit()

# Query per ottenere studenti nati nel 2000
cur.execute('''
    SELECT first_name, last_name
    FROM studenti_drop
    WHERE year_of_birth = 2000
''')

# Stampa i risultati
students_2000 = cur.fetchall()
if students_2000:
    print("Studenti nati nel 2000:")
    for student in students_2000:
        print(f"{student[0]} {student[1]}")
else:
    print("Nessuno studente trovato.")

print('---')

# Query per trovare lo studente con il maggior numero di assignments
cur.execute('''
    SELECT s.first_name, s.last_name, COUNT(a.id) AS assignment_count
    FROM studenti_drop s
    INNER JOIN assignments a ON s.id = a.student_id
    GROUP BY s.id
    ORDER BY assignment_count DESC
    LIMIT 1
''')

# Stampa il risultato
max_assignments = cur.fetchone()
if max_assignments:
    print(f"Studente con il maggior numero di assignments: {max_assignments[0]} {max_assignments[1]} con {max_assignments[2]} assignments")

print('---')

# Query per trovare le studentesse di nome "Jane"
cur.execute('''
    SELECT s.last_name
    FROM studenti_drop s
    WHERE s.first_name = 'Jane'
''')

# Stampa i risultati
jane_students = cur.fetchall()
if jane_students:
    print("Le studentesse di nome Jane sono:")
    for student in jane_students:
        print(student[0])
else:
    print("Nessuna studentessa di nome Jane trovata.")

print('---')

# Query per ottenere la graduatoria degli studenti ordinati per numero di assignments
cur.execute('''
    SELECT s.first_name, s.last_name, COUNT(a.id) AS assignment_count
    FROM studenti_drop s
    LEFT JOIN assignments a ON s.id = a.student_id
    GROUP BY s.id
    ORDER BY assignment_count DESC
''')

# Stampa la graduatoria
print("Graduatoria degli studenti ordinata per numero di assignments:")
ranking = cur.fetchall()
for pos, student in enumerate(ranking, start=1):
    print(f"{pos}. {student[0]} {student[1]} - {student[2]} assignments")

print('---')

# Chiudere la connessione al database
conn.close()