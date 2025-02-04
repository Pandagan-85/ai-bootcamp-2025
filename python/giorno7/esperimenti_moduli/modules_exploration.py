from collections import Counter, defaultdict, OrderedDict
import datetime
from time import time
from array import array
import pdb

print(datetime.time(5,45,2)) # 05:45:02
print(datetime.date.today()) # 2025-02-04

print(time()) # 1738670264.263846

li = [1,2,3,4,5,6,7,7,1,2]
sentence = "blah blah blah thinking about python"
# mi conta quante volte è presente un elemento
print(Counter(li))
print(Counter(sentence))

dictionary = {'a':1, 'b':2}

print(dictionary['a'])
# print(dictionary['c']) ottengo un errore perchè non abbiamo una c

# defaultdict prende come parametri una callable e un dict, e imposta
# il risultato della callable come valore di default

dictionary2 = defaultdict(lambda: 5,{'a':1, 'b':2})
print(dictionary2['e'])  # 5

dictionary3 = OrderedDict()

dictionary3['a'] = 1
dictionary3['b'] = 2

dictionary4 = OrderedDict()
dictionary4['b'] = 2
dictionary4['a'] = 1

print(dictionary4 == dictionary3)
print(dictionary3.items(), dictionary4.items())

# Prima di python 3.7 dizionari normalmente non avevano il senso dell'ordine,
# in questo caso diamo rilievo all'ordine dei dati

arr = array('i', [1,2,3])
print(arr[0])

# python debugger module
# mi permette di scavare da terminale i problemi
# con step vedo i vari passaggi che fa il codice riga per riga
def add(num1,num2):
    # pdb.set_trace()
    return num1 + num2

# add(4,'dsfdsfds')

# Working with files
my_file = open("test.txt")

# legge tutto
# print(my_file.read())

# legge riga per riga, perchè fa muovere il cursore
# print(my_file.readline())

# Ottengo una lista contenente tutte le righe
# Ogni riga è un elemento dell'array
print(my_file.readlines())

my_file.close()

## Read, write, append
"""with open('test.txt', mode='r+') as my_file:
    text = my_file.write('Hei, It\'s me')"""


with open('test.txt', mode='a') as my_file:
    text = my_file.write('\nuiiiiiii')

## La modalità WRITE crea il file se non esiste
with open('sad.txt', mode='w') as sad:
    text2 = sad.write(':(')

## File error

try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IO error ')
    raise err

