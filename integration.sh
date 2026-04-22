#!/bin/bash
echo "Waiting for API to start..."
timeout 30s bash -c 'until curl -f -s http://localhost:8000/openapi.json > /dev/null; do sleep 2; done' || exit 1
echo "Integration test passed"