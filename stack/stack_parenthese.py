class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if len(self.items) > 0 else None

    def is_empty(self):
        return len(self.items) == 0



def equation_checker(equation):
    stack = Stack()
    for char in equation:
        if char == "(":
            stack.push("(")
        elif char == ")":
            if stack.pop() is None:
                return False
    return stack.is_empty()

