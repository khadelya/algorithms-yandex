def sort2(a, b):
    if a > b:
        a, b = b, a
    return a, b


with open("input.txt", "r") as file:
    contents = file.read().split()
    seq = [int(x) for x in contents]
    a, b, c = seq[0], seq[1], seq[2]
    a, b = sort2(a, b)
    b, c = sort2(b, c)
    a, b = sort2(a, b)
    max3, max2, max1 = a, b, c
    if len(seq) > 3:
        for item in seq[3:]:
            if item > max1:
                max3 = max2
                max2 = max1
                max1 = item
            elif item > max2:
                max3 = max2
                max2 = item
            elif item > max3:
                max3 = item
        min1, min2 = a, b
        for item in seq[3:]:
            if item < min1:
                min2 = min1
                min1 = item
            elif item < min2:
                min2 = item
        if (min1 * min2 > max2 * max3) and (max1 > 0):
            max3 = min1
            max2 = min2
    print(max1, max2, max3)
