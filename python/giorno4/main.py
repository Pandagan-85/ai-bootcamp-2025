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