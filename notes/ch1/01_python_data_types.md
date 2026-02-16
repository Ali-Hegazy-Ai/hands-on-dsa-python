# Python Data Types and Structures Notes #title

## Python 3.10 Overview #python-310-overview

### Core Concepts #core-concepts

* **Interpreted language**: Python executes code line by line, which makes debugging easier and allows for interactive programming
* **Dynamically typed**: Variable types are determined at runtime, eliminating the need for explicit type declarations
* **Object-oriented**: Supports classes, inheritance, and polymorphism
* **Open source**: Free to use with a large, active community
* **Cross-platform**: Runs on Windows, Linux, macOS, and other operating systems

### Why Python for Data Structures? #why-python

* **Readable syntax**: Clean, intuitive code that closely resembles pseudocode
* **Rich built-in types**: Extensive collection of data structures ready to use
* **Fast development**: Quick prototyping and implementation of algorithms
* **Large ecosystem**: Abundant libraries and tools for data manipulation

> 🔍 **Extra context (not in PDF)**: Python's dynamic nature makes it excellent for learning data structures because you can focus on concepts rather than memory management and type declarations. However, this same feature can make Python slower than compiled languages like C++ or Java for production systems.

---

## Python Installation #python-installation

### Windows Installation #windows-install

1. Navigate to https://www.python.org/downloads/
2. Select Python 3.10.0 (or latest) matching your system architecture (32-bit or 64-bit)
3. Download and run the `.exe` file
4. **Critical**: Check "Add Python 3.10 to PATH" before installing
5. Click "Install Now" and wait for completion
6. Verify installation:
   ```bash
   python --version
   ```
   Expected output: `Python 3.10.0`

### Linux Installation #linux-install

```bash
# Check if Python is already installed
python --version

# Install Python 3.10 if not present
sudo apt-get install python3.10

# Verify installation
python3.10 --version
```

### macOS Installation #mac-install

1. Visit https://www.python.org/downloads/
2. Download Python 3.10.0 installer
3. Open the downloaded file and click "Install Now"
4. Verify installation:
   ```bash
   python --version
   ```

### Installation Comparison Table #install-comparison

| OS | Installation Method | PATH Handling | Verification Command |
|-----|---------------------|---------------|----------------------|
| Windows | Executable installer | Manual check required | `python --version` |
| Linux | Package manager (apt) | Automatic | `python3.10 --version` |
| macOS | Installer package | Automatic | `python --version` |

---

## Development Environment Setup #dev-environment

### Command Line Setup #cli-setup

```bash
# Windows: Open Command Prompt and type:
py

# Linux/macOS: Open terminal and type:
python3
```

**Features:**
- Immediate feedback with REPL (Read-Eval-Print Loop)
- Good for quick tests and small code snippets
- Limited for larger programs

### Jupyter Notebook Setup #jupyter-setup

#### Installation Methods:

**Windows (via Anaconda):**
1. Download Anaconda from https://www.anaconda.com/products/individual
2. Run installer
3. Launch via Command Prompt: `jupyter notebook`
4. Or use the Anaconda Navigator GUI

**Linux/macOS:**
```bash
# Install using pip
pip3 install notebook

# Launch Jupyter
jupyter notebook

# Alternative command if the above fails
python3 -m notebook
```

### Environment Comparison #env-comparison

| Feature | Command Line | Jupyter Notebook |
|---------|--------------|------------------|
| Best for | Quick tests, simple scripts | Data analysis, tutorials, documentation |
| Code persistence | Not saved automatically | Saved in .ipynb files |
| Visualization | Text-only | Rich output (charts, images) |
| Code organization | Linear | Cell-based, mix of code and text |
| Learning curve | Minimal | Slightly steeper |

---

## Data Types and Objects Fundamentals #data-types-basics

### Core Concepts #data-types-core

* **Variables**: Containers that store values in memory
* **Objects**: Every piece of data in Python is an object of a specific type
* **Dynamic typing**: Variables can reference different types throughout program execution
* **Type checking**: Use `type()` function to determine an object's type

### Dynamic Typing Demonstration #dynamic-typing

```python
# Variable assignment creates objects automatically
p = "Hello India"     # String object created
q = 10                # Integer object created  
r = 10.2              # Float object created

# Check types at runtime
print(type(p))        # <class 'str'>
print(type(q))        # <class 'int'>
print(type(r))        # <class 'float'>
print(type(12 + 31j)) # <class 'complex'>
```

**Output:**
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
```

### Variable Reassignment #var-reassignment

```python
var = 13.2            # Creates float object
print(var)            # 13.2
print(type(var))      # <class 'float'>

var = "Now the type is string"  # Reassigns to string object
print(type(var))      # <class 'str'>
```

**Explanation:**
- Python doesn't "convert" the variable's type—it creates a new string object and makes `var` reference it
- The original float object becomes eligible for garbage collection
- This illustrates Python's dynamic typing in action

### Memory Representation #memory-diagram

```
Step 1: var = 13.2
┌─────────┐     ┌─────────────┐
│   var   │────▶│ Float Object│
└─────────┘     │   value:13.2│
                └─────────────┘

Step 2: var = "Now the type is string"
┌─────────┐     ┌─────────────┐
│   var   │────▶│ String Object│
└─────────┘     │ value: "Now..."│
                └─────────────┘
```

### Built-in Types Overview #builtin-types

| Category | Types | Mutability |
|----------|-------|------------|
| Numeric | `int`, `float`, `complex` | Immutable |
| Boolean | `bool` | Immutable |
| Sequence | `str`, `range`, `list`, `tuple` | Mixed (list mutable, others immutable) |
| Mapping | `dict` | Mutable |
| Set | `set`, `frozenset` | Mixed (set mutable, frozenset immutable) |

---

## Numeric Data Types #numeric-types

### Integer (int) #int-type

* Represents whole numbers (positive, negative, zero)
* No size limit (can handle arbitrarily large numbers)
* Base-10 by default

```python
# Integer examples
age = 25
population = -1000
large_number = 9999999999999999999999

print(type(age))      # <class 'int'>
```

### Float (float) #float-type

* Represents numbers with decimal points
* Double-precision (accurate to ~15 decimal places)
* Scientific notation supported

```python
# Float examples
price = 99.99
temperature = -2.5
scientific = 1.5e-4    # 0.00015

