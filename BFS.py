from collections import defaultdict
class BFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self,fro,to):
        self.graph[fro].append(to)

    def bfs_traversal(self,s): #s is source
        visited = [False]*len(graph)
        queue = [s]
        visited[s] = True
        while len(queue):
            node = queue.pop(0)
            print('{} '.format(node))
            for child in self.graph[node]:
                if not visited[child]:
                    queue.append(child)
                    visited[child] = True
