
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
        self.stack = Stack()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        if self.is_empty():
            return None

        temp_stack = Stack()
        while not self.stack.is_empty():
            temp_stack.push(self.stack.pop())

        # pick last element
        value = temp_stack.pop()

        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())

        return value


    def is_empty(self):
        return self.stack.is_empty()

    def size(self):
        return self.stack.size()