print(type(price))     # <class 'float'>
```

### Complex (complex) #complex-type

* Represents complex numbers: `a + bj`
* `a` = real part, `b` = imaginary part
* `j` represents √-1

```python
# Complex examples
c1 = 3 + 4j
c2 = 2.5j
c3 = complex(2, 3)     # 2 + 3j

print(type(c1))        # <class 'complex'>
print(c1.real)         # 3.0
print(c1.imag)         # 4.0
```

### Numeric Type Comparison #numeric-comparison

| Type | Range | Precision | Use Case |
|------|-------|-----------|----------|
| `int` | Unlimited | Exact | Counting, indexing, whole numbers |
| `float` | ~1e-308 to 1e+308 | ~15 decimal digits | Measurements, scientific calculations |
| `complex` | Same as float | Same as float | Engineering, physics, signal processing |

---

## Boolean Data Type #boolean-type

### Core Concepts #boolean-core

* Represents truth values: `True` or `False`
* Subclass of integer (`True` = 1, `False` = 0)
* Used for conditional logic and comparisons

```python
# Boolean examples
is_active = True
is_complete = False

print(type(True))      # <class 'bool'>
print(type(False))     # <class 'bool'>
```

### Boolean Conversion #bool-conversion

```python
# Using bool() function - any non-zero value is True, zero is False
print(bool(22))        # True
print(bool(0))         # False
print(bool(-2.3))      # True
print(bool(0j))        # False
print(bool(""))        # False (empty string)
print(bool("Hello"))   # True (non-empty string)

# Practical example
val1 = 0
val2 = 11
val3 = -2.3

print(bool(val1))      # False
print(bool(val2))      # True
print(bool(val3))      # True
```

### When to Use Boolean #when-to-use-bool

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Flags and switches | Use `True`/`False` directly | Clearer intent than 1/0 |
| Checking conditions | Let Python evaluate implicitly | More Pythonic |
| Function return values | Return `bool` type | Explicit and self-documenting |

---

## Sequence Types #sequence-types

## Strings (str) #string-type

### Core Concepts #string-core

* **Immutable**: Cannot be changed after creation
* **Ordered**: Characters maintain their position
* **Iterable**: Can loop through each character
* **Zero-indexed**: First character at position 0

### String Creation #string-creation

```python
# Single quotes
str1 = 'Hello how are you'

# Double quotes (useful when string contains single quotes)
str2 = "Hello how are you"

# Triple quotes (multi-line strings)
str3 = """This is a
multi-line
string"""

print(str1)
print(str2)
print(str3)
```

**Output:**
```
Hello how are you
Hello how are you
This is a
multi-line
string
```

### String Operations #string-operations

```python
# Concatenation (+)
first = 'data'
second = 'structure'
print(first + second)           # datastructure
print('Data' + 'structure')     # Datastructure

# Repetition (*)
st = 'data.'
print(st * 3)                    # data.data.data.
print(3 * st)                    # data.data.data.

# Membership testing
print('a' in 'data')             # True
print('x' not in 'data')         # True
```

### String Methods Table #string-methods

| Method | Syntax | Example | Description |
|--------|--------|---------|-------------|
| `upper()` | `s.upper()` | `"hello".upper()` → `"HELLO"` | Converts to uppercase |
| `lower()` | `s.lower()` | `"HELLO".lower()` → `"hello"` | Converts to lowercase |
| `split()` | `s.split(sep)` | `"a,b,c".split(",")` → `["a","b","c"]` | Splits string into list |
| `join()` | `sep.join(iterable)` | `",".join(["a","b"])` → `"a,b"` | Joins iterable with separator |
| `strip()` | `s.strip()` | `" hello ".strip()` → `"hello"` | Removes leading/trailing whitespace |
| `replace()` | `s.replace(old, new)` | `"hi".replace("i","ello")` → `"hello"` | Replaces substring |

### When to Use Strings #when-to-use-string

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Text processing | Use string methods | Built-in, optimized operations |
| Building strings from loops | Use `join()` not `+` | `+` creates new strings each iteration (inefficient) |
| Complex formatting | f-strings (Python 3.6+) | Most readable and fastest |
| Regular expressions | `re` module | Pattern matching beyond simple operations |

---

## Range Type #range-type

### Core Concepts #range-core

* **Immutable** sequence of numbers
* **Memory efficient**: Doesn't store all values, generates them on demand
* **Commonly used** in `for` loops

### Range Syntax #range-syntax

```python
range(start, stop, step)
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `start` | First number in sequence | 0 |
| `stop` | Sequence stops BEFORE this number | Required |
| `step` | Increment between numbers | 1 |

### Range Examples #range-examples

```python
# Basic range (0 to 9)
print(list(range(10)))           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(10))                  # range(0, 10)

# Range with start and stop
print(list(range(1, 10, 2)))      # [1, 3, 5, 7, 9]
print(range(1, 10, 2))            # range(1, 10, 2)

# Negative step (counting down)
print(list(range(20, 10, -2)))    # [20, 18, 16, 14, 12]

# Using range in loops
for i in range(3):
    print(f"Iteration {i}")
```

**Output:**
```
Iteration 0
Iteration 1
Iteration 2
```

### Range Characteristics #range-properties

| Property | Description |
|----------|-------------|
| Memory usage | O(1) - constant regardless of size |
| Access time | O(1) - can calculate any element directly |
| Mutability | Immutable |
| Use case | Generating sequences without storing them |

---

## Lists #list-type

### Core Concepts #list-core

* **Mutable**: Can add, remove, or modify elements
* **Ordered**: Elements maintain insertion order
* **Heterogeneous**: Can contain different types
* **Dynamic**: Grows and shrinks as needed
* **Zero-indexed**: First element at position 0

### List Creation #list-creation

```python
# Empty list
empty_list = []

# List with elements
fruits = ['apple', 'banana', 'orange']

# Mixed types
mixed = [10, "India", "world", 8]

# Nested lists
nested = [1, [2, 3], [4, 5, 6]]

print(fruits)          # ['apple', 'banana', 'orange']
print(mixed[1])        # India (access by index)
```

### List Operations #list-operations

```python
# Accessing elements
my_list = [10, "India", "world", 8]
print(my_list[1])       # India (positive index)
print(my_list[-1])      # 8 (negative index - last element)
print(my_list[1:3])     # ['India', 'world'] (slicing)

# Modifying elements
my_list[1] = "Bharat"
print(my_list)          # [10, 'Bharat', 'world', 8]

# Adding elements
my_list.append(25)      # Add to end
my_list.insert(1, "new") # Insert at position 1
print(my_list)          # [10, 'new', 'Bharat', 'world', 8, 25]

# Removing elements
my_list.remove('world') # Remove by value
popped = my_list.pop()  # Remove and return last element
del my_list[0]          # Remove by index

# List concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b               # [1, 2, 3, 4, 5, 6]

# List replication
print([0] * 5)          # [0, 0, 0, 0, 0]
```

