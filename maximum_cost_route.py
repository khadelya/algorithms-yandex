with open("input.txt", "r") as file:
    contents = file.readlines()
    N, M = list(map(int, contents[0].split()))
    table_lines = contents[1:]
    table = []
    for line in table_lines:
        table.append(list(map(int, line.split())))
    for j in range(1, M):
        table[0][j] += table[0][j - 1]
    for i in range(1, N):
        table[i][0] += table[i - 1][0]
    for i in range(1, N):
        for j in range(1, M):
            table[i][j] += max(table[i - 1][j], table[i][j - 1])
    num_of_steps = N + M - 2
    x = N - 1
    y = M - 1
    route = []
    for _ in range(num_of_steps):
        if x and y:
            if table[x - 1][y] >= table[x][y - 1]:
                route.append("D")
                x -= 1
            else:
                route.append("R")
                y -= 1
        elif x:
            route.append("D")
            x -= 1
        elif y:
            route.append("R")
            y -= 1
    route.reverse()
    print(table[-1][-1])
    print(*route)
