with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    K = contents[1]
    num = contents[2:]
    ans = 0
    first = last = 0
    sum = 0
    while first < N and last < N:
        if sum == 0:
            sum = num[first]
            last = first
        while last < N - 1 and sum < K:
            last += 1
            sum += num[last]
        if sum == K:
            ans += 1
        sum -= num[first]
        first += 1
    print(ans)
