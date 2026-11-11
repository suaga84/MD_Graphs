class UndirectedGraph:

    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def add_edge(self, source, target, weight=1):
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source][target] = weight
        self.adjacency[target][source] = weight #reverse direction for make it Undirected.

    def vertices(self):
        return list(self.adjacency)

    def neighbors(self, vertex):
        return list(self.adjacency[vertex])


class DirectedGraph:

    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def add_edge(self, source, target, weight=1):
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source][target] = weight #only source target, for become it Directional

    def vertices(self):
        return list(self.adjacency)

    def neighbors(self, vertex):
        return list(self.adjacency[vertex])