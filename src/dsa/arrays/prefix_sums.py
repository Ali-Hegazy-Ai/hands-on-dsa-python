"""Prefix sum algorithms.

Prefix sums are a technique to quickly compute sums over ranges of an array.

TODO:
    - Implement prefix_sum (compute all prefix sums)
    - Implement range_sum (query sum over range)
    - Implement 2D prefix sum
    - Implement difference array technique
"""

from typing import List

# Type alias for numeric types
Numeric = int | float


def prefix_sum(arr: List[Numeric]) -> List[Numeric]:
    """
    Compute prefix sum array.

    For array [a, b, c, d], returns [a, a+b, a+b+c, a+b+c+d]

    Args:
        arr: Input array

    Returns:
        Prefix sum array where prefix[i] = sum of arr[0..i]

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO: Implement using a single pass
    """
    raise NotImplementedError("prefix_sum not yet implemented")


def range_sum(prefix: List[Numeric], left: int, right: int) -> Numeric:
    """
    Query sum of elements from left to right using prefix sum.

    Args:
        prefix: Prefix sum array (computed via prefix_sum)
        left: Start index (inclusive)
        right: End index (inclusive)

    Returns:
        Sum of elements from left to right

    Time Complexity: O(1)

    TODO: Implement using prefix sum property
    """
    raise NotImplementedError("range_sum not yet implemented")


def prefix_sum_2d(matrix: List[List[Numeric]]) -> List[List[Numeric]]:
    """
    Compute 2D prefix sum matrix.

    TODO:
        - Implement 2D prefix sum computation
        - Handle edge cases for empty matrix
    """
    raise NotImplementedError("prefix_sum_2d not yet implemented")


def range_sum_2d(
    prefix: List[List[Numeric]], r1: int, c1: int, r2: int, c2: int
) -> Numeric:
    """
    Query 2D rectangular sum using prefix sum matrix.

    TODO:
        - Implement 2D range query
        - Include inclusion-exclusion principle
    """
    raise NotImplementedError("range_sum_2d not yet implemented")


__all__ = ["prefix_sum", "range_sum", "prefix_sum_2d", "range_sum_2d"]
