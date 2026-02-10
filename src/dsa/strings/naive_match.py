"""Naive string matching.

Simple approach: check every position in text.

TODO:
    - Implement naive matching
"""

from typing import List


def naive_match(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text (naive approach).

    Args:
        text: Text to search in
        pattern: Pattern to find

    Returns:
        List of starting indices of matches

    Time Complexity: O((n - m + 1) × m)
    Space Complexity: O(1) if not counting output

    TODO: Check every position in text
    """
    raise NotImplementedError("naive_match not yet implemented")


__all__ = ["naive_match"]
