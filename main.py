from graph import UndirectedGraph
from graph import DirectedGraph
from graph import load_graph
from algorithms import is_connected

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

# Load graph from file
print("Examples -------------------------------------")
print("Example 1: ")
loaded = load_graph("examples_MD/ejemplo_1.csv")
print("Loaded vertices:", loaded.vertices())
print("Loaded:", loaded.adjacency)

print("-------------------------------------")
print("Example 2: ")
loaded = load_graph("examples_MD/ejemplo_2.csv")
print("Loaded vertices:", loaded.vertices())
print("Loaded:", loaded.adjacency)

# Connectivity tests
print("Connectivity -------------------------------------")
for number in range(1, 7):
    print(f"Example {number}:")
    is_connected(load_graph(f"examples_MD/ejemplo_{number}.csv"))