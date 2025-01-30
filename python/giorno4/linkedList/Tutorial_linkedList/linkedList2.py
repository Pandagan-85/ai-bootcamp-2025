"""
Tutorial qui https://www.youtube.com/watch?v=1iz9SRWdpX8
Fare la parte delle double linked list in nuovo file
"""
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        # Nodo iniziale, quando vuota è None
        self.head = None
    # O (n)
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head

            return_string = f"[{last.value}"

            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"

            return return_string


    # O(n) Linear Time
    # metodo che ci da True o False
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) linear Time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter+=1
            last = last.next
        return counter



    # O(n) - Linear time
    # Aggiungiamo a seguire
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            # scorro fino a quando non trovo un nodo che non ha un next e inserisco il nuovo nodo
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # O(1) constant time
    # Aggiungiamo come primo nodo
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n) Linear Time
    # Aggiungiamo ad uno specifico index
    def insert(self,value,index):
        if index == 0:
            self.prepend(value)
        # Se provo ad aggiungere con un indice a una lista vuota alzo un errore
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                # se la lista non è vuota
                last = self.head
                # andiamo fino a prima dell'elemento, perchè non vogliamo arrivare all'elemento
                for i in range(index-1):
                    # se non c'è' un next significa che voglio inserirlo in una posizione che non esiste
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                # Creiamo il nodo ad esempio B che vogliamo inserire tra A e C
                new_node = Node(value)
                # Puntiamo B a C
                new_node.next = last.next
                # Puntiamo A al nuovo B
                last.next = new_node

    # O(n) Linear time
    def delete(self,value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                # quando cancelliamo un nodo es B, vogliamo che A (Che precede B) punti a C (ovvero a quello a cui puntava B)
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        break
                    last = last.next


    # O(n) Linear Time
    def pop(self,index):
        if self.head is None:
            raise ValueError("Index out of Bounds")
        else:
            last = self.head

            for i in range(index-1):
                if last.next is None:
                    raise ValueError("Index out of Bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of Bounds")
            else:
                last.next = last.next.next

    # O(n) linear runtime
    def get(self,index):
        if self.head is None:
            raise ValueError("Index out of Bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of Bounds")
                last = last.next
            return last.value



if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(5)
    ll.append(18)
    ll.append(22)
    ll.append(29)
    ll.append(32)
    print(ll)
    ll.prepend(100)
    print(ll)
    ll.insert(200,1)
    print(ll)
    ll.delete(18)
    print(ll)
    ll.pop(1)
    print(ll)
    print(ll.get(1))
    #contain
    print(29 in ll)
    print(800 in ll)