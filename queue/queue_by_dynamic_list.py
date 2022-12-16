class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, value):
        self.arr.append(value)

    def dequeue(self):
        return self.arr.pop(0)

    def is_empty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

