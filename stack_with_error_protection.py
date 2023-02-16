with open("input.txt", "r") as file:
    contents = file.readlines()
    stack = []
    for line in contents:
        command = line.split()
        if command[0] == "push":
            n = int(command[1])
            stack += [n]
            print("ok")
        elif command[0] == "pop":
            if stack:
                print(stack[-1])
                stack.pop()
            else:
                print("error")
        elif command[0] == "back":
            if stack:
                print(stack[-1])
            else:
                print("error")
        elif command[0] == "size":
            print(len(stack))
        elif command[0] == "clear":
            stack.clear()
            print("ok")
        elif command[0] == "exit":
            print("bye")
            break
