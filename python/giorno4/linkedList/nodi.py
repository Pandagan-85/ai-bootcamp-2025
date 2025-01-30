from linked_lists import LinkedList, Node

# Part 1 - tests for the nodes of a linked list

head_node = Node("Napoli")

assert head_node.next is None

head_node.next = Node("Rome")
# Napoli → Rome → None
head_node.next.next = Node("Milan")
# Napoli → Rome → Milan → None

# Part 2 - tests for the linked list

my_list = LinkedList()
# LinkedList: head → None

assert len(my_list) == 0
assert my_list.head is None

my_list.add_node(data="Napoli")
# LinkedList: head → [Napoli] → None

assert len(my_list) == 1
assert my_list.head.data == "Napoli"


my_list.add_node(data="Milan")
# LinkedList: head → [Napoli] → [Milan] → None

assert len(my_list) == 2

# Check that we have two objects of type Node
assert [type(el) for el in my_list] == [Node, Node]

# Itera sui nodi e stampa data, next e head
for node in my_list:
    print(f"Data: {node.data}")  # Stampa il dato del nodo
    print(f"Next: {node.next.data if node.next else None}")  # Stampa il prossimo nodo (next)
    print(f"Head: {my_list.head.data}")  # Stampa la testa della lista
    print("-" * 20)  # Aggiunge una linea separatrice per chiarezza

