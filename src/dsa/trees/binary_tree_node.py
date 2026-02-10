"""Binary tree node definition.

TODO:
    - Implement TreeNode with left/right pointers
    - Add height tracking for balancing algorithms
    - Add parent pointer option for bottom-up traversals
"""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    """
    Node for binary tree.

    Attributes:
        val: Value stored in node
        left: Left child
        right: Right child
        height: Height for AVL balancing (optional)
    """

    def __init__(self, val: T) -> None:
        """
        Initialize tree node.

        Args:
            val: Value to store
        """
        raise NotImplementedError("TreeNode.__init__ not yet implemented")

    def __repr__(self) -> str:
        """Return string representation."""
        raise NotImplementedError("TreeNode.__repr__ not yet implemented")


__all__ = ["TreeNode"]
