class Graph:
    def __init__(self) -> None:
        self.Nodes = {}
    
    def addEdge(self,val1: int,val2: int) -> None:
        self.Nodes[val1] = Node(val1,val2)

class Node:
    def __init__(self, val: int, out: int) -> None:
        self.val = val
        self.out = out
    
n = int(input())
g = Graph()
for i in range(n):
    g.addEdge(i+1,int(input()))
