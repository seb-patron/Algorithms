import pytest
from selection_sort import selection_sort

def test_selection_sort_unsorted_array():
    array = [5, 3, 6, 2, 10]
    assert selection_sort(array.copy()) == [2, 3, 5, 6, 10]  # Should sort in ascending order

def test_selection_sort_already_sorted():
    array = [1, 2, 3, 4, 5]
    assert selection_sort(array.copy()) == [1, 2, 3, 4, 5]  # Already sorted array

def test_selection_sort_reverse_sorted():
    array = [5, 4, 3, 2, 1]
    assert selection_sort(array.copy()) == [1, 2, 3, 4, 5]  # Reverse sorted array

def test_selection_sort_empty_array():
    array = []
    assert selection_sort(array.copy()) == []  # Empty array should return empty array

def test_selection_sort_single_element():
    array = [42]
    assert selection_sort(array.copy()) == [42]  # Single element array

def test_selection_sort_duplicate_elements():
    array = [3, 1, 3, 2, 5, 1]
    assert selection_sort(array.copy()) == [1, 1, 2, 3, 3, 5]  # Array with duplicate elements

