# Copyright (c) Thamer-H2K 2025

import pytest
import asyncio

@pytest.fixture(scope='session')
def event_loop():
    """Creates an instance of the asyncio event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def sample_config():
    """Sample configuration fixture."""
    return {
        'db_url': 'sqlite:///:memory:',
        'debug': True,
    }

@pytest.fixture
def mock_threat_data():
    """Fixture for mocking threat data."""
    return [
        {'id': 1, 'name': 'Threat A', 'level': 'high'},
        {'id': 2, 'name': 'Threat B', 'level': 'medium'},
    ]

@pytest.fixture
def mock_user_data():
    """Fixture for mocking user data."""
    return [
        {'id': 1, 'username': 'user1', 'email': 'user1@example.com'},
        {'id': 2, 'username': 'user2', 'email': 'user2@example.com'},
    ]
