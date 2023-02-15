with open("input.txt", "r") as file:
    contents = [int(x) for x in file.read().split()]
    num = contents[0]
    before = contents[1::2]
    after = contents[2::2]
    pairs = set(zip(before, after))
    ans = 0
    for x, y in pairs:
        if (x>=0) and (y>=0) and (x + y == num - 1):
            ans += 1
    print(ans)
