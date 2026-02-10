"""String matching algorithms module.

This module contains string pattern matching algorithms:
- Naive string matching
- KMP (Knuth-Morris-Pratt)
- Rabin-Karp (uses rolling hash)
- Trie data structure

TODO:
    - Implement naive matching
    - Implement KMP with failure function
    - Implement Rabin-Karp with rolling hash
    - Implement Trie for prefix matching
"""

from . import kmp, naive_match, rabin_karp, trie

__all__ = ["naive_match", "kmp", "rabin_karp", "trie"]
