with open("input.txt", "r") as file:
    contents = file.readlines()
    N = int(contents[0])
    sequence_1 = [0] + list(map(int, contents[1].split()))
    M = int(contents[2])
    sequence_2 = [0] + list(map(int, contents[3].split()))
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if sequence_1[j] == sequence_2[i]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    lcs = []
    i = M
    j = N
    while i > 0 and j > 0:
        if sequence_2[i] == sequence_1[j]:
            lcs += [sequence_2[i]]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()
    print(*lcs)