### List Characteristics #list-properties

| Property | Description | Example |
|----------|-------------|---------|
| **Ordered** | Elements keep their order | `[10,12,31,14]` != `[14,10,31,12]` |
| **Dynamic** | Can grow/shrink | `b += [32]` adds element |
| **Heterogeneous** | Mixed types allowed | `[2.2, 'python', 31, False]` |
| **Mutable** | Can modify in place | `b[2:3] = []` removes slice |

### Dynamic List Operations #list-dynamic

```python
# Demonstrating list mutability
b = ['data', 'and', 'book', 'structure', 'hello', 'st']
print(b)                # ['data', 'and', 'book', 'structure', 'hello', 'st']

# Adding elements
b += [32]
print(b)                # ['data', 'and', 'book', 'structure', 'hello', 'st', 32]

# Removing a slice
b[2:3] = []
print(b)                # ['data', 'and', 'structure', 'hello', 'st', 32]

# Deleting by index
del b[0]
print(b)                # ['and', 'structure', 'hello', 'st', 32]
```

### List Methods Table #list-methods

| Method | Syntax | Description | Example |
|--------|--------|-------------|---------|
| `append()` | `list.append(x)` | Adds x to end | `[1].append(2)` → `[1,2]` |
| `extend()` | `list.extend(iter)` | Adds all items from iterable | `[1].extend([2,3])` → `[1,2,3]` |
| `insert()` | `list.insert(i, x)` | Inserts x at position i | `[1,3].insert(1,2)` → `[1,2,3]` |
| `remove()` | `list.remove(x)` | Removes first occurrence of x | `[1,2,1].remove(1)` → `[2,1]` |
| `pop()` | `list.pop([i])` | Removes and returns item at i (default last) | `[1,2,3].pop(1)` → `2` |
| `index()` | `list.index(x)` | Returns index of first x | `[1,2,3].index(2)` → `1` |
| `count()` | `list.count(x)` | Counts occurrences of x | `[1,2,2,3].count(2)` → `2` |
| `sort()` | `list.sort()` | Sorts list in place | `[3,1,2].sort()` → `[1,2,3]` |
| `reverse()` | `list.reverse()` | Reverses list in place | `[1,2,3].reverse()` → `[3,2,1]` |

### When to Use Lists #when-to-use-list

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Ordered collection that changes | Use list | Mutable and maintains order |
| Stack (LIFO) | Use `append()` and `pop()` | O(1) operations at end |
| Queue (FIFO) | Use `collections.deque` | List pop(0) is O(n) |
| Need random access by index | Use list | O(1) access time |
| Frequently checking membership | Use set instead | List membership is O(n) |

---

## Tuples #tuple-type

### Core Concepts #tuple-core

* **Immutable**: Cannot change after creation
* **Ordered**: Elements maintain position (zero-indexed)
* **Heterogeneous**: Can contain different types
* **Hashable**: Can be used as dictionary keys (if all elements are hashable)
* **More memory efficient** than lists

### Tuple Creation #tuple-creation

```python
# Empty tuple
empty_tuple = ()

# Single element tuple (note the comma!)
single = (5,)          # Without comma, it's just an integer

# Multiple elements
my_tuple = ("Shyam", 23, True, "male")

# Without parentheses (tuple packing)
another_tuple = 1, 2, 3

print(type(my_tuple))   # <class 'tuple'>
print(my_tuple[1])      # 23 (access by index)
```

### Tuple Operations #tuple-operations

```python
# Length
print(len((4, 5, "hello")))      # 3

# Concatenation
print((4, 5) + (10, 20))          # (4, 5, 10, 20)

# Repetition
print((2, 1) * 3)                  # (2, 1, 2, 1, 2, 1)

# Membership
print(3 in ('hi', 'xyz', 3))       # True

# Iteration
for p in (6, 7, 8):
    print(p)                        # 6, 7, 8 (each on new line)
```

### Tuple Indexing and Slicing #tuple-indexing

```python
x = ("hello", "world", "india")

# Zero-based indexing (starts at 0)
print(x[1])            # "world"

# Negative indexing (from right)
print(x[-2])           # "world"

# Slicing (start:stop)
print(x[1:])           # ("world", "india")
```

| Expression | Result | Description |
|------------|--------|-------------|
| `x[1]` | `"world"` | Zero-based indexing |
| `x[-2]` | `"world"` | Negative indexing (from right) |
| `x[1:]` | `("world", "india")` | Slicing from index 1 to end |

### Tuple vs List Comparison #tuple-vs-list

| Aspect | Tuple | List |
|--------|-------|------|
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Mutability | Immutable | Mutable |
| Memory | More efficient | Less efficient |
| Speed | Faster access | Slower access |
| Use as dict key | Yes (if hashable) | No |
| Methods | Few (count, index) | Many |

### When to Use Tuples #when-to-use-tuple

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Fixed data (coordinates, RGB values) | Use tuple | Immutability prevents accidental changes |
| Dictionary keys | Use tuple | Lists can't be keys |
| Function returning multiple values | Return tuple | Python automatically packs them |
| Data that shouldn't change | Use tuple | Self-documenting immutability |
| High-performance requirements | Consider tuple | Slightly faster than lists |

---

## Operators #operators

## Membership Operators #membership-operators

### Core Concepts #membership-core

* Test whether a value exists in a sequence
* Return `True` or `False`
* Work with strings, lists, tuples, dictionaries (keys), and sets

### `in` Operator #in-operator

```python
# Check if element exists in list
mylist1 = [100, 20, 30, 40]
mylist2 = [10, 50, 60, 90]

if mylist1[1] in mylist2:
    print("elements are overlapping")
else:
    print("elements are not overlapping")
```

**Output:**
```
elements are not overlapping
```

### `not in` Operator #not-in-operator

```python
val = 104
mylist = [100, 210, 430, 840, 108]

if val not in mylist:
    print("Value is NOT present in mylist")
else:
    print("Value is present in mylist")
```

**Output:**
```
Value is NOT present in mylist
```

---

## Identity Operators #identity-operators

### Core Concepts #identity-core

* Compare object identity (whether two variables point to the same object)
* Different from equality (`==`) which compares values
* Use `is` and `is not`

