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
    i = M
    j = N
    ans = []
    for _ in range(1, min(N + 1, M + 1)):
        if dp[i][j - 1] == dp[i][j]:
            j -= 1
        if dp[i - 1][j - 1] < dp[i][j] and dp[i][j - 1] != dp[i][j]:
            ans += [sequence_1[j]]
        i -= 1
        j -= 1
    ans.reverse()
    print(*ans)
