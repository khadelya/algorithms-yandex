with open("input.txt", "r") as file:
    contents = file.readlines()
    N, M, S, T, Q = list(map(int, contents[0].split()))
    fleas = []
    for line in contents[1:]:
        fleas.append(tuple(map(int, line.split())))
    path_exists = True
    path_length_sum = []
    end = (S - 1, T - 1)
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    for flea in fleas:
        if path_exists:
            flea = tuple([coord - 1 for coord in flea])
            visited = {flea}
            path_length = {}
            path_length[flea] = 0
            queue = [flea]
            while len(queue) > 0:
                first_element = queue.pop(0)
                neighbours = []
                i_cur, j_cur = first_element
                for i in range(8):
                    if 0 <= i_cur + dy[i] < N and 0 <= j_cur + dx[i] < M:
                        neighbours.append((i_cur + dy[i], j_cur + dx[i]))
                for neig in neighbours:
                    if neig not in visited:
                        path_length[neig] = path_length[first_element] + 1
                        visited.add(neig)
                        queue.append(neig)
            if end not in path_length:
                path_exists = False
            else:
                path_length_sum.append(path_length[end])
    if path_exists:
        print(sum(path_length_sum))
    else:
        print("-1")
