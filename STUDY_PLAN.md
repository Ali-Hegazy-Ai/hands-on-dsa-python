# 4-Week Intensive DSA Study Plan

Master every data structure and algorithm in *Hands-On DSA with Python (3rd ed.)* through implementation, testing, benchmarking, and three mini projects.

---

## High-Level Plan

| Week | Theme | Book Chapters | Focus |
|------|-------|---------------|-------|
| 1 | Foundations | 1-5 | Arrays, linked lists, stacks, queues, recursion |
| 2 | Trees and Hashing | 6-9 | Binary trees, BSTs, heaps, hash tables |
| 3 | Graphs and Searching | 10-12 | Graph representations, BFS, DFS, shortest paths, binary search |
| 4 | Sorting, Strings, Projects | 13-16 | All sorting algorithms, string matching, tries, mini projects |

---

## Weekly Rhythm

Each week: 5 sessions, roughly 2-2.5 hours each.

| Session | Activity | Time |
|---------|----------|------|
| Mon | Read chapter, implement core structures | 2.5 h |
| Tue | Write unit tests, fix edge cases | 2 h |
| Wed | Implement algorithms, compare with built-ins | 2.5 h |
| Thu | Solve 2-3 practice problems, run benchmarks | 2 h |
| Fri | Review, refactor, write mini project chunk or notes | 2 h |

Total: ~11 hours/week.

---

## Week 1: Foundations

**Read:** Chapters 1-5 (Python overview, arrays, linked lists, stacks, queues, recursion).

**Implement:**
- `DynamicArray` with amortized append (`src/dsa/arrays/`)
- `SinglyLinkedList`, `DoublyLinkedList` with reverse, cycle detection
- `StackArray`, `QueueArray` (circular buffer), `Deque`
- Recursive utilities: factorial, Fibonacci (memoized), tower of Hanoi

**Tests:**
- 5+ tests per module covering empty, single, many, duplicate inputs
- Edge cases: overflow, underflow, None values

**Benchmarks:**
- `DynamicArray.append` vs `list.append` for n = 10k, 100k, 1M
- Stack push/pop: array vs linked list

**Deliverable:** All Week 1 modules pass `pytest -v`. Benchmark results in `benchmarks/week1.txt`.

---

## Week 2: Trees and Hashing

**Read:** Chapters 6-9 (binary trees, BSTs, heaps, priority queues, hash tables).

**Implement:**
- `BinaryTree` with height, is_balanced, is_complete
- `BST` with insert, search, delete (3 cases), validate, successor
- All traversals: preorder, inorder, postorder, level_order, zigzag
- `MinHeap`, `MaxHeap` with heapify in O(n)
- `PriorityQueue` using heap
- `HashTableChaining`, `HashTableOpenAddressing` (linear probing)

**Tests:**
- BST: insert sequence produces correct inorder, delete preserves BST property
- Heap: extract_min returns elements in sorted order
- Hash table: collision handling, resize triggers

**Benchmarks:**
- BST search vs `dict` lookup for n = 10k
- Custom heap vs `heapq` for n insertions + extractions

**Deliverable:** All Week 2 modules green. Start Mini Project 1.

---

## Week 3: Graphs and Searching

**Read:** Chapters 10-12 (graph representations, BFS, DFS, shortest paths, binary search).

**Implement:**
- `GraphAdjList`, `GraphAdjMatrix`
- BFS: traversal, shortest path (unweighted), connected components
- DFS: traversal, cycle detection (3-color), topological sort
- Dijkstra, Bellman-Ford, Floyd-Warshall
- Binary search: iterative, recursive, find_first, find_last
- `binary_search_on_answer` pattern

**Tests:**
- BFS shortest path on known graph matches expected distances
- Cycle detection: positive and negative cases
- Dijkstra on weighted graph vs known solution
- Binary search edge cases: empty, single, all duplicates

**Benchmarks:**
- BFS vs DFS traversal time on dense vs sparse graphs (100, 1000 nodes)
- `binary_search` vs `bisect.bisect_left` for n = 1M

**Deliverable:** All Week 3 modules green. Complete Mini Project 2.

---

## Week 4: Sorting, Strings, Projects

**Read:** Chapters 13-16 (sorting, selection, string matching, tries).

**Implement:**
- All sorts: bubble, selection, insertion, merge, quick, heap, radix, counting
- Quickselect, median of medians
- Naive string match, KMP (failure function), Rabin-Karp (rolling hash)
- `Trie` with insert, search, starts_with, prefix enumeration

