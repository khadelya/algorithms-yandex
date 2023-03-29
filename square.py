with open("input.txt", "r") as file:
    n, m, t = list(map(int, file.read().split()))
    vacant_space = n * m - t
    if t < (2 * n + 2 * m - 4):
        max_width = 0
    else:
        left = 0
        right = min(n, m) // 2
        while left < right:
            middle = (left + right + 1) // 2
            if (n - 2 * middle) * (m - 2 * middle) >= vacant_space:
                left = middle
            else:
                right = middle - 1
        max_width = left
    print(max_width)
