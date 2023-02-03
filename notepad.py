with open("input.txt", "r") as file:
    contents = file.read().split()
    corr = [True if 0 < int(x) <= 1000 else False for x in contents]
    if all(corr):
        a1, b1, a2, b2 = [int(x) for x in contents]
        if a1 == a2:
            ans = f"{a1} {b1+b2}"
        elif a1 == b2:
            ans = f"{a1} {b1+a2}"
        elif b1 == a2:
            ans = f"{a2} {a1+b2}"
        elif b1 == b2:
            ans = f"{b1} {a1+a2}"
        elif max(a1, b1) < max(a2, b2):
            if max(a1, b1) < min(a2, b2):
                a = min(a2, b2)
                b = min(a1, b1) + max(a2, b2)
                ans = f"{a} {b}"
            else:
                a = max(a2, b2)
                b = min(a1, b1) + min(a2, b2)
                ans = f"{a} {b}"
        else:
            if max(a2, b2) < min(a1, b1):
                a = min(a1, b1)
                b = max(a1, b1) + min(a2, b2)
                ans = f"{a} {b}"
            else:
                a = max(a1, b1)
                b = min(a1, b1) + min(a2, b2)
                ans = f"{a} {b}"
    else:
        ans = "Wrong input"

with open("output.txt", "w") as file:
    file.write(ans)
