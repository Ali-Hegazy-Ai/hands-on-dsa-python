"""Study notes for DSA learning."""

# Study Method: Hands-On Data Structures and Algorithms with Python

## Learning Strategy

This repository follows a **test-driven, implementation-first** approach to learning DSA.

### Principles

1. **Understand first**: Read book section and understand the concept
2. **Design**: Plan the implementation and test cases
3. **Implement**: Write code from scratch (no copy-paste from book)
4. **Test**: Verify correctness with comprehensive tests
5. **Optimize**: Profile and optimize for performance
6. **Benchmark**: Compare with built-ins and alternatives

### Structure of Each Topic

For every data structure/algorithm:

```
1. Read the concept in the book
2. Study the files in src/dsa/<module>/
3. Understand the TODO items
4. Implement the functions (replace NotImplementedError)
5. Run pytest for the module tests/test_<module>/
6. Run benchmarks in benchmarks/
7. Take notes in notes/<topic>.md
```

### Components

- **Implementation files** (`src/dsa/`): Algorithm/DS code
- **Test files** (`tests/`): 5+ tests per module
- **Benchmarks** (`benchmarks/`): Performance comparison
- **Notes** (`notes/`): Key concepts, complexity, tips

## Complexity Classes

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Simple loop |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(n³) | Cubic | Naive matrix mult |
| O(2ⁿ) | Exponential | Brute force subset |
| O(n!) | Factorial | Permutations |

## Time vs Space Tradeoff

- Sorting: Compare time complexity with space used
- Hashing: Trade time (lookup O(1)) for space
- Dynamic programming: Use space to save computation time

## Tips for Implementation

1. **Start simple**: Get it working, then optimize
2. **Test edge cases**: Empty, single element, duplicates
3. **Type hints**: Use Python type hints for clarity
4. **Docstrings**: Explain time/space complexity
5. **Error handling**: Raise meaningful exceptions
6. **Clean code**: Follow PEP 8 style

## Common Mistakes

- Not handling edge cases (empty, nil, out of bounds)
- Forgetting to update pointers in linked lists
- Off-by-one errors in loops
- Not considering integer overflow (Python is safe)
- Modifying input when shouldn't (unless in-place intended)
- Ignoring time/space complexity

## Daily Practice

Goal: Implement 1-2 algorithms/data structures per day

1. **Morning**: Read book section, understand concepts
2. **Midday**: Implement skeleton with TODO markers
3. **Afternoon**: Write comprehensive tests
4. **Evening**: Implement the actual code, optimize if needed

## Resources

- Official book: "Hands-On Data Structures and Algorithms with Python (3rd Edition)"
- Online judges: LeetCode, HackerRank for practice
- Visualizations: VisuAlgo, AlgoExpert for understanding
- References: GeeksforGeeks, Wikipedia for quick lookups

## Progress Tracking

Use this checklist to track your progress:

- [ ] Arrays and Dynamic Arrays
- [ ] Linked Lists (Singly, Doubly, Circular)
- [ ] Stacks and Queues
- [ ] Trees and Binary Search Trees
- [ ] Heaps and Priority Queues
- [ ] Hash Tables
- [ ] Graphs (BFS, DFS, Shortest Paths)
- [ ] Searching (Linear, Binary)
- [ ] Sorting (all 8 major algorithms)
- [ ] Selection (QuickSelect, Median of Medians)
- [ ] String Matching (KMP, Rabin-Karp, Trie)

---

**Remember**: The goal is not just to memorize but to deeply understand the why, when, and how of each concept!
