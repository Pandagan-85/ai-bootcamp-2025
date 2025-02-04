
class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

    def to_dict(self):
        """Restituisce un dizionario con i dati della persona."""
        return {
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone
        }

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname}, phone={self.phone})"


class Business:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def to_dict(self):
        """Restituisce un dizionario con i dati dell'azienda."""
        return {
            "name": self.name,
            "phone": self.phone
        }

    def __repr__(self):
        return f"Business(name={self.name}, phone={self.phone})"


class Directory:
    def __init__(self):
        self.contacts = []
        self.name_index = {}
        self.surname_index = {}
        self.phone_index = {}

    def add(self, contact):
        # Verifica se esiste già un contatto con lo stesso nome, cognome e telefono
        if isinstance(contact, Person):
            for existing_contact in self.contacts:
                if (isinstance(existing_contact, Person) and
                        existing_contact.name == contact.name and
                        existing_contact.surname == contact.surname):
                    print("Un contatto con lo stesso nome e cognome esiste già!")
                    return
        elif isinstance(contact, Business):
            for existing_contact in self.contacts:
                if (isinstance(existing_contact, Business) and
                        existing_contact.name == contact.name):
                    print("Un'attività con lo stesso nome esiste già!")
                    return

        # Aggiunge il contatto se non ci sono duplicati
        self.contacts.append(contact)

        # Aggiornamento degli indici
        if contact.name not in self.name_index:
            self.name_index[contact.name] = []
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
        search_term = search_term.lower()

        for contact in self.contacts:
            if (search_term in contact.name.lower() or
                    (isinstance(contact, Person) and search_term in contact.surname.lower()) or
                    (contact.phone and search_term in contact.phone)):
                results.append(contact)

        return results