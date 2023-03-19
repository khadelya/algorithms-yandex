with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    n = contents[0]
    r = contents[1]
    distance = contents[2:]
    first = 0
    ways = 0
    for last in range(1, n):
        ways += first
        while first < last and distance[last] - distance[first] > r:
            ways += 1
            first += 1
    print(ways)
