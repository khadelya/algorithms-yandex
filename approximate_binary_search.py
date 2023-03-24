with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    N, K = contents[0], contents[1]
    arr1 = contents[2 : N + 2]
    arr2 = contents[N + 2 :]
    smallest_num = arr1[0]
    largest_num = arr1[-1]
    for num in arr2:
        if num <= smallest_num:
            print(smallest_num)
        elif num >= largest_num:
            print(largest_num)
        else:
            left = 0
            right = N - 1
            while left < right:
                middle = (left + right) // 2
                if arr1[middle] >= num:
                    right = middle
                else:
                    left = middle + 1
            closest_larger_num = arr1[left]
            closest_smaller_num = arr1[left - 1]
            if num - closest_smaller_num <= closest_larger_num - num:
                print(closest_smaller_num)
            else:
                print(closest_larger_num)
