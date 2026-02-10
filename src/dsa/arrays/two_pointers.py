"""Two-pointer technique.

Two-pointer technique is useful for sorted arrays, partitioning, and merging.

TODO:
    - Implement partition for quicksort
    - Implement two-sum with sorted array
    - Implement three-sum
    - Implement container with most water
    - Implement merge sorted arrays
"""

from typing import List, Optional, Tuple

Numeric = int | float


def two_sum(arr: List[Numeric], target: Numeric) -> Optional[Tuple[int, int]]:
    """
    Find two indices whose values sum to target in sorted array.

    Args:
        arr: Sorted array
        target: Target sum

    Returns:
        Tuple of (index1, index2) or None if not found

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
        - Implement two-pointer approach from both ends
        - Handle edge cases (empty array, target not found)
    """
    raise NotImplementedError("two_sum not yet implemented")


def partition(arr: List[Numeric], pivot: Numeric) -> int:
    """
    Partition array so elements < pivot are left, >= pivot are right.

    Used by quicksort.

    Args:
        arr: Array to partition (modified in-place)
        pivot: Pivot value

    Returns:
        Index where pivot value ends up

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
        - Implement Hoare partition scheme
        - Support pivot selection strategies
    """
    raise NotImplementedError("partition not yet implemented")


def merge_sorted_arrays(
    arr1: List[Numeric], arr2: List[Numeric]
) -> List[Numeric]:
    """
    Merge two sorted arrays using two-pointer technique.

    Args:
        arr1: First sorted array
        arr2: Second sorted array

    Returns:
        Merged sorted array

    Time Complexity: O(n + m)
    Space Complexity: O(n + m)

    TODO:
        - Implement two-pointer merge from both ends
        - Support in-place merge when space is available
    """
    raise NotImplementedError("merge_sorted_arrays not yet implemented")


def container_with_most_water(heights: List[int]) -> int:
    """
    Find two lines that form container with maximum water.

    LeetCode classic problem.

    Args:
        heights: List of heights

    Returns:
        Maximum area

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
        - Implement two-pointer approach
        - Move pointer with smaller height
    """
    raise NotImplementedError("container_with_most_water not yet implemented")


__all__ = [
    "two_sum",
    "partition",
    "merge_sorted_arrays",
    "container_with_most_water",
]