### `is` Operator #is-operator

```python
Firstlist = []
Secondlist = []

# Equality comparison (values)
if Firstlist == Secondlist:
    print("Both are equal")
else:
    print("Both are not equal")

# Identity comparison (same object)
if Firstlist is Secondlist:
    print("Both variables are pointing to the same object")
else:
    print("Both variables are not pointing to the same object")

thirdlist = Firstlist

if thirdlist is Firstlist:
    print("Both are pointing to the same object")
else:
    print("Both are not pointing to the same object")
```

**Output:**
```
Both are equal
Both variables are not pointing to the same object
Both are pointing to the same object
```

### `is not` Operator #is-not-operator

```python
Firstlist = []
Secondlist = []

if Firstlist is not Secondlist:
    print("Both Firstlist and Secondlist variables are not the same object")
else:
    print("Both Firstlist and Secondlist variables are the same object")
```

**Output:**
```
Both Firstlist and Secondlist variables are not the same object
```

### Identity vs Equality #identity-vs-equality

| Aspect | `is` / `is not` | `==` / `!=` |
|--------|-----------------|--------------|
| Compares | Object identity (memory address) | Object value |
| Returns `True` for | Same object in memory | Equal values |
| Use for | Checking `None`, singletons | Value comparison |
| Can be overridden? | No | Yes (`__eq__` method) |

---

## Logical Operators #logical-operators

### Core Concepts #logical-core

* Combine conditional statements
* Short-circuit evaluation (stop as soon as result is determined)
* Return `True` or `False`

### AND Operator #and-operator

```python
a = 32
b = 132

if a > 0 and b > 0:
    print("Both a and b are greater than zero")
else:
    print("At least one variable is less than 0")
```

**Output:**
```
Both a and b are greater than zero
```

### OR Operator #or-operator

```python
a = 32
b = -32

if a > 0 or b > 0:
    print("At least one variable is greater than zero")
else:
    print("Both variables are less than 0")
```

**Output:**
```
At least one variable is greater than zero
```

### NOT Operator #not-operator

```python
a = 32

if not a:
    print("Boolean value of a is False")
else:
    print("Boolean value of a is True")
```

**Output:**
```
Boolean value of a is True
```

### Logical Operators Truth Table #logical-truth

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

---

## Dictionaries #dict-type

### Core Concepts #dict-core

* **Key-value pairs**: Each element has a key and associated value
* **Unordered** (in Python <3.7) / **Ordered** (Python 3.7+ maintains insertion order)
* **Mutable**: Can add, remove, modify pairs
* **Keys must be immutable**: Strings, numbers, tuples (of immutables)
* **Values can be any type**: Including lists, dictionaries, etc.
* **Fast lookup**: O(1) average time complexity

### Dictionary Creation #dict-creation

```python
# Empty dictionary
empty_dict = {}

# Dictionary with items
my_dict = {'1': 'data', '2': 'structure', '3': 'python'}

# Using dict() constructor
another_dict = dict(name='ABC', age=31, city='Jaipur')

# Building dynamically
person = {}
person['name'] = 'ABC'
person['lastname'] = 'XYZ'
person['age'] = 31
person['address'] = ['Jaipur']

print(person)
# {'name': 'ABC', 'lastname': 'XYZ', 'age': 31, 'address': ['Jaipur']}
print(person['name'])    # ABC
```

### Dictionary Operations #dict-operations

```python
# Accessing values
print(person.get('name'))           # ABC (safe access, returns None if missing)
print(person.get('phone', 'N/A'))   # N/A (default value)

# Checking membership (works on keys)
print('name' in person)             # True
print('phone' not in person)        # True

# Getting all keys, values, items
print(person.keys())                # dict_keys(['name', 'lastname', 'age', 'address'])
print(person.values())              # dict_values(['ABC', 'XYZ', 31, ['Jaipur']])
print(person.items())               # dict_items([('name', 'ABC'), ...])

# Updating values
person['age'] = 32

# Adding new key-value pairs
person['phone'] = '123-456-7890'

# Removing items
removed_value = person.pop('phone')   # Removes and returns value
last_item = person.popitem()          # Removes and returns last inserted item
del person['age']                      # Deletes key-value pair
person.clear()                          # Removes all items
```

### Dictionary Methods Table #dict-methods

| Method | Description | Example |
|--------|-------------|---------|
| `clear()` | Removes all items | `d.clear()` |
| `get(key[, default])` | Returns value for key, or default | `d.get('x', 0)` |
| `items()` | Returns view of (key, value) pairs | `d.items()` |
| `keys()` | Returns view of keys | `d.keys()` |
| `values()` | Returns view of values | `d.values()` |
| `pop(key[, default])` | Removes key and returns value | `d.pop('a')` |
| `popitem()` | Removes and returns last inserted item | `d.popitem()` |
| `update([other])` | Updates with key-value pairs from other | `d.update({'b': 200})` |

### Dictionary Examples #dict-examples

```python
# Creating and accessing
person = {}
person['name'] = 'ABC'
person['lastname'] = 'XYZ'
person['age'] = 31
person['address'] = ['Jaipur']
print(person)           # {'name': 'ABC', 'lastname': 'XYZ', 'age': 31, 'address': ['Jaipur']}
print(person['name'])   # ABC

# Membership testing
print('name' in person)                     # True
print('address' in person)                  # True
print('city' not in person)                 # True

# pop() example
mydict = {'a': 1, 'b': 2, 'c': 3}
print(mydict.pop('b'))   # 2
print(mydict)            # {'a': 1, 'c': 3}

# popitem() example
mydict = {'a': 1, 'b': 2, 'c': 3}
print(mydict.popitem())  # ('c', 3)
print(mydict)            # {'a': 1, 'b': 2}

# update() example
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1)                # {'a': 10, 'b': 200, 'c': 30, 'd': 400}
```

### Dictionary Characteristics #dict-properties

| Property | Description | Example |
|----------|-------------|---------|
| Keys unique | Duplicate keys not allowed | Last value overwrites earlier |
| Keys immutable | Must be hashable | Lists can't be keys |
| Values mutable | Can be any type | Lists, dicts allowed |
| Dynamic | Grows/shrinks as needed | Adding new keys |
| Fast lookup | O(1) average | Hash table implementation |

