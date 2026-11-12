def is_connected(graph):
    vertices = graph.vertices()
    
    if not vertices: # An empty graph has nothing to disconnect, so we treat it as connected
        result = True
    else:
        start = vertices[0]
        visited = {start}   #vertices we have already reached
        stack = [start] #vertices we still need to explore

        while stack:
            current = stack.pop()
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        result = len(visited) == len(vertices)

    print(f"is_connected: {result}")
    return result

def has_cycle(graph):
    result = False
    visited = set()
    # Here we start a search from every vertex not reached yet
    for start in graph.vertices():
        if start in visited or result:
            continue
        visited.add(start)
        stack = [(start, None)]

        while stack and not result:
            current, parent = stack.pop()
            for neighbor in graph.neighbors(current):
                if neighbor == current:
                    result = True  # An edge from a vertex to itself, self loop.
                elif neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, current))
                elif neighbor != parent:
                    result = True  # already visited and not our parent: cycle

    print(f"has_cycle: {result}")
    return result