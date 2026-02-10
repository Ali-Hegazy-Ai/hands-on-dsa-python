#!/bin/bash
# Run type checking with mypy

echo "Running mypy type checking..."
mypy src/ tests/

echo ""
echo "Type check complete!"
