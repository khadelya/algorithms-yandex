with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N, M = contents[0], contents[1]
    observation_start = contents[2::2]
    observation_end = contents[3::2]
    observed_students = []
    for i in range(M):
        observed_students.append((observation_start[i], "start"))
        observed_students.append((observation_end[i], "end"))
    observed_students.sort()
    observers_count = 0
    students = observed_students[0][0]
    students += N - 1 - observed_students[-1][0]
    for i in range(len(observed_students)):
        if (
            observers_count == 0
            and i != 0
            and observed_students[i][0] != observed_students[i - 1][0]
        ):
            students += observed_students[i][0] - observed_students[i - 1][0] - 1
        if observed_students[i][1] == "start":
            observers_count += 1
        elif observed_students[i][1] == "end":
            observers_count -= 1
    print(students)
