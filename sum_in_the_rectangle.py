with open("input.txt", "r") as file:
    contents = file.readlines()
    N, M, K = list(map(int, contents[0].split()))
    matrix = [[0] * (M + 1) for i in range(N + 1)]
    n = 1
    for i in range(1, N + 1):
        matrix[i] = [0] + list(map(int, contents[n].split()))
        n += 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            matrix[i][j] = (
                matrix[i][j]
                + matrix[i][j - 1]
                + matrix[i - 1][j]
                - matrix[i - 1][j - 1]
            )
    for i in range(K):
        x1, y1, x2, y2 = list(map(int, contents[n].split()))
        ans = (
            matrix[x2][y2]
            - matrix[x1 - 1][y2]
            - matrix[x2][y1 - 1]
            + matrix[x1 - 1][y1 - 1]
        )
        print(ans)
        n += 1
