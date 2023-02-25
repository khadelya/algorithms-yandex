from math import inf

with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    n = contents[0]
    coordinates = [-inf] + sorted(contents[1:]) + [inf] + [0] + [inf]
    print(coordinates)
    arr = []
    for i in range(2, n + 1):
        arr += [coordinates[i] - coordinates[i - 1]]
    print(arr)

    flag = [0] * (n + 2)
    ans = 0
    for i in range(1, n + 1):
        if flag[i] == 0:
            left = coordinates[i] - coordinates[i - 1]
            right = coordinates[i + 1] - coordinates[i]
            right_next = coordinates[i + 2] - coordinates[i + 1]
            right_next_next = coordinates[i + 3] - coordinates[i + 2]
            if left <= right and right >= right_next and right_next <= right_next_next:
                ans += left
                flag[i - 1], flag[i] = 1, 1
            else:
                ans += right
                flag[i + 1], flag[i] = 1, 1
    print(ans)
