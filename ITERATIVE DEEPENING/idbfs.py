
def depth_limited_search(graph, node, goal, depth, visited):

    print(node, end=" ")

    if node == goal:
        return True

    if depth <= 0:
        return False

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            if depth_limited_search(
                graph, neighbor, goal, depth - 1, visited
            ):
                return True

    return False


def iddfs(graph, start, goal, max_depth):

    for depth in range(max_depth + 1):

        print("\nDepth Limit:", depth)
        visited = set()

        if depth_limited_search(
            graph, start, goal, depth, visited
        ):
            print("\nGoal Found!")
            return True

    print("\nGoal Not Found!")
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'F'
max_depth = 3

iddfs(graph, start, goal, max_depth)
