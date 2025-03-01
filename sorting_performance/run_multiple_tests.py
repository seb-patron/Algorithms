#!/usr/bin/env python3
"""
Script to run multiple performance tests and generate statistics.
"""

import argparse
from performance_test import run_multiple_tests, calculate_statistics, print_statistics, plot_results

def main():
    """Run multiple performance tests and generate statistics."""
    parser = argparse.ArgumentParser(description="Run multiple sorting algorithm performance tests.")
    parser.add_argument("--size", type=int, default=10000, help="Size of the random arrays to generate (default: 10000)")
    parser.add_argument("--tests", type=int, default=10, help="Number of tests to run (default: 10)")
    args = parser.parse_args()
    
    print(f"Running {args.tests} tests with arrays of size {args.size}...")
    
    # Run tests
    results = run_multiple_tests(args.tests, args.size)
    
    # Calculate and print statistics
    stats = calculate_statistics(results)
    print_statistics(stats)
    
    # Plot results
    for metric in ["mean", "median", "min", "max", "stdev"]:
        plot_results(stats, metric)
    
    print("\nDone! Results have been saved to the sorting_performance directory.")

if __name__ == "__main__":
    main() 