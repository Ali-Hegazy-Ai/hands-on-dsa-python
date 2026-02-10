# Autocomplete Engine

Prefix-based word completion using a custom Trie implementation.

## Goal

- Insert a dictionary of words into your `Trie`.
- Given a prefix, return sorted suggestions via `get_words_with_prefix`.
- Benchmark lookup time vs naive linear scan.

## Acceptance Criteria

- [ ] Returns correct completions for 10 test prefixes.
- [ ] Sub-millisecond lookup for a 50k-word dictionary.
- [ ] Unit tests pass for insert, search, prefix enumeration.
- [ ] Writeup (<200 words) on trie space vs time tradeoff.

## Usage

```bash
python -m projects.autocomplete.main words.txt --prefix "algo"
```
