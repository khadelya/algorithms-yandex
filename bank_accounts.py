from math import floor

with open("input.txt", "r") as file:
    contents = file.readlines()
    dct = {}
    operation = []
    for line in contents:
        operation = line.split()
        if operation[0] == "DEPOSIT":
            user = operation[1]
            sum = int(operation[2])
            if user not in dct:
                dct[user] = 0
            dct[user] += sum
        elif operation[0] == "WITHDRAW":
            user = operation[1]
            sum = int(operation[2])
            if user not in dct:
                dct[user] = 0
            dct[user] -= sum
        elif operation[0] == "BALANCE":
            user = operation[1]
            if user in dct:
                print(dct[user])
            else:
                print("ERROR")
        elif operation[0] == "TRANSFER":
            user1 = operation[1]
            user2 = operation[2]
            sum = int(operation[3])
            if user1 not in dct:
                dct[user1] = 0
            dct[user1] -= sum
            if user2 not in dct:
                dct[user2] = 0
            dct[user2] += sum
        elif operation[0] == "INCOME":
            percentage = int(operation[1])
            for user in dct:
                current_sum = dct[user]
                if current_sum > 0:
                    dct[user] = floor(current_sum * (1 + percentage / 100))
