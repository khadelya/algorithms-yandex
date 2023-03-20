with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    K = contents[1]
    seq = contents[2:]
    first = last = 0
    all_trees_set = set(range(1, K + 1))
    smallest_segment_len = N
    set_now = set()
    while first <= last and last < N:
        set_now.add(seq[first])
        while last + 1 < N and set_now != all_trees_set:
            last += 1
            while first < last and seq[last] == seq[first]:
                first += 1
            set_now.add(seq[last])
        segment_len = last - first
        if segment_len < smallest_segment_len and set_now == all_trees_set:
            ans = [first + 1, last + 1]
            smallest_segment_len = segment_len
        set_now.remove(seq[first])
        first += 1
    print(*ans)
