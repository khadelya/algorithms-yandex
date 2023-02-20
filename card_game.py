"""" Ordinary list version"""

with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    queue1 = contents[:5]
    queue2 = contents[5:]
    step = 0
    while (len(queue1) > 0) and (len(queue2) > 0) and (step < 1e06):
        if (queue1[0] > queue2[0] and (queue1[0] != 9 and queue2[0] != 0)) or (
            queue1[0] == 0 and queue2[0] == 9
        ):
            queue1.append(queue1[0])
            queue1.append(queue2[0])
        elif (queue2[0] > queue1[0] and (queue1[0] != 0 and queue2[0] != 9)) or (
            queue1[0] == 9 and queue2[0] == 0
        ):
            queue2.append(queue1[0])
            queue2.append(queue2[0])
        queue1 = queue1[1:]
        queue2 = queue2[1:]
        step += 1
    if len(queue1) == 0:
        print(f"second {step}")
    elif len(queue2) == 0:
        print(f"first {step}")
    elif step == 1e06:
        print("botva")
