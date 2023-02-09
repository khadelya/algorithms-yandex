with open("input.txt", "r") as file:
    contents = file.read().split()
    a, b, n, m = [int(x) for x in contents]
    min_time = (n - 1) * a + n
    max_time = (n + 1) * a + n
    min_time_b = (m - 1) * b + m
    max_time_b = (m + 1) * b + m
    min_t = max(min_time, min_time_b)
    max_t = min(max_time, max_time_b)
    if min_t < max_t:
        ans = f"{min_t} {max_t}"
    else:
        ans = str(-1)


with open("output.txt", "w") as file:
    file.write(ans)
