# Esercizio 0

# 0. Stampa "ciao, mondo!"
print("ciao, mondo!")

# 1. Stampa il risultato della somma dei numeri 40 e 2
print(40 + 2)

# 2. Gestisce la divisione per 0 e stampa un messaggio appropriato
try:
    result = 40 / 0
    print(result)
except ZeroDivisionError:
    print("Errore: Non è possibile dividere per zero! ;)")


# bonus
try:
    # Apri il file README.md in modalità lettura
    with open("README.md", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Errore: Il file 'README.md' non è stato trovato!")