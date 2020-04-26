from collections import defaultdict

class Graph:
	"""
	The logic is , that if a neighbour of a node is already visited 
	then if it is not its parentt node then there is a cycle
	Just lazy for utiline comment, this not doctring
	"""


	def __init__(self):
		self.adj_list = defaultdict(list)
		self.visited = list()

	def addEdge(self,source,destination):
		if source not in self.adj_list:
			self.visited.append(False)
		if destination not in self.adj_list:
			self.visited.append(False)
		if destination not in self.adj_list[source]:
			self.adj_list[source].append(destination)
		if source not in self.adj_list[destination]:
			self.adj_list[destination].append(source)

	def isCyclic(self):
		for node in self.adj_list:
			if not self.visited[node]:
				if self.isCyclicUtil(node,-99):
					return True
		return False

	def isCyclicUtil(self,node,parent):
		self.visited[node] = True
		for neighbour in self.adj_list[node]:
			if not self.visited[neighbour]:
				if self.isCyclicUtil(neighbour,node):
					return True
			elif parent != neighbour and parent != 99:
				return True
		return False

g = Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,0)
print(g.isCyclic())

g2 = Graph()
g2.addEdge(0,1)
g2.addEdge(1,2)
g2.addEdge(0,3)
print(g2.isCyclic())	