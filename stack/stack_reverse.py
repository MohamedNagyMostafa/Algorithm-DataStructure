class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if len(self.items) > 0 else None

    def is_empty(self):
        return len(self.items) == 0

def reverse_stack(stack):
    stack_out = Stack()
    while not stack.is_empty():
        stack_out.push(stack.pop())
    return stack_out