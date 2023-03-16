with open("input.txt", "r") as file:
    contents = file.readlines()
    N = list(map(int, contents[1].split()))
    K = list(map(int, contents[3].split()))
    common_sorted_set = sorted(list(set(K + N)))
    n = 0
    dct = {}
    K_sorted = sorted(K)
    for collector in K_sorted:
        dct[collector] = common_sorted_set.index(collector) - n
        if collector not in set(N):
            n += 1
    for collector in K:
        if dct[collector] < 1:
            print("0")
        else:
            print(dct[collector])
