"""Example scripts for sending notifications."""
import asyncio
import logging
from typing import Any

from tvoverlay import ConnectError, Notifications
from tvoverlay.const import Positions

_LOGGER = logging.getLogger(__name__)

HOST = "10.10.10.150"


async def main() -> None:
    """Run the example script."""
    notifier = Notifications(HOST)
    response: Any = None

    # validate connection
    try:
        response = await notifier.async_connect()
        print(response)
    except ConnectError:
        print("Connect Error")

    # send notification
    print(await notifier.async_send("This is a notification message"))

    # Customize all parameters in the notification
    response = await notifier.async_send(
        message="This is a notification message",
        title="Notification Title",
        message_id="0",
        source_name="abc",
        app_title="PyTest",
        app_icon="mdi:unicorn",
        image="https://picsum.photos/200/100",
        small_icon="mdi:bell",
        small_icon_color="#FFC107",
        corner=Positions.TOP_RIGHT.value,
        duration="5",
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
