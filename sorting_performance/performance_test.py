import time
import random
import statistics
import sys
import os
import matplotlib.pyplot as plt
from typing import Callable, Dict, List, Tuple

# Add parent directory to path to import sorting modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import sorting algorithms
from insertion_sort.insertion_sort import insertion_sort
from quick_sort.quick_sort import quick_sort
from merge_sort.merge_sort import merge_sort
from selection_sort.selection_sort import selection_sort
from timsort.simplified_timsort import simplified_timsort

# Dictionary of sorting algorithms
SORTING_ALGORITHMS: Dict[str, Callable] = {
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Selection Sort": selection_sort,
    "Tim Sort": simplified_timsort,
    # Add new sorting algorithms here as you implement them
    # "Heap Sort": heap_sort,
    # "Intro Sort": intro_sort,
}

def generate_random_array(size: int, min_val: int = 0, max_val: int = 1000) -> List[int]:
    """Generate a random array of integers."""
    return [random.randint(min_val, max_val) for _ in range(size)]

def test_sorting_algorithm(sort_func: Callable, array: List[int]) -> float:
    """Test the performance of a sorting algorithm on a given array.
    
    Args:
        sort_func: The sorting function to test
        array: The array to sort (will be copied to avoid modifying the original)
        
    Returns:
        float: The time taken to sort the array in seconds
    """
    # Create a copy of the array to avoid modifying the original
    test_array = array.copy()
    
    # Measure the time taken to sort the array
    start_time = time.time()
    sort_func(test_array)
    end_time = time.time()
    
    return end_time - start_time

def run_single_test(array_size: int = 10000) -> Dict[str, float]:
    """Run a single test for all sorting algorithms on the same random array.
    
    Args:
        array_size: The size of the random array to generate
        
    Returns:
        Dict[str, float]: A dictionary mapping algorithm names to execution times
    """
    # Generate a random array
    array = generate_random_array(array_size)
    
    # Test each sorting algorithm
    results = {}
    for name, sort_func in SORTING_ALGORITHMS.items():
        execution_time = test_sorting_algorithm(sort_func, array)
        results[name] = execution_time
        print(f"{name}: {execution_time:.6f} seconds")
    
    return results

def run_multiple_tests(num_tests: int = 100, array_size: int = 10000) -> Dict[str, List[float]]:
    """Run multiple tests for all sorting algorithms and collect execution times.
    
    Args:
        num_tests: The number of tests to run
        array_size: The size of the random arrays to generate
        
    Returns:
        Dict[str, List[float]]: A dictionary mapping algorithm names to lists of execution times
    """
    # Initialize results dictionary
    results = {name: [] for name in SORTING_ALGORITHMS.keys()}
    
    # Run tests
    for i in range(num_tests):
        print(f"\nTest {i+1}/{num_tests}")
        array = generate_random_array(array_size)
        
        for name, sort_func in SORTING_ALGORITHMS.items():
            execution_time = test_sorting_algorithm(sort_func, array)
            results[name].append(execution_time)
            print(f"{name}: {execution_time:.6f} seconds")
    
    return results

def calculate_statistics(results: Dict[str, List[float]]) -> Dict[str, Dict[str, float]]:
    """Calculate statistics for the test results.
    
    Args:
        results: A dictionary mapping algorithm names to lists of execution times
        
    Returns:
        Dict[str, Dict[str, float]]: A dictionary mapping algorithm names to statistics
    """
    stats = {}
    
    for name, times in results.items():
        stats[name] = {
            "min": min(times),
            "max": max(times),
            "mean": statistics.mean(times),
            "median": statistics.median(times),
            "stdev": statistics.stdev(times) if len(times) > 1 else 0
        }
    
    return stats

def print_statistics(stats: Dict[str, Dict[str, float]]) -> None:
    """Print statistics for the test results."""
    print("\nStatistics:")
    for name, algorithm_stats in stats.items():
        print(f"\n{name}:")
        print(f"  Min: {algorithm_stats['min']:.6f} seconds")
        print(f"  Max: {algorithm_stats['max']:.6f} seconds")
        print(f"  Mean: {algorithm_stats['mean']:.6f} seconds")
        print(f"  Median: {algorithm_stats['median']:.6f} seconds")
        print(f"  Standard Deviation: {algorithm_stats['stdev']:.6f} seconds")

def plot_results(stats: Dict[str, Dict[str, float]], metric: str = "mean") -> None:
    """Plot the results as a bar chart.
    
    Args:
        stats: A dictionary mapping algorithm names to statistics
        metric: The metric to plot (min, max, mean, median, stdev)
    """
    # Create output directory if it doesn't exist
    os.makedirs("sorting_performance/output", exist_ok=True)
    
    algorithms = list(stats.keys())
    values = [stats[algo][metric] for algo in algorithms]
    
    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, values)
    plt.title(f"Sorting Algorithm Performance ({metric})")
    plt.xlabel("Algorithm")
    plt.ylabel(f"Time ({metric}, seconds)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot to the output directory
    plt.savefig(f"sorting_performance/output/performance_{metric}.png")
    plt.close()

def main() -> None:
    """Main function to run the performance tests."""
    print("Sorting Algorithm Performance Test")
    print("=================================")
    
    # Parameters
    array_size = 10000
    num_tests = 10
    
    print(f"\nRunning {num_tests} tests with arrays of size {array_size}...")
    
    # Run tests
    results = run_multiple_tests(num_tests, array_size)
    
    # Calculate and print statistics
    stats = calculate_statistics(results)
    print_statistics(stats)
    
    # Plot results
    for metric in ["mean", "median", "min", "max", "stdev"]:
        plot_results(stats, metric)
    
    print("\nDone! Results have been saved to the sorting_performance/output directory.")

if __name__ == "__main__":
    main() 