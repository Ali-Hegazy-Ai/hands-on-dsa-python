"""Rolling hash implementation.

Rolling hash is an efficient way to compute hash of substrings.
Used in Rabin-Karp string matching algorithm.

Solves: Hash updates in O(1) when sliding window moves (instead of O(m) for rehashing).

TODO:
    - Implement rolling hash computation
    - Implement hash update when window slides
    - Use in Rabin-Karp algorithm
"""

from typing import List

BASE = 256  # Base for rolling hash
PRIME = 101  # Prime for modulo (prevents overflow)


def rolling_hash(s: str, size: int) -> List[int]:
    """
    Compute rolling hash for all substrings of given size.

    Args:
        s: String to hash
        size: Substring size

    Returns:
        List of hash values for each substring

    Time Complexity: O(n)

    TODO: Implement rolling hash with O(1) updates
    """
    raise NotImplementedError("rolling_hash not yet implemented")


def update_hash(prev_hash: int, removed_char: str, added_char: str, base: int) -> int:
    """
    Update rolling hash when window slides.

    Removes contribution of leftmost char, shifts, adds new char.

    Args:
        prev_hash: Previous hash value
        removed_char: Character leaving window
        added_char: Character entering window
        base: Base for rolling hash

    Returns:
        New hash value

    Time Complexity: O(1)

    TODO: Implement the sliding window update formula
    """
    raise NotImplementedError("update_hash not yet implemented")


__all__ = ["rolling_hash", "update_hash"]
