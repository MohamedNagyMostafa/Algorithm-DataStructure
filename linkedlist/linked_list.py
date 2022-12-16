
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        node = Node(value)
        pointer = self.head

        if pointer is None:
            self.head = node
            return
        while pointer.next is not None:
            pointer = pointer.next

        pointer.next = node
        self.pointer = self.head
        return

    def search(self, value):
        pointer = self.head

        while pointer is not None and pointer.value != value:
            pointer = pointer.next

        return pointer

    def remove(self, value):
        pointer = self.head
        preNode = None
        while pointer is not None and pointer.value != value:
            preNode = pointer
            pointer = pointer.next


        if pointer is None:
            return None

        preNode.next = pointer.next

        return pointer

    def to_list(self):
        nodes_value = []
        pointer = self.head

        while pointer is not None:
            nodes_value.append(pointer.value)
            pointer = pointer.next

        return nodes_value

    def __iter__(self):
        pointer = self.head
        while pointer is not None:
            yield pointer
            pointer = pointer.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)

        if self.tail is None:
            self.head = node
            self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        return

    def to_list(self):
        nodes_value = []
        pointer = self.head

        while pointer is not None:
            nodes_value.append(pointer.value)
            pointer = pointer.next

        return nodes_value

    def __iter__(self):
        pointer = self.head
        while pointer is not None:
            yield pointer.value
            pointer = pointer.next

def reverse(linked_list):
    reversed_linked_list = LinkedList()

    for i in linked_list:
        reversed_linked_list.prepend(i.value)

    return reversed_linked_list

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(10)
linked_list.append(30)
# for i in linked_list.to_list():
#     print(i)
linked_list.prepend(9)

for i in linked_list.to_list():
    print(i)


print(linked_list.remove(10).value)
print('after')
for i in iter(linked_list):
    print(i.value)
print('reverse')

for i in iter(reverse(linked_list)):
    print(i.value)