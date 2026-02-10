"""Priority queue implementation using heap.

Priority queue: Highest priority element is dequeued first.

Usually implemented with max-heap where priority is the key.

TODO:
    - Implement PriorityQueue wrapping heap
    - Support element updates
    - Support different priority types
"""

from typing import Generic, Optional, Tuple, TypeVar

T = TypeVar("T")
P = TypeVar("P")  # Priority type


class PriorityQueue(Generic[T, P]):
    """
    Priority queue using heap backend.

    Each element has associated priority.
    Higher priority = dequeued first.

    Time Complexity:
        enqueue: O(log n)
        dequeue: O(log n)
        peek: O(1)
    """

    def __init__(self) -> None:
        """Initialize empty priority queue."""
        raise NotImplementedError("PriorityQueue.__init__ not yet implemented")

    def enqueue(self, element: T, priority: P) -> None:
        """
        Add element with priority.

        Args:
            element: Element to add
            priority: Priority value (higher = more urgent)
        """
        raise NotImplementedError("PriorityQueue.enqueue not yet implemented")

    def dequeue(self) -> Tuple[T, P]:
        """
        Remove and return highest priority element.

        Returns:
            Tuple of (element, priority)

        Raises:
            IndexError: If queue empty
        """
        raise NotImplementedError("PriorityQueue.dequeue not yet implemented")

    def peek(self) -> Optional[Tuple[T, P]]:
        """View highest priority element without removing."""
        raise NotImplementedError("PriorityQueue.peek not yet implemented")

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        raise NotImplementedError("PriorityQueue.is_empty not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("PriorityQueue.__len__ not yet implemented")


__all__ = ["PriorityQueue"]
