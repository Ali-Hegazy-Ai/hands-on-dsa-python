"""Python data types and built-ins."""

# Python Data Types and Built-in Structures

## Primitive Types

### int
- Arbitrary precision (no overflow in Python 3)
- Performance: O(1) for basic operations
- Use: Counting, indices, discrete values

### float
- IEEE 754 double precision
- Performance: O(1)
- Use: Continuous values, coordinates

### str
- Immutable sequence of Unicode characters
- Performance: O(n) for concatenation, O(1) for indexing
- Use: Text processing, keys (hashable)

### bool
- True/False, subclass of int
- Performance: O(1)
- Use: Conditions, flags

## Collections

### list (Dynamic Array)
```python
arr = [1, 2, 3]  # O(1) amortized append
arr[0]            # O(1) access
arr += [4]        # O(n) operation
```

Time Complexity:
- index: O(1)
- append: O(1) amortized
- insert: O(n)
- remove: O(n)
- search: O(n)

### tuple (Fixed Sequence)
```python
t = (1, 2, 3)     # Immutable
```

Time Complexity: Same as list but no modifications

### dict (Hash Table)
```python
d = {"key": "value"}
d["key"]          # O(1) average
d["key"] = "new"  # O(1) average
```

Time Complexity:
- lookup: O(1) average, O(n) worst
- insert: O(1) average
- delete: O(1) average
- iteration: O(n)

### set (Hash Set)
```python
s = {1, 2, 3}
1 in s            # O(1) average
s.add(4)          # O(1) average
```

Use for: Membership testing, removing duplicates

### deque (Double-Ended Queue)
```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)  # O(1)
dq.pop()          # O(1)
```

Use for: BFS, sliding window

## Built-in Functions for DSA

### Sorting
```python
sorted(arr)               # O(n log n) merge sort based
sorted(arr, reverse=True) # Reverse order
sorted(arr, key=func)     # Custom key function
```

### Searching
```python
"x" in lst        # O(n) for lists
"x" in dct        # O(1) for dicts
lst.index("x")    # O(n), raises ValueError
lst.count("x")    # O(n)
```

### Iteration
```python
enumerate(lst)    # (index, value) pairs
zip(lst1, lst2)   # Parallel iteration
map(func, lst)    # Apply function
filter(func, lst) # Keep where func(x) true
```

### Functional
```python
sum(lst)          # O(n)
min(lst)          # O(n)
max(lst)          # O(n)
any(lst)          # O(n) short-circuit
all(lst)          # O(n) short-circuit
```

### Type Conversion
```python
list(iterable)    # O(n)
tuple(iterable)   # O(n)
set(iterable)     # O(n)
dict(pairs)       # O(n)
```

## Important Properties

### Hashability
Only immutable types are hashable:
- int, float, str, tuple, frozenset
- NOT: list, dict, set

Use for dict keys:
```python
{(1, 2): "key"}   # tuple OK
# {[1, 2]: "key"}  # Error: list not hashable
```

### Mutability
- Mutable: list, dict, set
- Immutable: int, float, str, tuple, frozenset

## Common Patterns

### Two Pointers
```python
left, right = 0, len(arr) - 1
while left < right:
    # process arr[left] and arr[right]
    left += 1
    right -= 1
```

### Sliding Window
```python
from collections import deque
window = deque(maxlen=k)
for i in range(len(arr)):
    window.append(arr[i])
    if len(window) == k:
        # process window
```

### Counter
```python
from collections import Counter
counts = Counter(arr)  # O(n)
counts[x]             # O(1)
```

### DefaultDict
```python
from collections import defaultdict
graph = defaultdict(list)
graph[u].append(v)    # No KeyError
```

## Time Complexity Reference

| Operation | list | dict | set |
|-----------|------|------|-----|
| index | O(1) | - | - |
| lookup | O(n) | O(1)* | O(1)* |
| insert | O(n) | O(1)* | O(1)* |
| delete | O(n) | O(1)* | O(1)* |
| iteration | O(n) | O(n) | O(n) |
| sort | O(n log n) | - | O(n log n) |
| copy | O(n) | O(n) | O(n) |

*average case; O(n) worst case

---

**When to use what:**
- **list**: Ordered, indexed access, modification
- **tuple**: Immutable, hashable (dict keys)
- **deque**: Queue/stack operations (O(1) both ends)
- **dict**: Key-value mapping, fast lookups
- **set**: Unique values, membership testing
