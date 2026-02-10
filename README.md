# Hands-On Data Structures and Algorithms with Python

A comprehensive study repository implementing data structures and algorithms from scratch for the **"Hands-On Data Structures and Algorithms with Python (3rd Edition)"** book.

## Goals

- Build a reusable DSA library (`dsa` package)
- Implement every algorithm from first principles
- Write type-safe, well-tested code
- Include comprehensive notes and benchmarks
- Daily practice with hands-on exercises

## Project Structure

```
hands-on-dsa-python/
├── src/dsa/                 # Main DSA library
│   ├── arrays/              # Array operations
│   ├── linked_lists/        # Linked list variants
│   ├── stacks_queues/       # Stack and queue implementations
│   ├── trees/               # Tree structures and algorithms
│   ├── heaps/               # Heap and priority queue
│   ├── hash_tables/         # Hash table implementations
│   ├── graphs/              # Graph algorithms
│   ├── searching/           # Search algorithms
│   ├── sorting/             # Sorting algorithms
│   ├── selection/           # Selection algorithms
│   └── strings/             # String matching algorithms
├── tests/                   # Comprehensive test suite
├── benchmarks/              # Performance benchmarks
├── notes/                   # Study notes by topic
├── notebooks/               # Interactive Jupyter notebooks
└── scripts/                 # Utility scripts
```

## Quick Start

```bash
# Install dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Format and lint code
ruff check . --fix
ruff format .

# Type check
mypy src/

# Run benchmarks
python benchmarks/benchmark_sorting.py
```

## Topics Covered

### Data Structures
- **Arrays**: Dynamic arrays, prefix sums, two-pointer technique
- **Linked Lists**: Singly, doubly, and circular linked lists
- **Stacks & Queues**: Array and linked-list implementations
- **Trees**: Binary trees, BSTs, traversals
- **Heaps**: Binary heaps, priority queues
- **Hash Tables**: Open addressing, chaining, rolling hash
- **Graphs**: Adjacency list/matrix, BFS, DFS, shortest paths

### Algorithms
- **Searching**: Linear search, binary search
- **Sorting**: Bubble, insertion, selection, merge, quick, heap, radix, counting sort
- **Selection**: QuickSelect, Median of Medians
- **String Matching**: Naive matching, KMP, Rabin-Karp, Trie

## Study Method

See [notes/00_study_method.md](notes/00_study_method.md) for the overall learning strategy.

## Testing & Quality

- **Type hints**: Full typing coverage with MyPy strict mode
- **Tests**: Comprehensive test suites with edge cases
- **Linting**: Ruff with selected rule sets (F, E, I, UP, B)
- **Formatting**: Black via Ruff

## Resources

- Official book: "Hands-On Data Structures and Algorithms with Python (3rd Edition)"
- Test-driven development approach
- Benchmark-driven optimization

## License

MIT License - See LICENSE file

## Progress

- [ ] Arrays
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Trees
- [ ] Heaps
- [ ] Hash Tables
- [ ] Graphs
- [ ] Searching
- [ ] Sorting
- [ ] Selection
- [ ] String Matching

---

**Started**: February 2026
**Status**: In Progress
