with open("input.txt", "r") as file:
    contents = file.read().split()
    contents.sort()
    dct = {}
    for word in contents:
        if word not in dct:
            dct[word] = 0
        dct[word] += 1
    ans = sorted(dct.items(), key=lambda x: x[1], reverse=True)[0][0]
print(ans)
