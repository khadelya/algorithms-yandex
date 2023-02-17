with open("input.txt", "r") as file:
    expression = file.read().split()
    stack = []
    for sym in expression:
        if sym.isdigit():
            stack.append(int(sym))
        elif sym == "+":
            if len(stack) >= 2:
                stack[-2] += stack[-1]
                stack.pop()
            else:
                print("wrong expression")
        elif sym == "-":
            if len(stack) >= 2:
                stack[-2] -= stack[-1]
                stack.pop()
            else:
                print("wrong expression")
        elif sym == "*":
            if len(stack) >= 2:
                stack[-2] *= stack[-1]
                stack.pop()
            else:
                print("wrong expression")
    print(stack[0])
