def binary_search(list, start, size, target):
    # base case
    if size <= 0:
        return -1

    mid = int((start + size) / 2)
    print("mid: ", mid)

    if list[mid] == target:
        return mid

    elif list[mid] < target:
        start = mid + 1

    elif list[mid] > target:
        size = mid - 1

    return binary_search(list, start, size, target)


print(binary_search([1, 2, 3, 4, 5], 0, 5, 5))
