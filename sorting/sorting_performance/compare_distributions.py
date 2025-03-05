#!/usr/bin/env python3
"""
Script to compare sorting algorithm performance with different data distributions.
"""

import argparse
import random
import os
import matplotlib.pyplot as plt
from typing import List, Dict, Callable, Tuple
from performance_test import test_sorting_algorithm, SORTING_ALGORITHMS, calculate_statistics, print_statistics

def generate_random_array(size: int) -> List[int]:
    """Generate a random array of integers."""
    return [random.randint(0, 1000) for _ in range(size)]

def generate_nearly_sorted_array(size: int) -> List[int]:
    """Generate a nearly sorted array of integers."""
    arr = list(range(size))
    # Swap a few elements to make it nearly sorted
    swaps = size // 20  # 5% of elements will be out of place
    for _ in range(swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def generate_reverse_sorted_array(size: int) -> List[int]:
    """Generate a reverse sorted array of integers."""
    return list(range(size, 0, -1))

def generate_few_unique_array(size: int) -> List[int]:
    """Generate an array with few unique values."""
    unique_values = [random.randint(0, 100) for _ in range(10)]
    return [random.choice(unique_values) for _ in range(size)]

def generate_sorted_with_outliers_array(size: int) -> List[int]:
    """Generate a mostly sorted array with a few outliers."""
    arr = list(range(size))
    # Add a few outliers
    outliers = size // 50  # 2% of elements will be outliers
    for _ in range(outliers):
        i = random.randint(0, size - 1)
        arr[i] = random.randint(size, size * 2)
    return arr

# Dictionary of array generators
ARRAY_GENERATORS: Dict[str, Callable[[int], List[int]]] = {
    "Random": generate_random_array,
    "Nearly Sorted": generate_nearly_sorted_array,
    "Reverse Sorted": generate_reverse_sorted_array,
    "Few Unique Values": generate_few_unique_array,
    "Sorted with Outliers": generate_sorted_with_outliers_array,
}

def compare_distributions(size: int, num_tests: int = 5) -> Dict[str, Dict[str, Dict[str, float]]]:
    """Compare sorting algorithm performance with different data distributions.
    
    Args:
        size: Size of the arrays to generate
        num_tests: Number of tests to run for each distribution
        
    Returns:
        Dict mapping distribution names to dictionaries mapping algorithm names to statistics
    """
    results = {}
    
    for dist_name, generator in ARRAY_GENERATORS.items():
        print(f"\nTesting with distribution: {dist_name}")
        dist_results = {algo: [] for algo in SORTING_ALGORITHMS.keys()}
        
        for i in range(num_tests):
            print(f"  Test {i+1}/{num_tests}")
            array = generator(size)
            
            for algo_name, sort_func in SORTING_ALGORITHMS.items():
                execution_time = test_sorting_algorithm(sort_func, array)
                dist_results[algo_name].append(execution_time)
                print(f"    {algo_name}: {execution_time:.6f} seconds")
        
        results[dist_name] = calculate_statistics(dist_results)
    
    return results

def plot_distribution_comparison(results: Dict[str, Dict[str, Dict[str, float]]], metric: str = "mean") -> None:
    """Plot the comparison of sorting algorithms with different data distributions.
    
    Args:
        results: Dict mapping distribution names to dictionaries mapping algorithm names to statistics
        metric: The metric to plot (mean, median, min, max, stdev)
    """
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    distributions = list(results.keys())
    algorithms = list(SORTING_ALGORITHMS.keys())
    
    # Prepare data for plotting
    data = {}
    for algo in algorithms:
        data[algo] = [results[dist][algo][metric] for dist in distributions]
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Set width of bars
    bar_width = 0.15
    
    # Set position of bars on x axis
    positions = list(range(len(distributions)))
    
    # Plot bars
    for i, algo in enumerate(algorithms):
        offset = (i - len(algorithms) / 2 + 0.5) * bar_width
        ax.bar([p + offset for p in positions], data[algo], bar_width, label=algo)
    
    # Add labels and title
    ax.set_xlabel('Distribution')
    ax.set_ylabel(f'Time ({metric}, seconds)')
    ax.set_title(f'Sorting Algorithm Performance by Data Distribution ({metric})')
    ax.set_xticks(positions)
    ax.set_xticklabels(distributions, rotation=45)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(f"output/distribution_comparison_{metric}.png")
    plt.close()

def main():
    """Compare sorting algorithm performance with different data distributions."""
    parser = argparse.ArgumentParser(description="Compare sorting algorithm performance with different data distributions.")
    parser.add_argument("--size", type=int, default=10000, help="Size of the arrays to generate (default: 10000)")
    parser.add_argument("--tests", type=int, default=5, help="Number of tests to run for each distribution (default: 5)")
    args = parser.parse_args()
    
    print(f"Comparing sorting algorithm performance with different data distributions")
    print(f"Array size: {args.size}")
    print(f"Number of tests per distribution: {args.tests}")
    
    # Run comparison
    results = compare_distributions(args.size, args.tests)
    
    # Print statistics for each distribution
    for dist_name, dist_results in results.items():
        print(f"\nStatistics for {dist_name} distribution:")
        print_statistics(dist_results)
    
    # Plot results
    for metric in ["mean", "median", "min", "max"]:
        plot_distribution_comparison(results, metric)
    
    print("\nDone! Comparison results have been saved to the output directory.")

if __name__ == "__main__":
    main() 