"""Deque (Double-Ended Queue) implementation.

Deque allows insertion and deletion at both ends.

Uses either circular array or doubly-linked list for O(1) operations at both ends.

TODO:
    - Implement push_front, push_back
    - Implement pop_front, pop_back
    - Implement peek_front, peek_back
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class Deque(Generic[T]):
    """
    Double-ended queue.

    Supports O(1) insertion/deletion at both front and rear.

    TODO: Choose array or linked list backend
    """

    def __init__(self) -> None:
        """Initialize empty deque."""
        raise NotImplementedError("Deque.__init__ not yet implemented")

    def push_front(self, data: T) -> None:
        """Add element to front."""
        raise NotImplementedError("Deque.push_front not yet implemented")

    def push_back(self, data: T) -> None:
        """Add element to rear."""
        raise NotImplementedError("Deque.push_back not yet implemented")

    def pop_front(self) -> T:
        """Remove and return front element."""
        raise NotImplementedError("Deque.pop_front not yet implemented")

    def pop_back(self) -> T:
        """Remove and return rear element."""
        raise NotImplementedError("Deque.pop_back not yet implemented")

    def peek_front(self) -> T:
        """View front element."""
        raise NotImplementedError("Deque.peek_front not yet implemented")

    def peek_back(self) -> T:
        """View rear element."""
        raise NotImplementedError("Deque.peek_back not yet implemented")

    def is_empty(self) -> bool:
        """Check if deque is empty."""
        raise NotImplementedError("Deque.is_empty not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("Deque.__len__ not yet implemented")


__all__ = ["Deque"]
