with open("input.txt", "r") as file:
    contents = file.read().split()
    a, b, c = [int(x) for x in contents]
    if (a + b > c) and (a + c > b) and (c + b > a):
        ans = "YES"
    else:
        ans = "NO"
with open("output.txt", "w") as file:
    file.write(ans)
