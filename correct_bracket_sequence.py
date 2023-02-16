with open("input.txt", "r") as file:
    seq = file.read()
    stack = []
    opening_brackets = ["(", "[", "{"]
    ans = ""
    for bracket in seq:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket == ")":
            if (len(stack) == 0) or (stack[-1] != "("):
                ans = "no"
            else:
                stack.pop()
        elif bracket == "]":
            if (len(stack) == 0) or (stack[-1] != "["):
                ans = "no"
            else:
                stack.pop()
        elif bracket == "}":
            if (len(stack) == 0) or (stack[-1] != "{"):
                ans = "no"
            else:
                stack.pop()
    if (len(stack) == 0) and (ans != "no"):
        print("yes")
    else:
        print("no")
