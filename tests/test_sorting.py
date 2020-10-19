import pytest
from src import sorting


@pytest.mark.parametrize(
    "input_array", [[1, 9, 2, 5, 9, 3, 7, 16, 10, 8], ["a", "f", "d", "c"], []],
)
def test_bubble_sort(input_array):
    expected = sorted(input_array)
    sorting.bubble_sort(input_array)
    assert input_array == expected


@pytest.mark.parametrize(
    "input_array", [[1, 9, 2, 5, 9, 3, 7, 16, 10, 8], ["a", "f", "d", "c"], []],
)
def test_insertion_sort(input_array):
    expected = sorted(input_array)
    sorting.insertion_sort(input_array)
    assert input_array == expected
