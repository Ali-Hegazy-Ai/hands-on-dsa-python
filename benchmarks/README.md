"""Benchmark README for DSA project."""

# Benchmarks

This directory contains performance benchmarks for DSA implementations.

## Running Benchmarks

```bash
python benchmarks/benchmark_sorting.py
python benchmarks/benchmark_searching.py
python benchmarks/benchmark_hash_tables.py
python benchmarks/benchmark_graph_traversal.py
```

## Benchmark Structure

Each benchmark:
- Generates test data
- Compares custom implementations with Python built-ins
- Measures execution time
- Displays results in table format
- Includes different input sizes

## Performance Goals

- Sorting: Compare with `sorted()`
- Searching: Compare with `in` operator
- Hashing: Compare with native dict
- Graph traversal: Measure scalability

## Notes

- Run benchmarks on the same machine for comparison
- Ensure no other heavy processes running
- Results depend on hardware and Python version
- Use for optimization insights, not absolute values
