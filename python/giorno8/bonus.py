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

"""
s.first_name e s.last_name selezionano i nomi e cognomi degli studenti dalla tabella studenti
COUNT(a.id) conta il numero di record (ovvero, compiti) nella tabella assignments (alias a) per ciascun studente. a.id si riferisce all’ID di ciascun compito.
L’alias AS assignment_count dà un nome più comprensibile a questa colonna: invece di COUNT(a.id), la colonna risultante sarà chiamata assignment_count.
TAb studenti:
| id  | first_name | last_name |
|-----|------------|-----------|
| 1   | Marco      | Rossi     |
| 2   | Anna       | Bianchi   |
| 3   | Luca       | Verdi     |
TAb assignment:
| id  | student_id | assignment_name |
|-----|------------|-----------------|
| 1   | 1          | Compito 1       |
| 2   | 1          | Compito 2       |
| 3   | 2          | Compito 1       |
| 4   | 3          | Compito 1       |
| 5   | 3          | Compito 2       |
| 6   | 3          | Compito 3       |
Tab temporanea con inner join
| id  | first_name | last_name | student_id | assignment_name |
|-----|------------|-----------|------------|-----------------|
| 1   | Marco      | Rossi     | 1          | Compito 1       |
| 1   | Marco      | Rossi     | 1          | Compito 2       |
| 2   | Anna       | Bianchi   | 3          | Compito 1       |
| 3   | Luca       | Verdi     | 3          | Compito 1       |
| 3   | Luca       | Verdi     | 3          | Compito 2       |
| 3   | Luca       | Verdi     | 3          | Compito 3       |
Count degli assignment raggruppati per id studente:
| first_name | last_name | assignment_count |
|------------|-----------|------------------|
| Marco      | Rossi     | 2                |
| Luca       | Verdi     | 3                |
L'INNER JOIN restituisce solo le righe che hanno una corrispondenza in entrambe le tabelle.
Se uno studente non ha alcun compito assegnato, quella riga non verrà inclusa nei risultati.
"""


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

"""
Spiegazione QUERY
Le tabelle di partenza sono
studenti
| id  | first_name | last_name |
|-----|------------|-----------|
| 1   | Marco      | Rossi     |
| 2   | Anna       | Bianchi   |

assignments
| id  | student_id | assignment_name |
|-----|------------|-----------------|
| 1   | 1          | Compito 1       |
| 2   | 1          | Compito 2       |
| 3   | 1          | Compito 3       |

s.first_name, s.last_name: Select dei nomi e i cognomi degli studenti dalla tabella studenti, che è aliasata come s.
COUNT(a.id) AS assignment_count: Questa parte della query conta il numero di compiti (assignments) associati a ciascun studente. 
Stiamo contando le righe nella tabella assignments per ogni studente, basandoci sull'ID del compito (a.id). 
Il risultato di questa conta verrà restituito con l'alias assignment_count.
---
Tabella Temporanea dopo il LEFT JOIN:
| id  | first_name | last_name | assignment_id |
|-----|------------|-----------|---------------|
| 1   | Marco      | Rossi     | 1             |
| 1   | Marco      | Rossi     | 2             |
| 1   | Marco      | Rossi     | 3             |
| 2   | Anna       | Bianchi   | NULL          |

LEFT JOIN assignments a: 
Qui stiamo usando un LEFT JOIN con la tabella assignments.
L'alias a è usato per fare riferimento a questa tabella. 
Un LEFT JOIN restituirà tutte le righe dalla tabella di sinistra (studenti in questo caso), 
e se esistono righe corrispondenti nella tabella di destra (assignments), queste verranno combinate 
con i dati della tabella di sinistra. Se non c'è corrispondenza (cioè, lo studente non ha assegnamenti), 
a query restituirà comunque lo studente, ma con valori NULL per le colonne della tabella assignments.

Risultato Finale con COUNT e GROUP BY:

| first_name | last_name | assignment_count |
|------------|-----------|------------------|
| Marco      | Rossi     | 3                |
| Anna       | Bianchi   | 0                |

La condizione che lega le due tabelle è: ON s.id = a.student_id
Il LEFT JOIN è particolarmente utile quando vuoi includere tutte le righe della tabella di sinistra 
(in questo caso, gli studenti), anche se non ci sono corrispondenze nella tabella di destra 
(in questo caso, assignments). Se usassi un INNER JOIN, invece, verrebbero inclusi solo gli studenti 
che hanno almeno un compito assegnato. In altre parole, con un LEFT JOIN potresti anche 
trovare studenti che non hanno compiti, mentre con un INNER JOIN non li vedresti affatto.
"""

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