"""Sends the output of `events.message.stringify()`.
"""

import re
from telethon import events
from .global_functions import log

@events.register(events.NewMessage(pattern=r"(?s)^(?!/(start|ping|help))(.+)?$", outgoing=False))
async def stringfy_message(event):
    if event.is_private:
        replied_msg = re.sub(r"(?<=.{100}).+", "...'", event.message.stringify())
        await event.reply(f"```{replied_msg}```")
        await log(event)
