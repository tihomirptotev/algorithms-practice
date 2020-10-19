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
        current = arr[i]
        position = i
        while arr[position - 1] > current and position > 0:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current

    return arr
