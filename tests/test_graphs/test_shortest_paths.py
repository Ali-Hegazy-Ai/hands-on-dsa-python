"""Tests for shortest paths."""

import pytest
from dsa.graphs.shortest_paths import dijkstra, bellman_ford


class TestShortestPaths:
    """Test shortest path algorithms."""

    @pytest.mark.unit
    def test_dijkstra_basic(self) -> None:
        """Test Dijkstra's algorithm."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_dijkstra_single_source(self) -> None:
        """Test Dijkstra finds distances to all vertices."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_bellman_ford(self) -> None:
        """Test Bellman-Ford algorithm."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_bellman_ford_negative_weights(self) -> None:
        """Test Bellman-Ford with negative weights."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_negative_cycle_detection(self) -> None:
        """Test detection of negative cycles."""
        pytest.skip("Not yet implemented")

    @pytest.mark.unit
    def test_unreachable_vertices(self) -> None:
        """Test distances to unreachable vertices."""
        pytest.skip("Not yet implemented")
