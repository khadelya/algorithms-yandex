with open("input.txt", "r") as file:
    seq1, seq2 = file.read().split()
    gen = []
    for i in range(len(seq2[:-1])):
        gen.append(seq2[i] + seq2[i + 1])
    gen = set(gen)
    ans = 0
    for i in range(len(seq1[:-1])):
        if (seq1[i] + seq1[i + 1]) in gen:
            ans += 1
with open("output.txt", "w") as file:
    file.write(str(ans))
