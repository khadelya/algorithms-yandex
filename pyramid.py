with open("input.txt", "r") as file:
    contents = [int(x) for x in file.read().split()]
    width = contents[1::2]
    height = contents[2::2]
    dct = {}
    dct = dict(zip(width, height))
    print(dct)
    # for w, h in zip(width, height):
    #     if w not in dct:
    #         dct[w] = 0
    #     if h > dct[w]:
    #         dct[w] = h
    # width_sort = sorted(dct.items(), key=lambda x: x[0], reverse=True)
    # ans = 0
    # for item in width_sort:
    #     ans += item[1]
    # print(ans)
