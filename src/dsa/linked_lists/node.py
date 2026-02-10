"""Node classes for linked lists.

TODO:
    - Create SinglyNode
    - Create DoublyNode
    - Create CircularNode
    - Add type hints
"""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class SinglyNode(Generic[T]):
    """
    Node for singly linked list.

    Attributes:
        data: Value stored in node
        next: Reference to next node
    """

    def __init__(self, data: T) -> None:
        """
        Initialize node.

        Args:
            data: Value to store
        """
        raise NotImplementedError("SinglyNode.__init__ not yet implemented")

    def __repr__(self) -> str:
        """Return string representation."""
        raise NotImplementedError("SinglyNode.__repr__ not yet implemented")


class DoublyNode(Generic[T]):
    """
    Node for doubly linked list.

    Attributes:
        data: Value stored in node
        prev: Reference to previous node
        next: Reference to next node
    """

    def __init__(self, data: T) -> None:
        """
        Initialize node.

        Args:
            data: Value to store
        """
        raise NotImplementedError("DoublyNode.__init__ not yet implemented")

    def __repr__(self) -> str:
        """Return string representation."""
        raise NotImplementedError("DoublyNode.__repr__ not yet implemented")


__all__ = ["SinglyNode", "DoublyNode"]
