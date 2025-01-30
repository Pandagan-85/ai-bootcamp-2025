# Implement qui il codice
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
        for user in self.users:
            if user.name == name:
                # print(user.name, user.phone)
                yield user
    def find(self, q_string):
        for user in self.users:
            # Cerco la stringa in tutti i valori contenuti nell'oggetto user
            if any(q_string in str(value) for value in vars(user).values()):
                #print(user)
                yield user


class Person:
    def __init__(self, name=None, phone=None, surname=None):
        self.name = name
        self.surname = surname
        self.phone = phone
    # rappresentare obj user in modo leggibile
    def __repr__(self):
        return f"Person(name='{self.name}', surname='{self.surname}', phone='{self.phone}')"


class Business:
    def __init__(self, name=None, phone=None):
        self.name = name
        self.phone = phone

    # rappresentare obj user in modo leggibile
    def __repr__(self):
        return f"Business(name='{self.name}', phone='{self.phone}')"