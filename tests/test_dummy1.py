from unittest.mock import patch

@patch('redis.Redis')
def test_redis_mock(mock_redis):
    assert True