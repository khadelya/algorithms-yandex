from math import ceil, floor

with open("input.txt", "r") as file:
    input = file.read().split()
    k1, M, k2, p2, n2 = [int(x) for x in input]
    if p2 > 1:
        num = ceil(k2 / (n2 + (p2 - 1) * M))
    else:
        num = ceil(k2 / n2)
    if n2 == 1 and p2 == 1:
        p1, n1 = 0, 1
    elif (
        (num * M * (p2 - 1) >= k2 and p2 > 1) or (n2 > M) or (k2 < (n2 + M * (p2 - 1)))
    ):
        p1, n1 = -1, -1
    else:
        fl = ceil(k1 / num)
        p1 = 1
        n1 = fl
        if fl > M:
            p1 = ceil(fl / M)
            diff = floor(fl / M)
            n1 = fl - M * diff


with open("output.txt", "w") as file:
    file.write(f"{p1} {n1}")
