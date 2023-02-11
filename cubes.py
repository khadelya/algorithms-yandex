with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    n, m = contents[:2]
    seq1 = set(contents[2 : 2 + n])
    seq2 = set(contents[2 + n :])
    intsc = sorted(seq1.intersection(seq2))
    diff1 = sorted(seq1.difference(intsc))
    diff2 = sorted(seq2.difference(intsc))
    output = [intsc, diff1, diff2]
    ans = ""
    for item in output:
        ans += str(len(item)) + "\n"
        ans += " ".join(map(str, item)) + "\n"
with open("output.txt", "w") as file:
    file.write(ans)
