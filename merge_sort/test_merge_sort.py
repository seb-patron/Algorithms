import pytest
from merge_sort import merge_sort

def test_merge_sort_unsorted_array():
    array = [5, 3, 6, 2, 10]
    assert merge_sort(array.copy()) == [2, 3, 5, 6, 10]  # Should sort in ascending order

def test_merge_sort_already_sorted():
    array = [1, 2, 3, 4, 5]
    assert merge_sort(array.copy()) == [1, 2, 3, 4, 5]  # Already sorted array

def test_merge_sort_reverse_sorted():
    array = [5, 4, 3, 2, 1]
    assert merge_sort(array.copy()) == [1, 2, 3, 4, 5]  # Reverse sorted array

def test_merge_sort_empty_array():
    array = []
    assert merge_sort(array.copy()) == []  # Empty array should return empty array

def test_merge_sort_single_element():
    array = [42]
    assert merge_sort(array.copy()) == [42]  # Single element array

def test_merge_sort_duplicate_elements():
    array = [3, 1, 3, 2, 5, 1]
    assert merge_sort(array.copy()) == [1, 1, 2, 3, 3, 5]  # Array with duplicate elements

def test_merge_sort_negative_numbers():
    array = [5, -1, 3, -7, 0, 10]
    assert merge_sort(array.copy()) == [-7, -1, 0, 3, 5, 10]  # Array with negative numbers

def test_merge_sort_large_array():
    array = list(range(100, 0, -1))  # 100 down to 1
    assert merge_sort(array.copy()) == list(range(1, 101))  # Large array (100 elements)

def test_merge_sort_same_elements():
    array = [4, 4, 4, 4, 4]
    assert merge_sort(array.copy()) == [4, 4, 4, 4, 4]  # Array with all same elements 