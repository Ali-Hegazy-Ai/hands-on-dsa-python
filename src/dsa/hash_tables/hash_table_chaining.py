"""Hash table with chaining collision resolution.

When hash collision occurs, elements are stored in a chain (e.g., linked list) at that bucket.

TODO:
    - Implement hash function
    - Implement insert with chaining
    - Implement search in chains
    - Implement delete
"""

from typing import Any, Dict, Generic, List, Optional, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class HashTableChaining(Generic[K, V]):
    """
    Hash table using separate chaining for collision resolution.

    Each bucket contains a chain (list) of entries.

    Time Complexity (average):
        insert: O(1)
        search: O(1)
        delete: O(1)

    Time Complexity (worst, all collisions):
        All operations: O(n)
    """

    def __init__(self, size: int = 16) -> None:
        """
        Initialize hash table with chaining.

        Args:
            size: Number of buckets (chains)
        """
        raise NotImplementedError(
            "HashTableChaining.__init__ not yet implemented"
        )

    def put(self, key: K, value: V) -> None:
        """
        Insert or update key-value pair.

        Args:
            key: Key to insert
            value: Value to associate

        TODO:
            - Compute hash of key
            - Add to appropriate bucket's chain
        """
        raise NotImplementedError("HashTableChaining.put not yet implemented")

    def get(self, key: K) -> Optional[V]:
        """
        Retrieve value by key.

        Args:
            key: Key to search

        Returns:
            Associated value or None if not found

        TODO: Search in the bucket's chain
        """
        raise NotImplementedError("HashTableChaining.get not yet implemented")

    def remove(self, key: K) -> bool:
        """
        Delete key-value pair.

        Args:
            key: Key to remove

        Returns:
            True if removed, False if not found

        TODO: Remove from bucket's chain
        """
        raise NotImplementedError("HashTableChaining.remove not yet implemented")

    def contains(self, key: K) -> bool:
        """Check if key exists."""
        raise NotImplementedError("HashTableChaining.contains not yet implemented")

    def __len__(self) -> int:
        """Return number of entries."""
        raise NotImplementedError("HashTableChaining.__len__ not yet implemented")


__all__ = ["HashTableChaining"]
