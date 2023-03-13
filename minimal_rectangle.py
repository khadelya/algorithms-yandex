with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    x_list = contents[1::2]
    y_list = contents[2::2]
    print(f"{min(x_list)} {min(y_list)} {max(x_list)} {max(y_list)}")
