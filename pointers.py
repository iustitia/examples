class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(2)
b = Node(5)
c = Node(1)
d = Node(7)

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

# Zadanie:

# Napisz funkcję, która dla listy wskaźnikowej wypisuje wszystkie wartości większe od 3


def bigger_than_3(head):
    while head is not None:
        if head.val > 3:
            print(head.val)
        head = head.next


bigger_than_3(a)
