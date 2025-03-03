# Algorithm Implementations with Python

This repository contains Python implementations of fundamental algorithms. Each algorithm is organized into its own folder with a `.py` file, making it easy to understand and test. Testing is automated with `pytest`, and the project dependencies are managed using `poetry`.

## Algorithms

### 1. **Binary Search**
   - **Description**: Binary search is an efficient algorithm for finding the position of a target value within a sorted array. It repeatedly divides the search interval in half.
   - **How It Works**:
     - Start with the middle element of the array.
     - If the target value matches the middle element, return its index.
     - If the target value is smaller, repeat the search on the left half.
     - If larger, repeat on the right half.
   - **Big O Complexity**:
     - Time: \( O(\log n) \)
     - Space: \( O(1) \)
   - **File**: [binary_search.py](binary_search/binary_search.py)

### 2. **Quick Sort**
   - **Description**: Quick sort is a divide-and-conquer sorting algorithm. It works by selecting a pivot and partitioning the array around the pivot.
   - **How It Works**:
     - Select a pivot element.
     - Partition the array such that elements less than the pivot are on the left, and elements greater are on the right.
     - Recursively apply the above steps to the subarrays.
   - **Big O Complexity**:
     - Time: \( O(n \log n) \) on average; \( O(n^2) \) in the worst case.
     - Space: \( O(\log n) \)
   - **File**: [quick_sort.py](quick_sort/quick_sort.py)

### 3. **Merge Sort**
   - **Description**: Merge sort is a divide-and-conquer algorithm that splits the array into halves, sorts each half, and then merges them back together.
   - **How It Works**:
     - Divide the array into two halves.
     - Recursively sort each half.
     - Merge the two sorted halves into a single sorted array.
   - **Big O Complexity**:
     - Time: \( O(n \log n) \)
     - Space: \( O(n) \)
   - **File**: [merge_sort.py](merge_sort/merge_sort.py)


### 4. **Selection Sort**
   - **Description**: Selection sort is a slow sorting algorithm that checks each element in an array for the smallest element, removes it from the current array and adds it to a new array, and repeats until there are no more elements in the previous array.
   - **How It Works**:
     - Find the smallest element in current array.
     - Remove element from current array and add it to new array.
     - Repeat until there are no more elements in previous array.
   - **Big O Complexity**:
     - Time: \( O(n^2) \)
     - Space: \( O(n) \)
   - **File**: [selection_sort.py](selection_sort/selection_sort.py)

### 5. **Breadth-First Search (BFS)**
   - **Description**: BFS is an algorithm for traversing or searching tree or graph structures. It explores all neighbors at the present depth before moving on to nodes at the next depth level.
   - **How It Works**:
     - Use a queue to explore nodes level by level.
     - Start at the root node and enqueue it.
     - Dequeue a node, process it, and enqueue its unvisited neighbors.
   - **Big O Complexity**:
     - Time: \( O(V + E) \), where \( V \) is the number of vertices and \( E \) is the number of edges.
     - Space: \( O(V) \)
   - **File**: [breadth_first_search.py](breadth_first_search/breadth_first_search.py)

### 6. **Dijkstra's Algorithm**
   - **Description**: Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph.
   - **How It Works**:
     - Initialize distances to all nodes as infinity, except the source node (distance = 0).
     - Use a priority queue to process the node with the smallest distance.
     - Update the distance to each neighbor if a shorter path is found.
   - **Big O Complexity**:
     - Time: \( O((V + E) \log V) \)
     - Space: \( O(V) \)
   - **File**: [dijkstras_algorithm.py](dijkstras_algorithm/dijkstras_algorithm.py)

## Sorting Algorithm Performance Testing

This repository includes a performance testing framework for comparing the efficiency of different sorting algorithms. The framework allows you to:

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

## Testing with Pytest

This project uses `pytest` to automate testing. Each algorithm has corresponding test cases to ensure correctness. To run the tests:

1. Ensure you are in the root directory of the project.
2. Run the following command:

   ```bash
   pytest
   ```

   Or, if you're using Poetry:

   ```bash
   poetry run pytest
   ```

   For more detailed test output, use the verbose flag:

   ```bash
   poetry run pytest -v
   ```

Pytest will execute all test files in the repository and report the results.

## Managing Dependencies with Poetry

Poetry is used to manage project dependencies and virtual environments.

### Setup Instructions

1. **Install Poetry**:
   Follow the [official Poetry installation guide](https://python-poetry.org/docs/#installation).

2. **Install Dependencies**:
   Run the following command in the project directory:

   ```bash
   poetry install
   ```

3. **Activate the Virtual Environment**:
   Use the following command to activate Poetry's virtual environment:

   ```bash
   poetry shell
   ```

4. **Run Tests or Scripts**:
   Once the environment is activated, you can run scripts or tests seamlessly.

---

Happy coding and learning!