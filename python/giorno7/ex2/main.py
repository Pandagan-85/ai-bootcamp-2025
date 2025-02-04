from utility_class import Directory
from terminal_action import show_help, add_entry
from save_load import save_to_file,load_from_file

def cmd_loop():
    directory = Directory()

    while True:
        user_input = input("> ").strip().lower()
        parts = user_input.split(maxsplit=1)  # Divide l'input in massimo due parti
        command = parts[0] if parts else ""  # Il primo elemento è il comando
        arg = parts[1] if len(parts) > 1 else None  # Il secondo è l'argomento, se presente

        if command == 'exit':
            print("Uscita...")
            break

        elif command == 'h':
            show_help()

        elif command == 'a':
            if arg in ["business", "person"]:
                add_entry(directory, arg)  # Passa il tipo di contatto
            else:
                print("Specifica il tipo di contatto: 'a business' o 'a person'.")

        elif command == 'f':
            if arg:
                found = False
                for contacts in directory.find(arg):
                    print(contacts)
                    found = True
                if not found:
                    print("Record non trovato!")
            else:
                print("Devi inserire un termine di ricerca. Esempio: 'f Mario'.")

        elif command == 's':
            if arg:
                save_to_file(directory, arg)
            else:
                print("Devi specificare un percorso di salvataggio. Esempio: 's rubrica.json'.")

        elif command == 'l':
            if arg:
                load_from_file(directory, arg)
            else:
                print("Devi specificare un percorso per il file da caricare. Esempio: 'l rubrica.json'.")

        else:
            print("Comando sconosciuto. Digita 'h' per vedere i comandi disponibili.")
"""
# loop comandi sbagliato che chiede più step

# Esegui il ciclo dei comandi
def cmd_loop():
    directory = Directory()

    while True:
        command = input("> ").strip()

        if command == 'exit':
            print("Uscita...")
            break

        elif command == 'h':
            show_help()

        elif command == 'a':
            add_entry(directory)

        elif command == 'f':
            search_term = input("Cerca: ").strip().lower()
            found = False
            # Ricerca nei vari indici
            for contacts in directory.find(search_term):
                print(contacts)
                found = True
            if not found:
                print("Record non trovato!")

        elif command == 's':
            path = input("Percorso del file di salvataggio: ").strip()
            save_to_file(directory, path)

        elif command == 'l':
            path = input("Percorso del file da caricare: ").strip()
            load_from_file(directory, path)

        else:
            print("Comando sconosciuto. Digita 'h' per vedere i comandi disponibili.")
"""
if __name__ == "__main__":
    print("Benvenuto nella rubrica! Digita 'h' per vedere i comandi disponibili.")
    print("Ti consiglio di caricare il database come prima operazione con 'l'")
    cmd_loop()