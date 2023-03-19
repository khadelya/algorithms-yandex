with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    y_coord = contents[2 : (2 * N + 1) : 2]
    M = contents[2 * N + 1]
    start = contents[(2 * N + 2) :: 2]
    end = contents[(2 * N + 3) :: 2]
    height_forward = [0]
    height_reverse = [0]
    for i in range(N - 1):
        last_forward = height_forward[-1]
        last_reverse = height_reverse[-1]
        if y_coord[i + 1] > y_coord[i]:
            last_forward += y_coord[i + 1] - y_coord[i]
        elif y_coord[i + 1] < y_coord[i]:
            last_reverse += y_coord[i] - y_coord[i + 1]
        height_forward.append(last_forward)
        height_reverse.append(last_reverse)
    for start, end in zip(start, end):
        if start < end:
            max_height = height_forward[end - 1] - height_forward[start - 1]
        elif start > end:
            max_height = height_reverse[start - 1] - height_reverse[end - 1]
        elif start == end:
            max_height = 0
        print(max_height)
