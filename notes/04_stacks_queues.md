"""Notes on stacks and queues."""

# Stacks and Queues

## Stack (LIFO - Last In First Out)

### Operations
- **Push:** Add to top - O(1)
- **Pop:** Remove from top - O(1)
- **Peek:** View top - O(1)
- **isEmpty:** Check if empty - O(1)

### Applications
- Expression evaluation (parentheses matching)
- Function call stack
- Undo/redo functionality
- Browser back button
- DFS in graphs

### Example Implementation
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)  # O(1) amortized
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # O(1)
        return None
```

### Balanced Parentheses Problem
```
({[]}) → Valid
({[)]} → Invalid

Algorithm: Use stack
- ( → push
- ) → pop and check match
```

## Queue (FIFO - First In First Out)

### Operations
- **Enqueue:** Add to rear - O(1)
- **Dequeue:** Remove from front - O(1) with circular buffer
- **Front:** View front - O(1)
- **isEmpty:** Check if empty - O(1)

### Applications
- BFS in graphs
- Print job queue
- Message queues
- CPU scheduling
- Traffic management

### Naive Implementation Problem
```python
# Bad: O(n) dequeue due to shifting
class Queue:
    def dequeue(self):
        return self.items.pop(0)  # O(n) - shift all elements!
```

### Solution: Circular Buffer or Deque
```python
from collections import deque
q = deque()
q.append(1)      # O(1)
q.popleft()      # O(1) - no shifting!
```

## Deque (Double-Ended Queue)

Allows insertion/deletion at both ends in O(1)

```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)   # O(1) - add to front
dq.append(4)       # O(1) - add to back
dq.popleft()       # O(1) - remove from front
dq.pop()           # O(1) - remove from back
```

### Uses
- Sliding window problems
- LRU cache (with dict)
- Palindrome checking

## Comparison

| Operation | Stack (Array) | Queue (Array) | Queue (Circular) | Deque |
|-----------|--------------|---------------|------------------|-------|
| Add | O(1) | O(1) | O(1) | O(1) |
| Remove | O(1) | O(n)! | O(1) | O(1) |
| Access | O(1) | O(1) | O(1) | O(1) |

## Stack vs Queue in Graphs

- **DFS (Depth-First):** Use Stack - explore deep first
- **BFS (Breadth-First):** Use Queue - explore level by level

## Common Problems

1. **Balanced Parentheses:** Stack to match pairs
2. **Next Greater Element:** Stack with monotonic ordering
3. **Sliding Window Maximum:** Deque to track max in window
4. **Trapping Rain Water:** Stack to find trapped positions

---

## Exercises

(Add your practice problems here)
