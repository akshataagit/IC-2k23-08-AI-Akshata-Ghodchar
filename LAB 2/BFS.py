
from collections import deque

def bfs(graph, start, goal):

    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == goal:
            print("Goal Found!")
            print("Path:", " -> ".join(path))
            print("Path Length:", len(path) - 1)
            return

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)

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

bfs(graph, 'S', 'G')
