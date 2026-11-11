from graph import UndirectedGraph
from graph import DirectedGraph

# Undirected graphs
undirected = UndirectedGraph()
undirected.add_edge("1", "2", 4)
undirected.add_edge("1", "3", 2)

print("Undirected:", undirected.adjacency)
print("Undirected vertices:", undirected.vertices())
print("Undirected neighbors of 1:", undirected.neighbors("1"))
print("Undirected neighbors of 2:", undirected.neighbors("2"))

# Directed graphs
directed = DirectedGraph()
directed.add_edge("1", "2", 4)
directed.add_edge("1", "3", 2)

print("-------------------------------------")
print("Directed:", directed.adjacency)
print("Directed neighbors of 1:", directed.neighbors("1"))
print("Directed neighbors of 2:", directed.neighbors("2"))
