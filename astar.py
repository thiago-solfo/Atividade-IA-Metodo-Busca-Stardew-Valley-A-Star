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

    open_list = []
    heappush(open_list, (heuristic_values[start], start))
    closed_list = set()

    came_from = {}
    g_cost = {start: 0}
    
    while open_list:
        f_cost, node = heappop(open_list)

        # The algorithm ends when the goal node has been explored, NOT when it is added to the open list.
        if node == goal:
            path = [node]
            while node in came_from:
                node = came_from[node]
                path.append(node)
            path.reverse()
            
            return g_cost[goal], path

        if node in closed_list:
            continue

        closed_list.add(node)

        for neighbor, edge_cost in graph[node]:
            if neighbor in closed_list:
                continue

            new_g = g_cost[node] + edge_cost

            if new_g < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = new_g
                came_from[neighbor] = node
                
                # f(x) = g(x) + h(x)
                new_f = new_g + heuristic_values[neighbor]
                heappush(open_list, (new_f, neighbor))

    return -1, []  # No path found


def a_star_with_checkpoints(graph: dict, start: str, goal: str, checkpoints: list, heuristic_values: dict):
    '''
    A* with optional checkpoints (0, 1 or 2 checkpoints).

    @param checkpoints: List of optional checkpoints.
    @return: Best path considering all possibilities.
    '''

    if len(checkpoints) == 0:
        return a_star_search(graph, start, goal, heuristic_values)

    if len(checkpoints) == 1:
        cp = checkpoints[0]
        c1, p1 = a_star_search(graph, start, cp, heuristic_values)
        c2, p2 = a_star_search(graph, cp, goal, heuristic_values)
        
        if -1 in (c1, c2):
            return -1, []
        return c1 + c2, p1 + p2[1:]

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
            
            if total_cost < best_cost:
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

        if best_cost == float('inf'):
            return -1, []
            
        return best_cost, best_path

    return -1, []


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
    'Casa': 57,
    'Montanha': 56,
    'Onibus': 49,
    'Floresta': 34,
    'Spa': 64,
    'Lago': 88,
    'Cidade': 30,
    'Praia': 0
}

# os dias da semana comecam na segunda (dia 1 = segunda)
dias_semana = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']

def get_dia_semana(dia):
    return dias_semana[(dia - 1) % 7]

def get_local_npc(dia):
    # retorna onde cada npc esta naquele dia
    semana = get_dia_semana(dia)
    npcs = {}

    npcs['Anao'] = 'Montanha'

    if semana == 'Segunda':
        npcs['Abgail'] = 'Praia'
    elif semana == 'Quarta':
        npcs['Abgail'] = 'Cidade'
    elif semana == 'Sexta':
        npcs['Abgail'] = 'Cidade'
    elif semana == 'Sabado':
        npcs['Abgail'] = 'Floresta'
    else:
        npcs['Abgail'] = 'Desconhecido'

    npcs['Feiticeiro'] = 'Floresta'

    if semana == 'Segunda' or semana == 'Quarta' or semana == 'Sexta':
        npcs['Sam'] = 'Cidade'
    else:
        npcs['Sam'] = 'Praia'

    if dia == 17:
        npcs['George'] = 'Onibus'
    else:
        npcs['George'] = 'Cidade'

    if semana == 'Segunda' or semana == 'Terca' or semana == 'Quinta':
        npcs['Alex'] = 'Spa'
    else:
        npcs['Alex'] = 'Cidade'

    npcs['Marlon'] = 'Lago'

    return npcs

def get_checkpoints(dia):
    npcs = get_local_npc(dia)
    checkpoints = []

    if dia == 9:
        # Marlon so aparece no dia 9
        local = npcs['Marlon']
        print("Dia 9: precisa falar com Marlon, ele ta no " + local)
        checkpoints.append(local)

    elif dia == 13:
        # Abgail e Alex no dia 13
        local_abgail = npcs['Abgail']
        local_alex = npcs['Alex']
        print("Dia 13 (" + get_dia_semana(dia) + "): Abgail ta em " + local_abgail + " e Alex ta em " + local_alex)
        checkpoints.append(local_abgail)
        if local_alex != local_abgail:
            checkpoints.append(local_alex)

    elif dia == 17:
        # Feiticeiro e Sam no dia 17
        local_feit = npcs['Feiticeiro']
        local_sam = npcs['Sam']
        print("Dia 17 (" + get_dia_semana(dia) + "): Feiticeiro ta em " + local_feit + " e Sam ta em " + local_sam)
        checkpoints.append(local_feit)
        if local_sam != local_feit:
            checkpoints.append(local_sam)

    elif dia == 22:
        # Anao no dia 22
        local = npcs['Anao']
        print("Dia 22: precisa falar com o Anao, ele ta no " + local)
        checkpoints.append(local)

    elif dia == 24:
        # George no dia 24
        local = npcs['George']
        print("Dia 24: precisa falar com George, ele ta em " + local)
        checkpoints.append(local)

    else:
        print("Dia " + str(dia) + " (" + get_dia_semana(dia) + "): dia normal, sem npc pra visitar")

    return checkpoints

if __name__ == '__main__':
    print("=== A* - Caminho de Casa ate a Praia ===")

    try:
        dia_input = input("Qual dia é hoje? (1 a 28): ")
        dia = int(dia_input)
        while dia < 1 or dia > 28:
            dia_input = input("Digite um numero entre 1 e 28: ")
            dia = int(dia_input)
            
        print()
        checkpoints = get_checkpoints(dia)

        print("Checkpoints: " + str(checkpoints))
        print()

        cost, path = a_star_with_checkpoints(
            GRAPH,
            'Casa',
            'Praia',
            checkpoints,
            HEURISTIC
        )

        if cost == -1:
            print("Nao achou caminho!")
        else:
            print("Custo total: " + str(cost) + " min")
            print("Caminho: " + ' -> '.join(path))
    except ValueError:
        print("Entrada invalida. Execute novamente e digite um numero.")
