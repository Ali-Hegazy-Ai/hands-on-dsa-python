"""Custom exceptions for DSA library."""


class DSAError(Exception):
    """Base exception for DSA library."""

    pass


class EmptyError(DSAError):
    """Raised when operation requires non-empty collection but collection is empty."""

    pass


class InvalidIndexError(DSAError):
    """Raised when index is out of bounds."""

    pass


class DuplicateKeyError(DSAError):
    """Raised when attempting to insert duplicate key in hash table."""

    pass


class CycleDetectedError(DSAError):
    """Raised when cycle is detected in graph."""

    pass


class NoPathError(DSAError):
    """Raised when no path exists between vertices in graph."""

    pass


__all__ = [
    "DSAError",
    "EmptyError",
    "InvalidIndexError",
    "DuplicateKeyError",
    "CycleDetectedError",
    "NoPathError",
]
