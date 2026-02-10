"""Tests for quick sort."""

import pytest
from dsa.sorting.quick_sort import quick_sort


class TestQuickSort:
    """Test quick sort."""

    @pytest.mark.unit
    def test_quick_sort_basic(self) -> None:
        """Test basic quick sort."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_quick_sort_pivot_selection(self) -> None:
        """Test with different pivot selection strategies."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_quick_sort_duplicates(self) -> None:
        """Test with duplicates."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_quick_sort_already_sorted(self) -> None:
        """Test on already sorted (worst case)."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_quick_sort_small(self) -> None:
        """Test with small input."""
        pytest.skip("Not yet implemented")

    @pytest.mark.slow
    def test_quick_sort_large(self) -> None:
        """Test with large input."""
        pytest.skip("Not yet implemented")
