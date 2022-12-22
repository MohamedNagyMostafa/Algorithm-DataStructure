from collections import deque
from search_tree_bfs import Queue

class Node:
    def __init__(self, value = None):
        self.value  = value
        self.left   = None
        self.right  = None
        self.parent = None

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

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return f"Node({self.value})"

class Tree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert_with_loop(self, value):
        node = Node(value= value)
        if self.root is None:
            self.root = node
            return

        curr_node = self.root
        while True:
            if curr_node.value < node.value:
                if curr_node.get_right_child() is not None:
                    curr_node = curr_node.get_right_child()
                else:
                    node.set_parent(curr_node)
                    curr_node.set_right_child(node)
                    break
            elif curr_node.value > node.value:
                if curr_node.get_left_child() is not None:
                    curr_node = curr_node.get_left_child()
                else:
                    node.set_parent(curr_node)
                    curr_node.set_left_child(node)
                    break
            else:
                break

    def insert_with_rec(self, value, node: Node):
        if value < node.value:
            if node.get_left_child() is None:
                node_to_insert = Node(value)
                node_to_insert.parent = node
                print(f'Insert Node({node_to_insert.value}) to left of Node({node.value}) with parent Node({node_to_insert.parent})')
                node.set_left_child(node_to_insert)
                return node.get_left_child()
            else:
                return self.insert_with_rec(value, node.get_left_child())

        elif value > node.value:
            if node.get_right_child() is None:
                node_to_insert = Node(value)
                node_to_insert.parent = node
                node.set_right_child(node_to_insert)
                #node.get_right_child().set_parent(node)
                print(f'Insert Node({node_to_insert.value}) to right of Node({node.value}) with parent Node({node_to_insert.parent})')
                return node.get_right_child()
            else:
                return self.insert_with_rec(value, node.get_right_child())
        else:
            return node

    def insert_with_recursion(self, value: int):
        if self.root is None:
            self.root = Node(value)
            return

        return self.insert_with_rec(value, self.root)

    def search_with_rec(self, value, node):
        # Check current value, yes return
        if node is None:
            return None

        if node.value == value:
            return node
        else:
            if value < node.value:
                return self.search_with_rec(value, node.get_left_child())
            else:
                return self.search_with_rec(value, node.get_right_child())


    def search(self, value):
        return self.search_with_rec(value, self.root)


    def get_next_smallest_node(self, node):
        if node.has_left_child():
            return self.get_next_smallest_node(node.get_left_child())

        return node

    def delete_node(self, value):
        # search for the node
        node = self.search_with_rec(value= value, node= self.root)
        if node is None:
            return None

        # no leaf case
        if int(node.has_left_child()) + int(node.has_right_child()) == 0:
            assert self.remove_node(node= node), f"Expected node {node.value} to be exist after parent {node.parent.value}, but it is not"
            print(f'Case (1): Node({node.value}) with no leaf exist, remove Node({node.value}) from parent Node({node.parent.value}).')
            return node

        # one leaf case
        elif int(node.has_left_child()) + int(node.has_right_child()) == 1:
            if node.has_left_child():
                if node.parent.get_left_child().value == node.value:
                    node.parent.set_left_child(node.get_left_child())
                    print(f'Case (2): Node({node.value}) with one leaf, remove Node({node.value}) from parent Node({node.parent.value}).')
                    return node
                elif node.parent.get_right_child().value == node.value:
                    node.parent.set_right_child(node.get_left_child())
                    print(f'Case (2): Node({node.value}) with one leaf, remove Node({node.value}) from parent Node({node.parent.value}).')
                    return node
                else:
                    assert f"Parent Node({node.parent.value}) doesn't have node equals the target Node({node.value})"
                    return None
            elif node.has_right_child():
                if node.parent.get_left_child().value == node.value:
                    node.parent.set_left_child(node.get_right_child())
                    print(f'Case (2): Node({node.value}) with one leaf, remove Node({node.value}) from parent Node({node.parent.value}).')
                    return node
                elif node.parent.get_right_child().value == node.value:
                    node.parent.set_right_child(node.get_right_child())
                    print(f'Case (2): Node({node.value}) with one leaf, remove Node({node.value}) from parent Node({node.parent.value}).')
                    return node
                else:
                    assert f"Parent Node({node.parent.value}) doesn't have node equals the target Node({node.value})"
                    return None
            else:
                assert f"Node({node.value}) doesn't have either left or right node!"
                return None

        # two leaf
        elif int(node.has_left_child()) + int(node.has_right_child()) == 2:
            # Search for next smallest node in subtree
            next_smallest_node = self.get_next_smallest_node(node= node.get_right_child())
            print(f'Found next smallest Node({next_smallest_node.value}) of subtree Node({node.value}), of parent Node({next_smallest_node.parent})')
            print('delete the smallest node')

            assert self.delete_node(value=next_smallest_node.value) is not None, f"Failed to delete the smallest Node({next_smallest_node.value}) from the subtree"
            print('the smallest node successfully deleted')
            next_smallest_node.set_left_child(None)
            next_smallest_node.set_right_child(None)
            next_smallest_node.set_parent(None)

            print(f'Replace Node({node.value}) with Node({next_smallest_node.value})')
            if node.parent.has_left_child() and node.parent.get_left_child().value == node.value:
                # Associate the node to parent
                node.parent.set_left_child(next_smallest_node)
                # Connect the node to left child
                next_smallest_node.set_left_child(node.get_left_child())
                print(f'Case (3): Node({node.value}) with one leaf, remove Node({node.value}) from parent Node({node.parent.value}).')

                return node
            elif node.parent.has_right_child() and node.parent.get_right_child().value == node.value:
                # Associate the node to parent
                node.parent.set_right_child(next_smallest_node)
                # Connect the node to left child
                next_smallest_node.set_left_child(node.get_left_child())
                print(f'Case (3): Node({node.value}) with one leaf, remove Node({node.value}) from parent Node({node.parent.value}).')

                return node

            else:
                assert f"Didn't find Node({node.value}) as a child of Node({node.parent.value})"
                return None

        else:
            assert f"Three cases of node deletion are failed!"
            return None

    def remove_node(self, node):
        if node.parent.has_left_child() and node.parent.get_left_child().value == node.value:
            node.parent.set_left_child(None)
            return True
        elif node.parent.has_right_child() and node.parent.get_right_child().value == node.value:
            node.parent.set_right_child(None)
            return True
        else:
            return False

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enqueue((node, level))
        while (q.size() > 0):
            node, level = q.dequeue()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enqueue((node.get_left_child(), level + 1))
            else:
                q.enqueue((None, level + 1))

            if node.has_right_child():
                q.enqueue((node.get_right_child(), level + 1))
            else:
                q.enqueue((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s




tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(3)
tree.insert_with_recursion(2)
tree.insert_with_recursion(1)
node = tree.insert_with_recursion(4)
print(tree)
tree.delete_node(3)
print(tree)

