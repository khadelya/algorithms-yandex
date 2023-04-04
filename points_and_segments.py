with open("input.txt", "r") as file:
    contents = file.readlines()
    n, m = map(int, contents[0].split())
    events = []
    for line in contents[1:-1]:
        a, b = map(int, line.split())
        events.append((min(a, b), "1_start"))
        events.append((max(a, b), "3_end"))
    points = list(map(int, contents[-1].split()))
    for point in points:
        events.append((point, "2_point"))
    events.sort()
    num_of_segments = {}
    segments = 0
    for event in events:
        if event[1] == "1_start":
            segments += 1
        elif event[1] == "2_point":
            if event[0] not in num_of_segments:
                num_of_segments[event[0]] = 0
            num_of_segments[event[0]] = segments
        elif event[1] == "3_end":
            segments -= 1
    for point in points:
        print(num_of_segments[point], end=" ")
