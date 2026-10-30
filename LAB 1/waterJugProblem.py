
from collections import deque

def water_jug(capacity1, capacity2, target):

    # Initial state: both jugs are empty
    start = (0, 0)

    # Queue for BFS
    queue = deque([(start, [])])

    # Visited states
    visited = set()

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Skip already visited states
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Store current state
        current_path = path + [(jug1, jug2)]

        # Check whether target is achieved
        if jug1 == target or jug2 == target:
            print("Solution Found!")
            print("Steps:")
            for state in current_path:
                print(state)
            return

        # Generate all possible operations

        # 1. Fill Jug 1
        queue.append(((capacity1, jug2), current_path))

        # 2. Fill Jug 2
        queue.append(((jug1, capacity2), current_path))

        # 3. Empty Jug 1
        queue.append(((0, jug2), current_path))

        # 4. Empty Jug 2
        queue.append(((jug1, 0), current_path))

        # 5. Pour Jug 1 into Jug 2
        transfer = min(jug1, capacity2 - jug2)
        queue.append(((jug1 - transfer, jug2 + transfer),
                      current_path))

        # 6. Pour Jug 2 into Jug 1
        transfer = min(jug2, capacity1 - jug1)
        queue.append(((jug1 + transfer, jug2 - transfer),
                      current_path))

    print("No solution exists!")


# Main program
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug(jug1_capacity, jug2_capacity, target)
