#!/usr/bin/env python3
"""
Script to compare sorting algorithm performance with different array sizes.
"""

import argparse
import os
import matplotlib.pyplot as plt
from typing import List, Dict
from performance_test import run_multiple_tests, calculate_statistics

def compare_sizes(sizes: List[int], num_tests: int = 5) -> Dict[str, Dict[str, List[float]]]:
    """Compare sorting algorithm performance with different array sizes.
    
    Args:
        sizes: List of array sizes to test
        num_tests: Number of tests to run for each size
        
    Returns:
        Dict mapping algorithm names to dictionaries mapping metrics to lists of values
    """
    results = {}
    
    for size in sizes:
        print(f"\nTesting with array size: {size}")
        test_results = run_multiple_tests(num_tests, size)
        stats = calculate_statistics(test_results)
        
        for algo, algo_stats in stats.items():
            if algo not in results:
                results[algo] = {"sizes": [], "mean": [], "median": [], "min": [], "max": [], "stdev": []}
            
            results[algo]["sizes"].append(size)
            results[algo]["mean"].append(algo_stats["mean"])
            results[algo]["median"].append(algo_stats["median"])
            results[algo]["min"].append(algo_stats["min"])
            results[algo]["max"].append(algo_stats["max"])
            results[algo]["stdev"].append(algo_stats["stdev"])
    
    return results

def plot_comparison(results: Dict[str, Dict[str, List[float]]], metric: str = "mean") -> None:
    """Plot the comparison of sorting algorithms with different array sizes.
    
    Args:
        results: Dict mapping algorithm names to dictionaries mapping metrics to lists of values
        metric: The metric to plot (mean, median, min, max, stdev)
    """
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    plt.figure(figsize=(12, 8))
    
    for algo, algo_results in results.items():
        plt.plot(algo_results["sizes"], algo_results[metric], marker='o', label=algo)
    
    plt.title(f"Sorting Algorithm Performance Comparison ({metric})")
    plt.xlabel("Array Size")
    plt.ylabel(f"Time ({metric}, seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save the plot to the output directory
    plt.savefig(f"output/comparison_{metric}.png")
    plt.close()

def main():
    """Compare sorting algorithm performance with different array sizes."""
    parser = argparse.ArgumentParser(description="Compare sorting algorithm performance with different array sizes.")
    parser.add_argument("--sizes", type=int, nargs="+", default=[1000, 5000, 10000, 20000, 50000],
                        help="List of array sizes to test (default: 1000 5000 10000 20000 50000)")
    parser.add_argument("--tests", type=int, default=5, help="Number of tests to run for each size (default: 5)")
    args = parser.parse_args()
    
    print(f"Comparing sorting algorithm performance with array sizes: {args.sizes}")
    print(f"Running {args.tests} tests for each size...")
    
    # Run comparison
    results = compare_sizes(args.sizes, args.tests)
    
    # Plot results
    for metric in ["mean", "median", "min", "max"]:
        plot_comparison(results, metric)
    
    print("\nDone! Comparison results have been saved to the output directory.")

if __name__ == "__main__":
    main() 