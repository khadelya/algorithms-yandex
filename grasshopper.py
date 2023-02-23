with open("input.txt", "r") as file:
    n, k = list(map(int, file.read().split()))
    n = max(1, n - 1)
    dp = [2**i for i in range(min(k, n))]
    for i in range(k, n):
        new_dp = 0
        for j in range(1, k + 1):
            new_dp += dp[-j]
        dp.append(new_dp)
    print(dp[-1])
