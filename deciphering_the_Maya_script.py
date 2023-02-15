with open("input.txt", "r") as file:
    g, s, W, S = file.read().split()
    g, s = int(g), int(s)
    word = set(W)
    remain = s % g
    line_set = []
    ans = 0
    for i in range(0, s - remain):
        line_set += [[S[i], S[i + 1], S[i + 2], S[i + 3]]]
    for item in line_set:
        if set(item) == word:
            ans += 1
    print(ans)
