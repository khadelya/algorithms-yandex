with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    way1 = contents[1:]
    stack = [0]
    way2 = []
    for num in way1:
        if num > stack[-1]:
            while (len(stack) > 0) and (num > stack[-1]):
                way2.append(stack[-1])
                stack.pop()
        stack.append(num)
    way2 += reversed(stack)
    if way2 == list(range(N + 1)):
        print("YES")
    else:
        print("NO")
