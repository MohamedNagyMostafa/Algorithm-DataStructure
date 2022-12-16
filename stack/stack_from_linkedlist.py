class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            node.next_node, self.head = self.head, node

        self.num_elements +=1

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next_node

        self.num_elements -=1

        return value


    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0



a = Stack()

a.push(1)
a.push(2)

print(a.size())
print(a.pop())
print(a.size())
a.push(3)
print(a.pop())
print(a.pop())
print(a.is_empty())


