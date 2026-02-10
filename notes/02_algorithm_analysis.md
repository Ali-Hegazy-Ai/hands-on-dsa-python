"""Algorithm analysis notes."""

# Algorithm Analysis: Time and Space Complexity

## Big O Notation

Describes asymptotic behavior as input size n → ∞.

We care about the **worst case** (most important), typically ignore constants and lower-order terms.

### Formal Definition

f(n) is O(g(n)) if there exist constants c > 0 and n₀ such that:
f(n) ≤ c·g(n) for all n ≥ n₀

**In practice:** We identify the dominant term and ignore coefficients.

## Common Time Complexities (Best to Worst)

| Notation | Name | Example | At n=1M |
|----------|------|---------|---------|
| O(1) | Constant | Array access | 1 op |
| O(log n) | Logarithmic | Binary search | ~20 ops |
| O(n) | Linear | Simple loop | 1M ops |
| O(n log n) | Linearithmic | Merge sort | 20M ops |
| O(n²) | Quadratic | Bubble sort | 1T ops |
| O(n³) | Cubic | Matrix mult | 1E18 ops |
| O(2ⁿ) | Exponential | Subsets | 2^1M ops 💥 |
| O(n!) | Factorial | Permutations | too much 💥 |

## Time Complexity Analysis

### Rules

1. **Sequential statements**: Add
   ```
   O(n) + O(n²) = O(n²)
   ```

2. **Conditional**: Take maximum
   ```
   if (O(n)) then O(n²) else O(1) → O(n²)
   ```

3. **Loop**: Multiply
   ```
   for i in range(n):
       for j in range(n):
           O(1) → O(n²)
   ```

4. **Logarithmic**: When dividing
   ```
   while (n > 1):
       n = n / 2
       O(1) → O(log n)
   ```

### Examples

**Linear Search:**
```
for i in range(n):
    if arr[i] == target:
        return True
return False
```
**Time:** O(n) - worst case check all elements

**Binary Search:**
```
left, right = 0, n-1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```
**Time:** O(log n) - halve search space each iteration

**Nested Loops:**
```
for i in range(n):
    for j in range(n):
        print(i, j)  # O(1)
```
**Time:** O(n²) - two nested loops of size n

**Nested with Early Exit:**
```
for i in range(n):
    for j in range(n):
        if some_condition:
            break  # Early exit loop j
```
**Time:** O(n²) worst case, O(n) best case

## Space Complexity

Measures additional memory used (excluding input).

### Examples

**In-place Swap:**
```
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
```
**Space:** O(1) - only swap variables

**Creating New Array:**
```
def copy_array(arr):
    return arr[:]  # Create new list
```
**Space:** O(n) - new array of size n

**Recursion Call Stack:**
```
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```
**Space:** O(n) - call stack depth is n

**Memoization:**
```
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    ...
    memo[n] = result
    return result
```
**Space:** O(n) - memoization dict grows with n

## Amortized Analysis

When operation takes O(n) sometimes but O(1) on average.

**Example: Dynamic Array Append with Doubling**
```
n individual appends:
- Most are O(1)
- Few trigger resize O(current_size)
- Total: O(n) work spread over n operations
- Amortized: O(1) per append
```

## Best, Average, Worst Cases

For quicksort with random pivot:
- **Best:** O(n log n) - balanced partition
- **Average:** O(n log n) - typical random partition
- **Worst:** O(n²) - pivot always smallest/largest

## Recurrence Relations

### Solving Recurrences

**Example: Merge Sort**
```
T(n) = 2·T(n/2) + O(n)
```

Solutions:
1. **Master Theorem:** For T(n) = a·T(n/b) + f(n)
   - If f(n) = O(n^d) where d < log_b(a): T(n) = O(n^(log_b(a)))
   - If f(n) = Θ(n^d) where d = log_b(a): T(n) = O(n^d · log n)
   - If f(n) = Ω(n^d) where d > log_b(a): T(n) = O(f(n))

For merge sort: a=2, b=2, d=1, log_2(2)=1
- d = log_b(a), so T(n) = O(n log n) ✓

## Space-Time Tradeoff

Classic tradeoff in algorithm design:

- **More time, less space:** Compute on the fly
  -Example: Binary search, no extra space
  
- **Less time, more space:** Precompute and store
  - Example: Hash table, memoization

**Hashing:** Trade O(memory) for O(1) lookup
```
Without hash: O(n) linear search
With hash: O(n) build + O(1) lookup
```

## Practical Considerations

Complexity tells us scaling behavior, but constants matter:

- O(n) with constant 100 might be slower than O(n²) with constant 0.001 for small n
- Modern CPUs prefer simpler operations (cache locality, branch prediction)
- Constant factors: cache effects, algorithm constants, language overhead

**Rule of Thumb:**
- Can computer solve for n=10⁶ in 1 second?
- O(n): Yes
- O(n log n): Yes
- O(n²): Maybe (depends on constant)
- O(n³ or 2ⁿ): No

---

**Key Takeaway:** Asymptotic analysis is essential for algorithm comparison, but always consider constants and practical constraints!
