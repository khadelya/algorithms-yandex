from math import sqrt

with open("input.txt", "r") as file:
    contents = file.read().split()
    a, b, c = [int(x) for x in contents]
    if a and c >= 0:
        ans = int((c**2 - b) / a)
    elif (c < 0) or (a != 0 and b == 0 and c == 0) or (a == 0 and b != 0 and c == 0):
        ans = "NO SOLUTION"
    elif (a == 0 and sqrt(b) == c) or (a == 0 and b == 0 and c == 0):
        ans = "MANY SOLUTIONS"

with open("output.txt", "w") as file:
    file.write(str(ans))
