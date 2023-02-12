with open("input.txt", "r") as file:
    contents = file.read().split()
    ans = [0 for _ in range(len(contents))]
    for i, word in enumerate(contents):
        previous_words = contents[:i]
        if word in set(previous_words):
            for previous_word in previous_words:
                if previous_word == word:
                    ans[i] += 1
    ans = " ".join(map(str, ans))
with open("output.txt", "w") as file:
    file.write(ans)
