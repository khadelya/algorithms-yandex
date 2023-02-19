with open("input.txt", "r") as file:
    contents = file.readlines()
    queue = []
    for line in contents:
        command = line.split()
        if command[0] == "push":
            n = int(command[1])
            queue += [n]
            print("ok")
        elif command[0] == "pop":
            if queue:
                print(queue[0])
                queue.pop(0)
            else:
                print("error")
        elif command[0] == "front":
            if queue:
                print(queue[0])
            else:
                print("error")
        elif command[0] == "size":
            print(len(queue))
        elif command[0] == "clear":
            queue.clear()
            print("ok")
        elif command[0] == "exit":
            print("bye")
            break
