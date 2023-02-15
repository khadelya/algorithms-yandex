with open("input.txt", "r") as file:
    contents = file.read().split()
    a, b, n, m = [int(x) for x in contents]
    min_a = (n - 1) * a + n
    max_a = (n + 1) * a + n
    min_b = (m - 1) * b + m
    max_b = (m + 1) * b + m
    min_time = max(min_a, min_b)
    max_time = min(max_a, max_b)
    if min_time <= max_time:
        ans = f"{min_time} {max_time}"
    else:
        ans = str(-1)


with open("output.txt", "w") as file:
    file.write(ans)
