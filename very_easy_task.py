with open("input.txt", "r") as file:
    N, x, y = list(map(int, file.read().split()))
    min_x_y = min(x, y)
    if N > 1:
        left = min_x_y
        right = min_x_y * N
        while left < right:
            middle = (left + right) // 2
            if (middle - min_x_y) // x + (middle - min_x_y) // y >= N - 1:
                right = middle
            else:
                left = middle + 1
        minimal_time = left
    else:
        minimal_time = min_x_y
    print(minimal_time)
