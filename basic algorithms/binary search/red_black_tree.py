class Node:

    def __init__(self, value, parent, color):
        self.value  = value
        self.color  = color
        self.parent = parent
        self.left   = None
        self.right  = None

class RedBlackTree(object):

    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, value):
        inserted_node = self.insert_node_to_tree(self.root, value)

        self.rebalance()

    def search(self, value):
        return False


    def insert_node_to_tree(self, current_node, value):
        if current_node.value > value:
            if current_node.left:
                self.insert_node_to_tree(current_node= current_node.left, value= value)
            else:
                current_node.left = Node(value, current_node, 'red')
                return current_node.left
        else:
            if current_node.right:
                self.insert_node_to_tree(current_node= current_node.right, value= value)
            else:
                current_node.right = Node(value, current_node, 'red')
                return current_node.right

    def rebalance(self, node):
        # Case 1 changing the parent color to black, (Skip)
        if node.parent is None:
            return
        # Case 2 make sure the insertion keeps number of black nodes per path.
        if node.parent.color == 'black':
            return

        # Case 3 parent and parent's sibling are red
        parent_sibling = node.parent.parent.right if node.parent.parent.left is node.parent else node.parent.parent.left
        if node.parent.color == 'red' and parent_sibling.color == 'red':
            node.parent.parent.left.color   = 'black'
            node.parent.parent.right.color  = 'black'
            node.parent.parent.color        = 'red'
            self.rebalance(node.parent.parent)

        # Case 4 
        if node.parent.color == 'red' and parent_sibling.color == 'black':
            # Case 4 inserted node on the right of the parent
            if node.parent.right is node:
                node.left, node.par