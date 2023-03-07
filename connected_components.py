with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    v, e = contents[0], contents[1]
    graph = {}
    V1 = contents[2::2]
    V2 = contents[3::2]
    vertices = list(range(1, v + 1))
    components = []
    visited_components = set()
    for v1, v2 in zip(V1, V2):
        if v1 not in graph:
            graph[v1] = set()
        if v2 not in graph:
            graph[v2] = set()
        graph[v1].add(v2)
        graph[v2].add(v1)
    for vertex in vertices:
        if vertex not in visited_components:
            if vertex not in graph:
                graph[vertex] = set()
            visited = {vertex}
            stack = list(graph[vertex])
            while len(stack):
                last_element = stack[-1]
                if last_element not in visited:
                    visited.add(last_element)
                    stack.pop()
                    neighbours = graph[last_element]
                    for neig in neighbours:
                        if neig not in visited:
                            stack.append(neig)
                else:
                    stack.pop()
            visited_components.update(visited)
            components.append(visited)
    print(len(components))
    for component in components:
        print(len(component))
        print(*component)
