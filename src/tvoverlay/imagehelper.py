"""ImageHelper for the TvOverlay library."""
from __future__ import annotations

import httpx

from .exceptions import InvalidAuthMethodError, MissingCredentialsError


class ImageSource:
    """Image source from url or local path."""

    def __init__(
        self,
        url: str,
        username: str | None = None,
        password: str | None = None,
        auth: str | None = None,
    ) -> None:
        """Initiate image source class."""
        self.url = url
        self.auth: httpx.BasicAuth | httpx.DigestAuth | None = None

        if auth:
            if auth not in ["basic", "digest"]:
                raise InvalidAuthMethodError
            if username is None or password is None:
                raise MissingCredentialsError
            if auth == "basic":
                self.auth = httpx.BasicAuth(username, password)
            else:
                self.auth = httpx.DigestAuth(username, password)