### When to Use Dictionaries #when-to-use-dict

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Lookup by unique key | Use dictionary | O(1) access time |
| Counting occurrences | Use `collections.Counter` | Built specifically for this |
| Grouping related data | Use dictionary | Natural key-value mapping |
| JSON-like data | Use dictionary | Direct mapping to JSON |
| Need ordered keys (Python 3.7+) | Use dictionary | Maintains insertion order |
| Need default values for missing keys | Use `defaultdict` | Avoids KeyError |

---

## Sets #set-type

### Core Concepts #set-core

* **Unordered**: Elements have no defined position
* **Unique**: No duplicate elements allowed
* **Mutable**: Can add and remove elements
* **Elements must be hashable**: Immutable types only
* **Mathematical set operations**: Union, intersection, difference, etc.

### Set Creation #set-creation

```python
# Using curly braces
x1 = {'and', 'python', 'data', 'structure'}
print(x1)               # Order may vary: {'python', 'structure', 'data', 'and'}
print(type(x1))         # <class 'set'>

# Using set() constructor
x2 = set(['and', 'python', 'data', 'structure'])
print(x2)               # Same as above

# Empty set (note: {} creates empty dictionary)
empty_set = set()

# From string (creates set of characters)
char_set = set('hello')
print(char_set)         # {'h', 'e', 'l', 'o'} (note: only one 'l')
```

> ⚠️ **Note**: Sets are unordered, so output order may differ from what's shown here. This doesn't affect set operations.

### Set Operations #set-operations

```python
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

# Length
print(len(x1))          # 2

# Membership (very fast, O(1))
print('structure' in x1)    # True
print('java' not in x1)     # True

# Union (elements in either set)
print(x1 | x2)                      # {'structure', 'data', 'java', 'c', 'python'}
print(x1.union(x2))                  # Same result

# Intersection (elements in both sets)
print(x1 & x2)                       # {'data'}
print(x1.intersection(x2))           # Same result

# Difference (elements in x1 but not x2)
print(x1 - x2)                       # {'structure'}
print(x1.difference(x2))             # Same result

# Symmetric difference (elements in either, but not both)
print(x1 ^ x2)                       # {'structure', 'python', 'c', 'java'}
print(x1.symmetric_difference(x2))   # Same result
```

### Set Operations Table #set-operations-table

| Operation | Operator | Method | Description |
|-----------|----------|--------|-------------|
| Union | `|` | `union()` | All elements from both sets |
| Intersection | `&` | `intersection()` | Elements common to both sets |
| Difference | `-` | `difference()` | Elements in first but not second |
| Symmetric Difference | `^` | `symmetric_difference()` | Elements in either but not both |
| Subset | `<=` | `issubset()` | All elements of first in second |
| Superset | `>=` | `issuperset()` | All elements of second in first |

### Set Methods #set-methods

```python
# Adding elements
s = {1, 2, 3}
s.add(4)                # {1, 2, 3, 4}
s.update([5, 6])        # {1, 2, 3, 4, 5, 6}

# Removing elements
s.remove(3)             # Raises KeyError if not present
s.discard(10)           # No error if not present
popped = s.pop()        # Removes and returns arbitrary element
s.clear()               # Removes all elements

# Set comparisons
a = {1, 2, 3}
b = {1, 2}
print(b.issubset(a))    # True
print(a.issuperset(b))  # True
print(a.isdisjoint({4})) # True (no common elements)
```

### Set Venn Diagram #set-venn

```
Union (|)           Intersection (&)     Difference (-)      Symmetric Diff (^)
┌─────┐ ┌─────┐     ┌─────┐ ┌─────┐     ┌─────┐ ┌─────┐     ┌─────┐ ┌─────┐
│ A   │ │ B   │     │ A   │ │ B   │     │ A   │ │ B   │     │ A   │ │ B   │
│  ┌──┼─┼──┐  │     │  ┌──┼─┼──┐  │     │  ┌──┼─┼──┐  │     │  ┌──┼─┼──┐  │
│  │░░│ │░░│  │     │  │░░│ │░░│  │     │  │░░│ │  │  │     │  │░░│ │░░│  │
│  └──┼─┼──┘  │     │  └──┼─┼──┘  │     │  └──┼─┼──┘  │     │  └──┼─┼──┘  │
└─────┘ └─────┘     └─────┘ └─────┘     └─────┘ └─────┘     └─────┘ └─────┘
All shaded          Only overlap         Only A             Both but not overlap
```

### When to Use Sets #when-to-use-set

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Remove duplicates | Convert to set | Automatically eliminates duplicates |
| Fast membership testing | Use set | O(1) vs O(n) for lists |
| Mathematical set operations | Use set | Built-in operators |
| Need unique elements | Use set | Enforces uniqueness |
| Order matters | Use list instead | Sets are unordered |

---

## Frozen Sets #frozenset-type

### Core Concepts #frozenset-core

* **Immutable version of set**
* **Hashable**: Can be used as dictionary keys or set elements
* **All other properties** same as set (unordered, unique elements)

### Frozen Set Creation #frozenset-creation

```python
# Creating frozenset
x = frozenset(['data', 'structure', 'and', 'python'])
print(x)                # frozenset({'python', 'structure', 'data', 'and'})

# From any iterable
y = frozenset({1, 2, 3})
z = frozenset('hello')
```

### Frozen Set Use Cases #frozenset-uses

```python
# Sets cannot contain other sets (unhashable)
a1 = set(['data'])
a2 = set(['structure'])
a3 = set(['python'])

try:
    x = {a1, a2, a3}    # This raises TypeError
except TypeError as e:
    print(f"Error: {e}")  # TypeError: unhashable type: 'set'

# Frozen sets can contain other frozen sets
a1 = frozenset(['data'])
a2 = frozenset(['structure'])
a3 = frozenset(['python'])
x = {a1, a2, a3}        # This works!
print(x)                 # {frozenset({'structure'}), frozenset({'python'}), frozenset({'data'})}

# Using frozenset as dictionary key
d = {frozenset([1, 2]): "value"}
print(d)                 # {frozenset({1, 2}): 'value'}
```

### Set vs FrozenSet Comparison #set-vs-frozenset

| Feature | Set | FrozenSet |
|---------|-----|-----------|
| Mutability | Mutable | Immutable |
| Hashable | No | Yes |
| Can be dict key | No | Yes |
| Can contain other sets | No | Yes (if frozen) |
| Methods for modification | Yes (add, remove, etc.) | No (only read methods) |
| Use case | Temporary collections | Fixed collections, dict keys |

