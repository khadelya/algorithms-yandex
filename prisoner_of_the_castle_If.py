with open("input.txt", "r") as file:
    contents = file.read().split()
    a, b, c, d, e = [int(x) for x in contents]
    hole_min = min(d, e)
    hole_max = max(d, e)
    brick = [a, b, c]
    brick_min = min(brick)
    brick_max = max(brick)
    for br in brick:
        if (br > brick_min) and (br < brick_max):
            brick_max = br
        elif (br == brick_min) and (br < brick_max):
            brick_max = br
    if (brick_min <= hole_min) and (brick_max <= hole_max):
        ans = "YES"
    else:
        ans = "NO"
with open("output.txt", "w") as file:
    file.write(ans)
