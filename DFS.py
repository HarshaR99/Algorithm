from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,from_node,to):
        if to not in self.graph[from_node]:
            self.graph[from_node].append(to)
            self.graph[from_node].sort()

class DFS:
    def __init__(self,graph): # graph is an instance of Graph
        self.graph = graph
        self.visited = [False]*len(self.graph.graph)

    def dfs_traversal(self,source):
        self.visited[source] = True
        print(source,end=',')
        for node in self.graph.graph[source]:
            if not self.visited[node]:
                self.dfs_traversal(node)

# driver code from GFG
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

dfs = DFS(g)
dfs.dfs_traversal(2)

# yup its working

