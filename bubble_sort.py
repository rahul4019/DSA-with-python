# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#
#     return arr


def bubble_sort(arr):
    flag = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1

        if flag == 0:
            break

    return arr


# print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([5, 4, 3, 2, 1]))
# print(bubble_sort([10, 4, 9, 27, 18, 29, 30]))
