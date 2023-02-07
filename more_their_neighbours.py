with open("input.txt", "r") as file:
    contents = file.read().split()
    lst = [int(x) for x in contents]
    ans = 0
    for i in range(1, len(lst[:-1])):
        if (lst[i] > lst[i - 1]) and (lst[i] > lst[i + 1]):
            ans += 1
with open("output.txt", "w") as file:
    file.write(str(ans))
