"""Exceptions raised by the library."""


class ConnectError(Exception):
    """Raised when a connection error occurs."""

    message = "Connection to host: {url} failed!"

    def __init__(self, url: str) -> None:
        """Initialize a new instance of the ConnectError class."""
        super().__init__(self.message.format(url=url))


class InvalidResponseError(Exception):
    """Raised when an invalid response is received."""

    message = "Error connecting host: {url}"

    def __init__(self, url: str) -> None:
        """Initialize a new instance of the InvalidResponseError class."""
        super().__init__(self.message.format(url=url))


class InvalidImageError(Exception):
    """Exception raised for invalid image."""

    def __init__(self, message: str) -> None:
        """Initialize a new instance of the InvalidImageError class."""
        super().__init__(message)


class InvalidAuthMethodError(ValueError):
    """Raised when an invalid authentication method is specified."""

    message = "Authentication method must be 'basic' or 'digest'."


class MissingCredentialsError(ValueError):
    """Raised when username and/or password are missing."""

    message = "Username and password must be specified."
