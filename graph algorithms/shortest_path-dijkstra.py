'''
# pick node from stack (print), mark visited
# re-call children
'''
from queue import PriorityQueue

class GraphEdge:

    def __init__(self, node, weight):
        self.node   = node
        self.weight = weight

class GraphNode:

    def __init__(self, val):
        self.value      = val
        self.distance   = float('inf')
        self.children   = []
        self.visited    = False

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __le__(self, other):
        return self.distance <= other.distance

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes

    def add_edge(self, node1, node2, weight):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(GraphEdge(node= node2, weight= weight))
            node2.add_child(GraphEdge(node= node1, weight= weight))


def dijkstra_algorithm(queue, target):
    if queue.empty():
        return None

    curr_node = queue.get()
    curr_node.visited = True

    print(f'Visited Node({curr_node.value}) with shortest cost {curr_node.distance}')
    if curr_node.value == target:
        return curr_node.distance

    for edge in curr_node.children:
        if not edge.node.visited:
            curr_path_cost = curr_node.distance + edge.weight
            if edge.node.distance > curr_path_cost:
                edge.node.distance = curr_path_cost

            queue.put(edge.node)

    return dijkstra_algorithm(queue= queue, target= target)

def shortest_path(initial_node, target):
    queue = PriorityQueue()

    initial_node.distance   = 0

    queue.put(initial_node, target)

    return dijkstra_algorithm(queue, target)

nodeA   = GraphNode('A')
nodeU   = GraphNode('U')
nodeD   = GraphNode('D')
nodeI   = GraphNode('I')
nodeC   = GraphNode('C')
nodeY   = GraphNode('Y')
nodeT   = GraphNode('T')

graph = Graph([nodeA, nodeU, nodeD, nodeI, nodeC, nodeY, nodeT])

graph.add_edge(nodeA, nodeU, 4)
graph.add_edge(nodeA, nodeI, 7)
graph.add_edge(nodeU, nodeC, 6)
graph.add_edge(nodeU, nodeD, 3)
graph.add_edge(nodeD, nodeC, 4)
graph.add_edge(nodeC, nodeI, 4)
graph.add_edge(nodeC, nodeT, 5)
graph.add_edge(nodeI, nodeY, 4)
graph.add_edge(nodeT, nodeY, 5)

print(f'The shortest path cost is ',shortest_path(initial_node= nodeU,target='Y'))