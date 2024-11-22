import random
import time


def is_sorted(list):

    if len(list) == 0:
        return True

    i = 0
    j = 1

    while i < len(list) - 1 and j < len(list):
        if list[i] > list[j]:
            return False

        i += 1
        j += 1

    return True


# print(is_sorted([5, 2, 3, 4, 5]))
# print(is_sorted([1, 2, 3, 4, 5]))
# print(is_sorted([]))


def monkey_sort(arr):

    while not is_sorted(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)

    print(arr)


monkey_sort([7, 4, 2, 3, 9])
