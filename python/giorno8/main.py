import csv, sqlite3
from datetime import datetime,timedelta
from random import randint
import os

# Crea una connessione al database (o lo apre se esiste già)
conn = sqlite3.connect('students.db')
cur = conn.cursor()

# Crea una cartella "splitted_csv" se non esiste
if not os.path.exists('splitted_csv'):
    os.makedirs('splitted_csv')

# Crea una tabella per i dati delle studenti
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        year_of_birth INTEGER,
        gender TEXT DEFAULT 'Non specificato',
        email TEXT,
        assignments INTEGER DEFAULT 0
    )
    ''')

## Leggere CSV e Inserire i dati nel database studenti
with open("students.csv") as st:
    reader = csv.reader(st, delimiter=';')
    next(reader)  # Salta l'intestazione del CSV
    for row in reader:
        cur.execute("SELECT id FROM studenti WHERE id = ?", (row[0],))
        if cur.fetchone():
            print(f"⚠️ ID {row[0]} già esistente, riga ignorata.")
            continue  # Salta questa riga se l'ID esiste già

        cur.execute('''
            INSERT INTO studenti (id, first_name, last_name, year_of_birth, gender, email, assignments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

conn.commit()


## Creo secondo DB

conn2 = sqlite3.connect('assignments.db')
cur2 = conn2.cursor()

cur2.execute('''
    CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    delivery_date TEXT,
    FOREIGN KEY (student_id) REFERENCES studenti(id) ON DELETE CASCADE
    )
    ''')
conn2.commit()

# Selezionare gli studenti dal database principale (studenti)
cur.execute('''SELECT id, assignments FROM studenti''')
students = cur.fetchall()

# Calcolare il numero totale di assignments (totale di tutte le colonne assignments degli studenti)
total_assignments = sum(student[1] for student in students)  # Somma totale di assignments

print(f"Totale assignments da generare: {total_assignments}")

# Genera e inserisce le date di consegna per ogni assignment
for student in students:
    student_id = student[0]
    num_assignments = student[1]

    # Genera `num_assignments` date casuali per lo studente
    for _ in range(num_assignments):
        # Genera una data casuale di consegna (entro i prossimi 30 giorni)
        """
        datetime.now() restituisce la data e l’ora correnti, cioè il momento esatto in cui viene eseguito il codice. 2025-02-05 14:30:00
        timedelta è una classe della libreria datetime che permette di aggiungere o sottrarre un intervallo di tempo a una data.
        randint(1, 30) genera un numero intero casuale tra 1 e 30. Questo numero viene passato a timedelta, che lo usa per definire l’intervallo di tempo in giorni
        strftime() è un metodo che permette di formattare un oggetto datetime in una stringa secondo un formato specificato.
        
        """
        delivery_date = (datetime.now() + timedelta(days=randint(1, 30))).strftime('%Y-%m-%d')

        # Inserisci la data nel database assignments
        cur2.execute('''
            INSERT INTO assignments (student_id, delivery_date)
            VALUES (?, ?)
        ''', (student_id, delivery_date))

# Commit delle modifiche al database assignments
conn2.commit()
print(f"Totale assignments inseriti: {total_assignments}")

print('---')

# Generazione dei CSV

## Estrai i dati degli studenti senza la colonna 'assignments'
cur.execute('''SELECT id, first_name, last_name, year_of_birth, gender, email FROM studenti''')
students = cur.fetchall()

# Crea il primo CSV con gli studenti senza 'assignments'
with open('splitted_csv/students_without_assignments.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['id', 'first_name', 'last_name', 'year_of_birth', 'gender', 'email'])  # Intestazione
    for student in students:
        writer.writerow(student)

## Estrai gli assignment (id studente e data di consegna)

cur2.execute('''SELECT id, student_id, delivery_date FROM assignments''')
assignments = cur2.fetchall()

# Crea il secondo CSV con l'ID del compito incluso
with open('splitted_csv/assignments.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['assignment_id', 'student_id', 'delivery_date'])  # Intestazione
    for assignment in assignments:
        writer.writerow(assignment)

print("CSV creati con successo!")


print('---')
## Gli studenti nati nel 2000
print("Studenti nati nel 2000:")
cur.execute('''SELECT last_name, first_name FROM studenti WHERE year_of_birth = 2000''')
rows = cur.fetchall()
if rows:
    for last_name, first_name in rows:
        print(f"{first_name} {last_name}")
else:
    print("Nessuno studente trovato.")
print('---')
## la persona che ha consegnato il maggior numero di assignments (usando `MAX()` in SQL o in Python)
print("Studente con il maggior numero di assignments: ")
cur.execute('''
    SELECT last_name, first_name, assignments
    FROM studenti
    WHERE assignments = (SELECT MAX(assignments) FROM studenti)
''')
max_assignment = cur.fetchall()
for last_name, first_name, assignments in max_assignment:
    print(f"{first_name} {last_name} with {assignments} assignments")
print('---')
## il cognome delle studentesse di nome "Jane"
cur.execute('''SELECT last_name from studenti WHERE first_name = "Jane"''')
cognomi = cur.fetchall()
if cognomi:  # Controlla se ci sono risultati
    print("Le studentesse di nome Jane sono:")
    for (last_name,) in cognomi:  # Scompatta la tupla con un solo elemento
        print(f"- {last_name}")
else:
    print("Nessuna studentessa di nome Jane trovata.")
print('---')
## Stampare la graduatoria degli studenti ordinati in base al numero di assignment usando `ORDER BY`
print("🏆Graduatoria degli studenti per assignments:")
cur.execute('''SELECT id, last_name, first_name, assignments FROM studenti ORDER BY assignments DESC''')
classifica = cur.fetchall()
for pos, (id, last_name, first_name, assignments) in enumerate(classifica, start=1):
    print(f"{pos}. user {id} {first_name} {last_name} - {assignments} assignments")
print('---')
## Stampare il totale dei compiti per capire quante date di consegna generare
cur.execute('''SELECT SUM(assignments) FROM studenti ''')
totale = cur.fetchone()
print(f"Assignment totali-{totale}")
print('---')



cur.close()
cur2.close()