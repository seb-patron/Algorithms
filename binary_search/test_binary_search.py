import pytest
from binary_search import binary_search

def test_binary_search_found():
    array = [1, 3, 5, 7, 9]
    target = 5
    assert binary_search(array, target) == 2  # Target is at index 2

def test_binary_search_not_found():
    array = [1, 3, 5, 7, 9]
    target = 4
    assert binary_search(array, target) == None  # Target is not in the array

def test_binary_search_empty_array():
    array = []
    target = 1
    assert binary_search(array, target) == None  # Empty array should return -1

def test_binary_search_single_element_found():
    array = [42]
    target = 42
    assert binary_search(array, target) == 0  # Single element match

def test_binary_search_single_element_not_found():
    array = [42]
    target = 13
    assert binary_search(array, target) == None  # Single element mismatch