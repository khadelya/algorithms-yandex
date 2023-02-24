n = int(input())
dp = [n]
num_of_operations = 0
last_dp = n
while last_dp > 1:
    if last_dp % 3 == 0:
        dp.append(last_dp // 3)
        num_of_operations += 1
    elif last_dp % 2 == 0:
        dp.append(last_dp // 2)
        num_of_operations += 1
    elif last_dp % 3 == 1 or last_dp % 2 == 1:
        dp.append(last_dp - 1)
        num_of_operations += 1
    last_dp = dp[-1]
dp.reverse()
print(num_of_operations)
print(*dp)
