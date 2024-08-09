from collections import deque

# The nodes of the graph is 0 indexed i.e 0, 1, 2,  . . . , n-1
# and the adjacencyList has n items (n lists) ith corresponding
# to ith node. The functions takes as input the source node and
# the adjacencyList and output a dictionary containing list indicating
# visited nodes, distance and parent based on DFS traversal

def DFS(source, adjacencyList):

    n = len(adjacencyList)
    visited = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    pre = [-1 for _ in range(n)]
    post = [-1 for _ in range(n)]
    count = 0

    def dfs(node):
        visited[node] = 1
        nonlocal count
        pre[node] = count
        count += 1

        for v in adjacencyList[node]:
            if visited[v] == -1:
                parent[v] = node
                dfs(v)

        post[node] = count
        count += 1

    dfs(source)

    return {"visited":visited, "parent":parent, "pre":pre, "post":post}
