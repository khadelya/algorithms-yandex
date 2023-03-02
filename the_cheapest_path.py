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
            table[i][j] += min(table[i - 1][j], table[i][j - 1])
    print(table[-1][-1])
