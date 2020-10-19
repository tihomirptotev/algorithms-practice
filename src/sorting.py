from typing import List, Sequence


def bubble_sort(input_array: Sequence) -> List:
    arr = list(input_array)

    last_index = len(arr) - 1

    for c in range(last_index, 0, -1):
        for i in range(c):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr
