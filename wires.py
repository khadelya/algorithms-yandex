with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N, K = contents[0], contents[1]
    wires = contents[2:]
    sum_wires = sum(wires)
    if sum_wires < K:
        max_len = 0
    else:
        left = 1
        right = sum_wires // K
        while left < right:
            middle = (left + right + 1) // 2
            if sum([wire // middle for wire in wires]) >= K:
                left = middle
            else:
                right = middle - 1
        max_len = left
    print(max_len)
