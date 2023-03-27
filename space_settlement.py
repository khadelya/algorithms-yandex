with open("input.txt", "r") as file:
    n, a, b, w, h = list(map(int, file.read().split()))
    if min(a, b) + 2 > min(w, h) or max(a, b) + 2 > max(w, h) or a * b * n == w * h:
        print("0")
    else:
        max_size = min(w, h) // 2
        left = 0
        right = max_size
        while left < right:
            middle = (left + right + 1) // 2
            if (
                max(
                    (w // (a + 2 * middle)) * (h // (b + 2 * middle)),
                    (w // (b + 2 * middle)) * (h // (a + 2 * middle)),
                )
                >= n
            ):
                left = middle
            else:
                right = middle - 1
        print(left)
