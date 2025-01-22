print("Inizio programma")

# Assegno la variabile foo
# False = foo
foo = False

# Questi controlli assert devono passare tutti
assert not bool(0)
assert False != True
assert True is not False
assert True == True
assert None is not False

# Faccio alcune operazioni aritmetiche sui numeri interi
# un numero non puà essere diviso per 0 quindi cambio il valore di bar
bar = 1
baz = 1
result = baz / bar
print(result)
# Incremento il risultato di uno

result += 1
print(result)
# Decremento il risultato di uno

result -= 1
print(result)
# Controllo che il valore non sia negativo
assert result >= 0

# Concateno le stringhe
message = "hello" + " " +  (b"world").decode()
print(message)

# Creo una lista e la estendo
li1 = [1, 2]
# li1 += [3],
li1.append(3)
print(li1)
# Non mi ricordo come si "prepende" un valore...
li1.insert(0,0)
print(li1)

# Verifico che il risultato sia quello che mi aspetto
assert li1 == [0, 1, 2, 3]

# Creo una tupla e la estendo
tu1 = (1, 2)
tu1 += (3,)

assert tu1 == (1, 2, 3)

# Creo un dict

d1 = {}
d1["a"] = 1
d1["b"] = 2

assert d1["a"] == 1
assert d1 == {"a": 1, "b": 2}
# print(d1)
# Cancello la chiave "b"
del d1["b"]
# print(d1)
# Controllo che il dict non contenga ancora la chiave "b"
assert "b" not in d1

# Potrei anche controllarlo in questo modo
# e verificare anche la presenza di "a"
if "b" not in d1 and "a" in d1:
    assert True
else:
    assert True

# Stampo la scritta "Ciao" tre volte poi esco
# Conto le volte che l'ho stampata
count = 0
for idx in [1, 2, 3]:
    count += 1
    print("Ciao")

# Controllo che l'abbia stampata tre volte
assert count == 3

# Stampo di nuovo la scritta "Ciao" tre volte poi esco
num = 3
while num > 0:
    print("Ciao 2")
    num -=1

print("Fine programma")

# Bonus: verifico la seguente operazione sui float
assert 0.1 + 0.2 != 0.3

a = 0.1 + 0.2
print(a)
# 0.30000000000000004
"""
Il risultato non combacia per come python rappresenta i numeri in virgola mobile
I numeri float sono rappresentati utilizzando una codifica binaria, 
che non può rappresentare con precisione alcuni numeri decimali (come 0.1 o 0.2). 
Di conseguenza, si verificano errori di approssimazione.
"""


import math
assert math.isclose(0.1 +  0.2, 0.3)
