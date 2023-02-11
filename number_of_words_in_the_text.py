with open("input.txt", "r") as file:
    contents = file.read().split()
    ans = str(len(set(contents)))
with open("output.txt", "w") as file:
    file.write(ans)
