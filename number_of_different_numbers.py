with open("input.txt", "r") as file:
    content = file.read().split()
    seq = [int(x) for x in content]
    ans = len(set(seq))
    print(ans)
