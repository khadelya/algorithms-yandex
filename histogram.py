with open("input.txt", "r") as file:
    s = "".join(file.read().split())
    symcount = {}
    maxsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])
    sorteduniqsyms = sorted(symcount.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniqsyms:
            if symcount[sym] >= row:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print("".join(sorteduniqsyms))
