def _is_connected(graph):
    vertices = graph.vertices()

    if not vertices: # An empty graph has nothing to disconnect, so we treat it as connected
        return True

    start = vertices[0]
    visited = {start}   #vertices we have already reached
    stack = [start] #vertices we still need to explore

    while stack:
        current = stack.pop()
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return len(visited) == len(vertices)

def _has_cycle(graph):
    visited = set()
    # Here we start a search from every vertex not reached yet
    for start in graph.vertices():
        if start in visited:
            continue

        visited.add(start)
        stack = [(start, None)]

        while stack:
            current, parent = stack.pop()
            for neighbor in graph.neighbors(current):
                if neighbor == current:
                    return True # An edge from a vertex to itself, self loop.
                elif neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, current))
                elif neighbor != parent:
                    return True # already visited and not our parent: cycle

    return False

def is_connected(graph):
    result = _is_connected(graph)
    print(f"is_connected: {result}")
    return result

def has_cycle(graph):
    result = _has_cycle(graph)
    print(f"has_cycle: {result}")
    return result

def is_tree(graph):
    result = _is_connected(graph) and not _has_cycle(graph)
    print(f"is_tree: {result}")
    return result