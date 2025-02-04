import os
import json
from utility_class import Person, Business

def save_to_file(directory, path=None):
    """Salva i contatti su file JSON."""
    if not path:
        if not os.path.exists('data'):
            os.makedirs('data')
        path = 'data/contacts.json'

    if not path.endswith('.json'):
        print("❌ Errore: il file deve avere estensione .json!")
        return

    try:
        with open(path, 'w') as file:
            json.dump([contact.to_dict() for contact in directory.contacts], file, indent=4)
        print(f"✅ Database salvato in {path}")
    except Exception as e:
        print(f"❌ Errore nel salvataggio del file: {e}")

def load_from_file(directory, path=None):
    """Carica i contatti da file JSON."""
    if not path:
        path = 'data/contacts.json'

    if not path.endswith('.json'):
        print("❌ Errore: il file deve avere estensione .json!")
        return

    if not os.path.exists(path):
        print("⚠️ Attenzione: Il file non esiste. Nessun dato caricato.")
        return

    try:
        with open(path, 'r') as file:
            data = json.load(file)
            directory.contacts = []
            for entry in data:
                if 'surname' in entry:  # Se c'è un cognome, è una persona
                    directory.add(Person(entry["name"], entry["surname"], entry["phone"]))
                else:  # Altrimenti, è un'azienda
                    directory.add(Business(entry["name"], entry["phone"]))
        print(f"✅ Database caricato da {path}")
    except Exception as e:
        print(f"❌ Errore nel caricamento del file: {e}")