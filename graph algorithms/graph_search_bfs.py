'''
# pick node from stack (print), mark visited
# re-call children
'''

class GraphNode:

    def __init__(self, val):
        self.value      = val
        self.children   = []
        self.visited    = False

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

def bfs_rec(queue):
    if len(queue) == 0:
        return
    curr_node = queue.pop(0)
    print(f'Visit Node({curr_node.value})')

    for node in curr_node.children:
        if not node.visited:
            node.visited = True
            queue.append(node)
    bfs_rec(queue)

def graph_search_bfs(initial_node):
    queue = []
    initial_node.visited = True
    queue.append(initial_node)
    bfs_rec(queue)


nodeG   = GraphNode('G')
nodeR   = GraphNode('R')
nodeH   = GraphNode('H')
nodeP   = GraphNode('P')
nodeS   = GraphNode('S')
nodeA   = GraphNode('A')

nodes = [nodeG, nodeR, nodeH, nodeP, nodeS, nodeA]

graph = Graph(nodes= nodes)

graph.add_edge(node1= nodeG, node2= nodeH)
graph.add_edge(node1= nodeR, node2= nodeP)
graph.add_edge(node1= nodeH, node2= nodeP)
graph.add_edge(node1= nodeG, node2= nodeA)
graph.add_edge(node1= nodeR, node2= nodeA)
graph.add_edge(node1= nodeG, node2= nodeR)
graph.add_edge(node1= nodeR, node2= nodeS)


graph_search_bfs(initial_node=nodeG)