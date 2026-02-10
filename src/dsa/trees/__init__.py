"""Trees module.

This module contains implementations of tree data structures:
- Binary tree nodes
- Binary trees
- Binary Search Trees (BST)
- Tree traversals (inorder, preorder, postorder, level-order)

TODO:
    - Implement BinaryTreeNode
    - Implement BinaryTree with basic operations
    - Implement BST with insertion, deletion, search
    - Implement tree traversals
    - Add balancing operations for AVL or Red-Black trees (future)
"""

from . import binary_tree, binary_tree_node, bst, traversals

__all__ = [
    "binary_tree_node",
    "binary_tree",
    "bst",
    "traversals",
]
