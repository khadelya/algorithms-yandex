with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    v, e = contents[0], contents[1]
    graph = {}
    V1 = contents[2::2]
    V2 = contents[3::2]
    vertices = list(range(1, v + 1))
    graph = {vertex: set() for vertex in vertices}
    visited = set()
    for v1, v2 in zip(V1, V2):
        graph[v1].add(v2)
    indegrees = {vertex: 0 for vertex in vertices}
    for vertex in graph:
        for neigbour in graph[vertex]:
            indegrees[neigbour] += 1
    nodes_with_no_incoming_edges = []
    for vertex in vertices:
        if indegrees[vertex] == 0:
            nodes_with_no_incoming_edges.append(vertex)
    topological_ordering = []
    while len(nodes_with_no_incoming_edges) > 0:
        node = nodes_with_no_incoming_edges.pop()
        topological_ordering.append(node)
        for neigbour in graph[node]:
            indegrees[neigbour] -= 1
            if indegrees[neigbour] == 0:
                nodes_with_no_incoming_edges.append(neigbour)
    if len(topological_ordering) == v:
        print(*topological_ordering)
    else:
        print("-1")
