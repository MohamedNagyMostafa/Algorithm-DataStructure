class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if len(self.items) > 0 else None

    def is_empty(self):
        return len(self.items) == 0

def do_operation(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 / num2

def evaluate_post_fix(equation):
    operations = ['+', '-', '/', '*']
    stack = Stack()

    for char in equation:
        if char not in operations:
            stack.push(int(char))
        else:
            num1, num2 = stack.pop(), stack.pop()
            result = int(do_operation(num2, num1, char))
            stack.push(result)
    return stack.pop()