### When to Use FrozenSet #when-to-use-frozenset

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Set as dictionary key | Use frozenset | Sets aren't hashable |
| Set of sets | Use frozenset | Nested sets require immutability |
| Configuration that shouldn't change | Use frozenset | Prevents accidental modification |
| Need hashable collection of unique items | Use frozenset | Combines hashability with uniqueness |

---

## Collections Module #collections-module

### Module Overview #collections-overview

The `collections` module provides specialized container data types that extend Python's built-in types.

| Container | Description |
|-----------|-------------|
| `namedtuple` | Tuple with named fields |
| `deque` | Double-ended queue (fast appends/pops from both ends) |
| `defaultdict` | Dictionary with default values for missing keys |
| `ChainMap` | Combines multiple dictionaries into one view |
| `Counter` | Dictionary for counting hashable objects |
| `OrderedDict` | Dictionary that remembers insertion order |
| `UserDict` | Wrapper for easier dictionary subclassing |
| `UserList` | Wrapper for easier list subclassing |
| `UserString` | Wrapper for easier string subclassing |

---

## NamedTuple #namedtuple

### Core Concepts #namedtuple-core

* **Extension of regular tuples**
* **Immutable** like standard tuples
* **Named fields**: Access elements by name (like objects) or index (like tuples)
* **Self-documenting**: Improves code readability

### NamedTuple Syntax #namedtuple-syntax

```python
from collections import namedtuple

# Syntax: namedtuple(typename, field_names)
nt = namedtuple(typename, field_names)
```

### NamedTuple Examples #namedtuple-examples

```python
from collections import namedtuple

# Define a named tuple type
Book = namedtuple('Book', ['name', 'ISBN', 'quantity'])

# Create instances
Book1 = Book('Hands on Data Structures', '9781788995573', '50')

# Access by index (like regular tuple)
print('Using index ISBN:', Book1[1])        # Using index ISBN: 9781788995573

# Access by key/name (like object)
print('Using key ISBN:', Book1.ISBN)        # Using key ISBN: 9781788995573

# Access by name (alternative)
print(Book1.name)                            # Hands on Data Structures

# Named tuples are still tuples
print(len(Book1))                            # 3
print(isinstance(Book1, tuple))               # True
```

### NamedTuple Methods #namedtuple-methods

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# _make(iterable) - create from iterable
data = [30, 40]
p2 = Point._make(data)
print(p2)               # Point(x=30, y=40)

# _asdict() - convert to OrderedDict
print(p._asdict())      # {'x': 10, 'y': 20}

# _replace() - create new instance with changed fields
p3 = p._replace(x=100)
print(p3)               # Point(x=100, y=20)

# _fields - get field names
print(p._fields)        # ('x', 'y')
```

### NamedTuple vs Regular Tuple #namedtuple-vs-tuple

| Aspect | Regular Tuple | NamedTuple |
|--------|---------------|------------|
| Access | By index only | By name or index |
| Readability | Less (magic numbers) | More (descriptive names) |
| Memory | Efficient | Same as tuple |
| Use case | Simple collections | Domain objects, records |

### When to Use NamedTuple #when-to-use-namedtuple

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Simple data containers | Use namedtuple | More readable than tuples |
| Database records | Use namedtuple | Access fields by name |
| Return multiple values from function | Consider namedtuple | Self-documenting return values |
| Need immutability | Use namedtuple | Ensures data doesn't change |

---

## Deque #deque

### Core Concepts #deque-core

* **Double-ended queue** (pronounced "deck")
* **Fast O(1) appends and pops** from both ends
* **Implemented as doubly-linked list**
* **Thread-safe** for appends and pops from both ends
* **Supports indexing** but slower than lists for random access

### Deque Creation #deque-creation

```python
from collections import deque

# Empty deque
s = deque()
print(s)                # deque([])

# Deque from list
my_queue = deque([1, 2, 'Name'])
print(my_queue)         # deque([1, 2, 'Name'])

# Deque with max length (when full, items are discarded from opposite end)
limited = deque(maxlen=3)
limited.append(1)
limited.append(2)
limited.append(3)
limited.append(4)       # 1 is automatically removed
print(limited)          # deque([2, 3, 4], maxlen=3)
```

### Deque Operations #deque-operations

```python
from collections import deque

d = deque([1, 2, 3])

# Adding elements
d.append(4)             # Add to right end
d.appendleft(0)         # Add to left end
print(d)                # deque([0, 1, 2, 3, 4])

# Removing elements
right = d.pop()         # Remove from right
left = d.popleft()      # Remove from left
print(f"Removed: {right}, {left}")  # Removed: 4, 0
print(d)                # deque([1, 2, 3])

# Extending
d.extend([5, 6])        # Add multiple to right
d.extendleft([-1, 0])   # Add multiple to left (note: reverses order)
print(d)                # deque([0, -1, 1, 2, 3, 5, 6])

# Rotating
d.rotate(1)             # Move all elements one step to the right
print(d)                # deque([6, 0, -1, 1, 2, 3, 5])
d.rotate(-2)            # Move all elements two steps to the left
print(d)                # deque([-1, 1, 2, 3, 5, 6, 0])
```

### Deque Methods Table #deque-methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `append(x)` | Add x to right end | O(1) |
| `appendleft(x)` | Add x to left end | O(1) |
| `pop()` | Remove and return from right | O(1) |
| `popleft()` | Remove and return from left | O(1) |
| `extend(iterable)` | Add multiple to right | O(k) |
| `extendleft(iterable)` | Add multiple to left | O(k) |
| `rotate(n)` | Rotate n steps | O(k) |
| `clear()` | Remove all elements | O(n) |
| `count(x)` | Count occurrences of x | O(n) |
| `index(x[, start[, stop]])` | Find first index of x | O(n) |

### Deque vs List Comparison #deque-vs-list

| Operation | List | Deque |
|-----------|------|-------|
| Append to right | O(1) amortized | O(1) |
| Pop from right | O(1) | O(1) |
| Append to left | O(n) | O(1) |
| Pop from left | O(n) | O(1) |
| Random access | O(1) | O(n) |
| Memory | Contiguous (efficient) | Linked (overhead) |

### When to Use Deque #when-to-use-deque

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Queue (FIFO) | Use deque with `append()`/`popleft()` | O(1) for both ends |
| Stack (LIFO) | Use deque or list | Both O(1) for right end |
| Sliding window | Use deque with maxlen | Automatically discards old items |
| Need fast operations at both ends | Use deque | Only data structure with O(1) for both ends |
| Random access needed | Use list instead | Deque indexing is O(n) |

---

## OrderedDict #ordereddict

### Core Concepts #ordereddict-core

* **Dictionary that remembers insertion order**
* **Same methods** as regular dict
* **Order matters** for equality and iteration
* **Useful** when key order is semantically important

### OrderedDict Examples #ordereddict-examples

```python
from collections import OrderedDict

