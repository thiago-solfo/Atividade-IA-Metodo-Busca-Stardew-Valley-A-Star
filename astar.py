from heapq import heappop, heappush

def a_star_search(graph: dict, start: str, goal: str, heuristic_values: dict):
    '''
    A* search algorithm implementation.

    @param graph: The graph to search.
    @param start: The starting node.
    @param goal: The goal node.
    @param heuristic_values: The heuristic values for each node. The goal node must be admissible, and the heuristic value must be 0.
    @return: The path cost from the start node to the goal node.
    '''

    # A min heap is used to implement the priority queue for the open list.
    # The heapq module from Python's standard library is utilized.
    # Entries in the heap are tuples of the form (cost, node), ensuring that the entry with the lowest cost is always smaller during comparisons.
    # The heapify operation is not required, as the heapq module maintains the heap invariant after every push and pop operation.

    # The closed list is implemented as a set for efficient membership checking.

    open_list, closed_list = [(heuristic_values[start], start)], set()

    came_from = {}
    
    while open_list:
        cost, node = heappop(open_list)

        # The algorithm ends when the goal node has been explored, NOT when it is added to the open list.
        if node == goal:
            path = [node]
            while node in came_from:
                node = came_from[node]
                path.append(node)
            path.reverse()
            
            return cost, path

        if node in closed_list:
            continue

        closed_list.add(node)

        # Subtract the heuristic value as it was overcounted.
        cost -= heuristic_values[node]

        for neighbor, edge_cost in graph[node]:
            if neighbor in closed_list:
                continue

            # f(x) = g(x) + h(x), where g(x) is the path cost and h(x) is the heuristic.
            neighbor_cost = cost + edge_cost + heuristic_values[neighbor]

            came_from[neighbor] = node
            
            heappush(open_list, (neighbor_cost, neighbor))

    return -1, []  # No path found


def a_star_with_checkpoints(graph: dict, start: str, goal: str, checkpoints: list, heuristic_values: dict):
    '''
    A* with optional checkpoints (0, 1 or 2 checkpoints).

    @param checkpoints: List of optional checkpoints.
    @return: Best path considering all possibilities.
    '''

    best_cost = float('inf')
    best_path = []

    # Paths with one checkpoint
    for cp in checkpoints:
        c1, p1 = a_star_search(graph, start, cp, heuristic_values)
        c2, p2 = a_star_search(graph, cp, goal, heuristic_values)

        if -1 not in (c1, c2):
            total_cost = c1 + c2
            full_path = p1 + p2[1:]

            if total_cost < best_cost:
                best_cost, best_path = total_cost, full_path

    # Paths with two checkpoints (both orders)
    if len(checkpoints) == 2:
        cp1, cp2 = checkpoints

        best_cost = float('inf')
        best_path = []

        # cp1 -> cp2
        c1, p1 = a_star_search(graph, start, cp1, heuristic_values)
        c2, p2 = a_star_search(graph, cp1, cp2, heuristic_values)
        c3, p3 = a_star_search(graph, cp2, goal, heuristic_values)

        if -1 not in (c1, c2, c3):
            total_cost = c1 + c2 + c3
            full_path = p1 + p2[1:] + p3[1:]

            best_cost, best_path = total_cost, full_path

        # cp2 -> cp1
        c1, p1 = a_star_search(graph, start, cp2, heuristic_values)
        c2, p2 = a_star_search(graph, cp2, cp1, heuristic_values)
        c3, p3 = a_star_search(graph, cp1, goal, heuristic_values)

        if -1 not in (c1, c2, c3):
            total_cost = c1 + c2 + c3
            full_path = p1 + p2[1:] + p3[1:]

            if total_cost < best_cost:
                best_cost, best_path = total_cost, full_path

        return best_cost, best_path

GRAPH = {
    'Casa': [('Montanha', 27), ('Onibus', 11), ('Floresta', 23)],
    'Montanha': [('Casa', 27), ('Spa', 8), ('Lago', 32), ('Cidade', 26)],
    'Onibus': [('Casa', 11), ('Cidade', 19)],
    'Floresta': [('Casa', 23), ('Cidade', 33), ('Praia', 34)],
    'Spa': [('Montanha', 8)],
    'Lago': [('Montanha', 32)],
    'Cidade': [('Montanha', 26), ('Onibus', 19), ('Floresta', 33), ('Praia', 30)],
    'Praia': [('Cidade', 30), ('Floresta', 34)]
}

# Node heuristic values (admissible heuristic values for the nodes)
HEURISTIC = {
    'Casa': 0,
    'Montanha': 0,
    'Onibus': 0,
    'Floresta': 0,
    'Spa': 0,
    'Lago': 0,
    'Cidade': 0,
    'Praia': 0
}

cost, path = a_star_with_checkpoints(
    GRAPH,
    'Casa',
    'Praia',
    ['Spa', 'Lago'],  # Can be [], 1 or 2 checkpoints
    HEURISTIC
)

print(f"Custo: {cost}")
print(f"Caminho: {' -> '.join(path)}")