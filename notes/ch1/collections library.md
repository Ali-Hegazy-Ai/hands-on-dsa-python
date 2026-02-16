Let’s do **`deque`** now.

`deque` (pronounced “deck”) means **double-ended queue**.

It’s from:
```python
from collections import deque
```
``

---

## What is `deque`?

A `deque` is like a list, but optimized for:

- **fast append at the end**
    
- **fast append at the front**
    
- **fast pop from the end**
    
- **fast pop from the front**
    

So it’s perfect for:

- **queues**
    
- [**BFS (Breadth First Search)**][ https://en.wikipedia.org/wiki/Breadth-first_search]
    
- sliding window problems
## Why not use a normal list?

### Bad queue using list

If you do:

```python
q.pop(0)
```



### Good queue using deque

`q.popleft()`

This is fast.

## How a Python list works (why shifting happens)

A list is stored like this in memory:

`[ 10 ][ 20 ][ 30 ][ 40 ]`


If you remove the first element:

`lst.pop(0)`

Python must make the list become:

`[ 20 ][ 30 ][ 40 ]`
To do that, it must shift 20, 30, 40 one step left.

That’s why it’s slow.
## How a deque works (no shifting)

A deque is more like:

`Block A: [10, 20, 30] Block B: [40, 50, 60]`

And it stores something like:

- a pointer to the **left position**
    
- a pointer to the **right position**
    

So if you do:

`q.popleft()`

It does NOT move 20, 30, 40, 50, 60.

It just says:

✅ “Left pointer moves one step right.”

So it becomes:

`left now points to 20`

No shifting.
## Simple visualization

Before:

`left -> 10 20 30 40 50 <- right`

After `popleft()`:

`left -> 20 30 40 50 <- right`

Nothing moved. Only the pointer changed.

---

## What if a block becomes empty?

If you remove enough items and a block becomes empty, deque can drop that block completely.

Still no shifting of the remaining elements.

---

## Summary

- **list** = one array → removing from front requires shifting
    
- **deque** = blocks + pointers → removing from front just moves pointer
    

That’s why `deque` is the best structure for queues and BFS.



A **pointer** is basically a value that stores the **memory address** of something.
So instead of storing the actual data, it stores **where the data is located**.
## Simple example idea

If a number is stored somewhere in memory like:

- `20` is stored at address `0xA120`
    

Then a pointer might store:

- `0xA120`
    

So the pointer “points to” the number `20`.

## Why pointers matter in deque

A `deque` keeps:

- a pointer/index to the **leftmost element**
    
- a pointer/index to the **rightmost element**
    

When you do `popleft()`:

- it doesn’t move elements
    
- it just moves the left pointer to the next slot
    

That’s why it’s fast.
Assume this deque:

`q = deque([10, 20, 30, 40])`

### Step 0 (start)

`L -> [10][20][30][40] <- R`

---

## Operation 1: `popleft()`

Returns: `10`

Now `L` moves right by 1:

`L -> [20][30][40] <- R`

---

## Operation 2: `appendleft(5)`

Adds `5` to the left side, so `L` moves left:

`L -> [5][20][30][40] <- R`

---

## Operation 3: `pop()`

Returns: `40`

Now `R` moves left by 1:

`L -> [5][20][30] <- R`

---

## Operation 4: `append(99)`

Adds to the right side, so `R` moves right:

`L -> [5][20][30][99] <- R`

---

### Final idea

`deque` is fast because most operations are just:

- move `L`
    
- move `R`
## 1) What “ordered dictionary” means

It means:

✅ Python keeps items in the dictionary in the **same order you inserted them**.

Example:

`d = {} d["a"] = 1 d["b"] = 2 d["c"] = 3  print(d)`

Output:

`{'a': 1, 'b': 2, 'c': 3}`

---

## 2) Since when?

- **Python 3.7+**: guaranteed by the language
    
- **Python 3.6**: worked in CPython, but not officially guaranteed
    
- **Before 3.6**: not ordered
    

---

## 3) Example: order is preserved in loops

`d = {"x": 10, "y": 20, "z": 30}  for k in d:     print(k)`

Output:

`x y z`

---

## 4) Important: Updating a value does NOT change its position

`d = {"a": 1, "b": 2, "c": 3} d["b"] = 999 print(d)`

Still:

`{'a': 1, 'b': 999, 'c': 3}`

---

## 5) Deleting and reinserting changes order

`d = {"a": 1, "b": 2, "c": 3}  del d["b"] d["b"] = 2  print(d)`

Now:

`{'a': 1, 'c': 3, 'b': 2}`

Because `"b"` was inserted again at the end.

---

## 6) What about `OrderedDict`?

Before Python 3.7, people used:

`from collections import OrderedDict`

Now, in most cases:

✅ normal `dict` is enough.

But `OrderedDict` still has extra features, like:

- `move_to_end()`
    
- easy reordering
    

---

## Mini problem

### Problem:

Given a dictionary, print the **first inserted key**.

`d = {"a": 10, "b": 20, "c": 30}`

### Answer:

`first_key = next(iter(d)) print(first_key)  # a`