# Creating OrderedDict
od = OrderedDict([('my', 2), ('name', 4), ('is', 2), ('Mohan', 5)])
print(od)               # OrderedDict([('my', 2), ('name', 4), ('is', 2), ('Mohan', 5)])

# Adding new items (preserves insertion order)
od['hello'] = 4
print(od)               # OrderedDict([('my',2), ('name',4), ('is',2), ('Mohan',5), ('hello',4)])

# Iteration respects order
for key, value in od.items():
    print(f"{key}: {value}")

# Regular dict (Python 3.7+) also preserves order
regular_dict = {'b': 2, 'a': 1}
print(regular_dict)     # {'b': 2, 'a': 1} (insertion order preserved)
```

### OrderedDict vs Regular Dict #ordereddict-vs-dict

| Aspect | Regular Dict (Python <3.7) | Regular Dict (Python 3.7+) | OrderedDict |
|--------|---------------------------|---------------------------|-------------|
| Order | Unordered | Insertion order preserved | Insertion order preserved |
| Equality | Order doesn't matter | Order doesn't matter | Order matters |
| Memory | Less | Less | Slightly more |
| Use case | General | General | When order matters for equality |

> ⚠️ **Note**: Since Python 3.7, regular dictionaries maintain insertion order. Use OrderedDict when order is semantically important for equality comparisons or you need methods like `move_to_end()`.

---

## DefaultDict #defaultdict

### Core Concepts #defaultdict-core

* **Subclass of regular dict**
* **Never raises KeyError** for missing keys
* **Provides default value** for missing keys using factory function
* **Useful for counting, grouping, and accumulating**

### DefaultDict Syntax #defaultdict-syntax

```python
from collections import defaultdict

d = defaultdict(default_factory)
```

Where `default_factory` is a callable (like `int`, `list`, `set`, `str`, etc.) that returns the default value.

### DefaultDict Examples #defaultdict-examples

```python
from collections import defaultdict

# Counting with int() factory (returns 0)
words = "data python data data structure data python".split()
dd = defaultdict(int)

for word in words:
    dd[word] += 1

print(dd)  # defaultdict(<class 'int'>, {'data': 4, 'python': 2, 'structure': 1})

# Grouping with list() factory
dd_list = defaultdict(list)
fruits = [('apple', 5), ('banana', 3), ('apple', 2), ('banana', 7)]

for fruit, count in fruits:
    dd_list[fruit].append(count)

print(dd_list)  # defaultdict(<class 'list'>, {'apple': [5, 2], 'banana': [3, 7]})

# Set default with set() factory
dd_set = defaultdict(set)
pairs = [('x', 1), ('y', 2), ('x', 3), ('y', 4)]

for key, value in pairs:
    dd_set[key].add(value)

print(dd_set)  # defaultdict(<class 'set'>, {'x': {1, 3}, 'y': {2, 4}})

# Custom default factory
def default_value():
    return "N/A"

dd_custom = defaultdict(default_value)
print(dd_custom['missing'])  # N/A
```

### DefaultDict vs Regular Dict #defaultdict-vs-dict

```python
# Without defaultdict (verbose)
word_counts = {}
words = "data python data".split()

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# With defaultdict (clean)
from collections import defaultdict
word_counts = defaultdict(int)

for word in words:
    word_counts[word] += 1  # No need to check existence
```

### Common Default Factories #default-factories

| Factory | Returns | Use Case |
|---------|---------|----------|
| `int` | 0 | Counting |
| `float` | 0.0 | Counting with decimals |
| `list` | `[]` | Grouping items |
| `set` | `set()` | Unique grouping |
| `str` | `""` | String accumulation |
| `dict` | `{}` | Nested dictionaries |
| `lambda: value` | Custom value | Custom defaults |

### When to Use DefaultDict #when-to-use-defaultdict

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Counting occurrences | Use `defaultdict(int)` | Cleaner code, no key checks |
| Grouping items by key | Use `defaultdict(list)` | Automatically creates lists |
| Building nested structures | Use `defaultdict(dict)` | Simplifies nested dictionary creation |
| Need custom defaults | Use `defaultdict(lambda: value)` | Flexible default values |

---

## ChainMap #chainmap

### Core Concepts #chainmap-core

* **Combines multiple dictionaries** into a single view
* **Searches dictionaries in order** until key is found
* **Updates affect first dictionary** only
* **Useful for** layered configurations, scopes, defaults

### ChainMap Examples #chainmap-examples

```python
from collections import ChainMap

# Create dictionaries
dict1 = {"data": 1, "structure": 2}
dict2 = {"python": 3, "language": 4}

# Combine into ChainMap
chain = ChainMap(dict1, dict2)

print(chain)  # ChainMap({'data': 1, 'structure': 2}, {'python': 3, 'language': 4})

# Accessing keys (searches dict1 first, then dict2)
print(chain["data"])       # 1 (from dict1)
print(chain["python"])     # 3 (from dict2)
print(list(chain.keys()))   # ['python', 'language', 'data', 'structure'] (order may vary)
print(list(chain.values())) # [3, 4, 1, 2] (corresponding to keys)

# Adding/updating affects first dictionary only
chain["new"] = 5
print(dict1)  # {'data': 1, 'structure': 2, 'new': 5}
print(dict2)  # {'python': 3, 'language': 4} (unchanged)
```

### ChainMap Use Cases #chainmap-use-cases

```python
from collections import ChainMap

# Configuration with defaults and overrides
defaults = {'theme': 'light', 'language': 'en', 'debug': False}
user_settings = {'theme': 'dark', 'language': 'es'}
runtime_args = {'debug': True}

# Priority: runtime_args > user_settings > defaults
config = ChainMap(runtime_args, user_settings, defaults)

print(config['theme'])     # 'dark' (from user_settings)
print(config['debug'])     # True (from runtime_args)
print(config['language'])  # 'es' (from user_settings)

# Simulating nested scopes
global_scope = {'x': 1, 'y': 2}
local_scope = {'x': 10}

