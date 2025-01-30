from main import Directory, Person, Business

directory = Directory()

assert len(directory) == 0

directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))

assert len(directory) == 3

# Domanda: perché usiamo le list comprehension?
# Risposta: perchè possiamo avere risultati multipli
assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]
assert [el.phone for el in directory.find("Hamilton")] == ["01-234-567", None]
assert [el.name for el in directory.find("333")] == ["Vedrai"]

# test controllo lunghezza
for user in directory.find("Msa"):
    print(user)
# test controllo nome inesistente
for user in directory.query("Ciccio"):
    print(user)
# test implementazione __repr__
print(directory.users)