"""Benchmark sorting algorithms."""

import timeit
from typing import Callable, List, Tuple
from dsa._utils import generate_random_array


def benchmark_algorithm(
    name: str,
    func: Callable[[List[int]], List[int]],
    data: List[int],
    iterations: int = 1,
) -> float:
    """
    Benchmark a single sorting algorithm.

    Args:
        name: Algorithm name for display
        func: Sorting function
        data: Input data
        iterations: Number of iterations

    Returns:
        Total execution time in seconds

    TODO: Implement timing measurement
    """
    raise NotImplementedError("benchmark_algorithm not yet implemented")


def main() -> None:
    """
    Run sorting algorithm benchmarks.

    Compares:
    - Merge sort
    - Quick sort
    - Heap sort
    - Python's built-in sorted()

    Measures different input sizes.

    TODO:
        - Generate test arrays of various sizes
        - Time each algorithm
        - Display results in table
        - Compare with built-in sorted()
    """
    raise NotImplementedError("Benchmark not yet implemented")


if __name__ == "__main__":
    main()
