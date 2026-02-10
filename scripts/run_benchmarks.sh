#!/bin/bash
# Run all benchmarks

echo "Running sorting benchmarks..."
python benchmarks/benchmark_sorting.py

echo ""
echo "Running searching benchmarks..."
python benchmarks/benchmark_searching.py

echo ""
echo "Running hash table benchmarks..."
python benchmarks/benchmark_hash_tables.py

echo ""
echo "Running graph traversal benchmarks..."
python benchmarks/benchmark_graph_traversal.py

echo ""
echo "Benchmarks complete!"
