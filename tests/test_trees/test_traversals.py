"""Tests for tree traversals."""

import pytest
from dsa.trees.traversals import (
    preorder_traversal,
    inorder_traversal,
    postorder_traversal,
    level_order_traversal,
)


class TestTraversals:
    """Test tree traversal functions."""

    @pytest.mark.unit
    def test_preorder(self) -> None:
        """Test preorder traversal."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_inorder(self) -> None:
        """Test inorder traversal (BST should be sorted)."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_postorder(self) -> None:
        """Test postorder traversal."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_level_order(self) -> None:
        """Test level-order (BFS) traversal."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_single_node(self) -> None:
        """Test traversal with single node."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_empty_tree(self) -> None:
        """Test traversal with empty tree."""
        pytest.skip("Not yet implemented")
