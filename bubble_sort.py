def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


# print(bubble_sort([5, 4, 3, 2, 1]))
# print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([10, 4, 9, 27, 18, 29, 30]))
