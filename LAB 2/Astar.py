
import heapq

def a_star(graph, heuristic, start, goal):

    # Priority queue: (f_cost, g_cost, node, path)
    pq = [(heuristic[start], 0, start, [start])]

    # Minimum actual cost to reach each node
    g_score = {start: 0}

    while pq:

        f, g, node, path = heapq.heappop(pq)

        # Skip outdated entries
        if g > g_score.get(node, float('inf')):
            continue

        if node == goal:
            print("Goal Found!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        for neighbor, cost in graph[node]:

            new_g = g + cost

            if new_g < g_score.get(neighbor, float('inf')):

                g_score[neighbor] = new_g

                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor,
                     path + [neighbor])
                )

    print("Goal not found!")


# Weighted graph
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 5)],
    'D': [('G', 3)],
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

a_star(graph, heuristic, 'S', 'G')
