"""Median of Medians algorithm.

Guarantees O(n) selection (not just average case).

Used to pick good pivot for quickselect.

TODO:
    - Implement median of medians pivot selection
    - Use in quickselect for guaranteed O(n)
"""

from typing import Any, List


def median_of_medians(arr: List[Any]) -> Any:
    """
    Find median of medians element.

    Recursively divide into groups, find medians, find median of those medians.

    Args:
        arr: Array

    Returns:
        The median-of-medians element

    Time Complexity: O(n)

    TODO:
        - Divide into groups of 5
        - Find median of each group
        - Recursively find median of medians
    """
    raise NotImplementedError("median_of_medians not yet implemented")


__all__ = ["median_of_medians"]
