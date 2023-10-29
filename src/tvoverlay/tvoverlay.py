"""Asynchronous Python client for sending notifications to TvOverlay."""
from __future__ import annotations

import base64
import logging
import re
import uuid
from datetime import timedelta
from typing import Any

import aiofiles
import httpx

from .const import (
    COLOR_GREEN,
    DEFAULT_APP_ICON,
    DEFAULT_APP_NAME,
    DEFAULT_DURATION,
    DEFAULT_SMALL_ICON,
    DEFAULT_SOURCE_NAME,
    DEFAULT_TITLE,
    UNITS,
    Positions,
    Shapes,
)
from .exceptions import ConnectError, InvalidImageError, InvalidResponseError
from .imagehelper import ImageSource

_LOGGER = logging.getLogger(__name__)


class Notifications:
    """Notifications class for TVOverlay."""

    def __init__(
        self,
        host: str,
        port: int = 5001,
        httpx_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Initialize notifier."""
        self.url = f"http://{host}:{port}"
        self.httpx_client = httpx_client
        _LOGGER.debug("TVOverlay initialized")

    async def async_connect(self) -> Any:
        """Test connecting to server."""
        httpx_client: httpx.AsyncClient = (
            self.httpx_client
            if self.httpx_client
            else httpx.AsyncClient(verify=False)  # noqa: S501
        )
        try:
            async with httpx_client as client:
                response = await client.get(self.url + "/get", timeout=5)
        except (httpx.ConnectError, httpx.TimeoutException) as exc:
            _LOGGER.exception("Connection to host '%s' failed!", self.url)
            raise ConnectError(self.url) from exc
        if response.status_code == httpx.codes.OK:
            _LOGGER.debug("TvOverlay connect response: %s", response.json())
            return response.json()
        raise InvalidResponseError(self.url)

    async def _convert_to_seconds(self, duration: str | Any) -> int | None:
        """Convert string formatted duration 1w2d3h4m5s in to seconds."""
        if not duration:
            return int(DEFAULT_DURATION)
        if isinstance(duration, int):
            return duration
        duration = duration.replace(" ", "")
        try:
            return int(
                timedelta(
                    **{
                        UNITS.get(m.group("unit").lower(), "seconds"): float(
                            m.group("val"),
                        )
                        for m in re.finditer(
                            r"(?P<val>\d+(\.\d+)?)(?P<unit>[smhdw])",
                            duration,
                            flags=re.I,
                        )
                    },
                ).total_seconds(),
            )
        except (ValueError, TypeError) as ex:
            _LOGGER.warning("Invalid duration: %s. %s", duration, ex)
            return int(DEFAULT_DURATION)

    # pylint: disable=too-many-locals, too-many-branches, too-many-arguments
    async def async_send(  # noqa: PLR0913
        self,
        message: str | None,
        message_id: str | None = str(uuid.uuid1()),
        title: str | None = DEFAULT_TITLE,
        source_name: str | None = DEFAULT_SOURCE_NAME,
        app_title: str | None = DEFAULT_APP_NAME,
        app_icon: str | ImageSource | None = None,
        image: str | ImageSource | None = None,
        video: str | None = None,
        small_icon: str | None = DEFAULT_SMALL_ICON,
        small_icon_color: str | None = COLOR_GREEN,
        corner: str = Positions.TOP_RIGHT.value,
        duration: str | None = None,
    ) -> Any:
        """Send notification with parameters."""
        if app_icon:
            app_icon_b64 = await self._async_get_b64_image(app_icon)
        else:
            app_icon_b64 = DEFAULT_APP_ICON

        if image:
            image_b64 = await self._async_get_b64_image(image)
        else:
            image_b64 = None

        final_duration = await self._convert_to_seconds(duration)
        if final_duration == 0:
            final_duration = int(DEFAULT_DURATION)

        data: dict[str, Any] = {
            "id": message_id,
            "title": title,
            "message": message,
            "deviceSourceName": source_name,
            "appIcon": app_icon_b64,
            "appTitle": app_title,
            "smallIcon": small_icon,
            "color": small_icon_color,
            "image": image_b64,
            "video": video,
            "corner": corner.replace("left", "start").replace("right", "end"),
            "seconds": final_duration,
        }

        headers = {"Content-Type": "application/json"}

        _LOGGER.debug("data: %s", data)

        httpx_client: httpx.AsyncClient = (
            self.httpx_client
            if self.httpx_client
            else httpx.AsyncClient(verify=False)  # noqa: S501
        )
        try:
            async with httpx_client as client:
                response = await client.post(
                    self.url + "/notify",
                    json=data,
                    headers=headers,
                    timeout=5,
                )
        except (httpx.ConnectError, httpx.TimeoutException) as exc:
            raise ConnectError(self.url) from exc
        if response.status_code == httpx.codes.OK:
            _LOGGER.debug(
                "TVOverlay send notification response: %s",
                response.json(),
            )
            return response.json()
        raise InvalidResponseError(self.url)

    # pylint: disable=too-many-locals, too-many-branches, too-many-arguments
    async def async_send_fixed(  # noqa: PLR0913
        self,
        message: str | None,
        message_id: str | None = str(uuid.uuid1()),
        icon: str | None = None,
        text_color: str | None = None,
        icon_color: str | None = None,
        border_color: str | None = None,
        background_color: str | None = None,
        shape: str = Shapes.CIRCLE.value,
        duration: str | None = DEFAULT_DURATION,
        visible: bool | None = True,  # noqa: FBT002
    ) -> Any:
        """Send Fixed notification."""
        if icon:
            app_icon_b64 = await self._async_get_b64_image(icon)
        else:
            app_icon_b64 = None

        data: dict[str, Any] = {
            "id": message_id,
            "message": message,
            "textColor": text_color,
            "icon": app_icon_b64,
            "iconColor": icon_color,
            "borderColor": border_color,
            "backgroundColor": background_color,
            "shape": shape,
            "expiration": duration,
            "visible": visible,
        }

        headers = {"Content-Type": "application/json"}

        _LOGGER.debug("data: %s", data)

        httpx_client: httpx.AsyncClient = (
            self.httpx_client
            if self.httpx_client
            else httpx.AsyncClient(verify=False)  # noqa: S501
        )
        try:
            async with httpx_client as client:
                response = await client.post(
                    self.url + "/notify_fixed",
                    json=data,
                    headers=headers,
                    timeout=5,
                )
        except (httpx.ConnectError, httpx.TimeoutException) as exc:
            raise ConnectError(self.url) from exc
        if response.status_code == httpx.codes.OK:
            _LOGGER.debug(
                "TVOverlay send fixed notification response: %s",
                response.json(),
            )
            return response.json()
        raise InvalidResponseError(self.url)

    async def _async_get_b64_image(
        self,
        image_source: ImageSource | str,
    ) -> Any | bytes | None:
        """Load file from path or url."""
        if isinstance(image_source, ImageSource):
            httpx_client: httpx.AsyncClient = (
                self.httpx_client if self.httpx_client else httpx.AsyncClient()
            )
            try:
                async with httpx_client as client:
                    response = await client.get(
                        image_source.url,
                        auth=image_source.auth,
                        timeout=10,
                        follow_redirects=True,
                    )
            except (httpx.ConnectError, httpx.TimeoutException) as err:
                raise InvalidImageError(image_source.url) from err
            if response.status_code != httpx.codes.OK:
                raise InvalidImageError(response.text)
            if "image" not in response.headers["content-type"]:
                raise InvalidImageError(response.headers["content-type"])
            return await self._get_base64(response.content)
        if image_source.startswith(("mdi:", "http://", "https://")):
            return image_source
        try:
            if image_source.lower().endswith(
                (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"),
            ):
                async with aiofiles.open(image_source, "rb") as file:
                    image = await file.read()
                return await self._get_base64(image)
            raise InvalidImageError(image_source)
        except FileNotFoundError as err:
            raise InvalidImageError(image_source) from err

    async def _get_base64(self, filebyte: bytes) -> str | None:
        """Convert the image to the expected base64 string."""
        return base64.b64encode(filebyte).decode("utf8")
