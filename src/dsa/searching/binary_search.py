"""Binary search algorithms.

Binary search for sorted array: eliminate half of remaining elements each step.

TODO:
    - Implement recursive binary search
    - Implement iterative binary search
    - Implement find_first (leftmost)
    - Implement find_last (rightmost)
"""

from typing import List, Optional, TypeVar

T = TypeVar("T")


def binary_search(arr: List[T], target: T) -> int:
    """
    Binary search in sorted array.

    Args:
        arr: Sorted array
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Time Complexity: O(log n)
    Space Complexity: O(1) iterative, O(log n) recursive

    TODO: Implement iterative version
    """
    raise NotImplementedError("binary_search not yet implemented")


def binary_search_recursive(arr: List[T], target: T, left: int = 0, right: Optional[int] = None) -> int:
    """
    Recursive binary search.

    Args:
        arr: Sorted array
        target: Value to find
        left: Left boundary
        right: Right boundary

    Returns:
        Index or -1

    Time Complexity: O(log n)
    Space Complexity: O(log n) for recursion

    TODO: Implement base cases and recursive calls
    """
    raise NotImplementedError("binary_search_recursive not yet implemented")


def find_first(arr: List[T], target: T) -> int:
    """
    Find first (leftmost) occurrence of target.

    Useful when array has duplicates.

    Args:
        arr: Sorted array with possible duplicates
        target: Value to find

    Returns:
        Index of first occurrence, or -1

    Time Complexity: O(log n)

    TODO:
        - Find any occurrence first
        - Move left if found to get first
    """
    raise NotImplementedError("find_first not yet implemented")


def find_last(arr: List[T], target: T) -> int:
    """
    Find last (rightmost) occurrence of target.

    Args:
        arr: Sorted array with possible duplicates
        target: Value to find

    Returns:
        Index of last occurrence, or -1

    Time Complexity: O(log n)

    TODO: Similar to find_first but move right
    """
    raise NotImplementedError("find_last not yet implemented")


__all__ = [
    "binary_search",
    "binary_search_recursive",
    "find_first",
    "find_last",
]
