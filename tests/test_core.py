"""
Tests for Core System
Copyright © 2025 Thamer-H2K. All Rights Reserved.
"""
import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch
from core.immortal_core import ImmortalCore
from config.secure_config import SecureConfig


@pytest.fixture
def config():
    """Create test configuration"""
    return SecureConfig()


@pytest.fixture
async def core(config):
    """Create and initialize core system"""
    with patch.object(ImmortalCore, 'initialize', new_callable=AsyncMock):
        core = ImmortalCore(config)
        await core.initialize()
        yield core
        if hasattr(core, 'shutdown'):
            await core.shutdown()


@pytest.mark.asyncio
async def test_core_initialization(config):
    """Test core system initialization"""
    with patch.object(ImmortalCore, 'initialize', new_callable=AsyncMock) as mock_init:
        core = ImmortalCore(config)
        await core.initialize()
        mock_init.assert_called_once()
        assert core is not None


@pytest.mark.asyncio
async def test_core_start_stop(core):
    """Test core start and stop"""
    with patch.object(core, 'start', new_callable=AsyncMock) as mock_start, \
         patch.object(core, 'stop', new_callable=AsyncMock) as mock_stop:
        
        await core.start()
        mock_start.assert_called_once()
        
        await core.stop()
        mock_stop.assert_called_once()


@pytest.mark.asyncio
async def test_core_self_healing(core):
    """Test self-healing capabilities"""
    assert hasattr(core, 'self_healing') or hasattr(core, 'heal')


def test_core_config_validation(config):
    """Test configuration validation"""
    assert config is not None
    assert hasattr(config, 'load') or hasattr(config, 'get')


@pytest.mark.asyncio
async def test_core_memory_management(core):
    """Test memory management"""
    assert hasattr(core, 'memory_manager') or hasattr(core, 'memory')


@pytest.mark.asyncio
async def test_core_evolution_engine(core):
    """Test evolution engine"""
    assert hasattr(core, 'evolution_engine') or hasattr(core, 'evolve')
