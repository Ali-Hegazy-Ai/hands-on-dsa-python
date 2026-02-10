"""Graph representation using adjacency matrix.

Dense representation, useful for dense graphs or when we need O(1) edge lookup.

TODO:
    - Implement Graph using 2D matrix
    - Support weighted edges
    - Support directed/undirected
"""

from typing import Any, List, Optional


class GraphAdjMatrix:
    """
    Graph using adjacency matrix representation.

    Uses 2D array where [i][j] = weight of edge from i to j.
    O(1) edge lookup, but requires O(V²) space.

    Space Complexity: O(V²)
    Edge lookup: O(1)

    Best for dense graphs or complete graphs.

    TODO:
        - Map vertex labels to indices
        - Support sparse matrix representation
    """

    def __init__(
        self, num_vertices: int, directed: bool = False, weighted: bool = False
    ) -> None:
        """
        Initialize graph with fixed size.

        Args:
            num_vertices: Number of vertices
            directed: If True, directed graph
            weighted: If True, store edge weights

        TODO: Initialize matrix and vertex labels
        """
        raise NotImplementedError("GraphAdjMatrix.__init__ not yet implemented")

    def add_edge(
        self, u: int, v: int, weight: float = 1.0
    ) -> None:
        """
        Add edge.

        Args:
            u: Source vertex index
            v: Destination vertex index
            weight: Edge weight
        """
        raise NotImplementedError("GraphAdjMatrix.add_edge not yet implemented")

    def has_edge(self, u: int, v: int) -> bool:
        """Check if edge exists."""
        raise NotImplementedError("GraphAdjMatrix.has_edge not yet implemented")

    def get_weight(self, u: int, v: int) -> Optional[float]:
        """Get edge weight."""
        raise NotImplementedError("GraphAdjMatrix.get_weight not yet implemented")

    def neighbors(self, vertex: int) -> List[int]:
        """Return neighbor vertices."""
        raise NotImplementedError("GraphAdjMatrix.neighbors not yet implemented")


__all__ = ["GraphAdjMatrix"]
