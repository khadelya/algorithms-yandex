with open("input.txt", "r") as file:
    contents = file.read().split()
    first_word = contents[1:-1:2]
    second_word = contents[2:-1:2]
    target_word = contents[-1]
    dct1 = dict(zip(first_word, second_word))
    dct2 = dict(zip(second_word, first_word))
    if target_word in first_word:
        ans = dct1[target_word]
    else:
        ans = dct2[target_word]

with open("output.txt", "w") as file:
    file.write(ans)
