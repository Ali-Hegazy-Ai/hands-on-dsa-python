"""Stack implementation using array (list).

Stack: Last In, First Out (LIFO)

Uses Python list internally. All operations are O(1) amortized.

TODO:
    - Implement push
    - Implement pop
    - Implement peek
    - Implement is_empty
    - Add capacity management
"""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class StackArray(Generic[T]):
    """
    Stack using array (list) backend.

    Time Complexity:
        push: O(1) amortized
        pop: O(1)
        peek: O(1)
    """

    def __init__(self, capacity: Optional[int] = None) -> None:
        """
        Initialize stack.

        Args:
            capacity: Optional max capacity (if None, unlimited growth)
        """
        raise NotImplementedError("StackArray.__init__ not yet implemented")

    def push(self, data: T) -> None:
        """
        Add element to top of stack.

        Args:
            data: Element to add

        Raises:
            OverflowError: If capacity reached
        """
        raise NotImplementedError("StackArray.push not yet implemented")

    def pop(self) -> T:
        """
        Remove and return top element.

        Returns:
            Top element

        Raises:
            IndexError: If stack is empty
        """
        raise NotImplementedError("StackArray.pop not yet implemented")

    def peek(self) -> T:
        """
        View top element without removing.

        Returns:
            Top element

        Raises:
            IndexError: If stack is empty
        """
        raise NotImplementedError("StackArray.peek not yet implemented")

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        raise NotImplementedError("StackArray.is_empty not yet implemented")

    def size(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("StackArray.size not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("StackArray.__len__ not yet implemented")


__all__ = ["StackArray"]
