from collections import deque

# The nodes in the graph are 0, 1, 2,  . . ., n-1, and
# adjacencyList is a list whose ith elements contains list
# of all j such that there is an edge from node i to node j,
# topological sort is conducted on Directed Graphs, so j in
# adjacencyList[i] does not necessarily inforce i in
# adjacencyList[j]. The objective of this function is to
# come up with topoloically sorted nodes, i.e a list of nodes
# in topologically sorted order. The topological sort is
# defined as the order which preserves the property that all
# nodes i from where there is an edge from i to j comes before j.
# The input of this function is adjacencyList, which defines
# the graph as n is length of adjacencyList, and edges is defined
# through the adjacencyList. The output is an array which is
# topologically sorted, if topological sort can not be done
# (in case of cyclic graph), the function would return False.


def topological_sort(adjacencyList):

    n = len(adjacencyList)
    degreeDict = defaultdict(int)

    for u in adjacencyList:
        for v in adjacencyList[u]:
            degreeDict[v] += 1

    queue = deque()
    queLen = 0
    for u in degreeDict:
        if degreeDict[u] == 0:
            queue.append(u)

    ans = []
    while queLen != 0:

        u = queue.popleft()
        queLen -= 1
        ans.append(u)

        for v in adjacencyList[u]:
            degreeDict[v] -= 1
            if degreeDict[v] == 0:
                queue.append(v)
                queLen += 1

    if len(ans) == n:
        return ans
    return False
