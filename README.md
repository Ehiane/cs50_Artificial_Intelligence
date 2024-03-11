# Data Structure and Algorithms in AI

This repository contains implementations of various data structures and algorithms used in Artificial Intelligence, focusing on search problems and agent behavior.

## Overview

The key concepts covered in this repository include:

- **Agent:** An entity that perceives its environment and acts upon it.
- **State:** A configuration of the agent and its environment.
- **Initial State:** The state where the agent begins.
- **Actions:** Choices that can be made in a state.
- **Transition Model:** Describes what state results from performing any action in any state.
- **State Space:** The set of all states reachable from the initial state by any sequence of actions.
- **Goal Test:** A way to determine whether a given state is a goal state.
- **Path Cost:** Numerical cost associated with a given path.
- **Solution:** A sequence of actions that leads from the initial state to a goal state.
- **Optimal Solution:** A solution with the lowest path cost among all solutions.

## Algorithms

The repository explores the following algorithms:

- **Depth First Search (DFS):** Explores the deepest node in a data structure first.
- **Breadth First Search (BFS):** Explores the shallowest node in a data structure first.

- **Uninformed search**: search strategy that uses no problem specific knowledege to find solutions to a problem. For example BFS and DFS.

- **Informed search**: search strategy that uses problem specific knowledege to find solutions more efficiently. e.g. : 
    * **greedy best-first search(gBFS)**: search algorithm that expands the mode that is closest to the goal, as estimated by a heuristic function h(n), where heuristic means estimation to goal, like the  
    
        * **Manhatten distance**: how many squares, horizontally and vertically would it take to reach the goal (while relaxing the problem). 
    
    * **A-star Search**: search algorithm that expands node with lowest value of g(n) + h(n) 

        g(n) = cost to reach node,
        h(n) = estimated cost to goal 
        A-star is optimal if:

            - h(n) is admissible (never overestimates the true cost), and,
            - h(n) is consistent (for every node n and successor n' with step cost c, h(n) <= h(n') + c)




## Program Approach

1. Start with a frontier that contains the initial state.
2. Start with an empty explored set.
3. Repeat:
    - If the frontier is empty, then no solution.
    - Remove a node from the frontier.
    - If the node contains the goal state, return the solution.
    - Add the node to the explored set to avoid duplicates.
    - Expand the node (i.e., look at all the neighbors of the node), add resulting nodes to the frontier if they aren't in the frontier or explored set.

## Additional Resources

- [YouTube Video Explanation](https://youtu.be/5NgNicANyqM?si=_HmYupuEek5eGLDw&t=4322)
- [Link to course materials](https://cs50.harvard.edu/ai/2020/weeks/)

## Notes

- The data structure being used is a node.
- The state can be represented as a 5x5 matrix, either empty or initialized with zeros.
