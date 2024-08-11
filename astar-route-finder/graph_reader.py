def read_graph(file_path):
    graph = {}
    heuristics = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            node = parts[0]
            heuristic = int(parts[1])
            heuristics[node] = heuristic
            edges = {}

            for i in range(2, len(parts), 2):
                neighbor = parts[i]
                distance = int(parts[i + 1])
                edges[neighbor] = distance
            graph[node] = edges

    return graph, heuristics