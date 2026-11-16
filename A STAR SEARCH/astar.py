
def astar(graph, heuristic, start, goal):

    open_list = [start]
    closed_list = set()

    g = {start: 0}
    parent = {}

    while open_list:

        current = min(open_list,
                      key=lambda node: g[node] + heuristic[node])

        if current == goal:
            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path, g[goal]

        open_list.remove(current)
        closed_list.add(current)

        for neighbor, cost in graph[current].items():

            if neighbor in closed_list:
                continue

            new_cost = g[current] + cost

            if neighbor not in g or new_cost < g[neighbor]:

                g[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None, float('inf')


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 3},
    'E': {'G': 5},
    'F': {'G': 2},
    'G': {}
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 4,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

path, cost = astar(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")
