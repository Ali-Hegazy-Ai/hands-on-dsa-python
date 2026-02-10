"""Tree traversal algorithms.

Different ways to visit all nodes in a tree:
- Depth-First: Preorder, Inorder, Postorder
- Breadth-First: Level-order

TODO:
    - Implement recursive traversals
    - Implement iterative versions using stacks/queues
    - Implement level-order with queue
"""

from typing import Any, Callable, Generic, List, Optional, TypeVar

T = TypeVar("T")


def preorder_traversal(root: Any) -> List[Any]:
    """
    Preorder traversal: Root -> Left -> Right.

    Args:
        root: Root node of tree

    Returns:
        List of values in preorder sequence

    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    TODO:
        - Implement recursive version
        - Implement iterative version using stack
    """
    raise NotImplementedError("preorder_traversal not yet implemented")


def inorder_traversal(root: Any) -> List[Any]:
    """
    Inorder traversal: Left -> Root -> Right.

    For BST, produces sorted sequence!

    Args:
        root: Root node of tree

    Returns:
        List of values in inorder sequence

    Time Complexity: O(n)
    Space Complexity: O(h)

    TODO:
        - Implement recursive version
        - Implement iterative version using stack
    """
    raise NotImplementedError("inorder_traversal not yet implemented")


def postorder_traversal(root: Any) -> List[Any]:
    """
    Postorder traversal: Left -> Right -> Root.

    Useful for deletion and evaluation.

    Args:
        root: Root node of tree

    Returns:
        List of values in postorder sequence

    Time Complexity: O(n)
    Space Complexity: O(h)

    TODO:
        - Implement recursive version
        - Implement iterative version using stack
    """
    raise NotImplementedError("postorder_traversal not yet implemented")


def level_order_traversal(root: Any) -> List[Any]:
    """
    Level-order traversal (BFS): Visit nodes level by level.

    Args:
        root: Root node of tree

    Returns:
        List of values in level-order sequence

    Time Complexity: O(n)
    Space Complexity: O(w) where w is max width

    TODO: Implement using queue
    """
    raise NotImplementedError("level_order_traversal not yet implemented")


def level_order_by_level(root: Any) -> List[List[Any]]:
    """
    Level-order grouped by level.

    Returns each level as separate list for 2D output.

    Args:
        root: Root node of tree

    Returns:
        2D list where each inner list is one level

    Time Complexity: O(n)

    TODO: Modify level_order to group by level
    """
    raise NotImplementedError("level_order_by_level not yet implemented")


def zigzag_level_order(root: Any) -> List[List[Any]]:
    """
    Zigzag level-order: alternate left-to-right and right-to-left.

    Args:
        root: Root node of tree

    Returns:
        2D list with alternating direction per level

    TODO: Implement using deque for reverse operations
    """
    raise NotImplementedError("zigzag_level_order not yet implemented")


__all__ = [
    "preorder_traversal",
    "inorder_traversal",
    "postorder_traversal",
    "level_order_traversal",
    "level_order_by_level",
    "zigzag_level_order",
]
