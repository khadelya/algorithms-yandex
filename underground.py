with open("input.txt", "r") as file:
    contents = file.readlines()
    stack = []
    train = {}
    for line in contents[1:]:
        command = line.split()
        if command[0] == "add":
            product = command[2]
            num = int(command[1])
            stack += [product] * num
            if product not in train:
                train[product] = 0
            train[product] += num
        elif command[0] == "delete":
            num = int(command[1])
            for _ in range(num):
                last_element = stack.pop()
                train[last_element] -= 1
        elif command[0] == "get":
            product = command[1]
            if product in train:
                print(train[product])
            else:
                print("0")
