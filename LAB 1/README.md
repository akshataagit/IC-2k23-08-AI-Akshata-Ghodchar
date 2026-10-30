
# Experiment 2: Water Jug Problem

## Aim
To implement the Water Jug Problem using Python
and solve it using Breadth-First Search (BFS).

## Introduction
The Water Jug Problem is a classical Artificial
Intelligence problem based on State Space Search.

We are given two jugs of different capacities and
an unlimited water supply. The objective is to
measure a specific quantity of water using the
available jugs.

## Problem Statement
Given two water jugs of capacities 4 litres and
3 litres, measure exactly 2 litres of water.

## Operations
The following operations can be performed:

1. Fill Jug 1 completely.
2. Fill Jug 2 completely.
3. Empty Jug 1.
4. Empty Jug 2.
5. Pour water from Jug 1 into Jug 2.
6. Pour water from Jug 2 into Jug 1.

## Algorithm
1. Initialize both jugs with zero water.
2. Create a queue and insert the initial state.
3. Maintain a visited set to avoid repeated states.
4. Remove a state from the queue.
5. Check whether either jug contains the target amount.
6. If the target is not achieved, generate all
   possible states using the six operations.
7. Add unvisited states to the queue.
8. Repeat until the target is achieved or the
   queue becomes empty.
9. Display the solution path.

## Python Concepts Used
- Functions
- Tuples
- Sets
- Lists
- Queue
- Breadth-First Search (BFS)
- State Space Search

## How to Execute

Run the following command:

```bash
python Experiment2.py
```

## Expected Output

```text
Solution Found!
Steps:
(0, 0)
(4, 0)
(1, 3)
(1, 0)
(0, 1)
(4, 1)
(2, 3)
```

## Result
The Water Jug Problem was successfully implemented
using Python and Breadth-First Search.

The program successfully measures exactly 2 litres
of water using 4-litre and 3-litre jugs.

## Time and Space Complexity
Let C1 and C2 represent the capacities of the two jugs.

Number of possible states = (C1 + 1) * (C2 + 1).

Time Complexity: O(C1 * C2)

Space Complexity: O(C1 * C2)
