def cycleInGraph(edges):
    for i in range(len(edges)):
        visitedNodes = set()
        hasLoop = dfs(i, edges, visitedNodes)
        if hasLoop:
            return hasLoop
        # Add all fully explored nodes to traversed list
    return False
    
def dfs(node, adjList, visitedNodes):
    if node in visitedNodes:
        return True
    visitedNodes.add(node)
    for targetNode in adjList[node]:
        newSet = visitedNodes.copy()
        hasLoop = dfs(targetNode, adjList, newSet)
        if hasLoop:
            print(node)
            print(targetNode)
            return True
    return False
# O(v+e) time, O(v^2) space