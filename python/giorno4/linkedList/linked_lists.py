"""
Modulo per la gestione di una lista concatenata (Linked List).

Questa implementazione include:
- La classe `Node`, che rappresenta un nodo della lista collegato a un possibile nodo successivo.
- La classe `LinkedList`, che permette di creare e gestire una lista concatenata, con operazioni come:
  - Aggiunta di un nodo in coda (`add_node`)
  - Iterazione sulla lista
  - Calcolo della lunghezza della lista

Funzionamento:
- Ogni nodo contiene un valore (`data`) e un riferimento al nodo successivo (`next`).
- Il primo nodo della lista è chiamato `head`.
- Quando viene aggiunto un nuovo nodo, esso viene inserito alla fine della lista, aggiornando il riferimento `next` dell'ultimo nodo.

Esempio di utilizzo:
    my_list = LinkedList()
    my_list.add_node("Napoli")
    my_list.add_node("Milan")
    for node in my_list:
        print(node.data)  # Output: Napoli, Milan
"""
class Node:
    def __init__(self, data):
        self.data = data  # Il nodo contiene un valore (dato)
        self.next = None  # Il puntatore al nodo successivo (inizialmente None)


class LinkedList:
    def __init__(self):
        self.head = None  # La lista inizia con nessun elemento

    def __len__(self):
        """Restituisce la lunghezza della lista contando i nodi."""
        count = 0 # Contatore per i nodi
        current = self.head # Partiamo dalla testa della lista
        while current: # Scorriamo la lista finché ci sono nodi
            count += 1 # Incrementiamo il contatore
            current = current.next  # Passa al nodo successivo finchè non diventa NONE
        return count # Restituiamo il numero totale di nodi

    def add_node(self, data):
        """Aggiunge un nodo in coda alla lista."""
        new_node = Node(data)  # Creiamo un nuovo nodo con il valore dato


        if self.head is None:
            # Se la lista è vuota, il nuovo nodo è la testa
            self.head = new_node
        else:
        # Altrimenti, percorri la lista fino all'ultimo nodo
            current = self.head  # Iniziamo dalla testa
            while current.next:  # Finché esiste un next, ci spostiamo in avanti
                current = current.next

            # Ora `current` è l'ultimo nodo, quindi colleghiamo il nuovo nodo
            current.next = new_node

    def __iter__(self):
        """Permette di iterare sulla lista in modo che possa essere usata nei cicli for."""
        current = self.head  # Partiamo dalla testa
        while current: # Scorriamo la lista finché ci sono nodi
            yield current  # Restituiamo il nodo corrente (iterabile)
            current = current.next  # Passiamo al nodo successivo
