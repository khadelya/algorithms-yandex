with open("input.txt", "r") as file:
    contents = file.read().split()
    lst = [int(x) for x in contents[:-1]]
    corr = []
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            corr.append("ASCENDING")
        elif lst[i - 1] == lst[i]:
            corr.append("CONSTANT")
        elif lst[i - 1] > lst[i]:
            corr.append("DESCENDING")
    if all([True if x == "CONSTANT" else False for x in corr]):
        ans = "CONSTANT"
    elif all([True if x == "ASCENDING" else False for x in corr]):
        ans = "ASCENDING"
    elif all([True if x == "ASCENDING" or x == "CONSTANT" else False for x in corr]):
        ans = "WEAKLY ASCENDING"
    elif all([True if x == "DESCENDING" else False for x in corr]):
        ans = "DESCENDING"
    elif all([True if x == "DESCENDING" or x == "CONSTANT" else False for x in corr]):
        ans = "WEAKLY DESCENDING"
    else:
        ans = "RANDOM"

with open("output.txt", "w") as file:
    file.write(ans)
