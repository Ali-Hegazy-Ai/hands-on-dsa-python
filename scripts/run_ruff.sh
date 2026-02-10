#!/bin/bash
# Run code formatter and linter with ruff

echo "Running ruff format..."
ruff format src/ tests/

echo ""
echo "Running ruff linter..."
ruff check src/ tests/

echo ""
echo "Ruff check complete!"
