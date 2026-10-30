
def hill_climbing(graph, heuristic, start, goal):

    current = start
    path = [current]

    while current != goal:

        neighbors = graph[current]

        if not neighbors:
            print("Goal not found!")
            return

        # Select neighbor with minimum heuristic
        next_node = min(
            neighbors,
            key=lambda node: heuristic[node]
        )

        # Check whether improvement is possible
        if heuristic[next_node] >= heuristic[current]:
            print("Local Maximum/Minimum reached!")
            print("Path:", " -> ".join(path))
            return

        current = next_node
        path.append(current)

    print("Goal Found!")
    print("Path:", " -> ".join(path))


# Graph representation
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'G': 0
}

hill_climbing(graph, heuristic, 'S', 'G')
