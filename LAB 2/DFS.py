
def dfs(graph, start, goal):

    visited = set()
    path = []

    def search(node):

        visited.add(node)
        path.append(node)

        if node == goal:
            return True

        for neighbor in graph[node]:

            if neighbor not in visited:
                if search(neighbor):
                    return True

        path.pop()
        return False

    if search(start):
        print("Goal Found!")
        print("Path:", " -> ".join(path))
        print("Path Length:", len(path) - 1)
    else:
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

dfs(graph, 'S', 'G')
