class Node:
    """Rappresenta un nodo della linked list."""
    def __init__(self, data):
        self.data = data  # Il valore del nodo
        self.next = None  # Puntatore al prossimo nodo (inizialmente None)



class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
       return self.length

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length +=1

    def __iter__(self):
        current_node = self.head  # Inizia dalla testa
        while current_node:  # Continua finché non raggiungi il nodo finale
            yield current_node  # Restituisce il nodo corrente
            current_node = current_node.next  # Passa al nodo successivo



