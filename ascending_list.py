with open("input.txt", "r") as file:
    contents = file.read().split()
    lst = [int(x) for x in contents]
    corr = []
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            corr += [True]
        else:
            corr += [False]
    if all(corr):
        ans = "YES"
    else:
        ans = "NO"
with open("output.txt", "w") as file:
    file.write(ans)
