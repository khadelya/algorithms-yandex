with open("input.txt", "r") as file:
    contents = file.readlines()
    deque = []
    for line in contents:
        command = line.split()
        if command[0] == "push_front":
            n = int(command[1])
            deque = [n] + deque
            print("ok")
        elif command[0] == "push_back":
            n = int(command[1])
            deque.append(n)
            print("ok")
        elif command[0] == "pop_front":
            if deque:
                print(deque[0])
                deque.pop(0)
            else:
                print("error")
        elif command[0] == "pop_back":
            if deque:
                print(deque[-1])
                deque.pop()
            else:
                print("error")
        elif command[0] == "front":
            if deque:
                print(deque[0])
            else:
                print("error")
        elif command[0] == "back":
            if deque:
                print(deque[-1])
            else:
                print("error")
        elif command[0] == "size":
            print(len(deque))
        elif command[0] == "clear":
            deque.clear()
            print("ok")
        elif command[0] == "exit":
            print("bye")
            break
