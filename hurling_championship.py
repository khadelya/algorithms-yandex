with open("input.txt", "r") as file:
    contents = file.read().split()
    lst = [int(x) for x in contents[1:]]
    ans = 0
    score = []
    min_lst = min(lst)
    max_lst = max(lst)
    max_lst_ind_1 = -1
    max_lst_ind_2 = len(lst)
    for i in range(len(lst)):
        if (lst[i] == max_lst) and (max_lst_ind_1 == -1):
            max_lst_ind_1 = i
        if (lst[i] == max_lst) and (max_lst_ind_1 > 0) and (max_lst_ind_2 == -1):
            max_lst_ind_2 = i

    for i in range(1, len(lst[:-1])):
        if (
            (str(lst[i])[-1] == "5")
            and (max_lst_ind_1 < max_lst_ind_2)
            and (lst[i + 1] == min_lst)
        ):
            score.append(lst[i])
    if len(score) > 0:
        ans = 1
        score_vas = max(score)
        for i in range(len(lst)):
            if lst[i] > score_vas:
                ans += 1

with open("output.txt", "w") as file:
    file.write(str(ans))
