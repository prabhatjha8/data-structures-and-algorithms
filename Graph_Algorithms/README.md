
Breadth-First Search (BFS) Algorithm
Overview
Breadth-First Search (BFS) is an algorithm used to traverse or search through graphs and trees. Starting from a source node, BFS explores all its 
neighboring nodes at the present depth level before moving on to nodes at the next depth level. This traversal method is particularly useful for finding 
the shortest path in unweighted graphs, as it guarantees that the shortest path to each node is found first.

BFS Algorithm Steps
Initialization:

Visited List: Keeps track of whether a node has been visited or not.
Parent List: Records the parent of each node in the traversal path.
Distance List: Stores the distance of each node from the source node.
Queue: A data structure to manage the nodes to be explored, following the FIFO (First In, First Out) principle.
Starting the Search:

Set the source node as visited and initialize its distance to 0.
Enqueue the source node into the queue.
Processing Nodes:

While the queue is not empty:
Dequeue a node from the front of the queue.
For each neighbor of this node:
If the neighbor has not been visited:
Mark it as visited.
Set its parent to the current node.
Update its distance.
Enqueue the neighbor.
Completion:

After processing all reachable nodes, return the results: lists of visited nodes, distances from the source, and parent nodes.


Multisource Breadth-First Search (BFS) Algorithm
Overview
Multisource Breadth-First Search (BFS) is an extension of the BFS algorithm designed to handle multiple source nodes simultaneously. Instead of starting 
the traversal from a single source, Multisource BFS begins from all given source nodes at the same time. This approach is particularly useful when you 
want to find the shortest distance from any of several sources to all other nodes in the graph.

Multisource BFS Algorithm Steps
Initialization:

Visited List: Keeps track of whether a node has been visited. Nodes are marked as visited when they are first encountered.
Parent List: Records the parent of each node in the traversal path.
Distance List: Stores the shortest distance from any source node to each node.
Queue: A data structure used to manage the nodes to be explored, following the FIFO (First In, First Out) principle.
Starting the Search:

Set all source nodes as visited and initialize their distances to 0.
Enqueue all source nodes into the queue.
Processing Nodes:

While the queue is not empty:
Dequeue a node from the front of the queue.
For each neighbor of this node:
If the neighbor has not been visited:
Mark it as visited.
Set its parent to the current node.
Update its distance.
Enqueue the neighbor.
Completion:

After processing all reachable nodes from all sources, return the results: lists of visited nodes, distances from the nearest source, and parent nodes¸.



Certainly! Here’s a detailed explanation and description for the README.md file for your DFS algorithm:

Depth-First Search (DFS) Algorithm
Depth-First Search (DFS) is a fundamental graph traversal technique that explores as far as possible along each branch before backtracking. This method 
is particularly useful for tasks such as pathfinding, cycle detection, and topological sorting.

Overview
The DFS algorithm traverses a graph or a tree structure by moving down to the deepest nodes before backtracking. This implementation assumes the graph 
is represented as an adjacency list, where each node has a list of its adjacent nodes.

Function Description
The DFS function performs a depth-first traversal of a graph starting from a given source node. The function takes two parameters:

source: The starting node for the DFS traversal. This is an integer representing the index of the source node in the adjacency list.
adjacencyList: A list of lists representing the graph. Each sublist contains the indices of adjacent nodes for a given node.
Output
The function returns a dictionary with the following keys:

visited: A list indicating the visitation status of each node. A value of 1 means the node has been visited, while -1 means it has not been visited.
parent: A list where each entry at index i contains the parent node of node i during the DFS traversal. The parent of the source node is set to -1.
pre: A list where each entry at index i contains the pre-order timestamp of node i. This timestamp is assigned when the node is first visited.
post: A list where each entry at index i contains the post-order timestamp of node i. This timestamp is assigned when the node has finished exploring 
all its adjacent nodes.
Detailed Explanation
Initialization:

The number of nodes n is determined from the length of the adjacency list.
Four lists are initialized:
visited to keep track of whether each node has been visited.
parent to record the parent of each node in the DFS tree.
pre to store the pre-order timestamps of nodes.
post to store the post-order timestamps of nodes.
A counter count is used to generate the timestamps for pre-order and post-order visits.
DFS Traversal:

The traversal starts with the given source node. The node is marked as visited, and its pre-order timestamp is recorded.
The algorithm then recursively visits all adjacent nodes that have not been visited yet, updating their parent information.
After all adjacent nodes are explored, the node’s post-order timestamp is recorded.
The traversal continues until all reachable nodes have been explored.
Returning Results:

After completing the DFS traversal, the function returns a dictionary containing the visited, parent, pre, and post lists.
Use Cases
Pathfinding: DFS can be used to find a path between nodes in a graph.
Cycle Detection: DFS helps in detecting cycles in a graph by tracking the visitation status and parent nodes.
Topological Sorting: In directed acyclic graphs (DAGs), DFS is used for topological sorting of nodes.
Example
Given an adjacency list representing a graph, the DFS function performs a depth-first traversal starting from a specified source node and provides 
detailed traversal information.

Notes
The graph is assumed to be undirected. For directed graphs, the adjacency list should reflect the direction of edges.
The algorithm handles cyclic graphs and will correctly visit all nodes reachable from the source node.
This DFS implementation provides a comprehensive view of the traversal process and is useful for various graph-related tasks and algorithms.
