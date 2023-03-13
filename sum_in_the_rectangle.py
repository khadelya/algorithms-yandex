with open("input.txt", "r") as file:
    contents = file.readlines()
    N, M, K = list(map(int, contents[0].split()))
    matrix = []
    n = 1
    for i in range(1, N + 1):
        matrix.append(list(map(int, contents[n].split())))
        n += 1
    for i in range(K):
        matrix_sum = 0
        x1, y1, x2, y2 = list(map(int, contents[n].split()))
        for i in range(x1 - 1, x2):
            for j in range(y1 - 1, y2):
                matrix_sum += matrix[i][j]
        print(matrix_sum)
        n += 1
