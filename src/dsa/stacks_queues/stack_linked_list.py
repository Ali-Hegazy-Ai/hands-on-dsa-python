"""Stack implementation using linked list.

Stack backed by linked list. Useful for understanding linked list operations
and for cases where max capacity is unknown.

TODO:
    - Implement push/pop using node insertion/deletion at head
    - All operations should be O(1)
"""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class StackLinkedList(Generic[T]):
    """
    Stack using linked list backend.

    All operations at head = O(1).

    Time Complexity:
        push: O(1)
        pop: O(1)
        peek: O(1)
    """

    def __init__(self) -> None:
        """Initialize empty stack."""
        raise NotImplementedError("StackLinkedList.__init__ not yet implemented")

    def push(self, data: T) -> None:
        """
        Add element to top of stack.

        Args:
            data: Element to add
        """
        raise NotImplementedError("StackLinkedList.push not yet implemented")

    def pop(self) -> T:
        """
        Remove and return top element.

        Returns:
            Top element

        Raises:
            IndexError: If stack is empty
        """
        raise NotImplementedError("StackLinkedList.pop not yet implemented")

    def peek(self) -> Optional[T]:
        """View top element without removing."""
        raise NotImplementedError("StackLinkedList.peek not yet implemented")

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        raise NotImplementedError("StackLinkedList.is_empty not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("StackLinkedList.__len__ not yet implemented")


__all__ = ["StackLinkedList"]
