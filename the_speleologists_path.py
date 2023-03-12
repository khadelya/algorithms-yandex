with open("input.txt", "r") as file:
    contents = file.read().split()
    N = int(contents[0])
    cave = contents[1:]
    availability_matrix = [[[0] * N for i in range(N)] for k in range(N)]
    n = 0
    for k in range(N):
        for i in range(N):
            cur_line = list(cave[n])
            availability_matrix[k][i] = cur_line
            if "S" in cur_line:
                start = (k, i, cur_line.index("S"))
            n += 1
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    visited = {start}
    path_length = {}
    path_length[start] = 0
    queue = [start]
    while len(queue) > 0:
        first_element = queue.pop(0)
        neighbours = []
        k_cur, i_cur, j_cur = first_element
        for i in range(6):
            if (
                0 <= k_cur + dz[i] < N
                and 0 <= i_cur + dy[i] < N
                and 0 <= j_cur + dx[i] < N
                and availability_matrix[k_cur + dz[i]][i_cur + dy[i]][j_cur + dx[i]]
                == "."
            ):
                neighbours.append((k_cur + dz[i], i_cur + dy[i], j_cur + dx[i]))
        for neig in neighbours:
            if neig not in visited:
                path_length[neig] = path_length[first_element] + 1
                visited.add(neig)
                queue.append(neig)
    escape = []
    for i in range(N):
        for j in range(N):
            if availability_matrix[0][i][j] == ".":
                escape.append((0, i, j))
    paths = []
    for esc in escape:
        if esc in path_length:
            paths.append(path_length[esc])
    if paths:
        print(min(paths))
    else:
        print("0")
