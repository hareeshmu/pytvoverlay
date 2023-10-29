"""Tests for notification."""
from unittest.mock import patch

import pytest
from httpx import AsyncClient

from tvoverlay import ConnectError, Notifications


@pytest.mark.asyncio
async def test_async_connect_success() -> None:
    """Tests async_connect."""
    with patch.object(AsyncClient, "get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"status": "ok"}
        notify_instance = Notifications("localhost")
        await notify_instance.async_connect()


@pytest.mark.asyncio
async def test_async_connect_failure() -> None:
    """Tests test_async_connect_failure."""
    with patch.object(AsyncClient, "get") as mock_get:
        mock_get.side_effect = ConnectError("Connection error")
        notify_instance = Notifications("localhost")
        with pytest.raises(ConnectError):
            await notify_instance.async_connect()


@pytest.mark.asyncio
async def test_async_send_success() -> None:
    """Tests test_async_send_success."""
    with patch.object(AsyncClient, "post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"status": "ok"}
        notify_instance = Notifications("localhost")
        await notify_instance.async_send("Test message")


@pytest.mark.asyncio
async def test_async_send_failure() -> None:
    """Tests test_async_send_failure."""
    with patch.object(AsyncClient, "post") as mock_post:
        mock_post.side_effect = ConnectError("Connection error")
        notify_instance = Notifications("localhost")
        with pytest.raises(ConnectError):
            await notify_instance.async_send("Test message")


@pytest.mark.asyncio
async def test_async_send_fixed_success() -> None:
    """Tests test_async_send_fixed_success."""
    with patch.object(AsyncClient, "post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"status": "ok"}
        notify_instance = Notifications("localhost")
        await notify_instance.async_send("Test message")


@pytest.mark.asyncio
async def test_async_send_fixed_failure() -> None:
    """Tests test_async_send_fixed_failure."""
    with patch.object(AsyncClient, "post") as mock_post:
        mock_post.side_effect = ConnectError("Connection error")
        notify_instance = Notifications("localhost")
        with pytest.raises(ConnectError):
            await notify_instance.async_send_fixed("Test message")
