from typing import List, Sequence


def bubble_sort(input_array: Sequence) -> List:
    arr = list(input_array)

    last_index = len(arr) - 1

    for c in range(last_index, 0, -1):
        for i in range(c):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def insertion_sort(input_array: Sequence) -> List:
    arr = list(input_array)

    for i in range(1, len(arr)):
        current = arr.pop(i)
        counter = 0
        while arr[i] > arr[counter] and counter < i:
            counter += 1
        arr.insert(counter, current)

    return arr
