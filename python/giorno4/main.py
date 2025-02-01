# Implement qui il codice
class SearchStringTooShortError(Exception):
    """Eccezione personalizzata per una stringa di ricerca troppo corta."""
    pass

class Directory:
    def __init__(self):
        self.users = []
    def __len__(self):
        return len(self.users)
    def add(self, user):
        self.users.append(user)
        # print(self.users)
        return self.users
    # Lazy object usando un generatore e non una lista per query a find
    def query(self, name):
        # Di default suppongo che l'utente non sia trovato
        found = False
        for user in self.users:
            if user.name == name:
                # Quando trovo l'utente imposto a true
                found = True
                # print(user.name, user.phone)
                yield user
        if not found:
                print(f"No users found with name: {name}")
    def find(self, q_string):
        if len(q_string) < 3:
            # Solleva un'eccezione se la stringa di ricerca è troppo corta
            raise SearchStringTooShortError("La stringa di ricerca deve essere di almeno 2 caratteri.")
        found = False
        for user in self.users:
            # Cerco la stringa in tutti i valori contenuti nell'oggetto user
            if any(q_string in str(value) for value in vars(user).values()):
                found = True
                #print(user)
                yield user
        if not found:
            print(f"No users found with string: {q_string}")


class Person:
    def __init__(self, name=None, phone=None, surname=None):
        self.name = name
        self.surname = surname
        self.phone = phone
    # rappresentare obj user in modo leggibile, traduco output <main.Person object at 0x100a7b4d0> in dati leggibili
    def __repr__(self):
        return f"Person(name='{self.name}', surname='{self.surname}', phone='{self.phone}')"


class Business:
    def __init__(self, name=None, phone=None):
        self.name = name
        self.phone = phone

    # rappresentare obj user in modo leggibile
    def __repr__(self):
        return f"Business(name='{self.name}', phone='{self.phone}')"


"""
Versione da studiare con l'implementazione degli indici di Giulia S.
Il suo metodo add aggiunge un contatto alla lista di contatti e,
contemporaneamente, lo indicizza per un accesso più veloce tramite
vari attributi (nome, cognome, numero di telefono). 
L’indicizzazione è fatta tramite i dizionari name_index, surname_index e phone_index. 

Nel codice di Giulia ogni volta che un contatto viene aggiunto, 
viene memorizzato nella lista principale (contacts) e indicizzato 
nei dizionari name_index, surname_index e phone_index per permettere 
ricerche più rapide.

Anche Query e find sfruttano gli indici

class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname}, phone={self.phone})"


class Business:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Business(name={self.name}, phone={self.phone})"


class Directory:
    def __init__(self):
        self.contacts = []
        self.name_index = {}
        self.surname_index = {}
        self.phone_index = {}

    def add(self, contact):
        self.contacts.append(contact)
        
        # Se il nome del contatto non è ancora presente nell’indice
        # name_index, viene creato un nuovo elenco vuoto come valore
        # associato a quel nome.
        if contact.name not in self.name_index:
            self.name_index[contact.name] = []
        # Aggiunge il contatto all’elenco associato al nome del contatto.
        self.name_index[contact.name].append(contact)

        if isinstance(contact, Person):
            if contact.surname not in self.surname_index:
                self.surname_index[contact.surname] = []
            self.surname_index[contact.surname].append(contact)

        if contact.phone:
            if contact.phone not in self.phone_index:
                self.phone_index[contact.phone] = []
            self.phone_index[contact.phone].append(contact)

    def __len__(self):
        return len(self.contacts)

    def query(self, name=None, surname=None):
        results = []
        if name:
            # get cerca il nome nell'indice, se esiste viene aggiunto
            # alla lista, se non esiste ritorna lista vuota
            results.extend(self.name_index.get(name, []))
        if surname:
            results.extend(self.surname_index.get(surname, []))
        return results

    def find(self, search_term):
        results = []
        # fa cercare in tutti gli indici e poi ricerca parziale nel telefono
        results.extend(self.name_index.get(search_term, []))
        results.extend(self.surname_index.get(search_term, []))
        # questa ricerca per telefono cerca corrispondenze esatte
        results.extend(self.phone_index.get(search_term, []))
        #  questa trova corrispondenze parziali
        for phone, contacts in self.phone_index.items():
            if search_term in phone:
                results.extend(contacts)
        return results
"""