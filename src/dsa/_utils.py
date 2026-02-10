"""Utility functions for DSA library."""

from typing import Any, List, TypeVar

T = TypeVar("T")


def swap(arr: List[Any], i: int, j: int) -> None:
    """
    Swap two elements in a list in-place.

    Args:
        arr: List to modify
        i: First index
        j: Second index

    Raises:
        IndexError: If indices are out of bounds
    """
    if not (0 <= i < len(arr) and 0 <= j < len(arr)):
        raise IndexError("Index out of bounds")
    arr[i], arr[j] = arr[j], arr[i]


def is_sorted(arr: List[Any]) -> bool:
    """
    Check if list is sorted in ascending order.

    Args:
        arr: List to check

    Returns:
        True if sorted, False otherwise
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def generate_random_array(size: int, min_val: int = 0, max_val: int = 100) -> List[int]:
    """
    Generate random array for testing.

    Args:
        size: Array size
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)

    Returns:
        List of random integers
    """
    import random
    return [random.randint(min_val, max_val) for _ in range(size)]


__all__ = ["swap", "is_sorted", "generate_random_array"]
