with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    y_coord = contents[2 : (2 * N + 1) : 2]
    M = contents[2 * N + 1]
    start = contents[(2 * N + 2) :: 2]
    end = contents[(2 * N + 3) :: 2]
    for start, end in zip(start, end):
        max_height = 0
        if start < end:
            first = last = start - 1
            while last < end - 1:
                while last < end - 1 and y_coord[last + 1] > y_coord[last]:
                    last += 1
                max_height_now = y_coord[last] - y_coord[first]
                max_height += max_height_now
                while last < end - 1 and y_coord[last + 1] < y_coord[last]:
                    last += 1
                first = last
            print(max_height)
        elif start > end:
            first = last = end - 1
            while last < start - 1:
                while last < start - 1 and y_coord[last + 1] < y_coord[last]:
                    last += 1
                max_height_now = y_coord[first] - y_coord[last]
                max_height += max_height_now
                while last < start - 1 and y_coord[last + 1] > y_coord[last]:
                    last += 1
                first = last
            print(max_height)
        elif start == end:
            print("0")
