def conta_valore_stringhe(lista):
    conteggio = {}
    if lista:
        try:
            for name in lista:
                conteggio[name] = conteggio.get(name, 0) + 1
            return conteggio
        except TypeError:
            raise TypeError("Per favore inserisci un lista")
    else: print("inserisci qualcosa")

