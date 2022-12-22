from collections import deque

class Queue:

    def __init__(self):
        self.arr = deque()

    def enqueue(self, value):
        self.arr.append(value)

    def dequeue(self):
        return self.arr.popleft()

    def is_empty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

class Node:
    def __init__(self, value = None):
        self.value  = value
        self.left   = None
        self.right  = None

    def get(self):
        return self.value

    def set(self, value):
        self.value  = value

    def set_left_child(self, node):
        self.left   = node

    def set_right_child(self, node):
        self.right  = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

class Tree:

    def __init__(self, value = None):
        self.root = Node(value)

    def get_root(self):
        return self.root

def bfs(tree):
    visited = []
    queue = Queue()

    queue.enqueue(tree.get_root())
    visited.append(tree.get_root())

    while not queue.is_empty():
        node = queue.dequeue()
        if node.has_left_child():
            queue.enqueue(node.get_left_child())
            visited.append(node.get_left_child())
        if node.has_right_child():
            queue.enqueue(node.get_right_child())
            visited.append(node.get_right_child())

    return visited

# build a tree
# tree = Tree(value='apple')
# tree.get_root().set_left_child(Node('banana'))
# tree.get_root().set_right_child(Node('cherry'))
# tree.get_root().get_left_child().set_left_child(Node('dates'))
#
# print([node.value for node in bfs(tree)])