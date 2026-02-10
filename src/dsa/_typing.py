"""Typing utilities and type aliases for DSA library."""

from typing import Any, Callable, Generic, List, Optional, Sequence, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
Comparable = TypeVar("Comparable", bound=object)


# Type aliases for common patterns
ArrayLike = Sequence[Any]
Numeric = int | float
Comparable_co = TypeVar("Comparable_co", bound=object, covariant=True)

__all__ = [
    "T",
    "K",
    "V",
    "Comparable",
    "ArrayLike",
    "Numeric",
    "Comparable_co",
]
