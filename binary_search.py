# левая правая граница
# пока левая меньше правой
# делим пополам
# если условие, то двигаем л
with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N, K = contents[0], contents[1]
    arr1 = contents[2 : N + 2]
    arr2 = contents[N + 2 :]
    smallest_num = arr1[0]
    largest_num = arr1[-1]
    for num in arr2:
        if num >= smallest_num and num <= largest_num:
            left = 0
            right = N - 1
            while left < right:
                middle = (left + right) // 2
                if arr1[middle] >= num:
                    right = middle
                else:
                    left = middle + 1
            if arr1[left] == num:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
