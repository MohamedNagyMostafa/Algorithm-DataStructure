
class Node:
    def __init__(self, value):
        self.value  = value
        self.next   = None

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        return self.arr.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0


    def enqueue(self, value):
        node = Node(value)

        if self.is_empty():
            self.head = self.tail = node
            self.num_elements += 1

            return

        self.tail.next, self.tail = node, node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.head.value

        self.head = self.head.next
        self.num_elements -=1
        # in case of one node
        if self.is_empty():
            self.tail = None

        return value

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements


def reverse_queue(queue):
    rev_queue   = Queue()
    stack       = Stack()

    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        rev_queue.enqueue(stack.pop())

    return rev_queue