scope = ChainMap(local_scope, global_scope)
print(scope['x'])          # 10 (from local)
print(scope['y'])          # 2 (from global)
```

### ChainMap Methods #chainmap-methods

| Method | Description |
|--------|-------------|
| `maps` | List of dictionaries in the chain |
| `new_child(m)` | Creates new ChainMap with m prepended |
| `parents` | Returns ChainMap without first dictionary |

```python
# Using new_child() and parents
c = ChainMap({'a': 1}, {'b': 2})
print(c)                     # ChainMap({'a': 1}, {'b': 2})

# Add new child dictionary
c2 = c.new_child({'c': 3})
print(c2)                    # ChainMap({'c': 3}, {'a': 1}, {'b': 2})

# Remove first dictionary (parents)
c3 = c2.parents
print(c3)                    # ChainMap({'a': 1}, {'b': 2})
```

### When to Use ChainMap #when-to-use-chainmap

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Configuration with defaults | Use ChainMap | Layered priority without copying |
| Multiple scopes | Use ChainMap | Natural representation of scope chain |
| Merging without copying | Use ChainMap | Memory efficient, views original dicts |
| Need to update originals | Use ChainMap | Changes reflect in source dicts |

---

## Counter #counter

### Core Concepts #counter-core

* **Dictionary subclass** for counting hashable objects
* **Elements stored as keys**, counts as values
* **Provides additional methods** for counting operations
* **Zero and negative counts allowed**

### Counter Examples #counter-examples

```python
from collections import Counter

# Create Counter from string
inventory = Counter('hello')
print(inventory)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Access counts (returns 0 for missing keys, no KeyError)
print(inventory['l'])     # 2
print(inventory['x'])     # 0 (doesn't raise KeyError)

# Create from list
word_counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(word_counts)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Create from dictionary
c = Counter({'a': 4, 'b': 2, 'c': 0})

# Create with keyword arguments
c = Counter(a=4, b=2, c=0)
```

### Counter Methods #counter-methods

```python
from collections import Counter

c = Counter('abracadabra')
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# most_common(n) - returns n most common elements
print(c.most_common(2))     # [('a', 5), ('b', 2)]

# elements() - iterator over elements repeating each as many times as its count
print(list(c.elements()))    # ['a','a','a','a','a','b','b','r','r','c','d']

# subtract() - subtract counts
c2 = Counter('abc')
c.subtract(c2)
print(c)  # Counter({'a': 4, 'b': 1, 'r': 2, 'c': 0, 'd': 1})

# update() - add counts
c.update(Counter('abc'))
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# total() - sum of counts (Python 3.10+)
print(c.total())  # 11
```

### Counter Operations #counter-operations

```python
from collections import Counter

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

# Addition (combine counts)
print(c1 + c2)  # Counter({'a': 4, 'b': 3})

# Subtraction (keep positive counts only)
print(c1 - c2)  # Counter({'a': 2})  # b: 1-2 = -1, not included

# Intersection (min counts)
print(c1 & c2)  # Counter({'a': 1, 'b': 1})  # min(3,1)=1, min(1,2)=1

# Union (max counts)
print(c1 | c2)  # Counter({'a': 3, 'b': 2})  # max(3,1)=3, max(1,2)=2

# Unary plus/minus (remove non-positive)
print(+c1)  # Counter({'a': 3, 'b': 1})  # Same, all positive
c3 = Counter(a=3, b=-1)
print(+c3)  # Counter({'a': 3})  # Removes negative counts
print(-c3)  # Counter({'b': 1})  # Inverts sign, keeps positive
```

### Counter vs Dictionary #counter-vs-dict

| Aspect | Regular Dictionary | Counter |
|--------|-------------------|---------|
| Default for missing | Raises KeyError | Returns 0 |
| Purpose | General key-value | Specifically counting |
| Methods | Standard dict methods | `most_common()`, `elements()`, etc. |
| Arithmetic | Not supported | Supports +, -, &, \| |

### When to Use Counter #when-to-use-counter

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Word/frequency counting | Use Counter | Built specifically for this |
| Finding most common items | Use `most_common()` | Simple, efficient |
| Multiset operations | Use Counter | Supports set-like operations on counts |
| Tallying votes/ratings | Use Counter | Automatic zero for missing |

---

## UserDict, UserList, UserString #user-containers

### Core Concepts #user-containers-core

* **Wrapper classes** around built-in types
* **Easier to subclass** than built-in types directly
* **Provide same interface** as underlying type
* **Useful for** adding custom behavior

### UserDict Example #userdict-example

```python
from collections import UserDict

# Custom dictionary that prevents insertion
class MyDict(UserDict):
    def push(self, key, value):
        raise RuntimeError("Cannot insert")

d = MyDict({"ab": 1, 'bc': 2, 'cd': 3})
print(d)  # {'ab': 1, 'bc': 2, 'cd': 3}

try:
    d.push('b', 2)  # This will raise error
except RuntimeError as e:
    print(f"Error: {e}")  # Error: Cannot insert

# You can still access items normally
print(d['ab'])  # 1
```

### UserList Example #userlist-example

```python
from collections import UserList

# Custom list that prevents insertion
class MyList(UserList):
    def push(self, key):
        raise RuntimeError("Cannot insert in the list")

d = MyList([11, 12, 13])
print(d)  # [11, 12, 13]

try:
    d.push(2)  # This will raise error
except RuntimeError as e:
    print(f"Error: {e}")  # Error: Cannot insert in the list

# Normal list operations still work
d.append(14)
print(d)  # [11, 12, 13, 14]
```

### UserString Example #userstring-example

```python
from collections import UserString

# Custom string with append functionality
class MyString(UserString):
    def append(self, value):
        self.data += value

s1 = MyString("data")
print("Original:", s1)      # Original: data

s1.append('h')
print("After append:", s1)   # After append: datah

# All string methods work
print(s1.upper())            # DATAH
print(s1.count('a'))         # 2
```

### When to Use User Containers #when-to-use-user-containers

| Scenario | Best Practice | Why |
|----------|---------------|-----|
| Customizing built-in behavior | Subclass UserDict/List/String | More reliable than subclassing built-ins |
| Adding methods to collections | Use User containers | Clean, object-oriented approach |
| Validating data on insertion | Override `__setitem__` | Control what goes into collection |
| Creating domain-specific collections | Use User containers | Self-documenting, reusable |

> 🔍 **Extra context (not in PDF)**: While you can subclass built-in types directly, it's often recommended to use the User versions because built-in types have optimizations that can make subclassing behavior unpredictable. The User containers provide a more consistent experience for customization.