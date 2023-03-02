from math import inf


n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    if i % 2 == 0:
        num_of_operations_prev_2 = dp[i // 2]
    else:
        num_of_operations_prev_2 = inf
    if i % 3 == 0:
        num_of_operations_prev_3 = dp[i // 3]
    else:
        num_of_operations_prev_3 = inf
    dp[i] = 1 + min(dp[i - 1], num_of_operations_prev_2, num_of_operations_prev_3)
ans = [n]
while n > 1:
    comparison = []
    comparison += [(dp[n - 1], n - 1)]
    if n % 2 == 0:
        comparison += [(dp[n // 2], n // 2)]
    if n % 3 == 0:
        comparison += [(dp[n // 3], n // 3)]
    n_next = sorted(comparison)[0][1]
    ans.append(n_next)
    n = n_next
print(dp[-1])
ans.reverse()
print(*ans)
