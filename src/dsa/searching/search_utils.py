"""Search utilities and helpers.

Common patterns and utilities for searching algorithms.

TODO:
    - Implement binary search on answer pattern
    - Implement exponential search
    - Implement interpolation search
"""

from typing import Any, List, Optional, TypeVar, Callable

T = TypeVar("T")


def is_sorted(arr: List[T]) -> bool:
    """Check if array is sorted."""
    raise NotImplementedError("is_sorted not yet implemented")


def binary_search_on_answer(
    left: int, right: int, predicate: Callable[[int], bool]
) -> int:
    """
    Binary search on answer pattern.

    Find smallest value where predicate is True.
    Useful for optimization problems.

    Args:
        left: Lower bound
        right: Upper bound
        predicate: Function that's True for valid answers

    Returns:
        Smallest valid value

    Time Complexity: O(log(right - left))

    TODO:
        - Implement binary search on range
        - Use predicate to narrow search
    """
    raise NotImplementedError("binary_search_on_answer not yet implemented")


__all__ = ["is_sorted", "binary_search_on_answer"]
