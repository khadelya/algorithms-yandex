with open("input.txt", "r") as file:
    a, b, c = list(map(int, file.read().split()))
    initial_sum = 2 * a + 3 * b + 4 * c
    divisor = a + b + c
    if initial_sum / divisor < 3.5:
        left = 0
        right = divisor
        while left < right:
            middle = (left + right) // 2
            if (initial_sum + 5 * middle) >= 3.5 * (divisor + middle):
                right = middle
            else:
                left = middle + 1
        print(left)
    else:
        print(0)
