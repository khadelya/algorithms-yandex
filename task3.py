from itertools import permutations
N,M = map(int, (input().split()))
words = []
for _ in range(N):
    words.append(list(input()))
ans = False
for permutation in permutations(list(range(N))):
    ans_p = []
    for i in range(N - 1):
        diff = 0
        for j in range(M):
            if words[permutation[i]][j] != words[permutation[i + 1]][j]:
                diff += 1
        if diff == 1:
            ans_p.append(True)
        else:
            ans_p.append(False)
    if all(ans_p):
        ans = True
if ans:
    print('Yes')
else:
    print('No')
