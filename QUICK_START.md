"""Quick Start Guide for hands-on-dsa-python Repository."""

# Quick Start Guide

## Repository Location

```
/home/alih/hands-on-dsa-python
```

## Project Summary

✅ **Complete DSA Learning Repository Created!**

### What's Included

**59 Python modules** in `src/dsa/` covering:
- ✅ Arrays (dynamic arrays, prefix sums, two-pointers)
- ✅ Linked Lists (singly, doubly, circular)
- ✅ Stacks & Queues (4 implementations)
- ✅ Trees (binary trees, BST, traversals)
- ✅ Heaps & Priority Queues
- ✅ Hash Tables (2 approaches)
- ✅ Graphs (adjacency list/matrix, BFS, DFS, shortest paths)
- ✅ Searching (linear, binary search variants)
- ✅ Sorting (8 algorithms)
- ✅ Selection (QuickSelect, Median of Medians)
- ✅ String Matching (KMP, Rabin-Karp, Trie)

**18 Test Files** with comprehensive test skeletons (5+ tests each)

**4 Benchmark Modules** for performance analysis

**5 Study Notes** on key concepts

### Key Features

✨ Modern Python Setup:
- `src/` layout (professional structure)
- Full type hints on all modules
- Clean docstrings with complexity analysis
- TODO markers for each function (clear what to implement)
- py.typed marker for type checkers
- Comprehensive pyproject.toml configuration

🧪 Testing & Quality:
- pytest configuration with markers (unit, slow, integration)
- Shared fixtures in conftest.py
- Custom exceptions module
- Type checking with mypy (strict mode)
- Code formatting with ruff
- 5+ test cases per major module

📚 Learning Materials:
- Algorithm analysis notes
- Python built-ins reference
- Topic-specific study notes
- Complexity comparison tables
- When-to-use guidelines

## How to Use

### 1. Start Development

```bash
cd /home/alih/hands-on-dsa-python

# Install development dependencies
pip install -e ".[dev]"
```

### 2. For Each Algorithm/Data Structure

a) **Read the book section** - understand the concept

b) **Navigate to the module** - e.g., `src/dsa/arrays/dynamic_array.py`

c) **Review the TODO items** - see what needs implementation

d) **Implement the functions** - replace NotImplementedError with code

e) **Run tests** - verify your implementation:
```bash
# Run tests for specific module
pytest tests/test_arrays/test_dynamic_array.py -v

# Run all tests
./scripts/run_all_tests.sh
```

f) **Type check** - ensure correctness:
```bash
./scripts/run_mypy.sh
```

g) **Add benchmarks** - performance test in benchmarks/ (if needed)

h) **Write study notes** - add learnings to notes/05_*.md (new files)

### 3. Code Quality Checks

```bash
# Format code
./scripts/run_ruff.sh

# Type checking
./scripts/run_mypy.sh

# All tests
./scripts/run_all_tests.sh

# Performance benchmarks
./scripts/run_benchmarks.sh
```

## Pushing to GitHub

### Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `hands-on-dsa-python`
3. Description: "Comprehensive DSA learning repository implementing algorithms from 'Hands-On Data Structures and Algorithms with Python'"
4. Choose Public (for best practice sharing)
5. Don't initialize with README (you already have one)
6. Click "Create repository"

### Step 2: Add Remote and Push

```bash
cd /home/alih/hands-on-dsa-python

# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/hands-on-dsa-python.git

# Rename branch to main (optional but recommended)
git branch -M main

# Push initial commit
git push -u origin main
```

### Step 3: Authenticate

When prompted for credentials:
- **Username:** Your GitHub username
- **Password:** Use a Personal Access Token (not your password)
  - GitHub Settings → Developer Settings → Personal Access Tokens → Generate new token
  - Select: repo, read:user
  - Copy and paste when prompted

### Verify Push Success

```bash
git log --oneline  # Should show commits
git remote -v      # Should show origin URL
```

## Project Structure at a Glance

```
hands-on-dsa-python/
├── src/dsa/                 # Main implementation (59 modules)
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
│   └── _typing.py, _errors.py, _utils.py
├── tests/                   # 18 test modules
├── benchmarks/              # Performance testing
├── notes/                   # 5 study note files
├── scripts/                 # Utility shell scripts
├── pyproject.toml          # Poetry/setuptools config
├── pytest.ini              # Pytest configuration
├── mypy.ini                # Type checking config
├── ruff.toml               # Linting/formatting config
└── README.md               # Main documentation
```

## Recommended Learning Path

### Week 1: Fundamentals
- Arrays (src/dsa/arrays/)
- Linked Lists (src/dsa/linked_lists/)

### Week 2: Collections
- Stacks & Queues (src/dsa/stacks_queues/)
- Trees (src/dsa/trees/)

### Week 3: Advanced Data Structures
- Heaps (src/dsa/heaps/)
- Hash Tables (src/dsa/hash_tables/)
- Graphs (src/dsa/graphs/)

### Week 4: Algorithms
- Searching (src/dsa/searching/)
- Sorting (src/dsa/sorting/)
- Selection (src/dsa/selection/)
- String Matching (src/dsa/strings/)

## Tips for Success

1. **Don't copy the book code** - Implement from understanding
2. **Write tests first** - Test skeleton already there
3. **Verify with benchmarks** - Ensure your code is efficient
4. **Type hints help** - Use them, let mypy catch errors
5. **Study the notes** - Read 01_python_data_types.md and 02_algorithm_analysis.md
6. **Commit often** - git add → git commit after each completed module
7. **Measure complexity** - Time vs space tradeoffs are important

## Daily Workflow

```bash
# 1. Choose what to implement (e.g., dynamic_array.py)
cd /home/alih/hands-on-dsa-python

# 2. Edit the file - replace NotImplementedError with implementation
nano src/dsa/arrays/dynamic_array.py

# 3. Run tests
pytest tests/test_arrays/test_dynamic_array.py -v

# 4. Check types
mypy src/dsa/arrays/dynamic_array.py

# 5. Run benchmarks (if applicable)
python benchmarks/benchmark_sorting.py

# 6. Commit your work
git add src/dsa/arrays/dynamic_array.py tests/test_arrays/test_dynamic_array.py
git commit -m "Implement DynamicArray with O(1) amortized append"

# 7. Push to GitHub
git push origin main
```

## Troubleshooting

**ImportError: No module named 'dsa'**
```bash
pip install -e .
```

**ModuleNotFoundError in tests**
```bash
export PYTHONPATH=/home/alih/hands-on-dsa-python/src:$PYTHONPATH
```

**Type checking errors**
```bash
mypy src/ --show-error-codes
```

## Next Steps

1. ✅ Repository created locally
2. ✅ Project structure complete
3. ✅ Stubs and tests ready
4. 📸 **Next: Push to GitHub** (see "Pushing to GitHub" section above)
5. 🚀 Start implementing algorithms!

---

**Happy Learning!** 🎓

Start with `notes/00_study_method.md` for the complete learning strategy.
