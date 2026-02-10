"""Linear-time sorting algorithms: Radix, Counting.

Non-comparison sorts that work for special input types.

TODO:
    - Implement counting sort
    - Implement radix sort (digits and buckets)
    - Implement bucket sort
"""

from typing import Any, List


def counting_sort(arr: List[int], max_val: int) -> List[int]:
    """
    Counting sort: for small non-negative integers.

    Counts occurrences and reconstructs sorted array.

    Args:
        arr: Array of non-negative integers
        max_val: Maximum value in array

    Time Complexity: O(n + k) where k = max_val
    Space Complexity: O(k)
    Stable: Yes
    In-place: No

    TODO:
        - Build count array
        - Compute prefix sums
        - Reconstruct sorted array
    """
    raise NotImplementedError("counting_sort not yet implemented")


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix sort: sort by digits/groups.

    Uses counting sort as subroutine for each digit.

    Args:
        arr: Array of non-negative integers

    Time Complexity: O(d × (n + k)) where d = number of digits, k = base
    Space Complexity: O(n + k)
    Stable: Yes
    In-place: No

    Efficient for large keys if digit count is small!

    TODO:
        - Extract digits (from least significant)
        - Apply counting sort for each digit
        - Complexity depends on digit representation
    """
    raise NotImplementedError("radix_sort not yet implemented")


def bucket_sort(arr: List[float]) -> List[float]:
    """
    Bucket sort: divide into buckets and sort each.

    Works well for uniformly distributed floating-point numbers.

    Args:
        arr: Array of numbers in range [0, 1) typically

    Time Complexity: O(n + k) average, O(n²) worst
    Space Complexity: O(n + k)
    Stable: Yes (if using stable sub-sort)

    TODO:
        - Create buckets
        - Distribute elements
        - Sort each bucket
        - Concatenate results
    """
    raise NotImplementedError("bucket_sort not yet implemented")


__all__ = ["counting_sort", "radix_sort", "bucket_sort"]
