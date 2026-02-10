"""Doubly linked list implementation.

TODO:
    - Implement DoublyLinkedList class
    - Implement insert/delete operations
    - Support forward and backward traversal
    - Implement reverse iteration
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class DoublyLinkedList(Generic[T]):
    """
    Doubly linked list implementation.

    Node structure: None <- Node <-> Node <-> Node -> None

    Advantages over singly linked list:
    - Can traverse in both directions
    - Efficient reverse operations
    - Easier deletion with node reference

    TODO: Full implementation with both pointers
    """

    def __init__(self) -> None:
        """Initialize empty list."""
        raise NotImplementedError("DoublyLinkedList.__init__ not yet implemented")

    def insert_head(self, data: T) -> None:
        """Insert at beginning."""
        raise NotImplementedError("DoublyLinkedList.insert_head not yet implemented")

    def insert_tail(self, data: T) -> None:
        """Insert at end."""
        raise NotImplementedError("DoublyLinkedList.insert_tail not yet implemented")

    def delete_head(self) -> T:
        """Remove and return first element."""
        raise NotImplementedError("DoublyLinkedList.delete_head not yet implemented")

    def delete_tail(self) -> T:
        """Remove and return last element."""
        raise NotImplementedError("DoublyLinkedList.delete_tail not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("DoublyLinkedList.__len__ not yet implemented")


__all__ = ["DoublyLinkedList"]
