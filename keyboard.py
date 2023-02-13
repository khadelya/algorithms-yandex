with open("input.txt", "r") as file:
    contents = [int(x) for x in file.read().split()]
    n1 = contents[0]
    threshold = contents[1 : n1 + 1]
    n2 = contents[n1 + 1]
    seq = contents[n1 + 2 :]
    seq.sort()
    dct = {}
    for item in seq:
        if item not in dct:
            dct[item] = 0
        dct[item] += 1
    for x, y in zip(threshold, dct.values()):
        if y > x:
            print("YES")
        else:
            print("NO")
