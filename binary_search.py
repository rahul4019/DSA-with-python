def binary_search(list, low, high, target):
    # base case
    if low <= high:
        return -1

    mid = int((low + high) / 2)
    print("mid: ", mid)

    if list[mid] == target:
        return mid

    elif list[mid] < target:
        low = mid + 1

    elif list[mid] > target:
        high = mid - 1

    return binary_search(list, low, high, target)


print(binary_search([1, 2, 3, 4, 5], 0, 5, 200))
