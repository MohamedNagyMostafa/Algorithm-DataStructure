import heapq

def min_bridge_connection_cost(bridges, num_island):
    graph = [ [] for _ in range(num_island)]

    # Graph representation
    for bridge in bridges:
        heapq.heappush(graph[bridge[0] - 1], (bridge[2], bridge[1]))
        heapq.heappush(graph[bridge[1] - 1], (bridge[2], bridge[0]))

    total_cost          = 0
    current_connection  = [(0, 1)]
    visited             = []

    while len(current_connection) > 0:
        edge = heapq.heappop(current_connection)

        if edge[1] in visited:
            continue
        else:
            visited.append(edge[1])
            total_cost += edge[0]
            [heapq.heappush(current_connection, (cost, child)) for cost, child in graph[edge[1] - 1]]

    return  total_cost

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]

cost = min_bridge_connection_cost(bridges= bridge_config, num_island= num_islands)
assert cost == 6
print(f'The least connection cost is : {cost}')

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]

cost = min_bridge_connection_cost(bridges= bridge_config, num_island= num_islands)
assert cost == 13
print(f'The least connection cost is : {cost}')

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]

cost = min_bridge_connection_cost(bridges= bridge_config, num_island= num_islands)
assert cost == 31
print(f'The least connection cost is : {cost}')