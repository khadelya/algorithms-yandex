with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    cost_of_living = contents[1:]
    stack = [(0, cost_of_living[0])]
    ans = [-1] * N
    for i, num in enumerate(cost_of_living):
        if num < stack[-1][1]:
            while (len(stack) > 0) and (stack[-1][1] > num):
                ans[stack[-1][0]] = i
                stack.pop()
        stack.append((i, num))
    print(*ans)
