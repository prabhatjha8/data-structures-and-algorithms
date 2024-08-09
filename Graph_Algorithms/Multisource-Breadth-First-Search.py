from collections import deque

# The nodes of the graph is 0 indexed i.e 0, 1, 2,  . . . , n-1
# and the adjacencyList has n items (n lists) ith corresponding
# to ith node. The functions takes as input a list of source nodes 
# and the adjacencyList and output a dictionary containing list 
# indicating visited nodes, distance and parent based on BFS traversal

def Multisource_BFS(sources, adjacencyList):
    n = len(adjacencyList)

    visited = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance = [-1 for _ in range(n)]
    queue = deque()
    queLen = 0

    # initialization
    for source in sources:
        visited[source] = 1
        distance[source] = 0
        queue.append(source)
        queLen += 1

    while queLen != 0:
        u = queue.popleft()
        queLen -= 1
        for v in adjacencyList[u]:
            if visited[v] == -1:
                visited[v] = 1
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.append(v)
                queLen += 1

    return {"visited":visited, "distance": distance, "parent": parent}
