#!/usr/bin/env python3
"""
Script to run all performance tests.
"""

import argparse
import subprocess
import os

def main():
    """Run all performance tests."""
    parser = argparse.ArgumentParser(description="Run all sorting algorithm performance tests.")
    parser.add_argument("--size", type=int, default=10000, help="Size of the arrays to generate (default: 10000)")
    parser.add_argument("--tests", type=int, default=5, help="Number of tests to run for each test type (default: 5)")
    parser.add_argument("--sizes", type=int, nargs="+", default=[1000, 5000, 10000, 20000],
                        help="List of array sizes for comparison (default: 1000 5000 10000 20000)")
    args = parser.parse_args()
    
    # Create the output directory if it doesn't exist
    os.makedirs("sorting_performance/output", exist_ok=True)
    
    print("Running all sorting algorithm performance tests...")
    
    # Run a single test
    print("\n1. Running a single test...")
    subprocess.run(["python", "sorting_performance/run_single_test.py", "--size", str(args.size)])
    
    # Run multiple tests
    print("\n2. Running multiple tests...")
    subprocess.run(["python", "sorting_performance/run_multiple_tests.py", "--size", str(args.size), "--tests", str(args.tests)])
    
    # Compare sizes
    print("\n3. Comparing different array sizes...")
    sizes_str = [str(size) for size in args.sizes]
    subprocess.run(["python", "sorting_performance/compare_sizes.py", "--sizes"] + sizes_str + ["--tests", str(args.tests)])
    
    # Compare distributions
    print("\n4. Comparing different data distributions...")
    subprocess.run(["python", "sorting_performance/compare_distributions.py", "--size", str(args.size), "--tests", str(args.tests)])
    
    print("\nAll tests completed! Results have been saved to the sorting_performance/output directory.")

if __name__ == "__main__":
    main() 