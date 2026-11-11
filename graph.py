import csv

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


def load_graph(path, directed=False):
    graph = DirectedGraph() if directed else UndirectedGraph()

    with open(path, newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header line

        for row in reader:
            if not row:  # ignore the empty lines
                continue
            source, target, weight = (value.strip() for value in row)
            graph.add_edge(source, target, float(weight))
    return graph