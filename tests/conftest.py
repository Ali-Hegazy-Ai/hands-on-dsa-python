"""Pytest configuration and shared fixtures."""

import pytest
from typing import List


@pytest.fixture
def sample_array() -> List[int]:
    """Provide a sample array for tests."""
    return [64, 34, 25, 12, 22, 11, 90]


@pytest.fixture
def sorted_array() -> List[int]:
    """Provide a sorted array."""
    return [11, 12, 22, 25, 34, 64, 90]


@pytest.fixture
def empty_array() -> List[int]:
    """Provide empty array."""
    return []


@pytest.fixture
def single_element() -> List[int]:
    """Array with single element."""
    return [42]


@pytest.fixture
def duplicates() -> List[int]:
    """Array with duplicates."""
    return [3, 3, 1, 2, 3, 1, 2]
