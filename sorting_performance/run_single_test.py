#!/usr/bin/env python3
"""
Script to run a single performance test with a specific array size.
"""

import argparse
from performance_test import run_single_test

def main():
    """Run a single performance test with a specific array size."""
    parser = argparse.ArgumentParser(description="Run a single sorting algorithm performance test.")
    parser.add_argument("--size", type=int, default=10000, help="Size of the random array to generate (default: 10000)")
    args = parser.parse_args()
    
    print(f"Running a single test with an array of size {args.size}...")
    run_single_test(args.size)
    print("\nDone!")

if __name__ == "__main__":
    main() 