with open("input.txt", "r") as file:
    contents = file.read().splitlines()
    seq1 = set([int(x) for x in contents[0].split()])
    seq2 = set([int(x) for x in contents[1].split()])
    ans = " ".join(map(str, sorted(seq1.intersection(seq2))))
with open("output.txt", "w") as file:
    file.write(ans)
