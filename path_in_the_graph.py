with open("input.txt", "r") as file:
    contents = file.readlines()
    num_of_vertices = int(contents[0])
    start, end = list(map(int, contents[-1].split()))
    adjacency_matrix = [list(map(int, line.split())) for line in contents[1:-1]]
    vertices = list(range(1, num_of_vertices + 1))
    graph = {vertex: set() for vertex in vertices}
    for i in range(num_of_vertices):
        for j in range(num_of_vertices):
            if adjacency_matrix[i][j] == 1:
                graph[i + 1].add(j + 1)
    visited = {start}
    path_length, prev = {}, {}
    prev[start] = -1
    path_length[start] = 0
    queue = [start]
    while len(queue) > 0:
        first_element = queue.pop(0)
        for neig in graph[first_element]:
            if neig not in visited:
                path_length[neig] = path_length[first_element] + 1
                prev[neig] = first_element
                visited.add(neig)
                queue.append(neig)
    if end not in path_length:
        print("-1")
    else:
        print(path_length[end])
        if path_length[end] > 0:
            path = [end]
            while prev[end] > 0:
                path.append(prev[end])
                end = prev[end]
            path.reverse()
            print(*path)
