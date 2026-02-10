"""Sorting algorithms: Bubble, Selection, Insertion.

Simple O(n²) sorts useful for learning and for nearly-sorted data.

TODO:
    - Implement bubble sort with early exit
    - Implement selection sort
    - Implement insertion sort (good for partially sorted)
"""

from typing import Any, List, TypeVar

T = TypeVar("T")


def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Bubble sort: repeatedly swap adjacent elements if out of order.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes

    TODO: Implement with swaps and early exit optimization
    """
    raise NotImplementedError("bubble_sort not yet implemented")


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Selection sort: find minimum and move to front repeatedly.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: No
    In-place: Yes

    TODO: Implement min finding and swapping
    """
    raise NotImplementedError("selection_sort not yet implemented")


def insertion_sort(arr: List[Any]) -> List[Any]:
    """
    Insertion sort: insert each element into sorted portion.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes

    Good for small or nearly-sorted arrays!

    TODO:
        - Maintain sorted prefix
        - Shift elements during insertion
    """
    raise NotImplementedError("insertion_sort not yet implemented")


__all__ = ["bubble_sort", "selection_sort", "insertion_sort"]
