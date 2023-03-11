with open("input.txt", "r") as file:
    contents = file.readlines()
    num_of_vertices = int(contents[0])
    adjacency_matrix = [list(map(int, line.split())) for line in contents[1:]]
    vertices = list(range(1, num_of_vertices + 1))
    graph = {vertex: set() for vertex in vertices}
    for i in range(num_of_vertices):
        for j in range(num_of_vertices):
            if adjacency_matrix[i][j] == 1:
                graph[i + 1].add(j + 1)
    components = []
    visited_components = set()
    cycle = False
    for vertex in vertices:
        if vertex not in visited_components:
            visited = [vertex]
            stack = list(graph[vertex])
            while len(stack):
                last_element = stack.pop()
                if last_element not in visited:
                    visited.append(last_element)
                    neighbours = graph[last_element]
                    for neig in neighbours:
                        if neig not in visited:
                            stack.append(neig)
                        elif neig in visited[:-2] and cycle == False:
                            print("YES")
                            print(len(visited))
                            print(*visited)
                            cycle = True
            visited_components.update(visited)
            components.append(visited)
    if not cycle:
        print("NO")
    print(components)
