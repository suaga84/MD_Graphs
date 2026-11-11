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