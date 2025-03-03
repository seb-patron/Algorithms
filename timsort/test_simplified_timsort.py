import pytest
from simplified_timsort import simplified_timsort

def test_simplified_timsort_unsorted_array():
    array = [5, 3, 6, 2, 10]
    assert simplified_timsort(array.copy()) == [2, 3, 5, 6, 10]  # Should sort in ascending order

def test_simplified_timsort_already_sorted():
    array = [1, 2, 3, 4, 5]
    assert simplified_timsort(array.copy()) == [1, 2, 3, 4, 5]  # Already sorted array

def test_simplified_timsort_reverse_sorted():
    array = [5, 4, 3, 2, 1]
    assert simplified_timsort(array.copy()) == [1, 2, 3, 4, 5]  # Reverse sorted array

def test_simplified_timsort_empty_array():
    array = []
    assert simplified_timsort(array.copy()) == []  # Empty array should return empty array

def test_simplified_timsort_single_element():
    array = [42]
    assert simplified_timsort(array.copy()) == [42]  # Single element array

def test_simplified_timsort_duplicate_elements():
    array = [3, 1, 3, 2, 5, 1]
    assert simplified_timsort(array.copy()) == [1, 1, 2, 3, 3, 5]  # Array with duplicate elements

def test_simplified_timsort_negative_numbers():
    array = [5, -1, 3, -7, 0, 10]
    assert simplified_timsort(array.copy()) == [-7, -1, 0, 3, 5, 10]  # Array with negative numbers

def test_simplified_timsort_same_elements():
    array = [4, 4, 4, 4, 4]
    assert simplified_timsort(array.copy()) == [4, 4, 4, 4, 4]  # Array with all same elements

# Tests for arrays larger than min_run (32)
def test_simplified_timsort_exactly_min_run():
    array = list(range(32, 0, -1))  # 32 down to 1
    assert simplified_timsort(array.copy()) == list(range(1, 33))  # Exactly min_run elements

def test_simplified_timsort_larger_than_min_run():
    array = list(range(65, 0, -1))  # 65 down to 1
    assert simplified_timsort(array.copy()) == list(range(1, 66))  # Larger than min_run (65 elements)

def test_simplified_timsort_multiple_min_runs():
    array = list(range(131, 0, -1))  # 131 down to 1
    assert simplified_timsort(array.copy()) == list(range(1, 132))  # Multiple min_runs (131 elements)

def test_simplified_timsort_random_large_array():
    import random
    random.seed(42)  # For reproducibility
    array = random.sample(range(1, 1000), 100)
    sorted_array = sorted(array.copy())
    assert simplified_timsort(array.copy()) == sorted_array  # Random large array 