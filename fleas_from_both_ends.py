with open("input.txt", "r") as file:
    contents = file.readlines()
    N, M, S, T, Q = list(map(int, contents[0].split()))
    fleas = []
    for line in contents[1:]:
        fleas.append(tuple(map(int, line.split())))
    path_exists = True
    path_length_sum = 0
    end = (S - 1, T - 1)
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    for flea in fleas:
        if path_exists:
            flea = tuple([coord - 1 for coord in flea])
            visited = {flea}
            visited_end = {end}
            path_length, path_length_end = {}, {}
            path_length[flea] = 0
            path_length_end[end] = 0
            queue = [flea]
            queue_end = [end]
            while (
                len(visited.intersection(visited_end)) == 0
                and len(queue) > 0
                and len(queue_end) > 0
            ):
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
                first_element_end = queue_end.pop(0)
                neighbours_end = []
                i_cur_end, j_cur_end = first_element_end
                for i in range(8):
                    if 0 <= i_cur_end + dy[i] < N and 0 <= j_cur_end + dx[i] < M:
                        neighbours_end.append((i_cur_end + dy[i], j_cur_end + dx[i]))
                for neig in neighbours_end:
                    if neig not in visited_end:
                        path_length_end[neig] = path_length_end[first_element_end] + 1
                        visited_end.add(neig)
                        queue_end.append(neig)
            if len(visited.intersection(visited_end)) > 0:
                common_coord = list(visited.intersection(visited_end))[0]
                path_length_sum += (
                    path_length[common_coord] + path_length_end[common_coord]
                )
            else:
                path_exists = False
    if path_exists:
        print(path_length_sum)
    else:
        print("-1")
