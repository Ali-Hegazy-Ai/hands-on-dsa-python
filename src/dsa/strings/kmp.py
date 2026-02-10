"""KMP (Knuth-Morris-Pratt) string matching.

Uses failure function to avoid re-checking matched characters.

TODO:
    - Implement failure function (LPS array)
    - Implement KMP matching
"""

from typing import List


def build_failure_function(pattern: str) -> List[int]:
    """
    Build LPS (Longest Proper Prefix which is also Suffix) array.

    Used to skip unnecessary comparisons.

    Args:
        pattern: Pattern string

    Returns:
        LPS array

    Time Complexity: O(m)

    TODO:
        - Use Z-algorithm or simple approach
        - LPS[i] = longest prefix of pattern[:i+1] that's also suffix
    """
    raise NotImplementedError("build_failure_function not yet implemented")


def kmp_match(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences using KMP algorithm.

    Args:
        text: Text to search
        pattern: Pattern to find

    Returns:
        List of starting indices

    Time Complexity: O(n + m)
    Space Complexity: O(m) for LPS array

    TODO:
        - Build failure function
        - Use it to skip comparisons
    """
    raise NotImplementedError("kmp_match not yet implemented")


__all__ = ["build_failure_function", "kmp_match"]
