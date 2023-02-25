from math import inf

with open("input.txt", "r") as file:
    contents = file.readlines()
    n = int(contents[0])
    contents = contents[1:]
    time_per_person = [[inf, inf, inf], [inf, inf, inf], [inf, inf, inf]]
    dp = [0] * (n + 3)
    for line in contents:
        new_time = list(map(int, line.split()))
        time_per_person.append(new_time)
    ans = 0
    for i in range(3, n + 3):
        dp[i] = min(
            dp[i - 1] + time_per_person[i][0],
            dp[i - 2] + time_per_person[i - 1][1],
            dp[i - 3] + time_per_person[i - 2][2],
        )
    print(dp[-1])
