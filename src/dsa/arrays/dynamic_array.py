"""Dynamic array implementation.

A dynamic array (also called vector or ArrayList) that grows as needed.
Unlike Python lists, this teaches the underlying growth strategy.

TODO:
    - Implement __init__ with initial capacity
    - Implement append with resize logic (usually 1.5x or 2x)
    - Implement insert at arbitrary position
    - Implement delete with shifting
    - Implement __getitem__ and __setitem__
    - Implement __len__
    - Add capacity tracking and resize callbacks
"""

from typing import Any, Generic, List, Optional, TypeVar

T = TypeVar("T")


class DynamicArray(Generic[T]):
    """
    Dynamic array that grows automatically when needed.

    Attributes:
        _data: Underlying list storing elements
        _size: Current number of elements
        _capacity: Total allocated space

    Time Complexity:
        append: O(1) amortized
        insert: O(n)
        delete: O(n)
        access: O(1)
    """

    def __init__(self, capacity: int = 10) -> None:
        """
        Initialize dynamic array.

        Args:
            capacity: Initial capacity

        Raises:
            ValueError: If capacity <= 0
        """
        raise NotImplementedError("DynamicArray.__init__ not yet implemented")

    def append(self, value: T) -> None:
        """
        Add element to end of array.

        Resizes if necessary.

        Args:
            value: Element to add

        TODO: Implement resize strategy (e.g., 1.5x or 2x growth)
        """
        raise NotImplementedError("DynamicArray.append not yet implemented")

    def insert(self, index: int, value: T) -> None:
        """
        Insert element at specified index.

        Args:
            index: Position to insert at (0-based)
            value: Element to insert

        Raises:
            IndexError: If index out of bounds

        TODO: Implement shifting and resizing
        """
        raise NotImplementedError("DynamicArray.insert not yet implemented")

    def delete(self, index: int) -> T:
        """
        Remove and return element at index.

        Args:
            index: Position to remove (0-based)

        Returns:
            Deleted element

        Raises:
            IndexError: If index out of bounds or array empty

        TODO: Implement shifting elements left
        """
        raise NotImplementedError("DynamicArray.delete not yet implemented")

    def __getitem__(self, index: int) -> T:
        """Get element at index."""
        raise NotImplementedError("DynamicArray.__getitem__ not yet implemented")

    def __setitem__(self, index: int, value: T) -> None:
        """Set element at index."""
        raise NotImplementedError("DynamicArray.__setitem__ not yet implemented")

    def __len__(self) -> int:
        """Return number of elements."""
        raise NotImplementedError("DynamicArray.__len__ not yet implemented")

    def __str__(self) -> str:
        """Return string representation."""
        raise NotImplementedError("DynamicArray.__str__ not yet implemented")

    def capacity(self) -> int:
        """Return total capacity."""
        raise NotImplementedError("DynamicArray.capacity not yet implemented")


__all__ = ["DynamicArray"]
