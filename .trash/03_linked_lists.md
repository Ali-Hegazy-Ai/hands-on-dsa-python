"""Notes on linked lists."""

# Linked Lists

## Definition

A linked list is a linear data structure where elements (nodes) are connected via pointers/references instead of contiguous memory.

Each node contains:
- Data (value)
- Next pointer (to next node)
- (For doubly-linked: Previous pointer)

## Singly Linked List

```
head → [data | next] → [data | next] → [data | None]
```

### Operations

| Operation | Time | Space |
|-----------|------|-------|
| Access | O(n) | O(1) |
| Search | O(n) | O(1) |
| Insert (head) | O(1) | O(1) |
| Insert (tail) | O(n) | O(1) |
| Insert (middle) | O(n) | O(1) |
| Delete (head) | O(1) | O(1) |
| Delete (tail) | O(n) | O(1) |
| Delete (middle) | O(n) | O(1) |

### Complexity Analysis

Best case (head operation): O(1)
Average case: O(n)
Worst case (tail operation): O(n)

## Doubly Linked List

Each node has both next and previous pointers:
```
None ← [prev | data | next] ↔ [prev | data | next] → None
```

Advantages:
- Can traverse backward
- Easier deletion (have parent reference)
- Can insert/delete at both ends efficiently

Trade-off: Extra pointer per node (more memory)

## Circular Linked List

Last node points back to first node (no None at end)

Uses:
- Round-robin scheduling
- Undo/redo functionality
- Carousel/playlist cycling

## Key Algorithms

### Reverse

**Problem:** Reverse a singly linked list

**Approach:** Use three pointers (prev, curr, next):
```
prev = None
curr = head
while curr:
    next = curr.next  # Save next
    curr.next = prev  # Reverse link
    prev = curr       # Move prev
    curr = next       # Move curr
```
Time: O(n), Space: O(1)

### Find Kth from End

**Problem:** Find node that is k positions from end

**Approach:** Two pointers with k gap
```
fast = head
slow = head
# Move fast k steps ahead
for _ in range(k):
    fast = fast.next
# Move both until fast reaches end
while fast.next:
    fast = fast.next
    slow = slow.next
return slow  # k-th from end
```
Time: O(n), Space: O(1)

### Detect Cycle

**Problem:** Detect if list contains cycle

**Floyd's Cycle Detection (Tortoise and Hare):**
```
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected
return False
```
Time: O(n), Space: O(1)

## Common Mistakes

1. **Lost head pointer:** Always keep reference to head
2. **Null pointer errors:** Check for None before using next
3. **Memory leaks:** Don't create cycles unless intentional
4. **Off-by-one:** Count nodes carefully (1st node is next=Node, not next.next)
5. **Modifying while iterating:** Can skip nodes or infinite loop

## When to Use

- **Singly LL:** Stack, custom queue, simple sequence
- **Doubly LL:** LRU cache, undo/redo, traversal both ways
- **Circular LL:** Round-robin, game turn cycles
- **vs Array:** When frequent insert/delete at front (LL better), otherwise array better for random access

---

## Exercises

(Add your practice problems here)
