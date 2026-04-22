#!/bin/bash
echo "Running integration tests..."
curl -f http://localhost:8000/health || exit 1
echo "Passed!"