#!/bin/bash
# Run all tests with pytest

echo "Running all tests..."
python -m pytest tests/ -v --tb=short

echo ""
echo "Test run complete!"
