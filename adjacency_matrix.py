from collections import defaultdict

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

class adjacencymatrix:
    vertices = defaultdict(list)  # dictionaries for storing vertex objects
    vertex_indices = dict()  # this stores the index of row of vertex in the matrix
    # and as it is symmetrical it is also index for column
    adjacency_matrix = []  # the matrix

    def add_vertex(self, vertex):
        if isinstance(vertex, vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * len(self.adjacency_matrix + 1))
            self.vertex_indices[vertex.name] = len(self.vertex_indices)
            return True
        return False

    def add_edge(self, start, dest, weight=1):
        if start in self.vertices and dest in self.vertices:
            self.adjacency_matrix[self.vertex_indices[start]][self.vertex_indices[dest]] = weight
            # as an adjacency matrix is a symmetric matrix
            self.adjacency_matrix[self.vertex_indices[dest]][self.vertex_indices[start]] = weight
            return True
        return False
