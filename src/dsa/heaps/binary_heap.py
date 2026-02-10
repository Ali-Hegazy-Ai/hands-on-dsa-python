"""Binary heap implementation.

Binary heap is a complete binary tree that satisfies heap property.
- Min-heap: parent <= children
- Max-heap: parent >= children

Stored in array where parent of i is i//2, left child is 2*i, right is 2*i+1.

TODO:
    - Implement MinHeap and MaxHeap
    - Implement insert (push up)
    - Implement delete (pop down)
    - Implement heapify
"""

from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class MinHeap(Generic[T]):
    """
    Min-heap where parent < any child.

    Time Complexity:
        insert: O(log n)
        delete_min: O(log n)
        peek: O(1)
    """

    def __init__(self) -> None:
        """Initialize empty min-heap."""
        raise NotImplementedError("MinHeap.__init__ not yet implemented")

    def insert(self, val: T) -> None:
        """
        Insert value and restore heap property.

        Args:
            val: Value to insert

        TODO: Implement bubble-up
        """
        raise NotImplementedError("MinHeap.insert not yet implemented")

    def extract_min(self) -> T:
        """
        Remove and return minimum element.

        Returns:
            Minimum value

        Raises:
            IndexError: If heap empty

        TODO: Implement bubble-down
        """
        raise NotImplementedError("MinHeap.extract_min not yet implemented")

    def peek_min(self) -> Optional[T]:
        """View minimum element without removing."""
        raise NotImplementedError("MinHeap.peek_min not yet implemented")

    def heapify(self, arr: List[T]) -> None:
        """
        Create heap from array in-place.

        Args:
            arr: Array to heapify

        Time Complexity: O(n)

        TODO: Implement bottom-up heapify
        """
        raise NotImplementedError("MinHeap.heapify not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("MinHeap.__len__ not yet implemented")


class MaxHeap(Generic[T]):
    """
    Max-heap where parent > any child.

    Time Complexity: Same as MinHeap
    """

    def __init__(self) -> None:
        """Initialize empty max-heap."""
        raise NotImplementedError("MaxHeap.__init__ not yet implemented")

    def insert(self, val: T) -> None:
        """Insert value and restore heap property."""
        raise NotImplementedError("MaxHeap.insert not yet implemented")

    def extract_max(self) -> T:
        """Remove and return maximum element."""
        raise NotImplementedError("MaxHeap.extract_max not yet implemented")

    def peek_max(self) -> Optional[T]:
        """View maximum element without removing."""
        raise NotImplementedError("MaxHeap.peek_max not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("MaxHeap.__len__ not yet implemented")


__all__ = ["MinHeap", "MaxHeap"]
