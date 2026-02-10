"""Trie (prefix tree) data structure.

Trie stores strings for efficient prefix matching, auto-complete, spelling check.

TODO:
    - Implement TrieNode
    - Implement insert, search
    - Implement prefix matching
    - Implement word list retrieval
"""

from typing import List, Optional


class TrieNode:
    """Node in trie."""

    def __init__(self) -> None:
        """Initialize trie node."""
        raise NotImplementedError("TrieNode.__init__ not yet implemented")


class Trie:
    """
    Trie (prefix tree) for efficient string storage and retrieval.

    Time Complexity:
        insert: O(m) where m = word length
        search: O(m)
        prefix match: O(m)
    """

    def __init__(self) -> None:
        """Initialize empty trie."""
        raise NotImplementedError("Trie.__init__ not yet implemented")

    def insert(self, word: str) -> None:
        """
        Insert word into trie.

        Args:
            word: Word to insert

        Time Complexity: O(m)
        """
        raise NotImplementedError("Trie.insert not yet implemented")

    def search(self, word: str) -> bool:
        """
        Check if word exists in trie.

        Args:
            word: Word to search

        Returns:
            True if word exists

        Time Complexity: O(m)
        """
        raise NotImplementedError("Trie.search not yet implemented")

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word starts with prefix.

        Args:
            prefix: Prefix to check

        Returns:
            True if words with this prefix exist

        Time Complexity: O(m)
        """
        raise NotImplementedError("Trie.starts_with not yet implemented")

    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words starting with prefix.

        Args:
            prefix: Prefix to match

        Returns:
            List of matching words

        TODO:
            - Navigate to prefix node
            - DFS to find all complete words
        """
        raise NotImplementedError("Trie.get_words_with_prefix not yet implemented")


__all__ = ["TrieNode", "Trie"]
