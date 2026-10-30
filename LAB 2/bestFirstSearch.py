
import heapq

def best_first_search(graph, heuristic, start, goal):

    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))

    visited = set()

    while priority_queue:

        h, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Goal Found!")
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[node]:

            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor],
                     neighbor,
                     path + [neighbor])
                )

    print("Goal not found!")


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

best_first_search(graph, heuristic, 'S', 'G')
