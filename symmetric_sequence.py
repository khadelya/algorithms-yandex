with open("input.txt", "r") as file:
    contents = file.read().split()
    seq = [int(x) for x in contents[1:]]
    flag = True
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        while (i < len(seq)) and (j >= 0) and (i <= j) and (seq[i] == seq[j]):
            i += 1
            j -= 1
        if i > j and flag:
            ans = []
            for i in range(start - 1, -1, -1):
                ans.append(seq[i])
            flag = False
print(len(ans))
print(*ans)
