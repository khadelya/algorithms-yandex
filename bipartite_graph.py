with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    v, e = contents[0], contents[1]
    graph = {}
    colors = {}
    V1 = contents[2::2]
    V2 = contents[3::2]
    vertices = list(range(1, v + 1))
    components = []
    visited_components = set()
    for v1, v2 in zip(V1, V2):
        if v1 not in graph:
            graph[v1] = set()
            colors[v1] = 0
        if v2 not in graph:
            graph[v2] = set()
            colors[v2] = 0
        graph[v1].add(v2)
        graph[v2].add(v1)
    for vertex in vertices:
        if vertex not in visited_components:
            if vertex not in graph:
                graph[vertex] = set()
                colors[vertex] = 0
            visited = [vertex]
            colors[vertex] = 1
            stack = list(graph[vertex])
            while len(stack):
                last_element = stack[-1]
                if last_element not in visited:
                    if colors[last_element] == 0:
                        colors[last_element] = 3 - colors[visited[-1]]
                    visited.append(last_element)
                    stack.pop()
                    neighbours = graph[last_element]
                    for neig in neighbours:
                        if neig not in visited:
                            colors[neig] = 3 - colors[last_element]
                            stack.append(neig)
                else:
                    stack.pop()
            visited_components.update(visited)
            components.append(visited)
    different_colors = set()
    for component in components:
        if len(component) > 1:
            print(component)
            for i in range(1, len(component)):
                if abs(colors[component[i]] - colors[component[i - 1]]) == 1:
                    different_colors.add(True)
                else:
                    different_colors.add(False)
            print(different_colors)
    if all(different_colors):
        print("YES")
    else:
        print("NO")
    print(graph)
    print(different_colors)
    print(components)
    print(colors)
    for v in [13, 87, 70, 36, 74, 52, 58, 31, 18, 54]:
        print(f"{v} {colors[v]}")
