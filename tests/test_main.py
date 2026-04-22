import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api')))

from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

# Test 1: Can we create a job successfully?
@patch("main.r")
def test_create_job(mock_redis):
    # Fake the Redis responses
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = 1

    response = client.post("/jobs")
    
    assert response.status_code == 200
    assert "job_id" in response.json()

# Test 2: Can we fetch a job that exists?
@patch("main.r")
def test_get_job_exists(mock_redis):
    # Fake Redis finding the job status as 'queued'
    mock_redis.hget.return_value = b"queued"
    
    response = client.get("/jobs/test-id-123")
    
    assert response.status_code == 200
    assert response.json() == {"job_id": "test-id-123", "status": "queued"}

# Test 3: Does it handle missing jobs correctly?
@patch("main.r")
def test_get_job_not_found(mock_redis):
    # Fake Redis returning nothing
    mock_redis.hget.return_value = None
    
    response = client.get("/jobs/fake-id-999")
    
    assert response.status_code == 200
    assert response.json() == {"error": "not found"}