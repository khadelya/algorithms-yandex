# делаю список
# убираю первый элемент
# проверить while
with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    K = contents[1]
    seq = contents[2:]
    first = last = 0
    all_trees_set = set(range(1, K + 1))
    list_set_now = [seq[first]]
    smallest_segment_len = N
    while first < N and smallest_segment_len > K - 1:
        while last + 1 < N and set(list_set_now) != all_trees_set:
            last += 1
            list_set_now.append(seq[last])
            if seq[last] == seq[first]:
                first += 1
                list_set_now.pop(0)
        segment_len = last - first
        if segment_len < smallest_segment_len and set(list_set_now) == all_trees_set:
            ans = [first + 1, last + 1]
            smallest_segment_len = segment_len
        first += 1
        list_set_now.pop(0)
    print(*ans)
