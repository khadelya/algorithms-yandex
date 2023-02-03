with open("input.txt", "r") as file:
    contents = file.read().split()
    troom, tcond, mode = contents
    troom, tcond = int(troom), int(tcond)
    temp = troom
    if ((troom >= -50) and (troom <= 50)) and ((tcond >= -50) and (tcond <= 50)):
        if mode == "freeze":
            if troom > tcond:
                temp = tcond
            else:
                temp = troom
        elif mode == "heat":
            if troom < tcond:
                temp = tcond
            else:
                temp = troom
        elif mode == "auto":
            temp = tcond
        elif mode == "fan":
            temp = troom
        else:
            temp = "Incorrect mode"
with open("output.txt", "w") as file:
    file.write(str(temp))
