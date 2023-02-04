
class Node:
    def __init__(self, value):
        self.visited    = False
        self.value      = value
        self.children   = []

    def add_child(self, node):
        self.children.append(node)

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def add_edge(self, node1, node2):
        node1.add_child(node2)
        node2.add_child(node1)

def detect3CycledNodes(graph):
    stack = []
    stack.append(graph.nodes[0])

    while len(stack) > 0:
        node = stack.pop()
        node.visited = True


        for child_node in node.children:
            if not child_node.visited:
                stack.append(child_node)
            else:
                # case(2): loop, check 3 cycle loop.

                for node_i in node.children:
                    for child_node_i in child_node.children:
                        if node_i is child_node_i:
                            return [node_i, node, child_node]
    return None





node0   = Node(0)
node1   = Node(1)
node2   = Node(2)
node3   = Node(3)
node4   = Node(4)

nodes = [node0, node1, node2, node3, node4]

graph = Graph(nodes= nodes)
graph.add_edge(node3, node4)
graph.add_edge(node0, node3)
graph.add_edge(node1, node0)
graph.add_edge(node1, node2)
graph.add_edge(node1, node4)
#graph.add_edge(node2, node0)

out = detect3CycledNodes(graph= graph)

if out is None:
    print('-1')
else:
    print(len(out[0].children) + len(out[1].children) + len(out[2].children) - 6)