**Tests:**
- Each sort: empty, single, sorted, reversed, duplicates, large random
- KMP: pattern at start, middle, end, overlapping, no match
- Trie: insert/search/prefix for word lists

**Benchmarks:**
- Sort comparison: merge vs quick vs heap vs `sorted()` for n = 10k, 100k
- KMP vs naive match on long text (100k chars)

**Deliverable:** All modules green. Complete Mini Project 3. Full benchmark report.

---

## Mini Projects

### Project 1: Text Frequency Analyzer (Week 2)
- Read a text file, tokenize words, count frequencies using your `HashTableChaining`.
- Find top-k words using your `MinHeap`.
- **Acceptance:** Matches `collections.Counter.most_common(k)` output. Unit tests pass. Writeup: <200 words on hash collision stats observed.

### Project 2: Route Planner (Week 3)
- Build a weighted graph from a CSV of city pairs and distances.
- Find shortest path between two cities using your `dijkstra`.
- Print path and total distance.
- **Acceptance:** Matches known shortest paths for test dataset. Handles disconnected nodes. Writeup: <200 words comparing Dijkstra vs Bellman-Ford on your dataset.

### Project 3: Autocomplete Engine (Week 4)
- Insert a dictionary of words into your `Trie`.
- Given a prefix, return sorted suggestions using `get_words_with_prefix`.
- Benchmark lookup time vs naive linear scan.
- **Acceptance:** Returns correct completions for 10 test prefixes. Sub-millisecond for 50k-word dictionary. Writeup: <200 words on trie space vs time tradeoff.

---

## Repo Skeleton

```
hands-on-dsa-python/
├── src/dsa/                  # All implementations
│   ├── arrays/
│   ├── linked_lists/
│   ├── stacks_queues/
│   ├── trees/
│   ├── heaps/
│   ├── hash_tables/
│   ├── graphs/
│   ├── searching/
│   ├── sorting/
│   ├── selection/
│   ├── strings/
│   ├── _typing.py
│   ├── _errors.py
│   └── _utils.py
├── tests/                    # Mirror structure
├── benchmarks/
├── projects/
│   ├── text_frequency/
│   ├── route_planner/
│   └── autocomplete/
├── notes/
├── .github/workflows/ci.yml
├── pyproject.toml
└── pytest.ini
```

---

## CI Workflow

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: pytest tests/ -v --tb=short
      - run: python -m mypy src/ --ignore-missing-imports
```

---

## Benchmark Instructions

Use `timeit` for consistent measurements. Run each benchmark 3+ times and take the median. Compare your implementation against Python built-ins to validate asymptotic behavior.

```python
import timeit
from dsa.sorting.merge_sort import merge_sort

data = list(range(10_000, 0, -1))

custom = timeit.timeit(lambda: merge_sort(data[:]), number=50)
builtin = timeit.timeit(lambda: sorted(data[:]), number=50)

print(f"merge_sort: {custom:.4f}s | sorted(): {builtin:.4f}s | ratio: {custom/builtin:.1f}x")
```

---

## Quick Checklist (paste into Notion)

```
## Week 1
- [ ] Read chapters 1-5
- [ ] Implement DynamicArray
- [ ] Implement SinglyLinkedList + DoublyLinkedList
- [ ] Implement StackArray + QueueArray + Deque
- [ ] Write recursive utilities
- [ ] 5+ tests per module, all green
- [ ] Run Week 1 benchmarks

## Week 2
- [ ] Read chapters 6-9
- [ ] Implement BST + traversals
- [ ] Implement MinHeap + MaxHeap + PriorityQueue
- [ ] Implement HashTableChaining + HashTableOpenAddressing
- [ ] All tests green
- [ ] Run Week 2 benchmarks
- [ ] Start Mini Project 1 (Text Frequency Analyzer)

## Week 3
- [ ] Read chapters 10-12
- [ ] Implement GraphAdjList + GraphAdjMatrix
- [ ] Implement BFS + DFS + shortest paths
- [ ] Implement binary search variants
- [ ] All tests green
- [ ] Run Week 3 benchmarks
- [ ] Complete Mini Project 2 (Route Planner)

## Week 4
- [ ] Read chapters 13-16
- [ ] Implement all sorting algorithms
- [ ] Implement quickselect + median of medians
- [ ] Implement KMP + Rabin-Karp + Trie
- [ ] All tests green
- [ ] Full benchmark report
- [ ] Complete Mini Project 3 (Autocomplete Engine)
- [ ] Final review and refactor
```

---

When you are satisfied, type: done
