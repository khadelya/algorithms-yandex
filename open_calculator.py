with open("input.txt", "r") as file:
    contents = file.read().split()
    seq = set(contents[:3])
    num = set(contents[3])
    ans = str(len(num.difference(seq)))
with open("output.txt", "w") as file:
    file.write(ans)
