from utility_class import Person, Business
def show_help():
    """Mostra i comandi disponibili."""
    print("Comandi disponibili:")
    print("a (person|business)  -> Aggiungi un record (persona o business)")
    print("f <text>             -> Trova un record")
    print("s <path>             -> Salva il database in un file JSON")
    print("l <path>             -> Carica il database da un file JSON")

def add_entry(directory, arg=None):
    entry_type = arg.strip().lower() if arg else input("Tipo di record (person/business): ").strip().lower()

    if entry_type == 'person':
        name = input("Nome: ")
        surname = input("Cognome: ")
        phone = input("Telefono: ")
        contact = Person(name, surname, phone)
        directory.add(contact)
        print(f"Persona aggiunta: {contact}")
    elif entry_type == 'business':
        name = input("Nome: ")
        phone = input("Telefono: ")
        contact = Business(name, phone)
        directory.add(contact)
        print(f"Azienda aggiunta: {contact}")
    else:
        print("Tipo non valido!")
