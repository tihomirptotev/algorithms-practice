from typing import List, Sequence


def bubble_sort(arr: List):
    last_index = len(arr) - 1
    for c in range(last_index, 0, -1):
        for i in range(c):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def insertion_sort(arr: List):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i
        while arr[position - 1] > current and position > 0:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current

    return arr


def merge_sort(input_list: List):
    pass
