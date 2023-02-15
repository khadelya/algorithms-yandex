def check_case(word):
    word_case = 0
    for character in word:
        if character.isupper():
            word_case += 1
    return word_case


with open("input.txt", "r") as file:
    content = file.read().split()
    n = int(content[0])
    words_for_dct = content[1 : n + 1]
    words_for_check = content[n + 1 :]
    dct = {}
    ans = 0
    for word in words_for_dct:
        word_l = word.lower()
        if word_l not in dct:
            dct[word_l] = set()
        dct[word_l].add(word)
    for word in words_for_check:
        word_l = word.lower()
        if word_l in dct:
            if word not in dct[word_l]:
                ans += 1
        else:
            word_case = check_case(word)
            if (word_case == 0) or (word_case > 1):
                ans += 1
    print(ans)
