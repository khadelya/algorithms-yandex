n = int(input())
dp = [2, 4, 7]
for i in range(3, n):
    new_dp = dp[-1] + dp[-2] + dp[-3]
    dp.append(new_dp)
print(dp[n - 1])
