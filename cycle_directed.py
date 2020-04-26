from collections import defaultdict

# unweighted directed graph
class Graph:
	def __init__(self):
		self.adj_list = defaultdict(list)

	def addEdge(self,source,dest):
		self.adj_list[source].append(dest)

	def isCylic(self):
		visited = [False]*len(self.adj_list)
		backedges = [False]*len(self.adj_list)
		for node in range(len(self.adj_list)):
			if not visited[node]:
				if self.isCylicUtil(node,visited,backedges):
					return True
		# print(visited,backedges)
		return False

	# i guess no helper function needed if visited and backedges are global
	def isCylicUtil(self,node,visited,backedges):
		visited[node] = True
		# backedges is to kee track of which vertices the node travels through
		backedges[node] = True
		for neighbour in self.adj_list[node]:
			if not visited[neighbour]:
				if self.isCylicUtil(neighbour,visited,backedges):
					print(neighbour,end = "-> ")
					return True
			# if neighbour is already visited
			elif backedges[neighbour]:
					print(neighbour,end = "-> ")
					return True
		# it will show some other vertex travelled through that vertex even if it is not true
		# if not set to false
		backedges[node] = False
		return False

#driver code
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
		
print(g.adj_list[2])
if g.isCylic():
	print("has cycle")
else:
	print("does not have cycle")




