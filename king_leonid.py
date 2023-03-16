with open("input.txt", "r") as file:
    contents = file.read().split()
    N, M = int(contents[0]), int(contents[1])
    availability_matrix = [[0] * M for i in range(N)]
    n = 2
    for i in range(N):
        availability_matrix[i] = list(contents[n])
        n += 1
    x1, y1, x2, y2 = list(map(int, contents[-4:]))
    start = (N - y1, x1 - 1)
    end = (N - y2, x2 - 1)
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    direction = [
        "left",
        "diag_left_up",
        "up",
        "diag_right_up",
        "right",
        "diag_right_down",
        "down",
        "diag_left_down",
    ]
    visited = {start}
    path_length = {}
    path_length[start] = 0
    queue = [start]
    direction_story = {}
    cur_direction = {}
    while len(queue) > 0:
        first_element = queue.pop(0)
        neighbours = []
        i_cur, j_cur = first_element
        for i in range(8):
            if (
                0 <= i_cur + dy[i] < N
                and 0 <= j_cur + dx[i] < M
                and availability_matrix[i_cur + dy[i]][j_cur + dx[i]] == "."
            ):
                neighbours.append((i_cur + dy[i], j_cur + dx[i]))
                if (i_cur + dy[i], j_cur + dx[i]) not in direction_story:
                    direction_story[(i_cur + dy[i], j_cur + dx[i])] = direction[i]
                cur_direction[(i_cur + dy[i], j_cur + dx[i])] = direction[i]
        for neig in neighbours:
            if neig not in visited:
                if (
                    first_element not in direction_story
                    or direction_story[neig] == direction_story[first_element]
                ):
                    path_length[neig] = path_length[first_element]
                else:
                    path_length[neig] = path_length[first_element] + 1
                visited.add(neig)
                queue.append(neig)
            elif (
                cur_direction[neig] == direction_story[first_element]
                and path_length[neig] > path_length[first_element]
            ):
                path_length[neig] = path_length[first_element]
                direction_story[neig] = cur_direction[neig]
    if end in path_length:
        print(path_length[end])
    else:
        print("-1")
print(path_length)
print(direction_story)
