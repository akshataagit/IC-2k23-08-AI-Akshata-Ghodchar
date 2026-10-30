
# Experiment 3: Breadth-First Search (BFS)

## Aim
To implement Breadth-First Search using Python
to find a path between the start node and goal node.

## Introduction
Breadth-First Search is an uninformed search
algorithm used in Artificial Intelligence.

It explores all neighboring nodes at the current
level before moving to the next level.

BFS uses a Queue data structure following
the FIFO (First In First Out) principle.

## Algorithm
1. Initialize a queue with the start node.
2. Create an empty visited set.
3. Remove the first path from the queue.
4. Check whether the last node is the goal.
5. If the goal is found, display the path.
6. Otherwise, mark the node as visited.
7. Add all unvisited neighboring nodes to the queue.
8. Repeat until the goal is found or the queue is empty.

## Data Structure Used
Queue (FIFO)

## Time Complexity
O(V + E)

## Space Complexity
O(V)

Where:
V = Number of vertices
E = Number of edges

## Execution
python Experiment3.py

## Expected Output
Goal Found!
Path: S -> A -> C -> G
Path Length: 3

## Result
Breadth-First Search was successfully implemented
using Python and the path to the goal node was found.





# Experiment 4: Depth-First Search (DFS)

## Aim
To implement Depth-First Search using Python
to find a path from the start node to the goal node.

## Introduction
Depth-First Search is an uninformed search
algorithm used in Artificial Intelligence.

It explores one branch completely before
backtracking and exploring another branch.

DFS uses a Stack (LIFO) or recursion.

## Algorithm
1. Start from the initial node.
2. Mark the current node as visited.
3. Add the current node to the path.
4. Check whether the current node is the goal.
5. If the goal is found, return the path.
6. Otherwise, visit an unvisited neighboring node.
7. If no path is found, backtrack.
8. Continue until the goal is found or all nodes
   have been explored.

## Data Structure Used
Stack / Recursion

## Time Complexity
O(V + E)

## Space Complexity
O(V)

Where:
V = Number of vertices
E = Number of edges

## Execution
python Experiment4.py

## Expected Output
Goal Found!
Path: S -> A -> C -> G
Path Length: 3

## Result
Depth-First Search was successfully implemented
using Python to find the path to the goal node.




# Experiment 6: Best First Search

## Aim
To implement Best First Search using Python
to find the path from the initial node to the goal.

## Introduction
Best First Search is an informed search algorithm
that uses heuristic information to select
the most promising node.

It selects the node having the lowest heuristic
value from the priority queue.

## Algorithm
1. Initialize a priority queue with the start node.
2. Assign the heuristic value to the start node.
3. Remove the node with the lowest heuristic value.
4. Check whether it is the goal node.
5. If the goal is found, display the path.
6. Otherwise, mark the node as visited.
7. Insert its unvisited neighbors into the
   priority queue with their heuristic values.
8. Repeat until the goal is found or the queue
   becomes empty.

## Data Structure Used
Priority Queue (Min Heap)

## Evaluation Function
f(n) = h(n)

Where:
h(n) = Estimated cost from node n to goal.

## Time Complexity
O((V + E) log V) with a heap-based implementation.

## Space Complexity
O(V + E)

## Execution
python Experiment6.py

## Expected Output
Goal Found!
Path: S -> B -> D -> G

## Result
Best First Search was successfully implemented
using Python and heuristic values.





# Experiment 7: A* Search Algorithm

## Aim
To implement the A* Search algorithm using Python
to find the optimal path from the start node
to the goal node.

## Introduction
A* is an informed search algorithm used in
Artificial Intelligence.

It combines the actual path cost and estimated
remaining cost to select the most promising node.

A* uses a priority queue to explore nodes
according to their evaluation function.

## Evaluation Function

f(n) = g(n) + h(n)

Where:
g(n) = Actual cost from start to current node.
h(n) = Estimated cost from current node to goal.
f(n) = Total estimated cost.

## Algorithm
1. Initialize a priority queue with the start node.
2. Set the actual cost of the start node to zero.
3. Calculate the evaluation function f(n).
4. Remove the node with the lowest f(n).
5. Check whether the current node is the goal.
6. If the goal is found, display the path and cost.
7. Otherwise, calculate the cost of each neighbor.
8. Update the cost if a better path is found.
9. Insert the updated node into the priority queue.
10. Repeat until the goal is found or the queue
    becomes empty.

## Data Structure Used
Priority Queue (Min Heap)

## Time Complexity
O((V + E) log V) with a heap-based implementation.

## Space Complexity
O(V + E)

## Execution
python Experiment7.py

## Expected Output
Goal Found!
Path: S -> B -> D -> G
Total Cost: 8

## Result
A* Search was successfully implemented using
Python to find the lowest-cost path from the
start node to the goal node.
