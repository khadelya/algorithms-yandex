# отсортировать классы
# отсортировать пары кондициореров по мощности
# для каждого отсортированного класса двигать last пока условие по мощности не выполнится
with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    n = contents[0]
    classes = sorted(contents[1 : n + 1])
    m = contents[n + 1]
    power = contents[n + 2 :: 2]
    price = contents[n + 3 :: 2]
    power_price = sorted(list(zip(power, price)), key=lambda x: x[1])
    last = 0
    overall_cost = 0
    for cls in classes:
        while last + 1 < m and power_price[last][0] < cls:
            last += 1
        overall_cost += power_price[last][1]
    print(overall_cost)
