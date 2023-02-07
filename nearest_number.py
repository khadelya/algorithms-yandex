with open("input.txt", "r") as file:
    contents = file.read().split()
    lst = [int(item) for item in contents[1:-1]]
    x = int(contents[-1])
    ans = lst[0]
    diff = abs(x - lst[0])
    for i in range(1, len(lst)):
        if abs(x - lst[i]) < diff:
            ans = lst[i]
            diff = abs(x - lst[i])

with open("output.txt", "w") as file:
    file.write(str(ans))
