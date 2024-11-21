def recursive_binary_search(list, low, high, target):
    # base case
    if low <= high:
        return -1

    mid = int((low + high) / 2)

    if list[mid] == target:
        return mid

    elif list[mid] < target:
        low = mid + 1

    elif list[mid] > target:
        high = mid - 1

    return recursive_binary_search(list, low, high, target)


# print(recursive_binary_search([1, 2, 3, 4, 5], 0, 5, 200))


def binary_search(list, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        print("mid: ", mid)

        if list[mid] == target:
            return mid

        elif list[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    # not found in the list
    return -1


print(binary_search([1, 2, 3, 4, 5], 0, 5, 7))
