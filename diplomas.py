with open("input.txt", "r") as file:
    w, h, n = list(map(int, file.read().split()))
    max_board_size = max(w, h) * n
    board_side_sizes = range(1, max_board_size + 1)
    left = 0
    right = max_board_size - 1
    while left < right:
        middle = (left + right) // 2
        if (board_side_sizes[middle] // w) * (board_side_sizes[middle] // h) >= n:
            right = middle
        else:
            left = middle + 1
    print(board_side_sizes[left])
