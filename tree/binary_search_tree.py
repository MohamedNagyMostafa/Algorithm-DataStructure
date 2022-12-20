class Stack:

    def __init__(self):
        self.arr = list()

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        return self.arr.pop()

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return self.size() == 0

    def top(self):
        return self.arr[-1] if not self.is_empty() else None

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


def post_order(stack, visited):


    # Check left
    if stack.top().has_left_child():
        stack.push(stack.top().get_left_child())
        in_order(stack, visited)

    # Check right
    if stack.top().has_right_child():
        stack.push(stack.top().get_right_child())
        in_order(stack, visited)

    # visit current node
    visited.append(stack.top())
    # remove the node
    stack.pop()

    if stack.is_empty():
        return visited


def in_order(stack, visited):


    # Check left
    if stack.top().has_left_child():
        stack.push(stack.top().get_left_child())
        in_order(stack, visited)

    # visit current node
    visited.append(stack.top())

    # Check right
    if stack.top().has_right_child():
        stack.push(stack.top().get_right_child())
        in_order(stack, visited)

    # remove the node
    stack.pop()

    if stack.is_empty():
        return visited

def pre_order(stack, visited):

    # visit current node
    visited.append(stack.top())

    # Check left
    if stack.top().has_left_child():
        stack.push(stack.top().get_left_child())
        pre_order(stack, visited)

    # Check right
    if stack.top().has_right_child():
        stack.push(stack.top().get_right_child())
        pre_order(stack, visited)

    # remove the node
    stack.pop()

    if stack.is_empty():
        return visited

def traversal_dfs_with_recursion(tree,
                                 pre_order_travl = False,
                                 in_order_travl = False,
                                 post_order_travl = False):
    stack   = Stack()
    visited = list()

    stack.push(tree.root)

    if pre_order_travl:
        visited = pre_order(stack, visited)
    elif in_order_travl:
        visited = in_order(stack, visited)
    elif post_order_travl:
        visited = post_order(stack, visited)

    return visited

def traversal_dfs_preorder(tree):
    stack   = Stack()
    visited = []

    stack.push(tree.root)
    visited.append(tree.root)
    while not stack.is_empty():
        curr_node = stack.top()

        # Check left
        if curr_node.has_left_child() and curr_node.get_left_child() not in visited:
            curr_node   = curr_node.get_left_child()
            stack.push(curr_node)
            visited.append(curr_node)
        # Check right
        elif curr_node.has_right_child() and curr_node.get_right_child() not in visited:
            curr_node   = curr_node.get_right_child()
            stack.push(curr_node)
            visited.append(curr_node)
        # pop node
        else:
            stack.pop()
    return visited

# build a tree
tree = Tree(value='apple')
tree.get_root().set_left_child(Node('banana'))
tree.get_root().set_right_child(Node('cherry'))
tree.get_root().get_left_child().set_left_child(Node('dates'))

visited = traversal_dfs_with_recursion(tree, post_order_travl= True)
print([node.value for node in visited])