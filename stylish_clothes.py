with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N = contents[0]
    seq1 = contents[1 : N + 1]
    M = contents[N + 1]
    seq2 = contents[N + 2 :]
    difference = {}
    first = last = 0
    while first < N and last < M:
        if seq1[first] < seq2[last]:
            while first < N - 1 and seq1[first + 1] < seq2[last]:
                first += 1
            min_diff_now = seq2[last] - seq1[first]
            difference[min_diff_now] = [seq1[first], seq2[last]]
            first += 1
        elif seq1[first] > seq2[last]:
            while last < M - 1 and seq2[last + 1] < seq1[first]:
                last += 1
            min_diff_now = seq1[first] - seq2[last]
            difference[min_diff_now] = [seq1[first], seq2[last]]
            last += 1
        elif seq1[first] == seq2[last]:
            difference[0] = [seq1[first], seq2[last]]
            break
    ans = difference[min(difference)]
    print(*ans)
