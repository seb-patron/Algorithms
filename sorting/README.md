# Sorting Algorithms

This directory contains implementations of various sorting algorithms in Python. Each algorithm is organized into its own folder with implementation and test files.

## Sorting Algorithms Overview

### 1. **Quick Sort**
   - **Description**: Quick sort is a divide-and-conquer sorting algorithm. It works by selecting a pivot and partitioning the array around the pivot.
   - **How It Works**:
     - Select a pivot element.
     - Partition the array such that elements less than the pivot are on the left, and elements greater are on the right.
     - Recursively apply the above steps to the subarrays.
   - **Big O Complexity**:
     - Time: \( O(n \log n) \) on average; \( O(n^2) \) in the worst case.
     - Space: \( O(\log n) \)
   - **File**: [quick_sort.py](quick_sort/quick_sort.py)

### 2. **Merge Sort**
   - **Description**: Merge sort is a divide-and-conquer algorithm that splits the array into halves, sorts each half, and then merges them back together.
   - **How It Works**:
     - Divide the array into two halves.
     - Recursively sort each half.
     - Merge the two sorted halves into a single sorted array.
   - **Big O Complexity**:
     - Time: \( O(n \log n) \)
     - Space: \( O(n) \)
   - **File**: [merge_sort.py](merge_sort/merge_sort.py)

### 3. **Selection Sort**
   - **Description**: Selection sort is a slow sorting algorithm that checks each element in an array for the smallest element, removes it from the current array and adds it to a new array, and repeats until there are no more elements in the previous array.
   - **How It Works**:
     - Find the smallest element in current array.
     - Remove element from current array and add it to new array.
     - Repeat until there are no more elements in previous array.
   - **Big O Complexity**:
     - Time: \( O(n^2) \)
     - Space: \( O(n) \)
   - **File**: [selection_sort.py](selection_sort/selection_sort.py)

### 4. **Insertion Sort**
   - **Description**: Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
   - **How It Works**:
     - Start with the second element.
     - Compare it with the elements before it and insert it at the correct position.
     - Repeat for all elements in the array.
   - **Big O Complexity**:
     - Time: \( O(n^2) \) in the worst case; \( O(n) \) for nearly sorted arrays.
     - Space: \( O(1) \)
   - **File**: [insertion_sort.py](insertion_sort/insertion_sort.py)

### 5. **Tim Sort**
   - **Description**: Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data.
   - **How It Works**:
     - Divide the array into small chunks (runs).
     - Sort these runs using insertion sort.
     - Merge the sorted runs using a merge sort approach.
   - **Big O Complexity**:
     - Time: \( O(n \log n) \) in the worst case; \( O(n) \) for nearly sorted arrays.
     - Space: \( O(n) \)
   - **File**: [simplified_timsort.py](timsort/simplified_timsort.py)
   - **More Details**: [Tim Sort README](timsort/README.md)

## Sorting Algorithm Complexity Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|-----------|-----------|--------------|------------|------------------|
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(n) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) |

**Note**: Although Tim Sort shares the same worst-case time complexity as Merge Sort (O(n log n)), its constants are lower due to optimizations like using insertion sort for small runs and taking advantage of pre-existing order in the data. This makes Tim Sort significantly faster in practice, especially for real-world data that often has some inherent order.

## Sorting Algorithm Performance Testing

This directory includes a performance testing framework for comparing the efficiency of different sorting algorithms. The framework allows you to:

1. Test the performance of each sorting algorithm on the same random array
2. Run multiple tests with different arrays and calculate average performance
3. Compare performance across different array sizes
4. Test how algorithms perform with different data distributions (random, nearly sorted, reverse sorted, etc.)
5. Visualize results with charts and graphs

### Running Performance Tests

The performance testing framework provides several scripts for different types of tests:

#### Run a Single Test

Test all sorting algorithms on a single random array:

```bash
python sorting_performance/run_single_test.py --size 10000
```

#### Run Multiple Tests

Run multiple tests and calculate statistics:

```bash
python sorting_performance/run_multiple_tests.py --size 10000 --tests 10
```

#### Compare Different Array Sizes

Compare performance across different array sizes:

```bash
python sorting_performance/compare_sizes.py --sizes 1000 5000 10000 20000 --tests 5
```

#### Compare Different Data Distributions

Test how algorithms perform with different data distributions:

```bash
python sorting_performance/compare_distributions.py --size 10000 --tests 5
```

#### Run All Tests

Run all performance tests with a single command:

```bash
python sorting_performance/run_all_tests.py --size 10000 --tests 5
```

### Adding New Sorting Algorithms

To add a new sorting algorithm to the performance tests:

1. Implement your sorting algorithm in a separate module
2. Import your sorting function in `sorting_performance/performance_test.py`
3. Add your sorting function to the `SORTING_ALGORITHMS` dictionary

For more details, see the [Sorting Performance README](sorting_performance/README.md). 