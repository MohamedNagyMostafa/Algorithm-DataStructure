
class Node:
    def __init__(self, value):
        self.value  = value
        self.next   = None


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


q = Queue()
q.enqueue(100)
print('head', q.head.value)
print('tail', q.tail.value)
q.enqueue(200)
print('head', q.head.value)
print('tail', q.tail.value)
q.enqueue(300)
print('head', q.head.value)
print('tail', q.tail.value)
print('dequeue', q.dequeue())
print('head', q.head.value)
print('tail', q.tail.value)
print('dequeue', q.dequeue())
print('head', q.head.value)
print('tail', q.tail.value)


