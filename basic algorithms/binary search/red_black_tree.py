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
        self.rebalance(inserted_node)

    def search(self, value):
        return False


    def insert_node_to_tree(self, current_node, value):
        if current_node.value > value:
            if current_node.left:
                return self.insert_node_to_tree(current_node= current_node.left, value= value)
            else:
                current_node.left = Node(value, current_node, 'red')
                return current_node.left
        else:
            if current_node.right:
                return self.insert_node_to_tree(current_node= current_node.right, value= value)
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
        if node.parent.parent is None: # No sblings
            return
        parent_sibling = node.parent.parent.right if node.parent.parent.left is node.parent else node.parent.parent.left
        if node.parent.color == 'red' and (parent_sibling is not None and parent_sibling.color == 'red'):
            node.parent.parent.left.color   = 'black'
            node.parent.parent.right.color  = 'black'
            node.parent.parent.color        = 'red'
            self.rebalance(node.parent.parent)

        # Case 4/5
        if node.parent.color == 'red' and (parent_sibling is None or parent_sibling.color == 'black'):
            # Case 4 inserted node is opposite of parent node (right-left) or (left-right)
            if node.parent.right is node and node.parent.parent.left is node.parent:
                # left rotation
                print('case 4: left rotation')
                #(1) update nodes' parents,
                #(2) update leafs
                print(node.parent.value, 'value last')

                node.parent.right, node.left, node.parent.parent.left, node.parent.parent,  node.parent = None, node.parent, node, node, node.parent.parent
                node = node.left
                print(node.value, 'value last')
            if node.parent.left is node and node.parent.parent.right is node.parent:
                # right rotation
                print('case 4: right rotation')
                node.parent.left, node.parent.parent.right, node.right, node.parent.parent, node.parent =  None, node, node.parent,node, node.parent.parent
                node = node.right
            # Case 5 two red nodes on a path
            if node.parent.right is node and node.parent.parent.right is node.parent:
                print('case 5: one path rotation right')
                # Swap color
                node.parent.color, node.parent.parent.color = node.parent.parent.color, node.parent.color
                if node.parent.parent.parent.right is node.parent.parent:
                    node.parent.parent.parent.right = node.parent
                else:
                    node.parent.parent.parent.left = node.parent


                node.parent.left, node.parent.parent.right, node.parent.parent.parent, node.parent.parent = node.parent.parent, None, node.parent, node.parent.parent.parent

            if node.parent.left is node and node.parent.parent.left is node.parent:
            
                # Swap color
                node.parent.color, node.parent.parent.color = node.parent.parent.color, node.parent.color

                if node.parent.parent.parent.left is node.parent.parent:
                    node.parent.parent.parent.left = node.parent
                else:
                    node.parent.parent.parent.right = node.parent

                node.parent.right, node.parent.parent.left, node.parent.parent.parent, node.parent.parent = node.parent.parent, None, node.parent,  node.parent.parent.parent


def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node.value, node.color)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)

tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)
print_tree(tree.root)

tree.insert(13)
print_tree(tree.root)
tree.insert(16)
print_tree(tree.root)


