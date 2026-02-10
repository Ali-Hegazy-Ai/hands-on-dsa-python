"""Linear search algorithm.

Simplest search: check each element sequentially until found.

TODO:
    - Implement linear search
    - Support custom comparison function
"""

from typing import Any, Callable, List, Optional, TypeVar

T = TypeVar("T")


def linear_search(arr: List[T], target: T) -> int:
    """
    Linear search for target in unsorted array.

    Args:
        arr: Array to search
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO: Simple iteration with comparison
    """
    raise NotImplementedError("linear_search not yet implemented")


def linear_search_custom(
    arr: List[T], predicate: Callable[[T], bool]
) -> int:
    """
    Linear search using custom predicate.

    Useful for complex search criteria.

    Args:
        arr: Array to search
        predicate: Function returning True for target

    Returns:
        Index of matching element, or -1

    Time Complexity: O(n)

    TODO: Search with custom predicate
    """
    raise NotImplementedError("linear_search_custom not yet implemented")


__all__ = ["linear_search", "linear_search_custom"]
