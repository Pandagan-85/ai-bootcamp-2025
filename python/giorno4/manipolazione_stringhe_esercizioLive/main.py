import os

print(os.listdir())

fd = open("scratch_4.py")
# print(fd)
# <_io.TextIOWrapper name='scratch_4.py' mode='r' encoding='UTF-8'>
# se a open non passo parametro di default prende "r" modalità lettura

# read ci butta fuori il contenuto del testo
print(fd.read())
name = "pippo.txt"
fd2 = open("pippo.txt", "w")
# se provo a leggerlo avrò un errore perchè non esiste.
fd2.write("ciao!, Pippo")
fd2.close()
fd2 = open("pippo.txt", "r")
print(fd2.read())

with open(name, "r") as fd3:
    print(fd3.read())

text = ""
while text == "":
    text = input("Nome? ")
print(f"il tuo nome è {text}")
